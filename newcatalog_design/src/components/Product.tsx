import React, { useEffect, useState } from 'react';
import CardComponent from './CardComponent'; // Импортируйте компоненту карточки
import { fetchData, ApiResponse } from '../pages/api/api';

function Product(): React.JSX.Element {
  const [apiData, setApiData] = useState<ApiResponse | null>(null);

  useEffect(() => {
    async function fetchDataForCPU() {
      const cpuData: ApiResponse | null = await fetchData<ApiResponse>('cpu');
      setApiData(cpuData); // Устанавливаем полученные данные в состояние компонента
    }

    fetchDataForCPU();
  }, []);

  // Проверяем, есть ли данные от API, и рендерим их как карточки
  return (
    <div className="cards-container" style={{ 
      display: 'grid',
      gridTemplateColumns: 'repeat(auto-fill, minmax(300px, 1fr))', /* 2 колонки с минимальной шириной 300px */
      gap: '20px' /* Расстояние между карточками */
    }}
    >
      {apiData && Object.values(apiData).length > 0 ? (
        // Используем map() для создания компоненты карточки для каждого элемента данных
        Object.values(apiData).map((data, index) => (
          <CardComponent key={index} data={data} />

        ))
      ) : (
        <p>Loading...</p> // Показываем сообщение о загрузке, пока данные не получены
      )}
    </div>
  );
}

export default Product;
