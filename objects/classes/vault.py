class Vault:
    def __init__(self, galleons=0, sickles=0, knuts=0):
        self.galleons = galleons
        self. sickles = sickles
        self. knuts = knuts
    
    def __str__(self):
        return f"{self.galleons} - {self. sickles} - {self. knuts}"
    
    def __add__(self, other):
        galleons = self.galleons + other.galleons
        sickles = self.sickles + other.sickles
        knuts = self.knuts + other.knuts
        return Vault(galleons=galleons, sickles=sickles, knuts=knuts)
    
potter = Vault(100, 50, 25)
print(potter)

weasley = Vault(100, 50, 50)
print(weasley)

total = potter + weasley
print(total)