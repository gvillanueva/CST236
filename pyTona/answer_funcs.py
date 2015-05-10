import getpass
import random
import socket
import subprocess
import threading
import time

seq_finder = None
woodChuck = None

def feet_to_miles(feet):
    return "{0} miles".format(float(feet) / 5280)

def hal_20():
    return "I'm afraid I can't do that {0}".format(getpass.getuser())

def get_git_branch():
    try:
        process = subprocess.Popen(['git', 'rev-parse', '--abbrev-ref', 'HEAD'], stdout=subprocess.PIPE)
        output = process.communicate()[0]
    except:
        return "Unknown"

    if not output:
        return "Unknown"
    return output.strip()

def get_git_url():
    try:
        process = subprocess.Popen(['git', 'config', '--get', 'remote.origin.url'], stdout=subprocess.PIPE)
        output = process.communicate()[0]
    except:
        return "Unknown"

    if not output:
        return "Unknown"
    return output.strip()

def get_other_users():
    try:
        host = '192.168.64.3'
        port = 1337

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        s.send('Who?')
        data = s.recv(255)
        s.close()
        return data.split('$')

    except:
        return "IT'S A TRAAAPPPP"


class FibSeqFinder(threading.Thread):
    def __init__(self, *args, **kwargs):
        super(FibSeqFinder, self).__init__(*args, **kwargs)
        self.sequence = [0, 1]
        self._stop = threading.Event()
        self.num_indexes = 0

    def stop(self):
        self._stop.set()

    def run(self):
        self.num_indexes = 0
        while not self._stop.isSet() and self.num_indexes < 1000:
            self.sequence.append(self.sequence[-1] + self.sequence[-2])
            self.num_indexes += 1
            time.sleep(.04)

def get_fibonacci_seq(index):
    index = int(index)
    global seq_finder
    if seq_finder is None:
        
        seq_finder = FibSeqFinder()
        seq_finder.start()

    if index > seq_finder.num_indexes:
        value = random.randint(0, 9)
        if value >= 4:
            return "Thinking..."
        elif value > 1:
            return "One second"
        else:
            return "cool your jets"
    else:
        return seq_finder.sequence[index]

class WoodChuck(threading.Thread):
    def __init__(self, secs, *args, **kwargs):
        super(WoodChuck, self).__init__(*args, **kwargs)
        self.secs = secs
        self.chuckedCords = 0
        self._stopEvent = threading.Event()
        self.t = None

    def stop(self, *args, **kwargs):
        self._stopEvent.set()
        if self.t is not None:
            self.t.cancel()

    def run(self):
        self.t = threading.Timer(10.0, self.stop)
        self.t.start()
        while not self._stopEvent.isSet():
            self.chuckedCords += 1
            time.sleep(1)

    def isDone(self):
        return self._stopEvent.isSet()

def chuck_wood(secs):
    secs = int(secs)
    global woodChuck
    if woodChuck is None:
        woodChuck = WoodChuck(secs)
        woodChuck.start()

    if woodChuck.isDone():
        return woodChuck.chuckedCords
    else:
        return 'Busy chucking'

def find_the_answer():
    t = threading.Timer(7.5, the_answer)
    t.start()
    return None

def the_answer():
    return 42