from setuptools import setup

setup(name='django-dynamic-profiles',
      version=0.1,
      description='User profiles with dynamic fields',
      author='John Groszko',
      author_email='john@tinythunk.com',
      url='http://github.com/jgroszko/django-dynamic-profiles',
      packages=['dynamicprofiles'],
      classifiers=['Development Status :: 4 - Beta',
                   'Environment :: Web Environment',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Utilities'],
      install_requires=[
          'django >= 1.10',
      ]
)
