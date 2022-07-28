alist1 = ["Hello", "How are", "you"]
list2 = ["Hai Im" "Good"]
list4 = ["My name is Wasel and yours"]
list3 = ["Waht is your name"]
list5 = ["My name is Max"]

print(list1)

print(list2)
print(list3)
print(list4)
print(list5)


list11 = ["13+13=", 26,  True, "im abc sind", 27, "buchtaben" ,False]
 
print(list11)
list6 = [ "Mahte test"]


thislists = ["Quatch", "Adiren", "Quatch"]
print(thislists[-2])

thislistsee = ["Quatch", "Suptrachiren", "Quatch"]
print(thislistsee[-2])

Thislists = ["Quatch", "Quatch", "dividreien"]
print(Thislists[-1])

thislistsees = ["Quatch", "Quatch", "I love ", "you mom", "°-°", "Quatch", "Quatch"]
print(thislistsees[2:5])




thislist = ["I", "love", "you", "mom", "and...", "Quatch", "Quatch"]
print(thislist[:5])


list9 = ["famlie", "is ", "the"]

list9.append("best")

print(list9)

thhislist = ["Ohne","kann ", "man","nichts"]

thhislist.insert(1, "Famile")
print(thhislist)

thislistt = ["Namen", "banana", "auseinander halten", "zu können"]
thislistt[1:2] = ["werden genutz ", "um Menschen"]
print(thislistt) 


thislist = ["Hallo mein name ist wasel"]
thislist.clear()
print(thislist)

thislist = ["Hallo mein ", " name ist", "Wasel"]
for x in thislist:
  print(x)

thislist = [5, 1, 2, 4, 5]

thislist.sort()

print(thislist)



thislist = [4, 5, 3, 2, 1]
thislist.sort(reverse = True)
print(thislist)


def myfunc(n):
  return abs(n - 4)

thislist = [5, 4, 3, 2, 1]

thislist.sort(key = myfunc)

print(thislist)


thislist = ["your", "the", "best"]
mylist = list(thislist)
print(mylist)


list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3) 



x = 9892984932

if x > 103332323:
  print("Tahts a big number")
  if x >  999999999999999:
    print("...")
  else:
    print("its now a small number")




    i = 1
while i < 6:
  print(i)
  if (i == 3):
    break
  i += 1
cars = ["Ford", "Volvo", "BMW"]

cars[0] = "Toyota"

print(cars)


cars = ["Ford", "Volvo", "BMW"]

x = len(cars)

print(x)
cars = ["Ford", "Volvo", "BMW"]

for x in cars:
  print(x)

cars = ["Ford", "Volvo", "BMW"]

cars.append("Honda")

print(cars)
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("wasel", 12)

print(p1.name)
print(p1.age) 

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("wasel", 12)
p1.myfunc()


class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

 
x = Person("wasel", "alhassan")
x.printname()

mystr = "Wasel"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

username = input("Enter username:")
print("Username is: " + username)
