#!/usr/bin/env python3

from setuptools import setup # type: ignore
import up_social_laws


long_description=\
'''
 ============================================================
    SOCIAL_LAWS
 ============================================================

    up_social_laws is a package that allows for various compilations and checks related to social law verification and synthesis.
'''

try:
    from wheel.bdist_wheel import bdist_wheel as _bdist_wheel

    class bdist_wheel(_bdist_wheel):

        def finalize_options(self):
            _bdist_wheel.finalize_options(self)
            # Mark us as not a pure python package
            self.root_is_pure = False

        def get_tag(self):
            python, abi, plat = _bdist_wheel.get_tag(self)
            # We don't link with python ABI, but require python3
            python, abi = 'py3', 'none'
            return python, abi, plat
except ImportError:
    bdist_wheel = None



setup(name='up_social_laws',
      version=up_social_laws.__version__,
      description='Unified Planning Integration of Social Laws',
      author='Technion Cognitive Robotics Lab',
      author_email='karpase@technion.ac.il',
      url='https://github.com/aiplan4eu/up-social-laws',
      classifiers=['Development Status :: 4 - Beta',
               'License :: OSI Approved :: Apache Software License :: 2.0',
               'Programming Language :: Python :: 3',
               'Topic :: Scientific/Engineering :: Artificial Intelligence'
               ],
      packages=['up_social_laws'],
    #   cmdclass={
    #       'bdist_wheel': bdist_wheel
    #   },
      install_requires=[],
      python_requires='>=3.7',
      license='APACHE'
)
