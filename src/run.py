from src.backend.parsers.to_parse import cpus, gpus, power_units, ssd, fans, hdd

a = [
    len(cpus.amd),
    len(gpus.amd),
    len(cpus.intel),
    len(gpus.nvidia),
    len(power_units.to_parse),
    len(ssd.to_parse),
    len(fans.to_parse),
    len(hdd.to_parse)
]

b = sum(a)+60*2+60
print(b)
print(b*4)
