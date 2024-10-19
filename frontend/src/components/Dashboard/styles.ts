import styled from 'styled-components';

export const Container = styled.main`
    max-width: 1120px;
    margin: 0 auto;
    padding: 2.5rem 1rem;
    
`;

// Definindo o estilo para o container do dashboard
export const DashboardContainer = styled.div`
  display: grid;
  grid-template-columns: repeat(4, 1fr);  /* Define 4 colunas de igual tamanho */
  gap: 16px;  /* Espaçamento entre as colunas */
  padding: 20px;

  /* Estilo de cada cardápio */
  .menu-card {
    background-color: #f9f9f9;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    text-align: left;

    /* Estilo do título "Almoço" */
    h2 {
      font-size: 1.5rem;
      margin-bottom: 16px;
      color: #333;
      text-align: center;
    }

    /* Estilo da lista de itens */
    ul {
      list-style-type: none;
      padding: 0;
      margin: 0;

      /* Estilo para cada item da lista */
      li {
        font-size: 1rem;
        margin-bottom: 8px;
        color: #555;
      }
    }
  }
`;