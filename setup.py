import setuptools

setuptools.setup(
        name='salesforce',
        verion='0.1',
        packages=setuptools.find_packages(),
        install_requires=[
            'pandas',
            'salesforce_reporting'
            ]
        )
