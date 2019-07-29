import ipaddress

def main():
    fileIP = open("IPs.txt")
    ipList = []
    ipExclude = []
    ipFinal = []
    for line in fileIP:
        line = line.rstrip()
        ip = ipaddress.ip_network(line)
        ipList.append(ip)
    fileExclude = open("IPsToExclude.txt")
    for line in fileExclude:
        line = line.rstrip()
        ip = ipaddress.ip_network(line)
        ipExclude.append(ip)

    for ip in ipList:
        exclude = 0
        for ipe in ipExclude:
            if ip.overlaps(ipe):
                exclude = 1
                ipFinal.extend(list(ip.address_exclude(ipe)))
        if exclude == 0:
            ipFinal.extend(ip)

    fileFinal = open("IPFinal.txt", "w")
    for iprange in ipFinal:
        fileFinal.write("".join(str(iprange)))
        fileFinal.write("\n")


if __name__ == '__main__':
    main()
