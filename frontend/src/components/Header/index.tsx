import React from 'react';
import { Container, Content } from './styles';

interface HeaderProps {
  onLoginClick: () => void;
  onLogoutClick: () => void;
  onViewStatementClick: () => void;
  isAuthenticated: boolean;
}

export function Header({ onLoginClick, onLogoutClick,onViewStatementClick, isAuthenticated }: HeaderProps) {
  return (
    <Container>
      <Content>
        <h1>
          <a href="/" style={{ textDecoration: 'none', color: 'inherit'}}>
            BandecoPay
          </a>
        </h1>
        {isAuthenticated ? (
          <div>
            <button type="button" onClick={onLogoutClick}>
              Logout
            </button>
            <button type="button" onClick={onViewStatementClick}>
              Extrato
            </button>
          </div>
        ) : (
          <button type="button" onClick={onLoginClick}>
            Login
          </button>
        )}
      </Content>
    </Container>
  );
}
