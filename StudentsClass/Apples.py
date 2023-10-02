
class apple:
    grown_stage = ['blooming', 'green', 'red']
    index =1
    def __init__(self,):
        self.index = apple.index
        apple.index += 1
        self.stage = 0
    def ripe(self):
        self.stage += 1

    def is_ripe(self):
        if self.stage > 2:
            return True
        else:
            return False

    def ripe_stage(self):
        if 2 < self.stage < 5:
            return apple.grown_stage[2]
        elif self.stage >= 5:
            return False
        else:
            return apple.grown_stage[self.stage]

class tree:
    def __init__(self, num, *args):
        self.age = 1
        self.apples = []
        self.apples.extend(args)
        self.num = num

    def grow(self):
        import random
        self.age += 10
        if self.age >= 10:
            self.apples =[]
        for ap in self.apples:
            ap.ripe()
            if ap.ripe_stage() == False:
                self.apples.remove(ap)
        if (2 < self.age < 5) and random.random() < 0.7






