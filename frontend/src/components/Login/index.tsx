import React, { useState, useEffect } from 'react';
import { ModalBackground, ModalContent } from './style';

import axios from 'axios';

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
      
      const loginData = {
        "username": username,
        "password": password
      }

      axios.post('http://127.0.0.1:5000/login', loginData)
        .then(response => {
          if (response.status == 200) {
            console.log(response.data);
            setError('');
            onLoginSuccess();  
            onClose();
          } else {
            // Não logado, deu erro
            setError('Usuário ou senha inválidos');
          }
      })
      .catch(error => {
        console.error("Erro ao conectar com a API:", error);
      });
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