
class Microwave:
    def __init__(self, brand: str, power: str) -> None:
        self.brand = brand
        self.power = power
        self.turned_on: bool = False

    def turn_on(self) -> None:
        if self.turned_on:
            print(f'Микров. {self.turned_on} БЫЛА ВКЛЮЧЕНА')
        else:
            self.turned_on = True
            print(f'Микров. {self.turned_on} ВКЛЮЧЕНА ТОЛЬКО ЧТО')

    def turn_off(self) -> None:
        if self.turned_on:
            self.turned_on = False
            print(f'Микров. {self.turned_on} была ВЫКЛЮЧЕНА')
        else:
            print(f'Микров. {self.turned_on} БЫЛА ВЫКЛЮЧЕНА')
        

smeg = Microwave('Smeg', 'C')

smeg.turn_off()
smeg.turn_on()
smeg.turn_off()