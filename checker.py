#!/usr/bin/python3
""" Command Line Interpreter Checker Interface. """
from modules.request_correction import request_correction
from modules.show_result import show_result
from modules.get_project import get_tasks
from modules.get_auth import get_auth

from os import path, get_terminal_size, getenv, makedirs
from getpass import getpass
from time import sleep
from cmd import Cmd
import json
import signal  # manage Ctrl-C

# GLOBAL VARIABLES
PATH_CREDS = path.expanduser('~/.config/hbn/hbnb_creds')
PATH_TOKEN = '/tmp/.hbnb_auth_token'
VERSION = 'v0.4 (tavo)'
REPO = "https://github.com/Athesto/CLI_Checker"
# Color format for text printing.
y = '\033[38;5;220m'  # Yellow.
g = '\033[92m'  # Green.
r = '\033[91m'  # Red
rs = '\033[m'  # Reset.

# Get the size of the tty.
size = get_terminal_size()
columns = size.columns

# debug credentials: This information should be in the .env file as
# EMAIL=<debugging-email>
# ENABLE=True/False
# API=<your-api-key>
# PASSWORD=<your-password>
debug = bool(getenv('DEBUG', False))
debug_cred = {
    "enable": debug,
    "email": getenv('EMAIL'),
    "api": getenv('API'),
    "password": getenv('PASSWORD')
}

if (debug is True):
    print(debug_cred)


