from pip.req import parse_requirements
from setuptools import setup
from pip.download import PipSession

session = PipSession()
install_reqs = parse_requirements('requirements.txt', session=session)
test_reqs = parse_requirements('test_requirements.txt', session=session)

setup(name='somecomfort',
      version='0.4.1',
      description='A client for Honeywell\'s US-based cloud devices',
      author='Dan Smith',
      author_email='dsmith+somecomfort@danplanet.com',
      url='http://github.org/kk7ds/somecomfort',
      packages=['somecomfort'],
      entry_points={
          'console_scripts': [
              'somecomfort = somecomfort.__main__:main'
          ]
      },
      install_requires=[str(r.req) for r in install_reqs],
      tests_require=[str(r.req) for r in test_reqs],
)
