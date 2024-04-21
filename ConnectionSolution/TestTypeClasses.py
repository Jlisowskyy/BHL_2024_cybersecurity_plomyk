import time

class LinkTestCase:
    start: float
    exp: int
    isClicked: bool
    isReported: bool

    def __init__(self, exp: int = 3):
        self.start = time.time()
        self.exp = exp
        self.isReported = False
        self.isClicked = False

    def IsExpired(self) -> bool:
        expSecs = float(self.exp * 3600 * 24)
        return time.time() > expSecs + self.start

    def IsClicked(self) -> bool:
        return self.isClicked

    def IsReported(self) -> bool:
        return self.isReported