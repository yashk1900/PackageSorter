import package_sorter
from package_sorter import sort
def test_package_sorter():
    assert(sort(50, 40, 30, 10)=="STANDARD")
    assert(sort(200, 100, 50, 15)=="SPECIAL") 
    assert(sort(100, 50, 20, 25)=="SPECIAL") 
    assert(sort(200, 200, 200, 30)=="REJECTED") 
    assert(sort(10, 10, 10, 5)=="STANDARD") 
    print("All test cases passed!")

if __name__ == "__main__":
    test_package_sorter()