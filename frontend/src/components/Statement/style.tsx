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
    font-size: 20px;
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
  .debit {
    color: var(--red);
  }

  .credit {
    color: var(--green);
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

  h3 {
    font-size: 24px;
  }

  input {
    padding: 10px;
    margin-top: 10px;
    margin-bottom: 32px;
    width: 90%;
    border-radius: 8px;
    font-size: 20px;
  }
  button {
    padding: 10px 20px;
    margin-right: 10px;
  }
`;

export const ButtonsContainer = styled.div`
  display: flex;
  justify-content: space-between; /* Align buttons side by side */
  margin-bottom: 24px; /* Space below the button container */
  margin-top: 24px;

  button {
    flex: 1; /* Make buttons take equal space */
    margin-right: 5px; /* Space between buttons */
    background-color: var(--green);
    color: white; /* Text color */
    border: none; /* Remove default border */
    border-radius: 5px; /* Rounded corners */
    padding: 10px; /* Padding inside the button */
    cursor: pointer; /* Pointer cursor on hover */
    transition: background-color 0.3s; /* Smooth transition for background color */

    &:hover {
      background-color: darkgreen; /* Darker green on hover */
    }

    &:last-child {
      margin-right: 0; /* Remove margin from the last button */
    }

    &.selected {
      background-color: var(--dark-green); /* Change background for selected button */
    }
  }
`;