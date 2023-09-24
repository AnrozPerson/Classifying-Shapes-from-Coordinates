shape_check_1 = {"square": ["1_parallel", "2_parallel", "all_sides_equal", "all_angle_90", "2_pair_equal_adjacent_side"],
                 "rhombus": ["1_parallel", "2_parallel", "all_sides_equal", "2_pair_equal_adjacent_side"],
                 "rectangle": ["1_parallel", "2_parallel", "all_angle_90"],
                 "parallelogram": ["1_parallel", "2_parallel"],
                 "kite": ["2_pair_equal_adjacent_side"],
                 "trapezium": ["1_parallel"]}
shape_check_2 = {"square": ["perpendicular_diagonals", "1_diagonal_bisect_other", "2_diagonal_bisects_others", "1_bisect_angle", "2_bisect_angles", "diagonals_equal_length"],
                 "rhombus": ["perpendicular_diagonals", "1_diagonal_bisect_other", "2_diagonal_bisects_others", "1_bisect_angle", "2_bisect_angles"],
                 "rectangle": ["1_diagonal_bisect_other", "2_diagonal_bisects_others", "diagonals_equal_length"],
                 "parallelogram": ["1_diagonal_bisect_other", "2_diagonal_bisects_others"],
                 "kite": ["perpendicular_diagonals", "1_diagonal_bisect_other", "1_bisect_angle"],
                 "trapezium": []}

###Respective output for each property

prop_1 = {"1_parallel": "One pair of parallel sides", "2_parallel": "Two pairs of parallel sides", "all_sides_equal": "All sides equal", "all_angle_90": "All angles 90 degrees", "2_pair_equal_adjacent_side": "Two pairs of adjacent equal sides"}
prop_2 = {"perpendicular_diagonals": "Diagonals are perpendicular", "1_diagonal_bisect_other": "One diagonal bisects the other", "2_diagonal_bisects_others": "Both diagonals bisect each other", "1_bisect_angle": "One diagonal bisects the angles it passes through", "2_bisect_angles": "Both diagonals bisect the angles they pass through", "diagonals_equal_length": "Diagonals are equal in length"}
