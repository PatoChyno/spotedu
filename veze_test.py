import unittest
import math
from veze import simple, fast, super_fast
from fib import memo
from random import randrange

class Test(unittest.TestCase):

    def setUp(self):
        self.solvers=[simple, fast, super_fast]
        self.n=6

    def test_empty_board(self):
        """
        result on board with no forbidden fields should be n!
        """
        for solver in self.solvers:
            res=solver(self.n, set())
            self.assertEqual(res, math.factorial(self.n))

    def test_impossible(self):
        """
        tests if result is zero if whole row is forbidden
        """
        for forb_row in range(self.n):
            forb={(forb_row, i) for i in range(self.n)}
            for solver in self.solvers:
                self.assertEqual(solver(self.n, forb), 0, "row %d"%forb_row)

    def test_random_board(self):
        """
        tests if all existent solvers are consistent on random board
        """
        for _ in range(10):
            forb={(randrange(self.n), randrange(self.n)) for i in range(randrange(self.n**2))}
            res=[solver(self.n, forb) for solver in self.solvers]
            self.assertEqual(min(res), max(res))

 
class MemoTest(unittest.TestCase):
    """
    tests behavior of the memo decorator
    """

    def setUp(self):
        self.fun_invokes=0

        @memo
        def fun(a,b):
            self.fun_invokes+=1
            return a+b
        self.fun=fun

    def test_memo_call_once(self):
        """
        test if memo really uses its cache
        """
        self.assertEqual(self.fun_invokes, 0)
        self.fun('ahoj', 'svet')
        self.assertEqual(self.fun_invokes, 1)
        self.fun('ahoj', 'svet')
        self.assertEqual(self.fun_invokes, 1)
        self.fun('ahoj', 'jozo')
        self.assertEqual(self.fun_invokes, 2)
        self.fun('ahoj', 'jozo')
        self.assertEqual(self.fun_invokes, 2)

    def test_memo_call_consistency(self):
        """
        test if memo returns correct result when using cache
        """
        res1=self.fun('ahoj', 'svet')
        res2=self.fun('ahoj', 'svet')
        self.assertEqual(res1, res2)

    def test_fail_if_mutable(self):
        """
        if memo-ing mutable (unhashable) arguments, Exception is raised
        """
        self.assertRaises(Exception, self.fun, [1,2],[3,4])


unittest.main()

