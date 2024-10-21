import React from 'react';
import { StatementContainer } from './style';


interface StatementProps {
    onBackToDashboard: () => void; // Função para voltar ao dashboard
  }
  
  export const Statement: React.FC<StatementProps> = ({ onBackToDashboard }) => {
    return (
      <StatementContainer>
        <h2>Seu Extrato</h2>
        
        <table>
          <thead>
            <tr>
              <th>Data</th>
              <th>Descrição</th>
              <th>Valor</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>10/10/2024</td>
              <td>Compra no Bandeco</td>
              <td>- R$ 10,50</td>
            </tr>
            <tr>
              <td>09/10/2024</td>
              <td>Depósito</td>
              <td>+ R$ 50,00</td>
            </tr>
            {/* Adicione mais linhas conforme necessário */}
          </tbody>
        </table>
  
        <button onClick={onBackToDashboard}>Voltar ao Dashboard</button>
      </StatementContainer>
    );
  };