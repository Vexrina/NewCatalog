// src/components/Header.js

import React from 'react';
import Image from 'next/image';
import GpuImage from '../public/svg/gpu.svg';
import CpuImage from '../public/svg/cpu.svg';
import CpuFanImage from '../public/svg/cpu_fan.svg';
import MotherboardImage from '../public/svg/motherboard.svg';
import PowerUnitImage from '../public/svg/power_unit.svg';
import ProfileImage from '../public/svg/profile.svg';
import RamImage from '../public/svg/ram.svg';
import StorageImage from '../public/svg/storage.svg';
import ShopImage from '../public/svg/shopping-cart.svg';


const Header = () => {
    return (
        <header>
            <nav className='flex justify-between items-center p-4 bg-gray-200'>
                <div>
                    <ul className='flex space-x-4'>
                        <li><a className='' href="/">newCatalog</a></li>
                        <div>
                            Search!
                            <input
                                type="text"
                                placeholder='search here!'
                                className='px-2 py-1 border rounded focus:outline-none focus:border-blue-500'
                            />
                        </div>
                        <li><a href="/cpu">
                            <Image src={CpuImage} alt="CPU" />
                        </a></li>
                        <li><a href="/gpu">
                            <Image src={GpuImage} alt="GPU" />
                        </a></li>
                        <li><a href="/ram">
                            <Image src={RamImage} alt="RAM" />
                        </a></li>
                        <li><a href="/motherboard">
                            <Image src={MotherboardImage} alt="Motherboard" />
                        </a></li>
                        <li><a href="/storage">
                            <Image src={StorageImage} alt="Storage" />
                        </a></li>
                        <li><a href="/powerunit">
                            <Image src={PowerUnitImage} alt="Power Unit" />
                        </a></li>
                        <li><a href="/cpufan">
                            <Image src={CpuFanImage} alt="CPU Fan" />
                        </a></li>
                        <li><a href="/shopping_cart">
                            <Image src={ShopImage} alt="Shopping Cart" />
                        </a></li>
                        <li><a href="/profile">
                            <Image src={ProfileImage} alt="Profile" />
                        </a></li>
                    </ul>
                </div>
            </nav>
        </header>
    );
};

export default Header;