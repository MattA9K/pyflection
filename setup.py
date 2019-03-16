from setuptools import setup

setup(name='pyflection',
      version='0.1',
      description='Helpers to make Python3 more dynamic. Import modules with strings, call methods using strings, etc...',
      long_description='Declare instances of any class by using strings and invoke methods that belong to a Python3 class without ever importing any modules or declaring any instances.',
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
        'Topic :: Console :: Shell',
      ],
      keywords='reflection dynamic object properties lazy loading import modules',
      url='',
      author='Matt Andrzejczuk',
      author_email='cinicraft@me.com',
      license='DBAD',
      packages=['pyflection'],
      install_requires=[],
      dependency_links=[],
      include_package_data=True,
      zip_safe=False)
