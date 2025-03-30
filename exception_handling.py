#try:
#    file=open("a,txt")
#    dict={"key":"value"}
#    print(dict["key"])
#except FileNotFoundError:
#    file=open("a.txt","w")
#    file.write("something")
#except KeyError as error_message:
#    print(f"The key {error_message} does not exist.")
#else:
#    content=file.read()
#    print(content)
#finally:
#    raise TypeError("This error I made up")

h =float(input("Height:"))
w=int(input("Weight:"))

if h>3:
    raise ValueError("Human height cannot be over 3 meters.")

bmi=w/h**2
print(bmi)