import rhinoscriptsyntax as rs
all=rs.AllObjects()
rs.DeleteObjects(all)


plane1 = rs.PlaneFromFrame( [0,0,0], [0,1,0], [1,0,0] )
plane2 = rs.PlaneFromFrame( [0,0,6], [0,1,0], [1,0,0] )
plane3 = rs.PlaneFromFrame( [0,0,40], [0,1,0], [1,0,0] )




nose=rs.AddCone (plane2, 6, 20, cap=True)
nose2=rs.AddCone (plane3, 24, 5, cap=True)
hat1=rs.AddCylinder (plane1, 110, 20, cap=True)
hat2=rs.AddCylinder (plane1, -6, 10, cap=True)
hat3=rs.AddCylinder (plane2, -10, 12, cap=True)
##neck=rs.AddCylinder ((0,0,-35), 10, 5, cap=True)