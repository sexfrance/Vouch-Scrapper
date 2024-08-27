import json
import os
from discord.ext import commands
from discord.http import Route
from colorama import Fore, Style
from pystyle import Write, System, Colors, Colorate, Anime
import getpass
from datetime import datetime

token = "enter token here"
username = "your discord username"

class logger:
    def __init__(self, prefix: str = "discord.cyberious.xyz"):
        self.WHITE: str = "\u001b[37m"
        self.MAGENTA: str = "\033[38;5;97m"
        self.MAGENTAA: str = "\033[38;2;157;38;255m"
        self.RED: str = "\033[38;5;196m"
        self.GREEN: str = "\033[38;5;40m"
        self.YELLOW: str = "\033[38;5;220m"
        self.BLUE: str = "\033[38;5;21m"
        self.PINK: str = "\033[38;5;176m"
        self.CYAN: str = "\033[96m"
        self.prefix: str = f"{self.PINK}[{self.MAGENTA}{prefix}{self.PINK}] "


    def get_time(self) -> str:
        return datetime.now().strftime("%H:%M:%S")
    
    def success(self, message: str, start: int = None, end: int = None, level: str = "Success") -> None:
        print(self.message(f"{self.GREEN}{level}", f"{self.GREEN}{message}", start, end))

    def failure(self, message: str, start: int = None, end: int = None, level: str = "Failure") -> None:
        print(self.message(f"{self.RED}{level}", f"{self.RED}{message}", start, end))
    
    def message(self, level: str, message: str, start: int = None, end: int = None) -> None:
        time = self.get_time()
        if start is not None and end is not None:
            print(f"{self.prefix}[{self.MAGENTAA}{time}] {Fore.RESET} {self.PINK}[{self.CYAN}{level}{self.PINK}] -> {Fore.RESET} {self.CYAN}{message}{Fore.RESET} [{Fore.CYAN}{end - start}s{Style.RESET_ALL}]")
        else:
            print(f"{self.prefix}[{self.MAGENTAA}{time}] {Fore.RESET} {self.PINK}[{self.CYAN}{level}{self.PINK}] -> {Fore.RESET} {self.CYAN}{message}{Fore.RESET}")
    

log = logger()

vouches = []
vouches_lengh = 0
username = getpass.getuser()
os.system('cls' if os.name == 'nt' else 'clear')
Write.Print(f"""
\t\t /$$    /$$                               /$$              /$$$$$$                                                                       
\t\t| $$   | $$                              | $$             /$$__  $$                                                                      
\t\t| $$   | $$  /$$$$$$  /$$   /$$  /$$$$$$$| $$$$$$$       | $$  \__/  /$$$$$$$  /$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$ 
\t\t|  $$ / $$/ /$$__  $$| $$  | $$ /$$_____/| $$__  $$      |  $$$$$$  /$$_____/ /$$__  $$ |____  $$ /$$__  $$ /$$__  $$ /$$__  $$ /$$__  $$
\t\t \  $$ $$/ | $$  \ $$| $$  | $$| $$      | $$  \ $$       \____  $$| $$      | $$  \__/  /$$$$$$$| $$  \ $$| $$  \ $$| $$$$$$$$| $$  \__/
\t\t  \  $$$/  | $$  | $$| $$  | $$| $$      | $$  | $$       /$$  \ $$| $$      | $$       /$$__  $$| $$  | $$| $$  | $$| $$_____/| $$      
\t\t   \  $/   |  $$$$$$/|  $$$$$$/|  $$$$$$$| $$  | $$      |  $$$$$$/|  $$$$$$$| $$      |  $$$$$$$| $$$$$$$/| $$$$$$$/|  $$$$$$$| $$      
\t\t    \_/     \______/  \______/  \_______/|__/  |__/       \______/  \_______/|__/       \_______/| $$____/ | $$____/  \_______/|__/      
\t\t                                                                                                 | $$      | $$                          
\t\t                                                                                                 | $$      | $$                          
\t\t                                                                                                 |__/      |__/  
\t\t                                      Welcome {username} | discord.cyberious.xyz  
\t\t                              ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
\t\t  ════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════
""", Colors.red_to_blue, interval=0.0000)

class SelfBot(commands.Bot):

    def __init__(self):
        super().__init__(command_prefix=commands.when_mentioned_or(''), self_bot=True)

    async def on_message(self, message):
        global vouches_lengh

        # Check if the author is a bot
        if message.author.bot:
            return

        content = message.content.lower()
        if "+rep" in content or "+vouch" in content:
            try:
                vouch_data = {}
                split_content = content.split()

                reason = " ".join(split_content[2:len(split_content)])

                vouch_data["id"] = vouches_lengh + 1
                vouch_data["vouched_by"] = message.author.name
                vouch_data["vouched_user"] = username
                vouch_data["stars"] = 5
                vouch_data["message"] = reason

                vouches.append(vouch_data)
                vouches_lengh += 1
                log.message("Success", f"Successfully Saved vouch {vouches_lengh} from {message.author.name} with message: {reason}", )

                with open("vouches.json", "w") as f:
                    json.dump(vouches, f)

            except Exception as e:
                log.failure(f"Failed to save vouch from {message.author.name}: {str(e)}")


bot = SelfBot()
bot.run(token, log_handler=None)
