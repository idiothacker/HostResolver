import argparse, socket, csv

parser = argparse.ArgumentParser(description="Example: \n\npython3 HostResolver.py -r hostnames -d bankcorp.com -i .\\ip_addresses.txt -o .\\results.csv")
parser.add_argument("-r", metavar="--resolver", help="The -r argument must be set to \"ips\" to resolve IPs from hostnames, or set to \"hostnames\" to resolve hostnames from IPs.", required=True)
parser.add_argument("-d", metavar="--domain", help="A domain name to append to the hostnames when resolving IPs.")
parser.add_argument("-i", metavar="--infile", help="The location of your input file, hostnames or IPs, 1 per line. (-i \".\\hosts.txt\")", required=True)
parser.add_argument("-o", metavar="--outfile", help="The location and name of the output file (-o \".\\results.csv\")", required=True)

args = parser.parse_args()
resolver = args.r
in_file = args.i
domain = args.d
out_file = args.o

def get_ip(host):
    res = {
        "IP Address": "",
        "Hostname": host
    }
    try:
        print(f"Looking up IP for {host}.")
        res["IP Address"] = socket.gethostbyname(host)
        return res
    except:
       print("Unable to resolve IP.\n\n")
       return None 

def get_hostname(ip):
    res = {
        "IP Address": ip,
        "Hostname": ""
    }
    try:
        print(f"Looking up hostname for {ip}")
        host = socket.gethostbyaddr(ip)
        res["Hostname"] = host[0]
        return res
    except:
       print("Unable to get hostname.\n\n")
       return None

if (resolver == "ips") or (resolver == "hostnames"):  
    with open(out_file, "w", newline="") as csvfile:
            fieldnames = ["IP Address", "Hostname"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)   
            writer.writeheader() 

            with open(in_file, "r") as hosts:
                for h in hosts:
                    if domain != None:
                        h = h.strip() + ".".strip() + domain.strip()
                    else:
                        h = h.strip() 
                    if resolver == "ips":
                        res = get_ip(h)
                    else:
                        res = get_hostname(h)
                    if res != None:
                        print(f"{res['IP Address']} :: {res['Hostname']}\n\n")
                        writer.writerow(res)
else:
    print("The -r argument must be set to \"ips\" to resolve IPs from hostnames, or set to \"hostnames\" to resolve hostnames from IPs.")
