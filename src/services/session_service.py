import json

from services.config_service import ConfigService

class Session:
    config = ConfigService();
    def WriteProgress(self, filepath, progress):
      absolte = self.config.get_session_file()+filepath
      with open(absolte, 'w') as outfile:
          outfile.write(progress)
          outfile.close()

    def GetProgress(self, filepath):
      absolte = self.config.get_session_file()+filepath
      try:
        with open(absolte, 'r', encoding='utf-8') as openfile:
          progress = json.load(openfile)
          return progress;
      except FileNotFoundError:
         return False;