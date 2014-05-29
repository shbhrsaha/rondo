from distutils.core import setup
setup(
  name = 'rondo',
  packages = ['rondo'], # this must be the same as the name above
  scripts=['scripts/rondo'],
  version = '0.2',
  description = 'Record and replay mouse and keyboard actions in VirtualBox sessions',
  author = 'Shubhro Saha',
  author_email = 'saha@princeton.edu',
  url = 'https://github.com/shbhrsaha/rondo', # use the URL to the github repo
  download_url = 'https://github.com/shbhrsaha/rondo/tarball/0.2', # I'll explain this in a second
  keywords = ['virtualbox', 'virtual machine', 'record', 'play'], # arbitrary keywords
  classifiers = [],
  install_requires=[
          'pyvbox',
  ],
)