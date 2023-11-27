def main():
    class rectangle:
        def __init__(self, length,width):
            self.length = length
            self.width = width
        
        def area(self):
            return self.length * self.width
        
        def __str__(self):
            return f"Rect({self.length},{self.width},{self.area()})" 
    class triangle:
        def __init__(self, base, height):
            self.base = base
            self.height = height
        
        def area(self):
            return int((self.base * self.height)/2)
        
        def __str__(self):
            return f"Tri({self.base},{self.height},{self.area()})"
    class circle:
        def __init__(self,radius):
            self.radius = radius
        
        def area(self):
            return int(3.14 * (self.radius ** 2))
        
        def __str__(self):
            return f"Circ({self.radius},{self.area()})"
        
    while True:
        try:
            print("Select an Option:\n\t1.Rectangle\n\t2.Triangle\n\t3.Circle\n\t0.EXIT", end='\n')
            choice = int(input("Choice: "))
            if(choice == 0):
                print("Exiting Program...")
                break
            elif(choice == 1):
                l = int(input("Enter a length: "))
                w = int(input("Enter a width: "))
                rect = rectangle(l,w)
                print(rect)
            elif(choice == 2):
                b = int(input("Enter a base: "))
                h = int(input("Enter a height: "))
                tri = triangle(b,h)
                print(tri)
            elif(choice == 3):
                r = int(input("Enter a radus: "))
                circ = circle(r)
                print(circ)
            else:
                print("Invalid Choice Try Again")


        except:
            break
            

            
    
    
    
    
    return


if __name__ == '__main__':
    main()