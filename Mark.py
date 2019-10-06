class Mark:
    def __init__(self, code, name, lat, longt):
        self.code = code
        self.name = name
        self.lat = lat
        self.longt = longt

    def describe(self):
        return f"Code: {self.code}, Name: {self.name}, Psn{self.lat}, {self.longt}"
