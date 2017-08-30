from vector import Vector
from plane import Plane
from linsys  import LinearSystem, MyDecimal
from decimal import Decimal, getcontext

getcontext().prec = 54

# p0 = Plane(normal_vector=Vector(['1','1','1']), constant_term='1')
# p1 = Plane(normal_vector=Vector(['0','1','0']), constant_term='2')
# p2 = Plane(normal_vector=Vector(['1','1','-1']), constant_term='3')
# p3 = Plane(normal_vector=Vector(['1','0','-2']), constant_term='2')

# s = LinearSystem([p0,p1,p2,p3])

# print s.indices_of_first_nonzero_terms_in_each_row()
# print '{},{},{},{}'.format(s[0],s[1],s[2],s[3])
# print len(s)
# print s

# s[0] = p1
# print s

# print MyDecimal('1e-9').is_near_zero()
# print MyDecimal('1e-11').is_near_zero()

# p0 = Plane(normal_vector=Vector(['1','1','1']), constant_term='1')
# p1 = Plane(normal_vector=Vector(['0','1','0']), constant_term='2')
# p2 = Plane(normal_vector=Vector(['1','1','-1']), constant_term='3')
# p3 = Plane(normal_vector=Vector(['1','0','-2']), constant_term='2')

# s = LinearSystem([p0,p1,p2,p3])
# s.swap_rows(0,1)
# if not (s[0] == p1 and s[1] == p0 and s[2] == p2 and s[3] == p3):
#     print 'test case 1 failed'

# s.swap_rows(1,3)
# if not (s[0] == p1 and s[1] == p3 and s[2] == p2 and s[3] == p0):
#     print 'test case 2 failed'

# s.swap_rows(3,1)
# if not (s[0] == p1 and s[1] == p0 and s[2] == p2 and s[3] == p3):
#     print 'test case 3 failed'

# s.multiply_coefficient_and_row(1,0)
# if not (s[0] == p1 and s[1] == p0 and s[2] == p2 and s[3] == p3):
#     print 'test case 4 failed'

# s.multiply_coefficient_and_row(-1,2)
# if not (s[0] == p1 and
#         s[1] == p0 and
#         s[2] == Plane(normal_vector=Vector(['-1','-1','1']), constant_term='-3') and
#         s[3] == p3):
#     print 'test case 5 failed'

# s.multiply_coefficient_and_row(10,1)
# if not (s[0] == p1 and
#         s[1] == Plane(normal_vector=Vector(['10','10','10']), constant_term='10') and
#         s[2] == Plane(normal_vector=Vector(['-1','-1','1']), constant_term='-3') and
#         s[3] == p3):
#     print 'test case 6 failed'

# s.add_multiple_times_row_to_row(0,0,1)
# if not (s[0] == p1 and
#         s[1] == Plane(normal_vector=Vector(['10','10','10']), constant_term='10') and
#         s[2] == Plane(normal_vector=Vector(['-1','-1','1']), constant_term='-3') and
#         s[3] == p3):
#     print 'test case 7 failed'

# s.add_multiple_times_row_to_row(1,0,1)
# if not (s[0] == p1 and
#         s[1] == Plane(normal_vector=Vector(['10','11','10']), constant_term='12') and
#         s[2] == Plane(normal_vector=Vector(['-1','-1','1']), constant_term='-3') and
#         s[3] == p3):
#     print 'test case 8 failed'

# s.add_multiple_times_row_to_row(-1,1,0)
# if not (s[0] == Plane(normal_vector=Vector(['-10','-10','-10']), constant_term='-10') and
#         s[1] == Plane(normal_vector=Vector(['10','11','10']), constant_term='12') and
#         s[2] == Plane(normal_vector=Vector(['-1','-1','1']), constant_term='-3') and
#         s[3] == p3):
#     print 'test case 9 failed'

# p1 = Plane(normal_vector=Vector(['1','1','1']), constant_term='1')
# p2 = Plane(normal_vector=Vector(['0','1','1']), constant_term='2')
# s = LinearSystem([p1,p2])
# t = s.compute_triangular_form()
# if not (t[0] == p1 and
#         t[1] == p2):
#     print 'test case 1 failed'

# p1 = Plane(normal_vector=Vector(['1','1','1']), constant_term='1')
# p2 = Plane(normal_vector=Vector(['1','1','1']), constant_term='2')
# s = LinearSystem([p1,p2])
# t = s.compute_triangular_form()
# if not (t[0] == p1 and
#         t[1] == Plane(constant_term='1')):
#     print 'test case 2 failed'

# p1 = Plane(normal_vector=Vector(['1','1','1']), constant_term='1')
# p2 = Plane(normal_vector=Vector(['0','1','0']), constant_term='2')
# p3 = Plane(normal_vector=Vector(['1','1','-1']), constant_term='3')
# p4 = Plane(normal_vector=Vector(['1','0','-2']), constant_term='2')
# s = LinearSystem([p1,p2,p3,p4])
# t = s.compute_triangular_form()
# if not (t[0] == p1 and
#         t[1] == p2 and
#         t[2] == Plane(normal_vector=Vector(['0','0','-2']), constant_term='2') and
#         t[3] == Plane()):
#     print 'test case 3 failed'

