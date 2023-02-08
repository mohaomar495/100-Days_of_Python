import math

def main():
    test_h = int(input("Height of wall: "))
    test_w = int(input("Width of wall: "))
    coverage = 5
    paint_calc(height=test_h, width=test_w, cover=coverage)
    
def paint_calc(height, width, cover):
    print(math.ceil((width * height) / cover))

# here is the above function with more breif clarification.
    """
    def paint_calc(height, width, cover):
        area = height * width
        num_cans = area / cover
        print(math.ceil(num_cans))
    """
# The ceil rounds number up to nearest integer
# The floor rounds number down to the nearest integer.

main()