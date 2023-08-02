
import json
import requests
from src.services.config_service import ConfigService
from src.services.session_service import Session
sessionService = Session();


class SongService:
  config = ConfigService();
  def __init__(self) -> None:
    self.base_url = self.config.get_url();

  def getNextSong(self):
    user = sessionService.GetProgress('session.json');
    Headers = { "X-AUTH-TOKEN" : user['token'] }
    endpoint = self.base_url + "/player/next/" + str(user['user_data']['punto_de_venta'])
    jsonResponse = requests.get(endpoint, headers = Headers)
    return jsonResponse
