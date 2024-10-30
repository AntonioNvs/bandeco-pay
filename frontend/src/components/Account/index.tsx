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
    const response = await axios.get('http://127.0.0.1:5000/balance', {
      headers: {
        'Authorization': `Bearer ${token}`,
        'Content-Type': 'application/json',
      },
    });

    const data = response.data;
    //console.log(data);
    
    return {
      name: data.name,
      balance: data.balance,
    };
  } catch (error) {
    console.error('Failed to fetch user data', error);
    return null;
  }
};


export const Account: React.FC<{ token: string }> = ({ token }) => {
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
  }, [token]);

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

