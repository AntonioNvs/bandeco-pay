import React, { useState } from 'react';
import { BalanceContainer, BalanceText, ToggleButton } from './style';

interface User {
  getName(): string;
  getBalance(): number;
  getPriceToPay(): number;
  setBalance(price: number): boolean;
}


export const Account: React.FC<{ user: User }> = ({ user }) => {
  const [isHidden, setIsHidden] = useState(false);

  const toggleVisibility = () => {
    setIsHidden(!isHidden);
  };

  return (
    <BalanceContainer>
      <BalanceText>
        Nome do titular: {user.getName()} <br />
        Saldo: {isHidden ? '*****' : new Intl.NumberFormat('pt-BR', { style: 'currency', currency: 'BRL' }).format(user.getBalance())}
      </BalanceText>
      <ToggleButton onClick={toggleVisibility}>
        {isHidden ? 'Mostrar' : 'Ocultar'}
      </ToggleButton>
    </BalanceContainer>
  );
};

