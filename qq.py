class Bow:
    def __init__(self, quality):
        self.quality = quality
        self.damage = 0

    def up_damage(self,howmany):
        self.damage = self.damage + howmany

    def stats(self):
        return f'Bow quality:{self.quality}, damage:{self.damage}'


if __name__ == '__main__':
    x = Bow('Epic')
    x.up_damage(20)
    with open('file', mode='w') as f:
        f.write(x.stats())
