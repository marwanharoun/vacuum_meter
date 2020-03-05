import datetime

class Timer(object):
    """A simple timer class"""
    
    def __init__(self):
        pass
    
    def start(self):
        """Starts the timer"""
        self.start = datetime.datetime.now()
        return self.start
    
    def stop(self):
        """Stops the timer.  Returns the time elapsed"""
        self.stop = datetime.datetime.now()
        return float(self.stop - self.start)
    
    def now(self):
        """Returns the current time with a message"""
        return float(datetime.datetime.now())
    
    def elapsed(self):
        """Time elapsed since start was called"""
        return str(datetime.datetime.now() - self.start)
    
    def split(self):
        """Start a split timer"""
        self.split_start = datetime.datetime.now()
        return float(self.split_start)
    
    def unsplit(self):
        """Stops a split. Returns the time elapsed since split was called"""
        return float(datetime.datetime.now() - self.split_start)
