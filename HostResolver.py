import argparse, socket, csv, concurrent.futures

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

def get_ip(host,host_list):
    res = {
        "IP Address": "",
        "Hostname": host
    }
    current = host_list.index(host) + 1
    total = len(host_list)
    try:
        print(f"Looking up IP for {host}. [{current}/{total}]")
        res["IP Address"] = socket.gethostbyname(host)
        return res
    except:
       return None 

def get_hostname(ip,host_list):
    res = {
        "IP Address": ip,
        "Hostname": ""
    }
    current = host_list.index(ip) + 1
    total = len(host_list)
    try:
        print(f"Looking up hostname for {ip}. [{current}/{total}]")
        host = socket.gethostbyaddr(ip)
        res["Hostname"] = host[0]
        return res
    except:
       return None

if (resolver == "ips") or (resolver == "hostnames"):
    host_list = []
    
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
                host_list.append(h)
            
        with concurrent.futures.ThreadPoolExecutor() as executor:
            if resolver == "ips":
                results = [executor.submit(get_ip, h,host_list) for h in host_list]
            else:
                results = [executor.submit(get_hostname, h,host_list) for h in host_list]
            for f in concurrent.futures.as_completed(results):
                if f.result() != None:
                    writer.writerow(f.result())
else:
    print("The -r argument must be set to \"ips\" to resolve IPs from hostnames, or set to \"hostnames\" to resolve hostnames from IPs.")
