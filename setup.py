from setuptools import setup

setup(
    name='AbstractAlgebraTools',
    version='0.0.1',    
    description='Grupo theory academic practices',
    url='https://github.com/cmessotfware/AbstractAlgebraTools',
    author='Sergio Salanitri',
    author_email='cmessoftware@gmail.com',    
    license='BSD 2-clause',
    packages=['AbstractAlgebraTools'],
    install_requires=['numpy',
                       'pandas',
                       'fractional',
                       'networkx',
                       'pytest',
                       'pytest-html'
                      ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',  
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 3.11',
    ],
)    