// components/Product.tsx
import React, { useEffect, useState } from 'react';
import CardComponent from './CardComponent';
import { fetchData, ApiResponse } from '../pages/api/api';

interface ProductProps {
  category: string;
}

const Product: React.FC<ProductProps> = ({ category }) => {
  const [apiData, setApiData] = useState<ApiResponse | null>(null);

  useEffect(() => {
    async function fetchDataForCategory() {
      const categoryData: ApiResponse | null = await fetchData<ApiResponse>(
        category
      );
      setApiData(categoryData);
    }

    fetchDataForCategory();
  }, [category]);

  return (
    <div className="cards-container">
      {apiData && Object.values(apiData).length > 0 ? (
        Object.values(apiData).map((data, index) => (
          <CardComponent key={index} data={data} />
        ))
      ) : (
        <p>Loading...</p>
      )}
    </div>
  );
};

export default Product;
