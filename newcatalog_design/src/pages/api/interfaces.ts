export interface Processor {
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