from googlesearch import search


def get_links(query:str)->list[str]:
    sites = ['dns-shop.ru', 'citilink.ru', 'regard.ru', 'onlinetrade.ru']

    dnsLinks = []
    citiLinks = []
    regardLinks = []
    onlineLinks = []

    for i in range(4):
        for link in search(query=query+sites[i], tld="co.in", num=1, stop=1, pause=2):
            match i:
                case 0:
                    dnsLinks.append(link)
                case 1:
                    citiLinks.append(link)
                case 2:
                    regardLinks.append(link)
                case 3:
                    onlineLinks.append(link)
    result = [
        dnsLinks[0],
        citiLinks[0],
        regardLinks[0],
        onlineLinks[0],
    ]
    return result

query = 'ryzen 5 3600 oem site:'
