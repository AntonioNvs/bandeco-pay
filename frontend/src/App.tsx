import React, { useState } from 'react';
import { Header } from './components/Header';
import { Dashboard } from './components/Dashboard';
import { Statement } from './components/Statement';
import { LoginModal } from './components/Login';
import { GlobalStyle } from './styles/global';

function App() {
  const [isLoginOpen, setIsLoginOpen] = useState(false);
  const [isAuthenticated, setIsAuthenticated] = useState(
    () => !!localStorage.getItem('isAuthenticated') // Verifica se está logado ao carregar
  );
  const [currentView, setCurrentView] = useState<'dashboard' | 'statement'>('dashboard'); // Controla o conteúdo exibido

  const toggleLoginModal = () => {
    setIsLoginOpen(!isLoginOpen);
  };

  const handleLoginSuccess = () => {
    setIsAuthenticated(true);
    localStorage.setItem('isAuthenticated', 'true');
  };

  const handleLogout = () => {
    setIsAuthenticated(false);
    localStorage.removeItem('isAuthenticated');
  };

  const handleViewStatement = () => {
    setCurrentView('statement'); // Exibe a página de extrato
  };

  const handleViewDashboard = () => {
    setCurrentView('dashboard'); // Volta para o dashboard
  };

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
          <Statement onBackToDashboard={handleViewDashboard} /> // Exibe o extrato
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
