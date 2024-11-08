# bandeco-pay

## Objetivo e principais features
O sistema de pagamento automático para restaurantes universitários foi projetado para solucionar o problema das longas filas, que tornam o processo de compra de refeições demorado e inconveniente para alunos e funcionários. Utilizando os cartões de proximidade já emitidos, o sistema simplifica as transações, permitindo que os usuários façam pagamentos apenas aproximando o cartão de um leitor, semelhante ao funcionamento das catracas de ônibus, eliminando a necessidade de dinheiro ou cartões adicionais. As principais funcionalidades incluem a integração com o saldo de crédito previamente carregado, garantindo transações rápidas e seguras, além de um site onde os usuários podem recarregar créditos, consultar o histórico de transações e visualizar os cardápios de forma simples. Para a administração do restaurante, o sistema oferece relatórios personalizados de uso, facilitando a gestão do fluxo de pessoas e dos recursos.

## Membros da equipe e papel (full, backend, frontend)
* **Backend:** Raphael Aroldo Carreiro
* **Frontend:** Bernardo Dutra Lemos
* **Fullstack:** Antônio Caetano Neves Neto

## Tecnologias 
O sistema de pagamento automático para restaurantes universitários será desenvolvido utilizando *Python* como linguagem de *backend*, com o framework *Flask* para gerenciar rotas e integrar funcionalidades comerciais, como o banco de dados e a tecnologia *NFC*. No frontend, será utilizado React com TypeScript, garantindo uma interface responsiva tanto em desktops quanto em dispositivos móveis. O banco de dados a ser utilizado ainda está em avaliação, com opções como *SQLITE3*, *MongoDB* e *PostgreSQL* sendo consideradas para melhor atender às necessidades do sistema.

## Backlog do produto

- **História 1:** Como usuário, gostaria de gerenciar meus cartões disponíveis (bloquear uso, liberar uso, remover, etc).

- **História 2:** Como usuário, gostaria de ter acesso a um extrato da conta, dividido mensalmente, contendo todos os depósitos e gastos.

- **História 3:** Como usuário, gostaria de acessar o sistema utilizando o login cadastrado da UFMG.

- **História 4:** Como usuário, gostaria de ver e adicionar saldo à minha conta através de Pix e Débito por meio de recarga no site.

 - **História 5:** Como usuário, gostaria de ter um registro do quanto eu devo pagar pelas refeições (visto que posso ser beneficiário da FUMP) e que a catraca me cobrasse esse valor.

- **História 6:** Como usuário, gostaria de transferir saldo da minha conta BandecoPay para outro usuário BandecoPay.

- **História 7:** Como usuário, gostaria de abrir uma requisição para o cancelamento e possível reembolso de um depósito de saldo no sistema.

- **História 8:** Como administrador do restaurante, gostaria de ter acesso a um relatório sobre a quantidade, o perfil (aluno, fumpista, externo) e o horário de cada cliente, para fins de análise.

- **História 9:** Como usuário, gostaria de pagar minha refeição e possibilitar minha entrada no restaurante universitário com o meu cartão da UFMG.

- **História 10:** Como usuário, gostaria de ver qual é o cardápio do dia de cada restaurante e quais são os cardápios dos próximos dias no site.


## Backlog da sprint

- **História 2:** Como usuário, gostaria de ter acesso a um extrato da conta, dividido mensalmente, contendo todos os depósitos e gastos.
  - Tarefa e responsáveis:
    - Instalar banco de dados, modelar como será o banco de dados relacional e criar primeiras tabelas [Raphael]
    - Instalar dependências a serem utilizadas do Python [Antônio]
    - Instalar todas as dependências necessárias para rodar o frontend por completo e a base de código do sistema [Antônio]
    - Implementar no backend a lógica de recuperar as compras do usuário [Raphael]
    - Adaptar na tela principal a possibilidade de acessar o extrato da conta [Bernardo]
    - Criar a tela de extrato da conta [Bernardo]

- **História 4:** Como usuário, gostaria de ver e adicionar saldo à minha conta através de Pix e Débito por meio de recarga no site.
  - Tarefa e responsáveis:
    - Implementar no backend a lógica de retornar o saldo da conta [Raphael]
    - Implementar no backend a lógica de adicionar saldo à conta do usuário [Raphael]
    - Criar a tela principal, onde será possível ver o saldo e outras informações, com a possibilidade de ocultar informações sensíveis [Bernardo]
    - Criar a tela de recarga de saldo [Bernardo]

- **História 9:** Como usuário, gostaria de pagar minha refeição e possibilitar minha entrada no restaurante universitário com o meu cartão da UFMG.
  - Tarefa e responsáveis:
    - Construir o sistema para leitura da informação dos cartões [Antônio]
    - Conectar o sistema de leitura NFC com o backend da aplicação [Raphael]
    - Em um sistema de WebSocket de status de uso da catraca com o backend, criar uma página de visualização do status da catraca e do usuário que a utilizou no momento [Antônio] 

- **História 10:** Como usuário, gostaria de ver qual é o cardápio do dia de cada restaurante e quais são os cardápios dos próximos dias no site.
  - Tarefa e responsáveis:
    - Criar a tabela de cadastro do cardápio de cada dia de cada restaurante [Raphael]
    - Implementar no backend a lógica de retornar o cardápio do dia [Antônio]
    - Adaptar na tela principal a visualização do cardápio do dia [Bernardo]

## Diagramas UML

### Diagrama de Classes

![Diagrama de classes UML](/UML/Diagrama-de-Classes.png)


### Diagrama de Sequência

![Diagrama de Sequência UML](/UML/diagrama-de-sequência.jpeg)


