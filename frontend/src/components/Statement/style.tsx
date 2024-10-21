import styled from 'styled-components';

export const StatementContainer = styled.div`
  padding: 20px;
  h2 {
    margin-bottom: 16px;
  }
  table {
    width: 100%;
    border-collapse: collapse;
    margin-bottom: 20px;
  }
  table, th, td {
    border: 1px solid #ddd;
  }
  th, td {
    padding: 12px;
    text-align: left;
  }
  th {
    background-color: #f4f4f4;
  }
  button {
    padding: 10px 20px;
    background-color: var(--green-light);
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    &:hover {
      filter: brightness(0.9);
    }
  }
`;