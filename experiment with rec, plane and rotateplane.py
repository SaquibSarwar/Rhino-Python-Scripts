import rhinoscriptsyntax as rs

plane = rs.WorldYZPlane()
j=0
for i in range(8):
   
   plane = rs.RotatePlane(plane, j, [1,1,1])
   j=j+45
   rs.AddRectangle( plane, 25.0, 25.0 )
   
plane = rs.WorldZXPlane()
for i in range(8):
   
   plane = rs.RotatePlane(plane, j, [1,1,1])
   j=j+45
   rs.AddRectangle( plane, 25.0, 25.0 )
   
plane = rs.WorldXYPlane()
for i in range(8):
   
   plane = rs.RotatePlane(plane, j, [1,1,1])
   j=j+45
   rs.AddRectangle( plane, 25.0, 25.0 )
   