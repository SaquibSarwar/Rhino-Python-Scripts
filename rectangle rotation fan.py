import rhinoscriptsyntax as rs

plane = rs.WorldYZPlane()
j=0
for i in range(8):
   
   plane = rs.RotatePlane(plane, j, [1,1,0])
   j=j+45
   rs.AddRectangle( plane, 10.0, 25.0 )
