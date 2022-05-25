#class Student:
    # [assignment] Skeleton class. Add your code here
#    def __init__(self):
#        pass



#Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
#Bob.change_name("Peter")
#Bob.change_age(34)
#Bob.add_track("UI/UX")
#Bob.get_score()

class Student:
    # [assignment] Skeleton class. Add your code here

    #The init Method or Constructor
    def __init__(self, name, age, tracks, score):

    #Instance Variable
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score

        pass

    #Methods
    def change_name(self, name):
        return ("Gideon Bature")

    def change_age(self, age):
        return (24)

    def add_tracks(self, tracks):
        return (["Frontend", "Backend"])

    def get_score(self, score):
        return (20.9)



Bob = Student("Bob", 26, ["FE","BE"], 20.90)

#print(Bob.age)
#print(Bob.tracks)
#print(Bob.score)

# Expected methods
info1 = Bob.change_name("Peter")
info2 = Bob.change_age(34)
info3 = Bob.add_tracks("UI/UX")
info4 = Bob.get_score(20.90)

print(info1)
print(info2)
print(info3)
print(info4)