# p1 = Plane(normal_vector=Vector(['0','1','1']), constant_term='1')
# p2 = Plane(normal_vector=Vector(['1','-1','1']), constant_term='2')
# p3 = Plane(normal_vector=Vector(['1','2','-5']), constant_term='3')
# s = LinearSystem([p1,p2,p3])
# t = s.compute_triangular_form()
# if not (t[0] == Plane(normal_vector=Vector(['1','-1','1']), constant_term='2') and
#         t[1] == Plane(normal_vector=Vector(['0','1','1']), constant_term='1') and
#         t[2] == Plane(normal_vector=Vector(['0','0','-9']), constant_term='-2')):
#     print 'test case 4 failed'

# p1 = Plane(normal_vector=Vector(['1','1','1']), constant_term='1')
# p2 = Plane(normal_vector=Vector(['0','1','1']), constant_term='2')
# s = LinearSystem([p1,p2])
# r = s.compute_rref()
# if not (r[0] == Plane(normal_vector=Vector(['1','0','0']), constant_term='-1') and
#         r[1] == p2):
#     print 'test case 1 failed'
# print r
# p1 = Plane(normal_vector=Vector(['1','1','1']), constant_term='1')
# p2 = Plane(normal_vector=Vector(['1','1','1']), constant_term='2')
# s = LinearSystem([p1,p2])
# r = s.compute_rref()
# if not (r[0] == p1 and
#         r[1] == Plane(constant_term='1')):
#     print 'test case 2 failed'
# print r
# p1 = Plane(normal_vector=Vector(['1','1','1']), constant_term='1')
# p2 = Plane(normal_vector=Vector(['0','1','0']), constant_term='2')
# p3 = Plane(normal_vector=Vector(['1','1','-1']), constant_term='3')
# p4 = Plane(normal_vector=Vector(['1','0','-2']), constant_term='2')
# s = LinearSystem([p1,p2,p3,p4])
# r = s.compute_rref()
# if not (r[0] == Plane(normal_vector=Vector(['1','0','0']), constant_term='0') and
#         r[1] == p2 and
#         r[2] == Plane(normal_vector=Vector(['0','0','-2']), constant_term='2') and
#         r[3] == Plane()):
#     print 'test case 3 failed'
# print r

# p1 = Plane(normal_vector=Vector(['0','1','1']), constant_term='1')
# p2 = Plane(normal_vector=Vector(['1','-1','1']), constant_term='2')
# p3 = Plane(normal_vector=Vector(['1','2','-5']), constant_term='3')
# s = LinearSystem([p1,p2,p3])
# r = s.compute_rref()
# if not (r[0] == Plane(normal_vector=Vector(['1','0','0']), constant_term=Decimal('23')/Decimal('9')) and
#         r[1] == Plane(normal_vector=Vector(['0','1','0']), constant_term=Decimal('7')/Decimal('9')) and
#         r[2] == Plane(normal_vector=Vector(['0','0','1']), constant_term=Decimal('2')/Decimal('9'))):
#     print 'test case 4 failed'
# print r

# p1 = Plane(Vector(['5.862','1.178','-10.366']), Decimal('-8.15'))
# p2 = Plane(Vector(['-2.931','-0.589', '5.183']), Decimal('-4.075'))
# s = LinearSystem([p1,p2])
# try:
#     # print s.compute_rref()
#     r = s.do_gaussian_elimination_and_extract_solution()
#     print r
# except Exception as e:
#     print str(e)


# p1 = Plane(Vector(['8.631', '5.112', '-1.816']), Decimal('-5.113'))
# p2 = Plane(Vector(['4.315', '11.132', '-5.27']), Decimal('-6.775'))
# p3 = Plane(Vector(['-2.158', '3.01', '-1.727']), Decimal('-0.831'))
# s = LinearSystem([p1,p2, p3])
# print s.compute_rref()
# try:
#     # print s.compute_rref()
#     r = s.do_gaussian_elimination_and_extract_solution()
#     print r
# except Exception as e:
#     print str(e)


# p1 = Plane(Vector(['5.262', '2.739', '-9.878']), Decimal('-3.441'))
# p2 = Plane(Vector(['5.111', '6.358', '7.638']), Decimal('-2.152'))
# p3 = Plane(Vector(['2.016', '-9.924', '-1.367']), Decimal('-9.278'))
# p4 = Plane(Vector(['2.167', '-13.543', '-18.883']),Decimal(' -10.567'))
# s = LinearSystem([p1,p2, p3, p4])
# try:
#     # print s.compute_rref()
#     r = s.do_gaussian_elimination_and_extract_solution()
#     print r
# except Exception as e:
#     print str(e)

p1 = Plane(normal_vector=Vector([0.786, 0.786, 0.588]), constant_term=-0.714)
p2 = Plane(normal_vector=Vector([-0.131, -0.131, 0.244]), constant_term=0.319)

system = LinearSystem([p1, p2])
print system.compute_solution()


p1 = Plane(Vector([8.631, 5.112, -1.816]), -5.113)
p2 = Plane(Vector([4.315, 11.132, -5.27]), -6.775)
p3 = Plane(Vector([-2.158, 3.01, -1.727]), -0.831)

system = LinearSystem([p1, p2, p3])
print system.compute_solution()

p1 = Plane(Vector([0.935, 1.76, -9.365]), -9.955)
p2 = Plane(Vector([0.187, 0.352, -1.873]), -1.991)
p3 = Plane(Vector([0.374, 0.704, -3.746]), -3.982)
p4 = Plane(Vector([-0.561, -1.056, 5.619]), 5.973)
system = LinearSystem([p1, p2, p3, p4])
print system.compute_solution()