import urllib.parse
import datetime
import time
class WaitFor():
    def __init__(self,delay):
        self.delay=delay
        self.domains=dict()

    def wait(self,url):
        domain=urllib.parse.urlparse(url).netloc
        last_down=self.domains.get(domain)
        if self.delay>0 and last_down is not None:
            sleep_sec=self.delay-(datetime.datetime.now()-last_down).seconds
            if sleep_sec>0:
                time.sleep(sleep_sec)

        self.domains[domain]=datetime.datetime.now()