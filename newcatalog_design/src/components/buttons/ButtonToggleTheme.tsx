// src/components/buttons/ButtonToggleTheme.js

import React from 'react';
import { useTheme } from '../../context/ThemeContext';

const ButtonToggleTheme: React.FC = () => {
  const { isDarkMode, toggleTheme } = useTheme();

  return (
    <button onClick={toggleTheme}>
      Toggle Theme
    </button>
  );
};

export default ButtonToggleTheme;
