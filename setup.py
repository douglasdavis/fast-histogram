import os
import io
import sys

from setuptools import setup
from setuptools.extension import Extension
from setuptools.command.build_ext import build_ext


class build_ext_with_numpy(build_ext):
    def run(self):
        import numpy
        self.include_dirs.append(numpy.get_include())
        build_ext.run(self)


extensions = [Extension("fast_histogram._histogram_core",
                        [os.path.join('fast_histogram', '_histogram_core.c')])]

with io.open('README.rst', encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

if 'egg_info' in sys.argv:
    setup_requires = []
else:
    setup_requires = ['numpy']

setup(name='fast-histogram',
      version='0.6.dev0',
      description='Fast simple 1D and 2D histograms',
      long_description=LONG_DESCRIPTION,
      setup_requires=setup_requires,
      install_requires=['numpy'],
      author='Thomas Robitaille',
      author_email='thomas.robitaille@gmail.com',
      license='BSD',
      url='https://github.com/astrofrog/fast-histogram',
      packages=['fast_histogram', 'fast_histogram.tests'],
      ext_modules=extensions,
      cmdclass={'build_ext': build_ext_with_numpy})
