import { GlobalStyle } from './styles/global';
import { Dashboard } from './components/Dashboard/Index';
import React from 'react';
import { Header } from './components/Header';

function App() {
  return (
    <>
      <Header />
      <Dashboard />
      <GlobalStyle />
    </>
  );
}


export default App;
