import netifaces
import requests

class NetworkService():
    
    @staticmethod
    def get_ipaddress():
        interfaces = [interface for interface in netifaces.interfaces(
        ) if interface.startswith("eth")]

        for interface in interfaces:
            addrs = netifaces.ifaddresses(interface)
            ip = addrs.get(netifaces.AF_INET)

            if ip and "addr" in ip[0]:
                return "IP: " + ip[0]["addr"]

        return ""


    @staticmethod
    def check_internet_connection() -> bool:
        url = "http://www.google.com"
        timeout = 5  # Adjust the timeout value as needed
        try:
            response = requests.head(url, timeout=timeout)
            if response.status_code == 200:
                return True
            else:
                return False

        except requests.ConnectionError:
          return False
