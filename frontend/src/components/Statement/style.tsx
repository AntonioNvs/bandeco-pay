import styled from 'styled-components';

export const StatementContainer = styled.div`
  padding: 20px;
  margin: 0 50px;
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

export const HeaderContainer = styled.div`
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 16px;

  h2 {
    margin: 0;
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


export const Modal = styled.div`
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
`;

export const ModalContent = styled.div`
  background-color: white;
  padding: 20px;
  border-radius: 8px;
  width: 400px;
  text-align: center;
  input {
    padding: 10px;
    margin-top: 10px;
    margin-bottom: 20px;
    width: 80%;
  }
  button {
    padding: 10px 20px;
    margin-right: 10px;
  }
`;