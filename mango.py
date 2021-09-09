class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = str(age)

  def myfunc(abc):
    print("Hello my name is " + abc.name)

    print("hello my age is " + abc.age)
p1 = Person("John", 36)
p1.myfunc()

