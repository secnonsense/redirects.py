
import requests
import argparse
from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

def redirect(url):
    if "http" not in url:
        url="http://"+url
    response = requests.get(url, verify=False)

    for r in response.history:
        print("\n" + str(r.status_code), r.url)
        #, r.headers, r.text)

    print("\n" + str(response.status_code), response.url + "\n")


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", help="Use file as input", action="store_true")
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
        redirect(args.input)
    else:
        print(args.help)

if __name__ == "__main__":
    main()
