import json
import vlc;
from src.services.songs_service import SongService;
from src.services.network_service import NetworkService;
from src.services.config_service import ConfigService;

class Player():
  songService = SongService();

  def __init__(self, logger):
    self.player: vlc.MediaPlayer = vlc.MediaPlayer();
    self.logger = logger;
  
  def play(self):
    has_internet = NetworkService.check_internet_connection();
    if has_internet:
      responseSong = self.songService.getNextSong();
      if responseSong.status_code == 200:
        pdvResponse = json.loads(responseSong.text);
        self.logger.info("Punto de venta cargado");
      else:
        self.logger.critical("Punto de venta fallido");
        return False;

      nextSong = pdvResponse['payload'];
      try:
        media = vlc.Media(nextSong['song']['url']);
        self.player.set_media(media);
        self.player.play();
        self.logger.info('Escuchando ' + nextSong['song']['name']);
        self.songService.logSong(nextSong);
      except Exception:
        self.logger.critical('Error al reporducir la canción');
        return False;
      
      while True:
        state = self.player.get_state();
        if state == vlc.State.Ended:
          self.play();
    else:
      self.logger.info("No internet connection available.");
      songdefault = self.playDefault();
      if songdefault:
            self.initApp();

  def playDefault(self):
    config = ConfigService();
    try:
      media = vlc.Media(config.get_backup_path());
      if media:
        self.player.set_media(media);
        self.player.play();
        self.logger.info('Escuchando ' + '7 Rings');
      else:
        self.logger.critical('Error al reporducir la canción');
    except Exception:
      self.logger.critical('Error al reporducir la canción');
      return False;
    
    while True:
      state = self.player.get_state();
      if state == vlc.State.Ended:
        return True;