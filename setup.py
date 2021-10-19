from setuptools import setup

install_requires = list(val.strip() for val in open('requirements.txt'))
tests_require = list(val.strip() for val in open('test_requirements.txt'))

setup(name='somecomfort',
      version='0.8.0',
      description='A client for Honeywell\'s US-based cloud devices',
      author='Dan Smith',
      author_email='dsmith+somecomfort@danplanet.com',
      url='https://github.com/kk7ds/somecomfort',
      packages=['somecomfort'],
      entry_points={
          'console_scripts': [
              'somecomfort = somecomfort.__main__:main'
          ]
      },
      install_requires=install_requires,
      tests_require=tests_require,
)