class CLI_Checker(Cmd):
    """ Class for controling the main loop of the Checker's Console. """

    # Class variables.
    yes_no_list = ['y', 'n', 'no', 'yes']
    task_dict = {}

    # Custom prompt definition.
    prompt = y + 'CLI-Checker ⚡ ' + rs

    # Help custom instance variables.
    doc_header = "🤔 Currently availbale commands are: 🤔"
    ruler = y + "─" + rs
    original_handler_ctrl_c = signal.getsignal(signal.SIGINT)

    def __init__(self):
        super().__init__()
        signal.signal(signal.SIGINT, self._ctrl_c_ignored)

    def _ctrl_c_ignored(self, signal, frame):
        '''Ignore SIGINT signal'''
        print('^C')
        print(self.prompt, end='', flush=True)

    # Overrides the preloop class method. - - - - - - - - - - - - - - - - - - |
    def preloop(self):
        """ Method that runs before the main loop of the console. """
        if path.exists(PATH_CREDS):
            with open(PATH_CREDS, 'r') as f:
                creds = json.load(f)
                email = creds['email']
                api = creds['api']
                password = creds['password']
                get_auth(email, api, password)
        else:
            if path.exists(PATH_TOKEN):
                return
            else:
                print('Credentials not found')
                print('\033[2J', end='')

                self.start_up()

    # 1st time startup method.- - - - - - - - - - - - - - - - - - - - - - - -|
    def start_up(self):
        """ Start-up method for getting and storing the user's credentials. """
        # Strings for 1st time welcome pre-message.
        if (debug is False):
            welcome_l0 = "Hi"
            welcome_l1 = "This is the"
            welcome_l2 = "CLI-Checker {}".format(VERSION)
            welcome_l3 = "We hope you enjoy"
            welcome_l4 = "Please"
            welcome_l5 = "Report any issues"
            welcome_l6 = "At:"
            welcome_l7 = REPO
            welcome_l8 = "Follow us in Twitter:"
            welcome_l9 = "https://twitter.com/LopezDfelo93"
            welcome_l10 = "https://twitter.com/wisvem"
            welcome_l11 = "https://twitter.com/leovalsan_dev"

            # Calculate the space around each line's welcome message.
            welcome_s0 = ' ' * ((columns // 2) - 1 - len(welcome_l0) // 2)
            welcome_s1 = ' ' * ((columns // 2) - 1 - len(welcome_l1) // 2)
            welcome_s2 = ' ' * ((columns // 2) - 1 - len(welcome_l2) // 2)
            welcome_s3 = ' ' * ((columns // 2) - 1 - len(welcome_l3) // 2)
            welcome_s4 = ' ' * ((columns // 2) - 1 - len(welcome_l4) // 2)
            welcome_s5 = ' ' * ((columns // 2) - 1 - len(welcome_l5) // 2)
            welcome_s6 = ' ' * ((columns // 2) - 1 - len(welcome_l6) // 2)
            welcome_s7 = ' ' * ((columns // 2) - 1 - len(welcome_l7) // 2)
            welcome_s8 = ' ' * ((columns // 2) - 1 - len(welcome_l8) // 2)
            welcome_s9 = ' ' * ((columns // 2) - 1 - len(welcome_l9) // 2)
            welcome_s10 = ' ' * ((columns // 2) - 1 - len(welcome_l10) // 2)
            welcome_s11 = ' ' * ((columns // 2) - 1 - len(welcome_l11) // 2)

            # Add color for the line 2 after spaces calculation above.
            welcome_l2 = "CLI-Checker" + g + " " + VERSION + rs

            # Start of printing animation...
            # \033[2;0f resets the cursor to line 2 column 0 of the terminal.
            print("\033[5;0f", end='')
            print("\033[2;0f", end='')
            print(welcome_s0 + welcome_l0 + welcome_s0)
            sleep(2)

            print(welcome_s1 + welcome_l1 + welcome_s1)
            sleep(1.5)

            print(welcome_s2 + welcome_l2 + welcome_s2)
            sleep(1.5)

            print("\033[2;0f", end='')
            print(welcome_s3 + welcome_l3 + welcome_s3)
            sleep(1.5)

            print(welcome_s4 + welcome_l4 + welcome_s4)
            sleep(1.5)

            print(welcome_s5 + welcome_l5 + welcome_s5)
            sleep(1.5)

            print("\033[2;0f", end='')
            print(welcome_s6 + welcome_l6 + welcome_s6)
            sleep(1.5)

            print(welcome_s7 + welcome_l7 + welcome_s7)
            sleep(1.5)

            print(welcome_s8 + welcome_l8 + welcome_s8)
            sleep(1.5)

            print("\033[2;0f", end='')
            print(welcome_s9 + welcome_l9 + welcome_s9)
            sleep(1.5)

            print(welcome_s10 + welcome_l10 + welcome_s10)
            sleep(1.5)

            print(welcome_s11 + welcome_l11 + welcome_s11)
            sleep(1.5)

        # Get user credentials with input box.- - - - - - - - - - - - - - - - |
        print("\033[5;0f", end='')
        print('┌' + '─' * (columns - 2) + '┐')  # These 3 lines print the box
        print('│' + ' ' * (columns - 2) + '│')  # Needs to be stored in a
        print('└' + '─' * (columns - 2) + '┘')  # Variable, somehow...
        print("\033[6;3f", end='')
        if (debug is True):
            email = debug_cred['email']
        else:
            email = str(input("Please enter your holberton e-mail: "))

        print("\033[5;0f", end='')
        print('┌' + '─' * (columns - 2) + '┐')
        print('│' + ' ' * (columns - 2) + '│')
        print('└' + '─' * (columns - 2) + '┘')
        print("\033[6;3f", end='')
        if (debug is True):
            api = debug_cred['api']
        else:
            api = str(input("Please enter your API key: "))

        print("\033[5;0f", end='')
        print('┌' + '─' * (columns - 2) + '┐')
        print('│' + ' ' * (columns - 2) + '│')
        print('└' + '─' * (columns - 2) + '┘')
        print("\033[6;3f", end='')
        if (debug is True):
            password = debug_cred['password']
        else:
            password = getpass("\033[6;3fPlease enter your password: ")

        # Load custom mock loading Bar... - - - - - - - - - - - - - - - - - - |
        i = 0
        print("\033[6;3f", end='')
        while i < columns - 3:
            sleep(0.01)
            print('▋' * i)
            print("\033[6;3f", end='')
            i += 1
        print('\n')

        auth_status = get_auth(email, api, password)

        if auth_status is None:
            return

        # If got correct authentication. - - - - - - - - - - - - - - - - - - -|
        if '200' in auth_status:
            success = "🥳 Correct Login 🥳"
            success_space = ' ' * ((columns - len(success) - 4) // 2)
            print('\033[92m', end='')
            print("\033[5;0f", end='')
            print('┌' + '─' * (columns - 2) + '┐')
            print('│' + success_space + success + success_space, end='│')
            print('└' + '─' * (columns - 2) + '┘')
            print('\033[m', end='')
            print("\033[6;3f", end='')
            sleep(3)

            question = ("Would you like to store these credentials "
                        "for future sessions Y/N?: ")
            answer = ""
            print("\033[5;0f", end='')
            print('\033[92m', end='')
            print('┌' + '─' * (columns - 2) + '┐')
            print('│' + ' ' * (columns - 2) + '│')
            print('└' + '─' * (columns - 2) + '┘')
            print('\033[m', end='')
            print("\033[6;3f", end='')
            answer = str(input(question)).lower()
            while answer not in self.yes_no_list:
                print("\033[5;0f", end='')
                print('\033[92m', end='')
                print('┌' + '─' * (columns - 2) + '┐')
                print('│' + ' ' * (columns - 2) + '│')
                print('└' + '─' * (columns - 2) + '┘')
                print('\033[m', end='')
                print("\033[6;3f", end='')
                answer = str(input("Please answer Yes or No: "))

            if answer in ['yes', 'y']:
                try:
                    makedirs(path.dirname(PATH_CREDS))
                except FileExistsError as f:
                    pass
                with open(PATH_CREDS, 'w+') as f:
                    cred = 'Your Credentials have been stored in {}'
                    cred.format(PATH_CREDS)
                    json.dump({'email': email, 'api': api,
                               'password': password, 'token': ""}, f)
                    print("\033[5;0f", end='')
                    print('\033[92m', end='')
                    print('┌' + '─' * (columns - 2) + '┐')
                    print('│' + ' ' * (columns - 2) + '│')
                    print('└' + '─' * (columns - 2) + '┘')
                    print('\033[m', end='')
                    print("\033[6;{}f".format((columns - len(cred)) // 2),
                          end='')
                    cred = 'Your Credentials have been stored in '
                    print(cred + g + " " + PATH_CREDS + " " + rs)
                    sleep(2)
                print('')

        elif auth_status:
            for key, value in auth_status.items():
                error = value['error']
                print(r, end='')
                print("\033[5;0f", end='')
                print('┌' + '─' * (columns - 2) + '┐')
                print('│' + ' ' * (columns - 2) + '│')
                print('└' + '─' * (columns - 2) + '┘')
                print("\033[6;{}f".format((columns - len(error)) // 2), end='')
                print(error + rs, end='')
            self.start_up()

        else:
            return False

    # Project command - - - - - - - - - - - - - - - - - - - - - - - - - - - - |
    def do_project(self, arg):
        """\n""" \
            """  ┌\033[92m─\033[m Fetches and updates the current project.\n""" \
            """  │\n""" \
            """  └─┬\033[92m─\033[m Usage:\n""" \
            """    │\n""" \
            """    ├──\033[92m─\033[m project <\033[92mnum\033[m>\n""" \
            """    │\n""" \
            """    ├\033[92m─\033[m The \033[92mnum\033[m variable represents """ \
            """the number from\n""" \
            """    │  the project's url in your current Holberton proje""" \
            """ct.\n""" \
            """    │\n""" \
            """    └─┬\033[92m─\033[m Example:\n""" \
            """      │\n""" \
            """      ├\033[92m─\033[m From: https://intranet.hbtn.io/projects""" \
            """/\033[92m212\033[m\n""" \
            """      │\n""" \
            """      └\033[92m─\033[m Run: project \033[92m212\033[m\n""" \

        self.task_dict = get_tasks(arg)

        if self.task_dict is None:
            return

        print('\n'
              '  ┌\033[92m─\033[m You may now run:\n'
              '  │\n'
              '  └─┬\033[92m─\033[m check <\033[92mtask number\033[m>\n'
              '    ├ To check a specific task.\n'
              '    │\n'
              '    ├\033[91m─\033[m check\033[91m Not implemented yet'
              '🤕, Sorry.\033[m\n'
              "    ├ \033[91mTo check all tasks of current project.\033[m\n"
              '    └─┐\n'
              '      ├\033[92m─\033[m To check only task 2 you would run\n'
              '      │\n'
              '      └\033[92m─\033[m Example: check \033[92m2\033[m\n')

    # Check command - - - - - - - - - - - - - - - - - - - - - - - - - - - - - |
    def do_check(self, arg):
        '''\n''' \
            '''  ┌\033[92m─\033[m You may now run:\n''' \
            '''  │\n''' \
            '''  └─┬\033[92m─\033[m check <\033[92mtask number\033[m>\n''' \
            '''    ├ To check a specific task.\n''' \
            '''    │\n''' \
            '''    ├\033[91m─\033[m check\033[91m Not implemented yet''' \
            '''🤕, Sorry.\033[m\n''' \
            '''    ├ \033[91mTo check all tasks of current project.\033[m\n''' \
            '''    └─┐\n''' \
            '''      ├\033[92m─\033[m To check only task 2 you would run\n''' \
            '''      │\n''' \
            '''      └\033[92m─\033[m Example: check \033[92m2\033[m\n'''
        # If tasks dictionary is empty try reading from project file.
        if path.exists('/tmp/.hbnb_current_project'):
            with open('/tmp/.hbnb_current_project') as f:
                self.task_dict = json.load(f)

        if bool(self.task_dict) is False:
            print('\n'
                  '  ┌\033[92m─\033[m Please run the command below:\n'
                  '  │\n'
                  '  └─┬\033[92m─\033[m project <\033[92mnum\033[m>\n'
                  '    │\n'
                  '    │  So that you can store the project into memory.\n'
                  '    │\n'
                  "    │  You can get the number from the intranet's "
                  'project url:\n'
                  '    └─┐\n'
                  '      ├\033[92m─\033[m https://intranet.hbtn.io/projects/'
                  '\033[92m212\033[m\n'
                  '      │\n'
                  '      └\033[92m─\033[m Example: project \033[92m212\033[m\n')
            return

        if arg not in self.task_dict:
            print('There is no task # {}'.format(arg))
            return

        try:
            signal.signal(signal.SIGINT, self.original_handler_ctrl_c)
            correction_id = request_correction(self.task_dict[arg][1])
            show_result(correction_id, self.task_dict, arg)
        except:
            print("\n\nstop")
        finally:
            signal.signal(signal.SIGINT, self._ctrl_c_ignored)

    def do_EOF(self, arg):
        """ Exits console when receiving an EOF (Ctrl-D)"""
        print("goodbye")
        return True

    def emptyline(self):
        """ Overwriting the emptyline method. """
        return False

    def do_quit(self, arg):
        """ Quit command to exit the console. """
        return True


if __name__ == '__main__':
    from os import get_terminal_size

    space_around = ' ' * \
        ((columns - len('┌───────────────────────────┐')) // 2)
    s = space_around

    CLI_Checker().cmdloop(
        s + '┌───────────────────────────┐\n' +
        s + '│         CLI-Checker       │\n' +
        s + '│         ' + g + VERSION + rs + '       │\n' +
        s + '│            by:            │\n' +
        s + '│ 🔥' + y + '     Diego Lopez     ' + rs + '🔥 │\n' +
        s + '│ 🔥' + y + '    Wiston Venera    ' + rs + '🔥 │\n' +
        s + '│ 🔥' + y + '  Leonardo Valencia  ' + rs + '🔥 │\n' +
        s + '│ 🔥' + y + '    Gustavo Mejia    ' + rs + '🔥 │\n' +
        s + '└───────────────────────────┘\n'
        'Please run help to see available commands..')
