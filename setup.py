from setuptools import setup

def readme():
  with open('README.md') as f:
    return f.read()

setup(name='mdtsne',
      version='0.1',
      description='Barnes-Hut t-SNE for analysis of molecular dynamics trajectories',
      long_description=readme(),
      classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Scientific/Engineering :: Chemistry',
      ],
      keywords='Barnes-Hut t-SNE dimensionality reduction molecular dynamics simulation',
      url='https://github.com/spiwokv/mdtsne',
      author='Vojtech Spiwok, ',
      author_email='spiwokv@vscht.cz',
      license='MIT',
      packages=['mdtsne'],
      scripts=['bin/mdtsne'],
      install_requires=[
          'numpy',
          'cython',
          'mdtraj',
          'sklearn',
          'argparse',
          'datetime',
      ],
      include_package_data=True,
      zip_safe=False)

