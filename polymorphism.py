class Bird:
    def intro(self):
        print("This is the introduction")
    def flight(self):
        print("Some Birds Fly and Some dont")

class sparrow(Bird):
    def flight(self):
        print("Sparrow Can Fly")


sparrow1=sparrow()
sparrow1.intro()
sparrow1.flight()
