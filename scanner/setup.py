from setuptools import setup

setup(
    name='scanner',
    version='1.0',
    description='Scans open ports',
    author='sandjaie',
    py_modules=['scanner', 'functions'],
    install_requires=['click', 'termcolor'],
    entry_points={
        'console_scripts': [
            'scanner=scanner:main'
        ]
    }
)
