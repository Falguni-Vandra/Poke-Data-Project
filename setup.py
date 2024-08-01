from setuptools import setup, find_packages


setup(
    name='pokemon_library',
    version='0.1.0',
    description='A library for Pokémon data processing and analysis',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Fal',
    author_email='your.email@example.com',
    url='https://github.com/Falguni-Vandra/Poke-Data-Analysis-Project.git',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    python_requires='>=3.11',
    install_requires=[
        'pandas',
        'requests',
        'pytest',
        'pylint',
        'pyspark',
        'sqlalchemy',
        'psycopg2-binary',
        'pymongo'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.11',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    entry_points={
        'console_scripts': [
            'pokemon_library=run_all:main',
        ],
    },
)
