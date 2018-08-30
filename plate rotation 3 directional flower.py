import rhinoscriptsyntax as rs
all=rs.AllObjects()
rs.DeleteObjects(all)


plane = rs.WorldYZPlane()
j=0
for i in range(20):
   
   plane = rs.RotatePlane(plane, j, [-1,1,1])
   j=j+10
   rs.AddRectangle( plane, 25.0, 25.0 )
plane = rs.WorldZXPlane()
for i in range(20):
   
   plane = rs.RotatePlane(plane, j, [1,-1,1])
   j=j+10
   rs.AddRectangle( plane, 25.0, 25.0 )
plane = rs.WorldXYPlane()
for i in range(20):
   
   plane = rs.RotatePlane(plane, j, [1,1,-1])
   j=j+10
   rs.AddRectangle( plane, 25.0, 25.0 )