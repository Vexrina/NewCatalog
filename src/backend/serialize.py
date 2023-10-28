def cpu_specs_serializer(cpu_specs):
    serialized = {
        'cache': cpu_specs.cache,
        'clock': cpu_specs.clock,
        'clock_videocore': cpu_specs.clock_videocore,
        'max_temp': cpu_specs.max_temp,
        'memory_channels': cpu_specs.memory_channels,
        'model_videocore': cpu_specs.model_videocore,
        'nm': cpu_specs.nm,
        'num_cores': cpu_specs.num_cores,
        'num_thr': cpu_specs.num_thr,
        'overclock': cpu_specs.overclock,
        'socket': cpu_specs.socket,
        'tdp': cpu_specs.tdp,
        'videocore': cpu_specs.videocore,
    }
    return serialized


def cpu_brand_serialize(cpu):
    serialized = {
        'brand': cpu.brand,
        'model': cpu.model,
        # 'prices': cpu.prices,
        'image': cpu.image,
        'specs': cpu_specs_serializer(cpu.specs[0]),
    }
    return serialized
