from decimal import Decimal, getcontext
from copy import deepcopy

from vector import Vector
from plane import Plane

getcontext().prec = 30


class LinearSystem(object):

    ALL_PLANES_MUST_BE_IN_SAME_DIM_MSG = 'All planes in the system should live in the same dimension'
    NO_SOLUTIONS_MSG = 'No solutions'
    INF_SOLUTIONS_MSG = 'Infinitely many solutions'

    def __init__(self, planes):
        try:
            d = planes[0].dimension
            for p in planes:
                assert p.dimension == d

            self.planes = planes
            self.dimension = d

        except AssertionError:
            raise Exception(self.ALL_PLANES_MUST_BE_IN_SAME_DIM_MSG)

    def compute_triangular_form(self):
        system = deepcopy(self)

        num_equations = len(system)
        dimensions = system.dimension

        j = 0

        for i in range(num_equations):

            while j < dimensions:
                coefficient_of_index = MyDecimal(system[i].normal_vector[j])

                if coefficient_of_index.is_near_zero():
                    swap_succeeded = system.swap_row_below_for_nonzero_if_able(i, j)
                    if not swap_succeeded:
                        j += 1
                        continue

                system.clear_coefficients_below(i, j)                         
                j += 1
                break

        return system
    
    def clear_coefficients_below(self, row, col):
        num_equations = len(self)
        coefficient_of_index = MyDecimal(self[row].normal_vector[col])

        for i_clear in range(row + 1, num_equations):
            n = self[i_clear].normal_vector
            numerator = n[col]
            multiplier = -numerator / coefficient_of_index
            self.add_multiple_times_row_to_row(multiplier, row, i_clear)

    def clear_coefficients_above(self, row, col):

        coefficient_of_index = MyDecimal(self[row].normal_vector[col])

        if row > -1:
            for i_clear in range(row - 1, -1, -1):
                n = self[i_clear].normal_vector
                numerator = n[col]
                multiplier = -numerator / coefficient_of_index
                self.add_multiple_times_row_to_row(multiplier, row, i_clear)
            
    def swap_row_below_for_nonzero_if_able(self, row, col):
        num_equations = len(self)

        for i in range(row + 1, num_equations):
            coefficient_of_i = MyDecimal(self.planes[i].normal_vector[col])
            if not coefficient_of_i.is_near_zero():
                self.swap_rows(row, i)
                return True

        return False

    def swap_rows(self, row1, row2):
        self[row1], self[row2] = self[row2], self[row1]


    def multiply_coefficient_and_row(self, coefficient, row):
        new_normal = self[row].normal_vector.scalar_multiply(coefficient)
        new_k = self[row].constant_term * coefficient

        self[row] = Plane(new_normal, new_k)

    def add_multiple_times_row_to_row(self, coefficient, row_to_add, row_to_be_added_to):
        new_normal = self[row_to_add].normal_vector.scalar_multiply(coefficient)
        new_k = self[row_to_add].constant_term * coefficient

        temp_plane_multiplied = Plane(new_normal, new_k)
        temp_plane_to_be_added = self[row_to_be_added_to]
        new_plane_normal = temp_plane_multiplied.normal_vector + temp_plane_to_be_added.normal_vector
        new_plane_k = temp_plane_multiplied.constant_term + temp_plane_to_be_added.constant_term

        self[row_to_be_added_to] = Plane(new_plane_normal, new_plane_k)

    def compute_rref(self):
        tf = self.compute_triangular_form()
        
        first_nonzero = tf.indices_of_first_nonzero_terms_in_each_row()   
        num_equations = len(first_nonzero)
        
        for i in range(num_equations):
            variable = first_nonzero[i]
            if variable != -1:
                
                coefficient_of_index = MyDecimal(tf[i].normal_vector[variable])   
                
                tf.clear_coefficients_below(i, variable)
                tf.clear_coefficients_above(i,variable)

                if coefficient_of_index != 1:
                    tf.multiply_coefficient_and_row(Decimal('1.0')/coefficient_of_index, i)     

        return tf
    
    def do_gaussian_elimination_and_extract_solution(self):
        rref = self.compute_rref()

        rref.raise_exception_if_contradictory_equation()
        rref.raise_exception_if_too_few_pivots()

        num_variables = rref.dimension
        solution_coordinates = [rref.planes[i].constant_term for i in range(num_variables)]
        return Vector(solution_coordinates)
    
    def raise_exception_if_contradictory_equation(self):
        for p in self.planes:
            try:
                p.first_nonzero_index(p.normal_vector)
            
            except Exception as e:
                if str(e) == 'No nonzero elements found':
                    constant_term = MyDecimal(p.constant_term)
                    print constant_term
                    if not constant_term.is_near_zero():
                        raise Exception(self.NO_SOLUTIONS_MSG)
                else:
                    raise e

    def raise_exception_if_too_few_pivots(self):
        pivot_indices = self.indices_of_first_nonzero_terms_in_each_row()
        print [1 if index >= 0 else 0 for index in pivot_indices]
        num_pivots = sum([1 if index >= 0 else 0 for index in pivot_indices])
        num_variables = self.dimension

        if num_pivots < num_variables:
            raise Exception(self.INF_SOLUTIONS_MSG)

    def indices_of_first_nonzero_terms_in_each_row(self):
        num_equations = len(self)
        num_variables = self.dimension

        indices = [-1] * num_equations

        for i,p in enumerate(self.planes):
            try:
                indices[i] = p.first_nonzero_index(p.normal_vector)
            except Exception as e:
                if str(e) == Plane.NO_NONZERO_ELTS_FOUND_MSG:
                    continue
                else:
                    raise e

        return indices


    def __len__(self):
        return len(self.planes)


    def __getitem__(self, i):
        return self.planes[i]


    def __setitem__(self, i, x):
        try:
            assert x.dimension == self.dimension
            self.planes[i] = x

        except AssertionError:
            raise Exception(self.ALL_PLANES_MUST_BE_IN_SAME_DIM_MSG)


    def __str__(self):
        ret = 'Linear System:\n'
        temp = ['Equation {}: {}'.format(i+1,p) for i,p in enumerate(self.planes)]
        ret += '\n'.join(temp)
        return ret


class MyDecimal(Decimal):
    def is_near_zero(self, eps=1e-10):
        return abs(self) < eps
