

import json
import requests

from src.services.config_service import ConfigService


class UserService:
  config = ConfigService();
  def __init__(self) -> None:
    self.base_url = self.config.get_url();
    self.user = self.config.get_user();
    self.password = self.config.get_pass();
  
  def loginUser(self):
    fromObject = {
      "username": 'jeison',
      "password": 'jeison',
    }
    endpoint = self.base_url+"/user/login";
    Headers = { "Content-Type" : "application/json" }
    jsonResponse = requests.post(endpoint, data=json.dumps(fromObject), headers = Headers)
    return jsonResponse
