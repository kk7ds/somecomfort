from setuptools import setup

setup(name='somecomfort',
      version='0.1',
      description='A client for Honeywell\'s US-based cloud devices',
      author='Dan Smith',
      author_email='dsmith+somecomfort@danplanet.com',
      url='http://github.org/kk7ds/somecomfort',
      packages=['somecomfort'],
      scripts=[],
      install_requires=['requests'],
      tests_require=['mock'],
)
