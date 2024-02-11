# General Kenobi would like to say....
def hello():    
    print('Well Hello there')

# Vader Responds with a taunt and his favorite numbers
def pack(x,y,z):
    return[x,y,z]

def eat_lunch(lunch):
    if len(lunch) == 0:
        print("I'M GONNA STARVE")
    else:
        for i in range(len(lunch)):
            if i == 0:
                print(f"First I'mma eat my {lunch[0]}")
            else:
                print(f"Next I'mma smash the {lunch[i]}")

    

hello()
print(pack("You will","Know the power","of the force"))
print(pack(56,52181,7516))
eat_lunch([])
eat_lunch(["sammich"])
eat_lunch(["pudding","chips","pickles","moar pudding"])