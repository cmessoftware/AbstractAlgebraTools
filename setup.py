from setuptools import setup

setup(
    name='pyexample',
    version='0.1.0',    
    description='Grupo theory academic practices',
    url='https://github.com/cmessotfware/pygroup',
    author='Sergio Salanitri',
    author_email='cmessoftware@gmail.com',    
    license='BSD 2-clause',
    packages=['pygroup'],
    install_requires=['numpy',
                      ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',  
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 3.11',
    ],
)    