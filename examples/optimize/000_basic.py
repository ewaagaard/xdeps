import numpy as np
import xdeps as xd


def my_function(x):
    return [(x[0]-0.0001)**2, (x[1]-0.0003)**2, (x[2]+0.0005)**2]

x0 = [0., 0., 0.]

opt = xd.Optimize.from_callable(my_function, x0=x0, steps=[1e-6, 1e-6, 1e-6],
                        tar=[0., 0., 0.], tols=[1e-12, 1e-12, 1e-12])
opt.solve()

