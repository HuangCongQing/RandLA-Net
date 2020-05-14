'''
@Description: 
@Author: HCQ
@Company(School): UCAS
@Date: 2020-05-04 18:18:08
@LastEditors: HCQ
@LastEditTime: 2020-05-14 21:55:10
'''
from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
import numpy

""" 
首先在utils/nearest_neighbors目录下的steup.py文件下进行编译，然后生成nearest_neighbors，
接着在helper_tool.py文件通过import nearest_neighbors.lib.python.nearest_neighbors as nearest_neighbors调用，具体用在knn_search函数里面调用，然后在main_S3DIS.py或者其他main_.py文件通过from helper_tool import DataProcessing as DP调用，
具体用在neighbour_idx = tf.py_func(DP.knn_search, [batch_xyz, batch_xyz, cfg.k_n], tf.int32)
以及up_i = tf.py_func(DP.knn_search, [sub_points, batch_xyz, 1], tf.int32)
 """

ext_modules = [Extension(
       "nearest_neighbors",
       sources=["knn.pyx", "knn_.cxx",],  # source file(s)
       include_dirs=["./", numpy.get_include()],
       language="c++",            
       extra_compile_args = [ "-std=c++11", "-fopenmp",],
       extra_link_args=["-std=c++11", '-fopenmp'],
  )]

setup(
    name = "KNN NanoFLANN",
    ext_modules = ext_modules,
    cmdclass = {'build_ext': build_ext},
)
