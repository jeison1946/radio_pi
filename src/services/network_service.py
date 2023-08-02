
import requests

class NetworkService():
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
