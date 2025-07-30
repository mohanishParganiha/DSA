steps = 8
path = "DDUUUUDD"


def countingVallleys(steps:int, path:str)->int: # return the number of valleys the hicker went to 
    # check the number of valleys by check if the previous is "U" and current alltitude is 0
    # that means the hicker just came out of valley and touched the sea level 
    # it only count as a valley if the hicker touches sea level (alltitude = 0)

    alltitude = 0 # always starts at sea level
    previous = None
    valley_counter = 0

    for char in path:

        if previous == "u" and alltitude == 0:
            valley_counter += 1

        if char.lower() == "u":
            alltitude += 1
        else :
            alltitude -= 1


        previous = char.lower()
        
    return valley_counter


print(countingVallleys(steps=steps , path = path))