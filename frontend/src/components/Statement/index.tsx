import React, { useEffect, useState } from 'react';
import { StatementContainer, HeaderContainer, Modal, ModalContent, ButtonsContainer  } from './style';
import axios from 'axios';

interface Compra {
  date: string;
  value: number;
  description: string;
  type: 'debit' | 'credit';
}

interface StatementProps {
  token: string;
  onBackToDashboard: () => void;
  setBalanceUpdated: React.Dispatch<React.SetStateAction<boolean>>;
}

const formatCurrency = (value: number) => new Intl.NumberFormat('pt-BR', {
  style: 'currency',
  currency: 'BRL',
}).format(value);

export const Statement: React.FC<StatementProps> = ({ token, onBackToDashboard, setBalanceUpdated }) => {
  const [compras, setCompras] = useState<Compra[]>([]);
  const [modalVisible, setModalVisible] = useState(false);
  const [newBalance, setNewBalance] = useState('');
  const [selectedPaymentMethod, setSelectedPaymentMethod] = useState('Pix');

  // Fetch de transações da API
  const fetchTransactions = async () => {
    try {
      const response = await axios.get('https://test-41378101111.southamerica-east1.run.app/history', {
        headers: { 'Authorization': `Bearer ${token}`, 'Content-Type': 'application/json' },
      });
      if (response.data.transactions) {
        setCompras(response.data.transactions);
        //console.log('Transações:', response.data.transactions);
      }
    } catch (error) {
      console.error('Erro ao buscar transações:', error);
    }
  };

  // Adicionar saldo
  const addBalance = async () => {
    if (!newBalance || Number(newBalance) <= 0) return;

    try {
      await axios.post(
        'https://test-41378101111.southamerica-east1.run.app/add_balance',
        { value: Number(newBalance), type: selectedPaymentMethod },
        { headers: { 'Authorization': `Bearer ${token}`, 'Content-Type': 'application/json' } }
      );
      await fetchTransactions();
      setBalanceUpdated((prev) => !prev);
      closeModal();
    } catch (error) {
      console.error('Erro ao adicionar saldo:', error);
    }
  };

  // Modal Handlers
  const openModal = () => setModalVisible(true);
  const closeModal = () => {
    setModalVisible(false);
    setNewBalance('');
  };

  useEffect(() => {
    fetchTransactions();
  }, []);

  const handlePaymentMethodSelect = (method: string) => {
    setSelectedPaymentMethod(method); // Set selected payment method
  };

  return (
    <StatementContainer>
      <HeaderContainer>
        <h2>Seu Extrato</h2>
        <button onClick={openModal}>Adicionar saldo</button>
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
                <td className={compra.type}>{compra.date}</td>
                <td className={compra.type}>{compra.description}</td>
                <td className={compra.type}>{formatCurrency(compra.value)}</td>
              </tr>
            ))
          )}
        </tbody>
      </table>

      <button onClick={onBackToDashboard}>Voltar ao Dashboard</button>

      {/* Modal de Adicionar Saldo */}
      {modalVisible && (
        <Modal onClick={closeModal}>
          <ModalContent onClick={(e) => e.stopPropagation()}>
            <h3>Adicionar Saldo</h3>
            <ButtonsContainer >
              <button 
                onClick={() => handlePaymentMethodSelect('Pix')} 
                style={{ backgroundColor: selectedPaymentMethod === 'Pix' ? '#33cc95' : '#ccc' }}>
                Pix
              </button>
              <button 
                onClick={() => handlePaymentMethodSelect('Crédito')} 
                style={{ backgroundColor: selectedPaymentMethod === 'Crédito' ? '#33cc95' : '#ccc' }}>
                Crédito
              </button>
            </ButtonsContainer >
            <input
              type="number"
              value={newBalance}
              onChange={(e) => setNewBalance(e.target.value)}
              placeholder="Digite o valor"
            />
            <br />
            <button onClick={addBalance}>Adicionar</button>
            <button onClick={closeModal}>Cancelar</button>
          </ModalContent>
        </Modal>
      )}
    </StatementContainer>
  );
};
