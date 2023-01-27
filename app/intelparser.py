def delete_str(data: list[str], flag):
    match flag:
        case 1:
            replace_data = [
                'Номер', '<a class', 'error', '[', 'Коллекция', 'Кодовое',
                'Литография', 'Условия', 'Client', 'Вертикальный', 'Desktop'
                ]
        case 2:
            replace_data = [
                'error', '<a class', 'Количество', 'Расчетная',
                'Базовая', 'Частота', 'Максимальная', 'Кэш'
                ]
        case 3:
            replace_data = ['class="label"', 'Макс', 'Поддержка', 'Типы']
        case 4:
            replace_data = [
                'class="label"', 'Разъёмы', 'разъемы', 'PackageSize',
                'ThermalSolutionSpecification', 'MaxCPUs', '>Спецификации',
            ]
    del_str = []
    for i in range(len(data)):
        for s in replace_data:
            index = data[i].find(s)
            if index == -1:
                continue
            else:
                del_str.append(i)
    for i in range(len(del_str)-1, -1, -1):
        data.pop(del_str[i])
    return data


def parserStr(data: list[str]) -> list[str]:
    for i in range(len(data)):
        index = data[i].find('>')
        if index == -1:
            data[i] = "error"
        else:
            data[i] = data[i][index+1:]
            data[i] = data[i].replace('\n', '')
            data[i] = data[i].replace(',', '')
            data[i] = data[i].strip()
    return data


def startParse(dataset, flag):
    data = dataset.find_all('span')
    data = str(data)
    data = data.replace('</span>', '')
    data = data.split('<span')
    data = delete_str(data, flag)
    data = parserStr(data)
    return data


def parseMainData(dataset):
    data = startParse(dataset, 1)
    data.pop(0)
    return {
        'name': data[0],
        'nm': data[1]
        }


def parseSpecData(dataset):
    data = startParse(dataset, 2)
    data.pop(0)
    data.pop(2)
    data.pop(-2)
    data[-1] = data[-1].replace(']', '')
    result = {
        'cores': data[0],
        'thr': data[1],
        'clock': data[3],
        'boost_clock': data[2],
        'cache': data[4],
        'tdp': data[5],
    }
    return result


def parseMemoryData(dataset):
    data = startParse(dataset, 3)
    data.pop()
    data.pop()
    data.pop(0)
    typeMemory = data.pop(1)
    typeMemory = typeMemory.split('-')
    data.append(typeMemory[0])
    data.append(typeMemory[1])
    result = {
        'maxMem': data[0],
        'maxChan': data[1],
        'type': data[2],
        'maxClock': data[3],
    }
    return result


def parsePhysData(dataset):
    data = startParse(dataset,4)
    data.pop(0)
    data.pop(1)
    data[0] = data[0].replace('FC','')
    result = {
        'socket': data[0],
        'maxT': data[1]
        }
    return result
