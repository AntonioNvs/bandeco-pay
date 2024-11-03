import React, { useState, useEffect } from 'react';
import { BalanceContainer, BalanceText, ToggleButton } from './style';

import axios from 'axios';
// interface User {
//   getName(): string;
//   getBalance(): number;
//   getPriceToPay(): number;
//   setBalance(price: number): boolean;
// }

interface User {
  name: string;
  balance: number;
}

const fetchUserData = async (token: string) => {
  try {
    const responseBalance = await axios.get('https://test-41378101111.southamerica-east1.run.app/balance', {
      headers: {
        'Authorization': `Bearer ${token}`,
        'Content-Type': 'application/json',
      },
    });

    const responseName = await axios.get('https://test-41378101111.southamerica-east1.run.app/get_user_name', {
      headers: {
        'Authorization': `Bearer ${token}`,
        'Content-Type': 'application/json',
      },
    })

    const dataBalance = responseBalance.data;
    const dataName = responseName.data;
    
    return {
      name: dataName.name,
      balance: dataBalance.balance,
    };
  } catch (error) {
    console.error('Failed to fetch user data', error);
    return null;
  }
};


export const Account: React.FC<{ token: string, balanceUpdated: boolean }> = ({ token, balanceUpdated }) => {
  const [isHidden, setIsHidden] = useState(false);
  const [user, setUser] = useState<User | null>(null);

  useEffect(() => {
    const loadUserData = async () => {
      const userData = await fetchUserData(token);
      if (userData) {
        setUser(userData);
      }
    };

    loadUserData();
  }, [balanceUpdated]);

  if (!user) {
    return <div>      
      <BalanceText>
        Carregando...
      </BalanceText>
  </div>;
  }

  const toggleVisibility = () => {
    setIsHidden(!isHidden);
  };

  return (
    <BalanceContainer>
      <BalanceText>
        Nome do titular: {user.name} <br />
        Saldo: {isHidden ? '*****' : new Intl.NumberFormat('pt-BR', { style: 'currency', currency: 'BRL' }).format(user.balance)}
      </BalanceText>
      <ToggleButton onClick={toggleVisibility}>
        {isHidden ? 'Mostrar' : 'Ocultar'}
      </ToggleButton>
    </BalanceContainer>
  );
};

