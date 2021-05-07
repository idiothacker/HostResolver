# HostResolver
HostResolver is a simple python script that can be used to resolve the hostnames of a list of IPs or to get the IPs of a list of hostnames. The results will be saved as a CSV file in a specified directory.

## How to Use
```
-h, --help     show this help message and exit
-r --resolver  The -r argument must be set to "ips" to resolve IPs from hostnames, or set to "hostnames" to resolve hostnames from IPs.
-d --domain    A domain name to append to the hostnames when resolving IPs.
-i --infile    The location of your input file, hostnames or IPs, 1 per line. (-i ".\hosts.txt")
-o --outfile   The location and name of the output file (-o ".\results.csv")
```

To Lookup IP addresses from hostnames.

### IPs to Hostnames Example:
``` bash
python3 HostResolver.py -r ips -d thelargebank.com -i hostnames.txt -o ip_results.csv
```
---
**NOTE**

The domain (-d) argument is not required. If you list already has FQDNs for the host, you should not pass the script a domain. You can also run this without FQDNs or providing a domain, but the resolution may not be as successful.

---

### Hostnames to IPs Example:
``` bash
python3 HostResolver.py -r hostnames -i IPs.txt -o hostnames_result.csv
```
