import vlc

from src.services.logger import LoggerService

class Player():
  def __init__(self, playerData, LoggerService: LoggerService):
    self.playerData =  playerData;
    self.player: vlc.MediaPlayer = vlc.MediaPlayer();
    self.logger: LoggerService;
  
  def play(self):
    try:
      media = vlc.Media(self.playerData['url']);
      self.player.set_media(media);
      self.player.play();
    except Exception:
      self.logger.error('Error playing song');
    while True:
      state = self.player.get_state();
      if state == vlc.State.Ended:
          self.play();