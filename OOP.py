
        #    oop 

# class info:
#     def __init__(self,name,age=18):
#         self.name=name
#         self.age=age

# p1=info("Mustafa",19)
# p2=info("Hamxa")

# print(p1.name,p1.age)
# print(p2.name,p2.age)

# class me:
#     Quantity="too much" 

#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     def greet(self):
#         print(f"name {self.name}, age is {self.age}")

# me.Quantity="Too less"    # modifying class propperty 
# p1=me("mus",19)
# # p1.age=40    #modifying data object 

# print(p1.age)
# print(p1.name)
# p1.greet()

# print(p1.Quantity)



# class info:
#     def __init__(self,name,age,length):
#         self.name=name
#         self.age=age
#         self.length=length

#     def display(self):
#         self.age+=1
#         self.length+=0.74
#         print(f"name is {self.name}, age is {self.age}, length is {self.length }")

# p1=info("Mustafa",20,2.5)
# p1.heigth=5.5  # add new property to obj

# p1.display()
# p1.display()
# # print(p1.heigth)

# class playlist:
#     def __init__(self,name):  #  class assign data 
#      self.name=name
#      self.songs=[]

#     def add (self,song):    #func 
#         self.songs.append(song)
#         print(f"Added: {song}")

#     def removeS(self,song):
#         if song in self.songs:
#          self.songs.remove(song)
#          print(f"Removed: {song}")

#     def showsongs(self):
#         print(f"Playlist {self.name}: ")
#         for song in self.songs:
#             print(f"{song}")



# p1=playlist("Best")
# p1.add("Rock")
# p1.add("Bestein")
# p1.removeS("Rock")
# p1.showsongs()

#inhertiance 


# class papa:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     def display(self):
#         print(f"name of mustafa son is  {self.name}, Age is {self.age }")
#         print(f" saboor father is {self.father},age is {self.ages} ")

# class son(papa):
#     pass

# x=son("saboor",13)
# x.father="Mustafa"
# x.ages="20"

# x.display()


class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def prnt(self):
       print(f"Name is {self.name}, Age is {self.age} ")

class student(person):
    def __init__(self,name,age,year):
     person.__init__(self,name,age)
     super().__init__(name,age)
     self.gradutionYear=year

x=student("Mustafa ",19,2028)

x.prnt()
print(f"year is x.gradutionYear")

# def total():
#   lists=[200,300,400,500]
#   sums=0

#   for x in lists:
#     sums=sums+x

# print(total())

# x=[200,300,400,500]

# def cart_total(x):
#    sums=sum(x)
#    return sums


# def total(sums):
#     if sums >1000:
#         sums=sums - (sums*10/100)
#         return sums
    
#     else:
#         return sums

# totals=cart_total(x)
# final=total(totals)

# print("Amount to pay",{final})





class student:
    def __init__(self,name,marksList):
        self.name=name
        self.marksList=marksList

    def average(self):
        ave=sum(self.marksList)/len(self.marksList)
        return ave

    def grade(self):
        if self.average() > 90:
            return ("A")
        elif self.average() > 70:
            return ("B")

        elif self.average() > 50:
            return ("C")
        
        else:
            return ("F")

    def display(self):
        print(f"name is  {self.name}  Average marks are  {self.average()}  Grade is {self.grade()} ")


s1=student("Mustafa ",[100,40,70,20])

s1.display()







