
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
    return jsonResponse;

  def logSong(self, dataInfo):
    user = sessionService.GetProgress('session.json');
    fromObject = {
      "title": dataInfo['song']['name'],
      "author": dataInfo['song']['artist'],
      "song_id": dataInfo['song']['self']['id'],
      "pos_id": user['user_data']['punto_de_venta'],
      "rule_id": dataInfo['ruleId']
    }
    endpoint = self.base_url+"/song/history";
    
    Headers = { 
      "Content-Type" : "application/json",
      "X-AUTH-TOKEN" : user['token']
    }
    jsonResponse = requests.post(endpoint, data=json.dumps(fromObject), headers = Headers)
    return jsonResponse
