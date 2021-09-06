
import requests
import argparse
from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

def redirect(url,headers=0,body=0):
    if "http" not in url:
        url="http://"+url
    response = requests.get(url, verify=False)

    for r in response.history:
        print("\n" + str(r.status_code), r.url)
        if headers==1:
            print(r.headers)
        if body==1:
            print(r.text)

    print("\n" + str(response.status_code), response.url + "\n")
    if headers==1:
        print(response.headers)
    if body==1:
        print(response.text)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", help="Use file as input", action="store_true")
    parser.add_argument("-x", "--headers", help="Display headers", action="store_true")
    parser.add_argument("-b", "--body", help="Display body", action="store_true")
    parser.add_argument("input", help="Enter a URL to check redirects or a file with URL's using the -f option")
    return parser.parse_args()

def main():
    args=parse_args()
    if args.file and args.input:
        with open(args.input, 'r',encoding='utf8') as f:
            for url in f:
                redirect(url.strip())
                print("============================")
    elif args.input:
        redirect(args.input,args.headers,args.body)
    else:
        print(args.help)

if __name__ == "__main__":
    main()
