def start():
    f_name = "Renato"
    l_name = "Svirsky"
    age = 28
    gender = "Male"
    get_info(f_name,l_name,age,gender) 


def get_info(f_name,l_name,age,gender):
    print ("My name is {} {}. I am {} years old and {}.".format(f_name,l_name,age,gender))


if __name__ == "__main__":
    start()
