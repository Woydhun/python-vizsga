class Verseny:
    def __init__(self, sor:str) -> None:
        v:list[str] = sor.strip().split(';')
        self.ev:int = int(v[0])
        self.orszag:str = v[1]
        self.varos:str = v[2]
        self.arany:int = int(v[3])
        self.ezust:int = int(v[4])
        self.bronz:int = int(v[5])
        self.osszeserem:int = self.arany + self.ezust + self.bronz
