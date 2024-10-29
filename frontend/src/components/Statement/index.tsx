import React from 'react';
import { StatementContainer, HeaderContainer, Modal, ModalContent } from './style';
import { useEffect, useState } from 'react';





interface Compra {
  data: string;
  valor: string;
  descricao: string;
}

const formatCurrency = (value: number) => {
  return new Intl.NumberFormat('pt-BR', { 
    style: 'currency', 
    currency: 'BRL' 
  }).format(value);
};

interface StatementProps {
  onBackToDashboard: () => void; // Função para voltar ao dashboard
}

export const Statement: React.FC<StatementProps> = ({ onBackToDashboard }) => {
  const [compras, setCompras] = useState<Compra[]>([]); // Estado para armazenar as compras
  const [modalVisible, setModalVisible] = useState(false);
  const [newBalance, setNewBalance] = useState('');

  // Simula uma "API" que traz os dados das compras após 2 segundos
  useEffect(() => {
    const fakeApiCall = () => {
      const comprasSimuladas: Compra[] = [
        { data: '10/10/2024', valor: '- R$ 10,50', descricao: 'Compra no Bandeco' },
        { data: '09/10/2024', valor: '+ R$ 50,00', descricao: 'Depósito' },
        { data: '08/10/2024', valor: '- R$ 20,00', descricao: 'Compra de Livros' },
        { data: '07/10/2024', valor: '- R$ 15,00', descricao: 'Compra de Material' },
      ];
      return comprasSimuladas;
    };

    // Simula o comportamento de delay de uma API
    setTimeout(() => {
      const compras = fakeApiCall();
      setCompras(compras); // Atualiza o estado com os dados simulados
    }, 1000); // 2 segundos de delay para simular uma API
  }, []);

  // Função para abrir o modal
  const handleAddBalanceClick = () => {
    setModalVisible(true);
  };

  // Função para fechar o modal
  const handleCloseModal = () => {
    
    setModalVisible(false);
    setNewBalance('');
  };

  const handleAddBalance = () => {
    if (newBalance) {
      const valorFormatado = formatCurrency(parseFloat(newBalance)); // Formatar o valor como moeda
      const novaCompra: Compra = {
        data: new Date().toLocaleDateString(),
        valor: valorFormatado,  // Usar valor formatado
        descricao: 'Depósito',
      };
      setCompras([...compras, novaCompra]);
      handleCloseModal(); // Fechar modal após adicionar saldo
    }
  };
  

  return (
    <StatementContainer>
      <HeaderContainer>
        <h2>Seu Extrato</h2>
        <button onClick={handleAddBalanceClick}>Adicionar saldo</button>
      </HeaderContainer>

        <table>
          <thead>
            <tr>
              <th>Data</th>
              <th>Descrição</th>
              <th>Valor</th>
            </tr>
          </thead>
          <tbody>
            {compras.length === 0 ? (
              <tr>
                <td colSpan={3}>Carregando...</td>
              </tr>
            ) : (
              compras.map((compra, index) => (
                <tr key={index}>
                  <td>{compra.data}</td>
                  <td>{compra.descricao}</td>
                  <td>{compra.valor}</td>
                </tr>
              ))
            )}
          </tbody>
        </table>

      <button onClick={onBackToDashboard}>Voltar ao Dashboard</button>

      {/* Modal para adicionar saldo */}
      {modalVisible && (
      <Modal onClick={handleCloseModal}> {/* Detecta clique no overlay */}
        <ModalContent onClick={(e) => e.stopPropagation()}> {/* Não fecha ao clicar dentro */}
          <h3>Adicionar Saldo</h3>
          <input
            type="number"
            value={newBalance}
            onChange={(e) => setNewBalance(e.target.value)}
            placeholder="Digite o valor"
          />
          <br />
          <button onClick={handleAddBalance}>Adicionar</button>
          <button onClick={handleCloseModal}>Cancelar</button>
        </ModalContent>
      </Modal>
    )}
    </StatementContainer>
  );
};