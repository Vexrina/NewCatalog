import React from 'react';
import Image from 'next/image';
import Link from 'next/link';
import { useRouter } from 'next/router';

import GpuImage from '../public/svg/gpu.svg';
import CpuImage from '../public/svg/cpu.svg';
import CpuFanImage from '../public/svg/cpu_fan.svg';
import MotherboardImage from '../public/svg/motherboard.svg';
import PowerUnitImage from '../public/svg/power_unit.svg';
import ProfileImage from '../public/svg/profile.svg';
import RamImage from '../public/svg/ram.svg';
import StorageImage from '../public/svg/storage.svg';
import ShopImage from '../public/svg/shopping-cart.svg';

const Header: React.FC = () => {
  const router = useRouter();
  return (
    <header className='h-50 w-full'>
      <nav className='flex justify-between items-center'>
        <div className='pl-48 pr-24 flex items-center h-12' style={{ backgroundColor: '#D88144' }}>
          <Link href='/'>
            <div className='text-lg font-bold text-white p-0 m-0'>
              newCatalog
            </div>
          </Link>
        </div>
        <div className='flex items-center space-x-4 pr-24 pl-24 w-full h-12' style={{ backgroundColor: '#084F93', color: 'black' }}>
          <input
            type="text"
            placeholder='Search here!'
            className='px-2 py-2 border rounded focus:outline-none focus:border-blue-500 w-80 h-10'
          />
          <div className='flex items-center space-x-4 pr-24 pl-4'>
            <Link href="/cpu">
              <div className={`pr-2 ${router.pathname === '/cpu' ? 'text-red-500' : ''}`}>
                <Image src={CpuImage} alt="CPU" />
              </div>
            </Link>
            <a href="/gpu" className='pr-2'><Image src={GpuImage} alt="GPU" /></a>
            <a href="/ram" className='pr-2'><Image src={RamImage} alt="RAM" /></a>
            <a href="/motherboard" className='pr-2'><Image src={MotherboardImage} alt="Motherboard" /></a>
            <a href="/storage" className='pr-2'><Image src={StorageImage} alt="Storage" /></a>
            <a href="/powerunit" className='pr-2'><Image src={PowerUnitImage} alt="Power Unit" /></a>
            <a href="/cpufan" className='pr-2'><Image src={CpuFanImage} alt="CPU Fan" /></a>
            <a href="/shopping_cart" className='pr-2'><Image src={ShopImage} alt="Shopping Cart" /></a>
            <a href="/profile" className='pr-2'><Image src={ProfileImage} alt="Profile" /></a>
          </div>
        </div>
      </nav>
    </header>
  );
};

export default Header;
