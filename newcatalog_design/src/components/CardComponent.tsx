import React from 'react';
import Link from 'next/link';
import { useRouter } from 'next/router';

interface Processor {
  brand: string;
  model: string;
  image: string;
  specs: {
    cache: number;
    clock: string;
    clock_videocore: string | null;
    max_temp: number;
    memory_channels: number;
    model_videocore: string | null;
    nm: number;
    num_cores: number;
    num_thr: number;
    overclock: number;
    socket: string;
    tdp: number;
    videocore: number;
  };
}

interface CardProps {
  data: Processor; // Используйте интерфейс Processor в качестве типа данных для пропсов
}

const CardProcessor: React.FC<CardProps> = ({ data }) => {
  const cardStyle = {
    background: '#FFC357',
    borderRadius: '10px',
    overflow: 'hidden',
  };
  const imageStyle = {
    width: '50%',
    height: 'auto',
  };

  return (
    <Link href={`/cpu/${data.model}`} passHref>
      <div className="card" style={cardStyle}>
        <h2>{data.brand} {data.model}</h2>
        <img src={data.image} alt={`${data.brand} ${data.model}`} style={imageStyle} />
        <p>Socket: {data.specs?.socket}</p>
        <p>Memory Channels: {data.specs?.memory_channels}</p>
        <p>Cores: {data.specs?.num_cores}</p>
        <p>Threads: {data.specs?.num_thr}</p>
        <p>Clock: {data.specs?.clock}</p>
        <p>Overclock: {data.specs?.overclock}</p>
        <p>Cache: {data.specs?.cache} MB</p>
        <p>TDP: {data.specs?.tdp}</p>
        <p>Maximum Temperature: {data.specs?.max_temp}</p>
        {data.specs?.videocore !== 0 ? (
          <>
            <p>Model Videocore: {data.specs?.model_videocore}</p>
            <p>Clock Videocore: {data.specs?.clock_videocore}</p>
          </>
        ) : (
          <>
            <p>Model Videocore: No videocore</p>
          </>
        )}
      </div>
    </Link>
  );
};

const CardComponent: React.FC<CardProps> = ({ data }) => {
  const router = useRouter();
  const category = router.query?.category as string;
  const containerStyle = {
    // display: 'flex',
    // justifyContent: 'space-between',
    // paddingLeft: '50px', // Ваши отступы справа и слева
    // paddingRight: '50px', // Ваши отступы справа и слева
  };

  switch (category) {
    case 'cpu':
      return (
        <div style={containerStyle}>
          <CardProcessor data={data} />
        </div>
      );
    // Add other cases for different categories as needed
    default:
      return <div>404</div>;
  }
};

export default CardComponent;
