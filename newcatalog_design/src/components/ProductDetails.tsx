import React, { useEffect, useState } from 'react';
import { fetchModelData, ApiResponse } from '../pages/api/api';

interface ProductDetailsProps {
    category: string;
    model: string;
}

interface Specs {
    [key: string]: string | number | null;
}

interface ProductData {
    brand: string;
    model: string;
    image: string;
    specs: Specs;
}

const ProductDetails: React.FC<ProductDetailsProps> = ({ category, model }) => {
    const [apiData, setApiData] = useState<ProductData | null>(null);

    useEffect(() => {
        async function fetchDataForModel() {
            const modelData: ProductData | null = await fetchModelData<ProductData>(
                category,
                model
            );
            console.log('Model Data:', modelData);
            setApiData(modelData);
        }


        fetchDataForModel();
    }, [category, model]);


    if (!apiData || !apiData.specs) {
        return <p>Loading...</p>;
    }

    return (
        <div className="product-details">
            <div className="title">
                <h1>{`${apiData.brand} ${apiData.model}`}</h1>
            </div>

            <div className="content">
                <img
                    src={apiData.image}
                    alt={`${apiData.brand} ${apiData.model}`}
                    className="product-image"
                />

                <div className="product-specs">
                    <h2>Characteristics:</h2>
                    <ul>
                        <li></li>
                        <li>
                            <strong>Socket:</strong> {apiData.specs.socket}
                        </li>
                        <li>
                            <strong>Cache:</strong> {apiData.specs.cache}Mb
                        </li>
                        <li>
                            <strong>Clock:</strong> {apiData.specs.clock}
                        </li>
                        <li>
                            <strong>Overclock:</strong> {apiData.specs.overclock}
                        </li>
                        <li>
                            <strong>Number of Cores:</strong> {apiData.specs.num_cores}
                        </li>
                        <li>
                            <strong>Number of Threads:</strong> {apiData.specs.num_thr}
                        </li>
                        <li>
                            <strong>Nanometers:</strong> {apiData.specs.nm}nm
                        </li>
                        <li>
                            <strong>TDP:</strong> {apiData.specs.tdp}W
                        </li>
                        <li>
                            <strong>Max Temperature:</strong> {apiData.specs.max_temp}°C
                        </li>
                        <li>
                            <strong>Memory Channels:</strong> {apiData.specs.memory_channels}
                        </li>
                        {apiData.specs.videocore === 1 ? (
                            <>
                                <li>
                                    <strong>Videocore:</strong> {apiData.specs.videocore}
                                </li>
                                <li>
                                    <strong>Videocore Model:</strong> {apiData.specs.model_videocore}
                                </li>
                                <li>
                                    <strong>Clock Videocore:</strong> {apiData.specs.clock_videocore}
                                </li>
                            </>
                        ) : (
                            <li>
                                <strong>Videocore:</strong> No Videocore
                            </li>
                        )}
                    </ul>
                </div>

            </div>
        </div>


    );
};

export default ProductDetails;
