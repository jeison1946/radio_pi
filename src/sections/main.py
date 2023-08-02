import json
from src.sections.player import Player
from src.services.songs_service import SongService;
from src.services.logger import LoggerService;
from src.services.user_service import UserService;
from src.services.network_service import NetworkService;
from src.services.session_service import Session;



class Main:
    logger = None;
    userService = None;
    sessionService = None;
    songService = None;

    def __init__(self):
        if not Main.logger:
            Main.logger = LoggerService();
        if not Main.userService:
            Main.userService = UserService();
        if not Main.sessionService:
            Main.sessionService = Session();
        if not Main.songService:
            Main.songService = SongService();

    def initApp(self):
      Main.logger.info("Program started!");
      has_internet = NetworkService.check_internet_connection();
      if has_internet:
        user = Main.sessionService.GetProgress('session.json');

        if user:
          Main.logger.info("Login Already");
        else:
          response = Main.userService.loginUser();
          if response.status_code == 200:
            loginResponse = json.loads(response.text)
            Main.sessionService.WriteProgress('session.json', json.dumps(loginResponse['payload']));
            Main.logger.info("Login Success");
          else:
            Main.logger.info("Login Failed");
        
        responseSong = Main.songService.getNextSong();
        if responseSong.status_code == 200:
          pdvResponse = json.loads(responseSong.text);
          Main.logger.info("Punto de venta cargado");
          player = Player(pdvResponse['payload']['song'], LoggerService);
          status = player.play();
        else:
          Main.logger.debug(responseSong.text);
          Main.logger.info("Punto de venta fallido");
      else:
        Main.logger.critical("No internet connection available.")