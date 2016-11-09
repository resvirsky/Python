def start(current=0,birth=0):
    birth=BirthYear(birth)
    current=CurrentYear(x)

def CurrentYear(x):
    x=2016

def BirthYear(birth):
    stop = True
    while stop:
        birth = int(raw_input("\nWhen were you born? Type the year: "))
        if birth==0:
            birth = int(raw_input("\nWhen were you born? Type the year: "))
        elif birth>=2016:
            print ("\nImpossible to be born in the future, Type again: ")
        else:
            print ("\nThanks!")
        
if __name__ == "__main__":
    start()


"""
def age(current,BirthYear):
    age=2016-BirthYear()
    
print age(2016,BirthYear())
"""

"""
if age(current,BirthYear())>19:
    print 'You are an adult'
elif age(current,BirthYear())>=13 and age(current,BirthYear())<=19:
    print 'You are a teenager'
else:
    print 'You are a child'

"""

"""
def reset (birth):
    birth != 0
    start(current,birth)
"""

"""
    if birth!= 0:
        print("\Thank you!")
    else:
        stop = True
        while stop:
            if birth == 0:
                birth = raw_input("\nWhen were you born? Type the year")
                if birth != 0:
                    print ("\nYou were born in {} !")
                    stop = False
    return birth
"""
