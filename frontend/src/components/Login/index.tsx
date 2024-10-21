import React, { useState } from 'react';
import { ModalBackground, ModalContent } from './style';


interface LoginModalProps {
    isOpen: boolean;
    onClose: () => void;
    onLoginSuccess: () => void; // Nova prop para chamar quando o login for bem-sucedido
  }
  
export const LoginModal: React.FC<LoginModalProps> = ({ isOpen, onClose, onLoginSuccess }) => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');
    
    // Nesse camarada aqui que vamos puxar dados da api...
    const handleLogin = () => {
      // Simulação de credenciais de login
      const mockUsername = 'admin';
      const mockPassword = 'password123';
  
      if (username === mockUsername && password === mockPassword) {
        setError('');
        onLoginSuccess();  // Chama a função para indicar que o login foi bem-sucedido
        onClose();  // Fecha o modal de login
      } else {
        setError('Usuário ou senha inválidos');
      }
    };
  
    if (!isOpen) return null;
  
    return (
      <ModalBackground onClick={onClose}>
        <ModalContent onClick={(e) => e.stopPropagation()}>
          <h2>Login</h2>
          {error && <div className="error">{error}</div>}
          <input 
            type="text" 
            placeholder="Usuário" 
            value={username}
            onChange={(e) => setUsername(e.target.value)}
          />
          <input 
            type="password" 
            placeholder="Senha" 
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
          <button onClick={handleLogin}>Entrar</button>
        </ModalContent>
      </ModalBackground>
    );
};