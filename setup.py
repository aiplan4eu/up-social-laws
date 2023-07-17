#!/usr/bin/env python3

from setuptools import setup # type: ignore
import social_laws


long_description=\
'''
 ============================================================
    SOCIAL_LAWS
 ============================================================

    social_laws is a package that allows for various compilations and checks related to social law verification and synthesis.
'''

setup(name='social_laws',
      version=social_laws.__version__,
      description='social_laws',
      author='Technion Cognitive Robotics Lab',
      author_email='karpase@technion.ac.il',
      url='https://github.com/aiplan4eu/up-social-laws',
      packages=['social_laws'],
      install_requires=[],
      python_requires='>=3.7',
      license='APACHE'
)
