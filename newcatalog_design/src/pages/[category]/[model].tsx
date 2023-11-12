// pages/[category]/[model].tsx
import { useRouter } from 'next/router';
import Header from '@/components/Header';
import ProductDetails from '@/components/ProductDetails';
import Botter from '@/components/Botter';

const ProductModelPage = () => {
  const router = useRouter();
  const { category, model } = router.query;

  // Предположим, что у вас уже есть данные о категории и модели
//   const data = /* Получите данные о категории и модели из вашего источника данных */;

  return (
    <div>
      <Header />
      <ProductDetails category={category as string} model={model as string} />
      <Botter />
    </div>
  );
};

export default ProductModelPage;
