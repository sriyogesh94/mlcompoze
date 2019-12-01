import setuptools

with open('readme.md') as readme_file:
    long_description = readme_file.read()

setuptools.setup(
    name='mlcompoze',
    version='0.0.1',
    description='A python package built from scratch to enable productive backend agnostic Data Science workflows',
    long_description=long_description,
    long_description_content_type='text/markdown',
    python_requires='>=3.5',
    packages=setuptools.find_packages(),
    url='https://github.com/sriyogesh94/mlcompoze',
    author='Sri Yogesh',
    author_email='sriyogesh94@gmail.com',
    install_requires=[
        'numpy',
        'pandas',
        'sklearn',
        'tensorflow'
    ],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'License :: OSI Approved :: MIT License'
    ]
)