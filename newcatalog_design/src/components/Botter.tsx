import React from 'react';
import ButtonToggleTheme from './buttons/ButtonToggleTheme';
import Image from 'next/image';
import github from '../public/svg/github.svg';

const Botter: React.FC = () => {
    return (
        <header className='fixed bottom-0 w-full p-4 bg-gray-200'>
            <nav className='flex justify-between items-center'>
                <a href="https://github.com/Vexrina/NewCatalog" className='pr-2'><Image src={github} alt="Source code" height={24} /></a>
                {/* <ButtonToggleTheme height={12}/> */}
            </nav>
        </header>
    );
};

export default Botter;
