// api.ts

export interface InnerDict {
    [key: string]: string | InnerDict;
}

export interface ApiResponse {
    [key: number]: InnerDict;
}

export async function fetchData<T>(route: string): Promise<T | null> {
    try {
        const response = await fetch(`http://localhost:55000/${route}`);
        const data: T = await response.json();
        return data;
    } catch (error) {
        console.error('Error fetching data:', error);
        return null;
    }
}

export async function fetchModelData<T>(category: string, model: string): Promise<T | null> {
    const route = `${category}/${model}`;

    try {
        const response = await fetch(`http://localhost:55000/${route}`);
        const data: T = await response.json();
        return data;
    } catch (error) {
        console.error('Error fetching model data:', error);
        return null;
    }
}