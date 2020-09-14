import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
        name='nau7802',
        version='0.8.5',
        author='Lukas Jaworski',
        author_email='ljaworski88@gmail.com',
        description='A library used to interact with the Nouvton NAU 7802 sensor',
        long_description=long_description,
        long_description_content_type='text/markdown',
        url='https://github.com/ljaworski88/nau7802-py',
        packages=setuptools.find_packages(),
        classifiers=[
            'Programming Language :: Python :: 3',
            'License :: OSI Approved :: GPLv3 License',
            'Operating System :: OS Independant',
            ],
        python_requires='>=3.6',
        )
