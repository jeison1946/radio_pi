import json
from src.services.display import display
from src.sections.player import Player
from src.services.logger import LoggerService;
from src.services.user_service import UserService;
from src.services.network_service import NetworkService;
from src.services.session_service import Session;



class Main:
    logger = None;
    userService = None;
    sessionService = None;

    def __init__(self):
        if not Main.logger:
            Main.logger = LoggerService();
        if not Main.userService:
            Main.userService = UserService();
        if not Main.sessionService:
            Main.sessionService = Session();

    def initApp(self):
      Main.logger.info("Program started!");
      """ display(); """
      has_internet = NetworkService.check_internet_connection();
      if has_internet:
        response = Main.userService.loginUser();
        if response.status_code == 200:
          loginResponse = json.loads(response.text)
          Main.sessionService.WriteProgress('session.json', json.dumps(loginResponse['payload']));
          Main.logger.info("Login Success");
          Player(LoggerService()).play();
        else:
          Main.logger.critical("Login Failed");
      else:
        Main.logger.info("No internet connection available.");
        self.defaultSong();

    def defaultSong(self):
      songdefault = Player(LoggerService()).playDefault();
      if songdefault:
         self.initApp();