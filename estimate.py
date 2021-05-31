import math
import unittest

def monte_carlo(n):
    import random
    inside_c=0
    outside_c=0
    for i in range (1,n+1):
        point_x= random.random()
        point_y=random.random()
        print(point_x,point_y)
        d= point_x**2+point_y**2
        dist=d**0.5
        print(dist)
        if dist<=1:
            inside_c=inside_c +1
        outside_c=outside_c+1
    print("Circle count Inside=", inside_c, "Outside=",outside_c)
    ratio=inside_c/outside_c
    return 4*ratio
def wallis(n):
    sum=1
    for i in range (1, n+1):
        c1= 4*i*i
        c2= c1-1
        sum = sum * (c1/c2)   
    return 2*sum

class TestWallis(unittest.TestCase):
    def test_low_iters(self):
        for i in range(0, 5):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) > 0.15, msg=f"Estimate with just {i} iterations is {pi} which is too accurate.\n")
            
    def test_high_iters(self):
        for i in range(500, 600):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) < 0.01, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")


class TestMC(unittest.TestCase):
    def test_randomness(self):
        pi0 = monte_carlo(15000)
        pi1 = monte_carlo(15000)
        
        self.assertNotEqual(pi0, pi1, "Two different estimates for PI are exactly the same. This is almost impossible.")

        self.assertFalse(abs(pi0 - pi1) > 0.05, "Two different estimates of PI are too different. This should not happen")

    def test_accuracy(self):
        for i in range(500, 600):
            pi = monte_carlo(i)
            self.assertTrue(abs(pi - math.pi) < 0.4, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")
        
    
if __name__ == "__main__":
    unittest.main()
