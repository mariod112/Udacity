from vector import Vector
from line import Line
from plane import Plane

# v = Vector([8.218,-9.341])
# v1 = Vector([-1.129,2.111])

# v2 = Vector([7.119, 8.215])
# v3 = Vector([-8.223, .878])

# v4 = Vector([1.671, -1.012, -0.318])

# print v + v1
# print v2 - v3
# print v4.scalar_multiply(7.41)

# v5 = Vector([-0.221, 7.437])
# v6 = Vector([8.813, -1.331, -6.247])

# print v5.magnitude()
# print v6.magnitude()

# v7 = Vector([5.581, -2.136])
# v8 = Vector([1.996, 3.108, -4.554])

# print v7.normalize()
# print v8.normalize()

# v9 = Vector([7.887, 4.138])
# v10 = Vector([-8.802, 6.776])

# v11 = Vector([-5.955, -4.904, -1.874])
# v12 = Vector([-4.496, -8.755, 7.103])

# print v9.dot_product(v10)
# print v11.dot_product(v12)

# v13 = Vector([3.183, -7.627])
# v14 = Vector([-2.668, 5.319])

# v15 = Vector([7.35, 0.221, 5.188])
# v16 = Vector([2.751, 8.259, 3.985])

# print v13.angle(v14)
# print v15.angle_degrees(v16)

#v17 = Vector([-7.579, -7.88])
#v18 = Vector([22.737, 23.64])

#print v17.parallel(v18)
#print v17.orthogonal(v18)

#v19 = Vector([-2.029, 9.97, 4.172])
#v20 = Vector([-9.231, -6.639, -7.245])

#print v19.parallel(v20)
#print v19.orthogonal(v20)

#v21 = Vector([-2.328, -7.284, -1.214])
#v22 = Vector([-1.821, 1.072, -2.94])

#print v21.parallel(v22)
#print v21.orthogonal(v22)

#v23 = Vector([2.118, 4.827])
#v24 = Vector([0, 0])

#print v23.parallel(v24)
#print v24.orthogonal(v24)

#v25 = Vector([3.039, 1.879])
#v26 = Vector([0.825, 2.036])

#print v25.component_parallel_to(v26)

#v27 = Vector([-9.88, -3.264, -8.159])
#v28 = Vector([-2.155, -9.353, -9.473])

#print v27.component_orthogonal_to(v28)

#v29 = Vector([3.009, -6.172, 3.692, -2.51])
#v30 = Vector([6.404, -9.144, 2.759, 8.718])

#print v29.component_parallel_to(v30)
#print v29.component_orthogonal_to(v30)

#v31 = Vector([8.462, 7.893, -8.187])
#v32 = Vector([6.984, -5.975, 4.778])

#print v31.cross_product(v32)

#v33 = Vector([-8.987, -9.838, 5.031])
#v34 = Vector([-4.268, -1.861, -8.866])

#print v33.area_of_parallelegram(v34)

#v35 = Vector([1.5, 9.547, 3.691])
#v36 = Vector([-6.007, 0.124, 5.772])

#print v35.area_of_triangle(v36)

# l1 = Line(Vector([4.046, 2.836]), 1.21)
# l2 = Line(Vector([10.115, 7.09]), 3.025)

# print l1.parallel(l2)
# print l1 == l2
# print l1.intersection(l2)

# l3 = Line(Vector([7.204, 3.182]), 8.68)
# l4 = Line(Vector([8.172, 4.114]), 9.883)

# print l3.parallel(l4)
# print l3 == l4
# print l3.intersection(l4)

# l5 = Line(Vector([1.182, 5.562]), 6.744)
# l6 = Line(Vector([1.773, 8.343]), 9.525)

# print l5.parallel(l6)
# print l5 == l6
# print l5.intersection(l6)

p1 = Plane(Vector([-0.412, 3.806, 0.728]), -3.46)
p2 = Plane(Vector([1.03, -9.515, -1.82]), 8.65)

print p1 == p2
print p1.parallel(p2)

p3 = Plane(Vector([2.611, 5.528, 0.283]), 4.6)
p4 = Plane(Vector([7.715, 8.306, 5.342]), 3.76)

print p3 == p4
print p3.parallel(p4)

p5 = Plane(Vector([-7.926, 8.625, -7.212]), -7.952)
p6 = Plane(Vector([-2.642, 2.875, -2.404]), -2.443)

print p5 == p6
print p5.parallel(p6)