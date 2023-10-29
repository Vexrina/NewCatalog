// pages/index.js

import React from 'react';
import { ThemeProvider } from '../context/ThemeContext';
import Header from '../components/Header';
import Botter from '../components/Botter';

const Home = () => {
  return (
    <ThemeProvider>
      <div>
        <Header />
        <h1> Home Page Content</h1>
        <Botter/>
      </div>
    </ThemeProvider>
  );
};

export default Home;
