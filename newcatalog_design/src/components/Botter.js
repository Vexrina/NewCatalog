// src/components/Botter.js

import React from 'react';
import ButtonToggleTheme from './buttons/ButtonToggleTheme';

const Botter = () => {
    return (
        <header className='fixed bottom-0 w-full p-4 bg-gray-200'>
        <nav className='flex justify-between items-center'>
            <div>
                smth
            </div>
            <ButtonToggleTheme/>
        </nav>
        </header>
    );
};

export default Botter