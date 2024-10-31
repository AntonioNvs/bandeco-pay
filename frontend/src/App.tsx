import React, { useState, useEffect } from 'react';
import { Header } from './components/Header';
import { Dashboard } from './components/Dashboard';
import { Statement } from './components/Statement';
import { Account } from './components/Account';
import { LoginModal } from './components/Login';
import { GlobalStyle } from './styles/global';

interface AuthState {
  token: string | null;
}

function App() {
  const [auth, setAuth] = useState<AuthState>({ token: localStorage.getItem('token') });
  const [balanceUpdated, setBalanceUpdated] = useState(false);
  const [isLoginOpen, setIsLoginOpen] = useState(false);
  const [currentView, setCurrentView] = useState<'dashboard' | 'statement'>('dashboard');

  const toggleLoginModal = () => setIsLoginOpen(!isLoginOpen);

  const handleLoginSuccess = (loginToken: string) => {
    setAuth({ token: loginToken });
    localStorage.setItem('token', loginToken);
  };

  const handleLogout = () => {
    setAuth({ token: null });
    localStorage.removeItem('token');
  };

  const handleViewStatement = () => setCurrentView('statement');
  const handleViewDashboard = () => setCurrentView('dashboard');
  return (
    <>
      <Header 
        onLoginClick={toggleLoginModal} 
        onLogoutClick={handleLogout} 
        isAuthenticated={!!auth.token}
        onViewStatementClick={handleViewStatement}
      />

      {/* Exibe conteúdo baseado no estado atual */}
      {auth.token ? (
        currentView === 'dashboard' ? (
          <Dashboard />
        ) : (
          <div>
            <Account token={auth.token} balanceUpdated={balanceUpdated}/>
            <Statement 
              token={auth.token} 
              setBalanceUpdated={setBalanceUpdated} 
              onBackToDashboard={handleViewDashboard}
            />
          </div>
        )
      ) : (
        <Dashboard />
      )}

      <LoginModal isOpen={isLoginOpen} onClose={toggleLoginModal} onLoginSuccess={handleLoginSuccess} />
      <GlobalStyle />
    </>
  );
}

export default App;