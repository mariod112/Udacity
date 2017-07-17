from vector import Vector

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

v17 = Vector([-7.579, -7.88])
v18 = Vector([22.737, 23.64])

print v17.parallel(v18)
print v17.orthogonal(v18)

v19 = Vector([-2.029, 9.97, 4.172])
v20 = Vector([-9.231, -6.639, -7.245])

print v19.parallel(v20)
print v19.orthogonal(v20)

v21 = Vector([-2.328, -7.284, -1.214])
v22 = Vector([-1.821, 1.072, -2.94])

print v21.parallel(v22)
print v21.orthogonal(v22)

v23 = Vector([2.118, 4.827])
v24 = Vector([0, 0])

print v23.parallel(v24)
print v24.orthogonal(v24)
