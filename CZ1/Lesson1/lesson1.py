#Pytanie do użytkownika
name=input("What's your name")
try:
    age=int(input("How old are you?"))
except ValueError:
    age=0
try:
    height=float(input("What's your height in meters"))
except:
    height=0

#Odpowiedzi 
print("Hello", name +"!")
print("you are", age, "years old.")
print("your height is", height, "in meters")

