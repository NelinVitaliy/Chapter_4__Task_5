
class Guns:
    def __init__(self, guns):
        self.guns = guns


class Solders:
    def __init__(self, name, guns):
        self.name = name
        self.guns = guns


class ActOfShooting(Solders, Guns):
    def __init__(self, name, guns):
        Solders.__init__(self, name, guns)
        Guns.__init__(self, guns)

    def solder_fire(self):
        for i in range(0, 10):
            print(f'Solder {self.name} of {self.guns} fire....tigi-tigitishh')
        print('Out of ammo! Need reload!!!')

    def solder_reload(self):
        return f'Solder {self.name} reload his {self.guns}\n'


# ryan = Solders('Ryan', 'AK-47')
valera = Solders('Valera', 'Automatic pistol Stechkin')

ActOfShooting.solder_fire(valera)
print(ActOfShooting.solder_reload(valera))
# print(ActOfShooting.solder_fire(ryan))
# print(ActOfShooting.solder_reload(ryan))
