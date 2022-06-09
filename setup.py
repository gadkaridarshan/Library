from setuptools import setup, find_packages

setup(
    name='DGBMICalculator',
    version='1.0.0',
    description='BMI Calculator by Darshan Gadkari',
    url='https://github.com/gadkaridarshan/DGBMICalculator.git',
    author='Darshan Gadkari',

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.9',
    ],

    keywords='rest restful api flask swagger flask-restplus bmi calculator',

    packages=find_packages(),

    install_requires=['flask-restplus==0.9.2', 'Flask-SQLAlchemy==2.5.1'],
)