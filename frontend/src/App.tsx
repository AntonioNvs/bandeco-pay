import React, { useState, useEffect } from 'react';
import { Header } from './components/Header';
import { Dashboard } from './components/Dashboard';
import { Statement } from './components/Statement';
import { Account } from './components/Account';
import { LoginModal } from './components/Login';
import { GlobalStyle } from './styles/global';

import axios from 'axios';

class User {
  private name: string;
  private balance: number;
  private price_to_pay: number;
 
  constructor(name: string, balance: number, price_to_pay: number) {
    this.name = name;
    this.balance = balance;
    this.price_to_pay = price_to_pay;
  }

  getName(): string {
    return this.name;
  }

  getBalance(): number {
    return this.balance;
  }

  getPriceToPay(): number {
    return this.price_to_pay;
  }

  setBalance(price: number): boolean {
    if (price < 0) return false;
    this.balance = price;
    return true;
  }
}

function App() {
  const [isLoginOpen, setIsLoginOpen] = useState(false);
  const [isAuthenticated, setIsAuthenticated] = useState(
    () => !!localStorage.getItem('isAuthenticated') // Verifica se está logado ao carregar
  );
  const [currentView, setCurrentView] = useState<'dashboard' | 'statement'>('dashboard'); // Controla o conteúdo exibido

  const [token, setToken] = useState('');

  const toggleLoginModal = () => {
    setIsLoginOpen(!isLoginOpen);
  };

  const handleLoginSuccess = () => {
    setIsAuthenticated(true);
    localStorage.setItem('isAuthenticated', 'true');
  };

  const handleLogout = () => {
    setIsAuthenticated(false);
    setToken('');
    localStorage.removeItem('isAuthenticated');
  };

  const handleViewStatement = () => {
    setCurrentView('statement'); // Exibe a página de extrato
  };

  const handleViewDashboard = () => {
    setCurrentView('dashboard'); // Volta para o dashboard
  };

  const handleToken = (token: string) => {
    setToken(token);
  }

  useEffect(() => {
    
  }, [])

  return (
    <>
      <Header 
        onLoginClick={toggleLoginModal} 
        onLogoutClick={handleLogout} 
        isAuthenticated={isAuthenticated}
        onViewStatementClick={handleViewStatement} // Função para ver o extrato
      />

      {/* Exibe conteúdo baseado no estado atual */}
      {isAuthenticated ? (
        currentView === 'dashboard' ? (
          <Dashboard />
        ) : (
          <div>
            <Account token={token} /> {/* Podemos buscar na api */}
            <Statement token={token} onBackToDashboard={handleViewDashboard} /> {/* Exibe o extrato*/}
          </div>
        )
      ) : (
        <Dashboard />
      )}
      
      <LoginModal isOpen={isLoginOpen} onClose={toggleLoginModal} onLoginSuccess={handleLoginSuccess} setToken={handleToken} />
      <GlobalStyle />
    </>
  );
}

export default App;
