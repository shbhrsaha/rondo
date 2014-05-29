from distutils.core import setup
setup(
  name = 'rondo',
  packages = ['rondo'],
  scripts=['scripts/rondo'],
  version = '0.2',
  description = 'Record and replay mouse and keyboard actions in VirtualBox sessions',
  author = 'Shubhro Saha',
  author_email = 'saha@princeton.edu',
  url = 'https://github.com/shbhrsaha/rondo',
  download_url = 'https://github.com/shbhrsaha/rondo/tarball/0.2',
  keywords = ['virtualbox', 'virtual machine', 'record', 'play'],
  classifiers = [],
  install_requires=[
          'pyvbox',
  ],
)