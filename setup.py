from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Developers',
  'Operating System :: Unix',
  'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='aiotranslate',
  version='0.0.1',
  description='Free Google translate module that uses async/await syntax.',
  long_description_content_type="text/markdown",
  long_description=open('README.md').read(),
  url='https://github.com/5elenay/aiotranslate/', 
  author='5elenay',
  author_email='',
  license='GNU General Public License v3 (GPLv3)', 
  classifiers=classifiers,
  keywords='translate', 
  packages=find_packages(),
  install_requires=['aiohttp', 'beautifulsoup4'] 
)