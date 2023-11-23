import numpy as np
import random
import time

def generate_random_traffic():
    # Set the lambda parameter for the Poisson distribution
    lambda_param = 20  # You can adjust this based on your desired rate

    # Generate Poisson random numbers
    poisson_numbers = np.random.poisson(lambda_param, size=1)

    # Clip values to be between 0 and 64
    poisson_numbers_clipped = np.clip(poisson_numbers, 0, 64)

    return poisson_numbers_clipped[0]

def generate_data():
    while True:
        # Generate random traffic for each link
        t0_1 = generate_random_traffic()
        t1_0 = t0_1
        t1_2 = generate_random_traffic()
        t2_1 = t1_2
        t2_3 = generate_random_traffic()
        t3_2 = t2_3
        t0_4 = generate_random_traffic()
        t4_0 = t0_4
        t4_5 = generate_random_traffic()
        t5_4 = t4_5
        t1_5 = generate_random_traffic()
        t5_1 = t1_5
        t5_6 = generate_random_traffic()
        t6_5 = t5_6
        t2_6 = generate_random_traffic()
        t6_2 = t2_6
        t6_7 = generate_random_traffic()
        t7_6 = t6_7
        t3_7 = generate_random_traffic()
        t7_3 = t3_7
        t4_8 = generate_random_traffic()
        t8_4 = t4_8
        t8_9 = generate_random_traffic()
        t9_8 = t8_9
        t5_9 = generate_random_traffic()
        t9_5 = t5_9
        t6_10 = generate_random_traffic()
        t10_6 = t6_10
        t9_10 = generate_random_traffic()
        t10_9 = t9_10
        t7_11 = generate_random_traffic()
        t11_7 = t7_11
        t11_10 = generate_random_traffic()
        t10_11 = t11_10
        t12_13 = generate_random_traffic()
        t13_12 = t12_13
        t8_12 = generate_random_traffic()
        t12_8 = t8_12
        t9_13 = generate_random_traffic()
        t13_9 = t9_13
        t10_14 = generate_random_traffic()
        t14_10 = t10_14
        t13_14 = generate_random_traffic()
        t14_13 = t13_14
        t14_15 = generate_random_traffic()
        t15_14 = t14_15
        t11_15 = generate_random_traffic()
        t15_11 = t11_15

        
        # print("t0_1:",(t0_1))
        # print("t1_2:",(t1_2))
        # print("t2_3:",(t2_3))
        # print("t4_5:",(t4_5))
        # print("t5_6:",(t5_6))
        # print("t6_7:",(t6_7))
        # print("t8_9:",(t8_9))
        # print("t9_10:",(t9_10))
        # print("t10_11:",(t10_11))
        # print("t12_13:",(t12_13))
        # print("t13_14:",(t13_14))
        # print("t14_15:",(t14_15))
        # print("t0_4:",(t0_4))
        # print("t1_5:",(t1_5))
        # print("t2_6:",(t2_6))
        # print("t3_7:",(t3_7))
        # print("t4_8:",(t4_8))
        # print("t5_9:",(t5_9))
        # print("t6_10:",(t6_10))
        # print("t7_11:",(t7_11))
        # print("t8_12:",(t8_12))
        # print("t9_13:",(t9_13))
        # print("t10_14:",(t10_14))
        # print("t11_15:",(t11_15))
        # print("t1_0:",(t1_0))
        # print("t2_1:",(t2_1))
        # print("t3_2:",(t3_2))
        # print("t5_4:",(t5_4))
        # print("t6_5:",(t6_5))
        # print("t7_6:",(t7_6))
        # print("t9_8:",(t9_8))
        # print("t10_9:",(t10_9))
        # print("t11_10:",(t11_10))
        # print("t13_12:",(t13_12))
        # print("t14_13:",(t14_13))
        # print("t15_14:",(t15_14))
        # print("t4_0:",(t4_0))
        # print("t5_1:",(t5_1))
        # print("t6_2:",(t6_2))
        # print("t7_3:",(t7_3))
        # print("t8_4:",(t8_4))
        # print("t9_5:",(t9_5))
        # print("t10_6:",(t10_6))
        # print("t11_7:",(t11_7))
        # print("t12_8:",(t12_8))
        # print("t13_9:",(t13_9))
        # print("t14_10:",(t14_10))
        # print("t15_11:",(t15_11))
        
        # print("******************************************************************************************")
        yield t0_1, t1_0, t1_2, t2_1, t2_3, t3_2, t0_4, t4_0, t4_5, t5_4, t1_5, t5_1, t5_6, t6_5, t2_6, t6_2, t6_7, t7_6, t3_7, t7_3, t4_8, t8_4, t8_9, t9_8, t5_9, t9_5, t6_10, t10_6, t9_10, t10_9, t7_11, t11_7, t11_10, t10_11, t12_13, t13_12, t8_12, t12_8, t9_13, t13_9, t10_14, t14_10, t13_14, t14_13, t14_15, t15_14, t11_15, t15_11
        time.sleep(0.5)