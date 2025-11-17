from setuptools import setup, find_packages

setup(
    name='satish_currency_lib',  # library's name
    version='0.1.0',  # library's version
    description='A currency conversion library',
    author='Satish Gupta',
    author_email='mysterysatish@gmail.com',
    url='https://github.com/experimentalsolution/currency-convertor-tool',

    packages=find_packages(),
    install_requires=[
     #No depedncy needed
    ],

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.x'
    ],

    test_suite='tests',  # specify the test directory here
    tests_require=[
        #No dependecny 
    ]
)
