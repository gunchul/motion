import os
import time
import datetime

class Action:
    name = None
    email = None
    url = None

    def __init__(self, name, email, url):
        self.name = name
        self.email = email
        self.url = url

    def read(self):
        f = open(self.name, "r")
        data = f.read()
        f.close()
        return data

    def disable(self):
        f = open(self.name, "w")
        data = f.write("0")
        f.close()
        return

    def enabled(self, data):
        if "1" in data:
            return True
        return False

    def do(self):
        data = self.read()
        if self.enabled(data) == False:
            return 0
        self.disable()
        ts = time.time()
        subject = "%s: Motion is detected" % datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        message = subject + "\n"
        command = 'echo "%s" | mail -s "%s" %s' % (message, subject, self.email)
        os.system(command)
        #print command

#a = Action("state.txt", "gunchul77@gmail.com", "http://192.168.1.201:2048")
#a.do()
