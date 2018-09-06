import rhinoscriptsyntax as rs
all=rs.AllObjects()
rs.DeleteObjects(all)


plane1 = rs.PlaneFromFrame( [0,0,0], [0,1,0], [0,0,1] )
plane2 = rs.PlaneFromFrame( [20,10,10], [0,0,1], [0,1,0])
plane3 = rs.PlaneFromFrame( [20,-10,10], [0,0,1], [0,1,0])
plane4 = rs.PlaneFromFrame( [40,0,0], [0,0,1], [0,1,0])
plane5 = rs.PlaneFromFrame( [-12,15,35], [1,0,.50], [0,1,-.4])
plane6 = rs.PlaneFromFrame( [0,5,17], [1,0,.50], [0,1,-.4])
#plane2 = rs.AddPlaneSurface (plane1, 50, 50)


x=rs.AddPoint(-11,15,35)
y=rs.AddPoint(1,0,.50)
z=rs.AddPoint(0,1,-.4)
j=0
plane11 = rs.RotatePlane(plane1, 0, [0,1,0])
#for i in range(50):
   
   #plane11 = rs.RotatePlane(plane1, j, [0,1,0])
   #j=j+10
   #rs.AddRectangle( plane11, 25.0, 25.0 )
   #rs.AddCircle( plane11, 25.0 )
   #rs.AddSphere ( plane11, 25.0 )

   #plane11 = rs.RotatePlane(plane1, j, [0,0,1])
   #j=j+10
   #rs.AddRectangle( plane11, 25.0, 25.0 )
   
   #rs.AddSphere ( plane11, 50.0 )\
head=rs.AddSphere ( plane11, 25.0 )
eyeL=rs.AddSphere ( plane2, 5.0 )
eyeR=rs.AddSphere ( plane3, 5.0 )
#rs.AddSphere ( plane11, 25.0 )
#rs.AddCircle( (0,0,25), 50.0 )
hat1=rs.AddCone (plane5, -25, 25, cap=False)
nose=rs.AddCone (plane4, 15, 5, cap=True)
hat2=rs.AddCylinder (plane6, -1, 50, cap=True)
hat2=rs.AddTorus (plane6, 50, 2)
neck=rs.AddCylinder ((0,0,-30), 10, 5, cap=True)
#body=rs.AddCylinder ((0,0,-70), 40, 50, cap=True)
body=rs.AddCylinder ((0,0,-95), 60, 30, cap=True)
#body=rs.GetRectangle (4, (0,0,-130),)
collar=rs.AddTorus( (0,0,-35), 15, 5 )
