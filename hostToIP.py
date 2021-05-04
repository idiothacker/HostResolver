import argparse, csv, socket

parser = argparse.ArgumentParser(description="This tool is a Hostname to IP resolver.")
parser.add_argument("-d", metavar="--domain", help="A domain name to append to the hostnames.", required=True)
parser.add_argument("-hL", metavar="--hosts", help="The location of a hostname list file, 1 host per line. (\".\\hosts.txt\")", required=True)
parser.add_argument("-o", metavar="--outfile_file", help="The location and name of the output file (\".\\results.csv\")", required=True)

args = parser.parse_args()
in_file = args.hL
domain = args.d
out_file = args.o

def get_ip(host):
    res = {
        "IP Address": "",
        "Hostname": host
    }
    try:
        res["IP Address"] = socket.gethostbyname(host)
        return res
    except:
       return None 

with open(out_file, "w", newline="") as csvfile:
    fieldnames = ["IP Address", "Hostname"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)   
    writer.writeheader() 

    with open(in_file, "r") as hosts:
        for h in hosts:
            h = h.strip() + ".".strip() + domain.strip()
            print(h)
            res = get_ip(h)
            if res != None:
                writer.writerow(res)
