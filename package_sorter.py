def sort(width, height, length, mass):

    volume = width * height * length
    is_bulky = volume >= 1000000 or width >= 150 or height >= 150 or length >= 150
    is_heavy = mass >= 20
    
    if is_bulky and is_heavy:
        return "REJECTED"
    elif is_bulky or is_heavy:
        return "SPECIAL"
    else:
        return "STANDARD"
# Standard package
assert(sort(50, 40, 30, 10)=="STANDARD")
assert(sort(200, 100, 50, 15)=="SPECIAL") 
assert(sort(100, 50, 20, 25)=="SPECIAL") 
assert(sort(200, 200, 200, 30)=="REJECTED") 
assert(sort(10, 10, 10, 5)=="STANDARD") 

