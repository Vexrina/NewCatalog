import React from 'react';

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

const CardComponent: React.FC<CardProps> = ({ data }) => {
    return (
        <div className="card">
            <h2>{data.brand} {data.model}</h2>
            <img src={data.image} alt={`${data.brand} ${data.model}`} />
            <p>Socket: {data.specs.socket}</p>
            <p>Memory Channels: {data.specs.memory_channels}</p>
            <p>Cores: {data.specs.num_cores}</p>
            <p>Threads: {data.specs.num_thr}</p>
            <p>Clock: {data.specs.clock}</p>
            <p>Overclock: {data.specs.overclock}</p>
            <p>Cache: {data.specs.cache} MB</p>
            <p>TDP: {data.specs.tdp}</p>
            <p>Maximum Temperature: {data.specs.max_temp}</p>
            <p>Videocore: {data.specs.videocore}</p>
            <p>Videocore model: {data.specs.model_videocore}</p>
            <p>Videocore clock: {data.specs.clock_videocore}</p>
        </div>
    );
};

export default CardComponent;
