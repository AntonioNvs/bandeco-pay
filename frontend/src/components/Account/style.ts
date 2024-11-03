import styled from 'styled-components';

export const BalanceContainer = styled.div`
  background-color: #f1f1f1;
  padding: 20px;
  border-radius: 3px;
  margin: -5rem auto 20px auto; /* Margem negativa para sobrepor o extrato */
  display: flex;
  justify-content: space-between;
  align-items: center;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  width: 40rem;
`;

export const BalanceText = styled.span`
  font-size: 1.2rem;
  color: #333;
`;

export const ToggleButton = styled.button`
  background: none;
  border: none;
  font-size: 1rem;
  cursor: pointer;
  color: var(--green);
`;