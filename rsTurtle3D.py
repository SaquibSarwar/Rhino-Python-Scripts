import rhinoscriptsyntax as rs





class Turtle:
    def __init__(self, pos = [0,0,0], heading = [1,0,0]):
        self.heading = heading
        self.point = rs.AddPoint(pos)
        pointPos = rs.PointCoordinates(self.point)
        self.direction = rs.VectorCreate(heading,pointPos)
        self.lines = []
    
    def forward(self,magnitude):
        print self.direction
        movement = rs.VectorScale(self.direction,magnitude)
        prevPos = rs.PointCoordinates(self.point)
        rs.MoveObject(self.point,movement)
        currentPos = rs.PointCoordinates(self.point)
        rs.AddLine(prevPos,currentPos)
        
    def left(self,angle,(X,Y,Z)):

        self.direction = rs.VectorRotate(self.direction, angle, [X,Y,Z])
        print(self.direction)   
        
    def right(self,angle,(X,Y,Z)):
        self.direction = rs.VectorRotate(self.direction, -angle, [X,Y,Z])
        print(self.direction)
    
    def goto(self, x, y, z):
        prevPos = rs.PointCoordinates(self.point)
        movement = rs.VectorCreate([x,y,z],prevPos)
        rs.MoveObject(self.point,movement)
        currentPos = rs.PointCoordinates(self.point)
        rs.AddLine(prevPos,currentPos)

m=Turtle()

for i in range(10):
    m.left(45,(0,0,1))
    m.forward(10)

#for i in range(10):
#    m.left(45,(0,1,0))
#    m.forward(10)
    
#for i in range(10):
#    m.left(45,(1,0,0))
#    m.forward(10)

#for i in range(10):
#    m.left(45,(0,1,1))
#    m.forward(10)

#for i in range(10):
#    m.left(45,(1,0,1))
#    m.forward(10)

#for i in range(10):
#    m.left(45,(1,1,0))
#    m.forward(10)

#for i in range(10):
#    m.left(45,(1,1,1))
#    m.forward(10)

#for i in range(10):
#    m.left(45,(0,0,-1))
#    m.forward(10)
    
#for i in range(10):
#    m.left(45,(0,-1,0))
#    m.forward(10)
    
#for i in range(10):
#    m.left(45,(-1,0,0))
#    m.forward(10)

#for i in range(10):
#    m.left(45,(0,-1,-1))
#    m.forward(10)

#for i in range(10):
#    m.left(45,(-1,0,-1))
#    m.forward(10)

#for i in range(10):
#    m.left(45,(-1,-1,0))
#    m.forward(10)

#for i in range(10):
#    m.left(45,(-1,-1,-1))
#    m.forward(10)