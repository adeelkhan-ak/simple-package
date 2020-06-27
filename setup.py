from setuptools import setup


# This setup is suitable for "python setup.py develop".

setup(name='mymath',
      version='0.1',
      description='A silly math package',
      author='adeel',
      
      
      packages=['mymath', 'mymath.adv'],
      )