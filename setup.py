import os
try:
    from setuptools import setup 
except ImportError: 
    from distutils.core import setup 

setup(name='wolframalpha',
      author='liato',
      author_email='x@x00.us',
      url='http://github.com/liato/wolframalpha',
      license='MIT',
      version=0.1,
      description="A python interface to WolframAlpha.",
      long_description="A python interface to WolframAlpha.",
      classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Database :: Front-Ends',
        'Topic :: Software Development :: Libraries :: Python Modules',
      ],
      keywords='wolframalpha wolfram alpha scraping mathematica database',
      py_modules=['wolframalpha'],
      install_requires=['lxml'])
