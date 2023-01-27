def startParse(dataset):
    data = dataset.find_all('span')
    data = str(data)
    data = data.replace('</span>','')
    data = data.split('<span')
    return data

def parserStr(dataitem:str)->str:
    index = dataitem.find('>')
    if index == -1:
        return "error"
    else:
        dataitem = dataitem[index+1:]
        dataitem = dataitem.replace('\n','')
        dataitem = dataitem.replace(',','')
        dataitem = dataitem.strip()
        return dataitem

def parseMainData(dataset):
    data = startParse(dataset)
    for __ in range(9):
        data.pop(0)
    for i in range(len(data)):
        data[i] = parserStr(data[i])
    for __ in range(3):
        data.pop()
        data.pop(2)
    data.pop(0)
    data.pop()
    result = {'name': data[0], 'nm': data[1]}
    return result

def parseSpecData(dataset):
    data = startParse(dataset)
    replace_data = ['error', '<a class', 'Количество', 'Базовая', 'Частота'
                    ,'Максимальная','Кэш','Расчетная']
    del_str = []
    for i in range(len(data)):
        for s in replace_data:
            index = data[i].find(s)
            if index == -1:
                continue
            else:
                del_str.append(i)
    for i in range(len(del_str)-1,-1, -1):
        data.pop(del_str[i])
    for i in range(len(data)):
        data[i] = parserStr(data[i])
    data.pop(0)
    data.pop(2)
    data.pop(5)
    data[5] = data[5].replace(']','')
    result = {
        'cores':data[0],
        'thr':data[1],
        'clock':data[3],
        'boost_clock':data[2],
        'cache':data[4],
        'tdp':data[5],
    }
    return result