from setuptools import setup

setup(
    name='tap-appcues',
    version='0.1.0',
    description='Singer.io tap for extracting data from Appcues using the bulk export API',
    author='Your Name',
    url='https://github.com/your-username/tap-appcues',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    packages=['tap_appcues'],
    install_requires=[
        'requests',
        'singer-python'
    ],
    entry_points='''
        [console_scripts]
        tap-appcues=tap_appcues.__main__:main
    '''
)
