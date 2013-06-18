# coding: latin-1
"""
@brief      test log(time=1s)

You should indicate a time in seconds. The program ``run_unittests.py``
will sort all test files by increasing time and run them.
"""


import sys, os, unittest


try :
    import src
except ImportError :
    path = os.path.normpath(os.path.abspath( os.path.join( os.path.split(__file__)[0], "..", "..")))
    if path not in sys.path : sys.path.append (path)
    import src

from pyhome3 import fLOG
from src.project_name.subproject.myexample import myclass
from src.project_name.subproject2.myexample2 import myclass2



class TestExample (unittest.TestCase):
    
    def test_split_cmp_command(self) :
        fLOG (__file__, self._testMethodName, OutputPrint = __name__ == "__main__")
        my = myclass(4)
        r  = my.get_value(5)
        ex = 20
        if r != ex : raise Exception("we expect %f, not %f" % (ex, r))
        my2 = myclass2(5)

if __name__ == "__main__"  :
    unittest.main ()    
