def main():
    # rectangle with a length, width, and calculated area
    class rectangle:
        def __init__(self, length,width):
            self.length = length
            self.width = width
        
        def area(self):
            return self.length * self.width
        
        def __str__(self):
            return f"Rect({self.length},{self.width},{self.area()})" 
    # triangle with a base, height, and calculated area
    class triangle:
        def __init__(self, base, height):
            self.base = base
            self.height = height
        
        def area(self):
            return int((self.base * self.height)/2)
        
        def __str__(self):
            return f"Tri({self.base},{self.height},{self.area()})"
    # circle with a radius and calculated area
    class circle:
        def __init__(self,radius):
            self.radius = radius
        
        def area(self):
            return int(3.14 * (self.radius ** 2))
        
        def __str__(self):
            return f"Circ({self.radius},{self.area()})"   
    # continue to run until stop character is input('0')
    while True:
        try:
            # print the available options
            print("Select an Option:\n\t1.Rectangle\n\t2.Triangle\n\t3.Circle\n\t0.EXIT", end='\n')
            choice = int(input("Choice: "))
            # if the input is the first choice quit running
            if(choice == 0):
                print("Exiting Program...")
                break
            # user input for the length and width of a rectangle
            elif(choice == 1):
                l = int(input("Enter a length: "))
                w = int(input("Enter a width: "))
                rect = rectangle(l,w)
                # prints info about the rectangle
                print(rect)
            # user input for the base and height of a triangle
            elif(choice == 2):
                b = int(input("Enter a base: "))
                h = int(input("Enter a height: "))
                tri = triangle(b,h)
                # prints info about the triangle
                print(tri)
            # user input for the radius of a circle
            elif(choice == 3):
                r = int(input("Enter a radus: "))
                circ = circle(r)
                # prints info about the circle
                print(circ)
            else:
                # Invalid choice if not a number or greater than 3
                print("Invalid Choice Try Again")


        except:
            break
            

            
    
    
    
    
    return


if __name__ == '__main__':
    main()