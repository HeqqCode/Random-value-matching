import random

#try to find i

type = input("Please enter the type of test you want to run. (in uppercase), [SIGNED TEST/UNSIGNED TEST]")

if type=="SIGNED TEST":
    try:
        #define a random integer i based on user input
        n = 10000*(int(input("ValueLevel: ")))
        i = random.randint(0,n)
    except ValueError:
        #error handling
        print(" invalid operatioN L bozo  ")
        #fallback code
        n = 10
    def findiS():
        #assign testinteger fi
        f_i = 0
        while f_i != i:
            f_i = random.randint(0,n)
            if f_i == i:
                print("Found it!", f_i)
    findiS()
elif type=="UNSIGNED TEST":
    try:
        #define a random integer i based on user input
        n = 1000*(int(input("ValueLevel:")))
        extent = int(input("Extent"))
        i = random.randint(extent,n)
    except ValueError:
        #error handling
        print(" invalid operation LOL boZo ")
        #fallback code
        n = 10
    def findiS():
        #assign testinteger fi
        f_i = 0
        while f_i != i:
            f_i = random.randint(extent,n)
            if f_i == i:
                print("Found it!", f_i)
    findiS()
            

