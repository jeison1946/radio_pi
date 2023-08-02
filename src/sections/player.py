import vlc

class Player():
  def __init__(self, playerData):
    self.playerData =  playerData;
    self.player: vlc.MediaPlayer = vlc.MediaPlayer();

  def createMedia(self):
    media = vlc.Media(self.playerData['url']);
    self.player.set_media(media);
  
  def play(self):
    try:
      self.player.play();
      return True;
    except Exception:
      return False;