// pages/[category].tsx
import { useRouter } from 'next/router';
import Header from '@/components/Header';
import Product from '@/components/Product';
import Botter from '@/components/Botter';

const CategoryPage = () => {
    const router = useRouter();
    const { category } = router.query;

    return (
        <div>
            <Header />
            <Product category={category as string} />
            <Botter />
        </div>
    );
};

export default CategoryPage;
