class Vecteur2D:
    # constructeur 
    def __init__(self, x=0,y=0):
        self.x = x
        self.y = y
    # show method
    def show(self):
        return "x= "+str(self.x)+" y="+str(self.y)
    # add operator
    def __add__(self,other):
        ax= self.x+other.x
        ay= self.y+other.y
        return Vecteur2D(ax,ay)
# creer des vecteurs
v1 = Vecteur2D()
v2 =Vecteur2D(3,2)
v3 =Vecteur2D(7,1)
# tester la method show()
print(v1.show())
print(v2.show())
# tester l'operation + avec 2 vectors
va= v2 + v3
print(va.show())      
# //////////////
# classe rectangle
class Rectangle:
    nom="rectangle"
    # constructeur
    def __init__(self, lo=0 ,la=0):
        self.longueur= lo  
        self.largeur= la  
    def show(self):
    # method pour afficher les attrb de classe
        return "nom: "+self.nom +" longueur =" +str(self.longueur) + " largeur = "+str(self.largeur)
    # calculer le surface
    def surface(self):
        return "surface : "+str(self.largeur * self.longueur)
# classe Carre
class Carre(Rectangle):
    nom="carre"
    def __init__(self, lo=0):
        super().__init__(lo=lo, la=lo)

r1= Rectangle(5,6)
c1= Carre(8)
# tester avvec le rectangle
print(r1.show())
print(r1.surface())
# tester aver le carre
print(c1.show())
print(c1.surface())
# ////////////
# classe Point
class Point:
    def __init__(self,x=0.0,y=0.0):
        self.x = x
        self.y = y
    def show(self):
        return "("+str(self.x)+","+str(self.y)+")"
# classe segment
class Segment():
    # constructeur qui prend 2 objects Point comme params
    def __init__(self,org,ext):
            self.org = Point(org.x,org.y)
            self.ext = Point(ext.x,ext.y)
    def show_seg(self):
        return "(org,ext) Segment = ["+ self.org.show() + ", "+ self.ext.show() + "]"

p1 = Point(1,2)
p2 = Point(3,4)
# tester le Point
print(p1.show())
# tester le Segment
s1= Segment(p1,p2)
print(s1.show_seg())