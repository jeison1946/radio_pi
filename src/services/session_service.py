import json

class Session:
    def WriteProgress(self, filepath, progress):
      absolte = './data/'+filepath
      with open(absolte, 'w') as outfile:
          outfile.write(progress)
          outfile.close()

    def GetProgress(self, filepath):
      absolte = './data/'+filepath
      try:
        with open(absolte, 'r', encoding='utf-8') as openfile:
          progress = json.load(openfile)
          return progress;
      except FileNotFoundError:
         return False;