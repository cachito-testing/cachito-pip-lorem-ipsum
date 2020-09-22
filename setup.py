import setuptools

setuptools.setup(
    name="lorem-ipsum",
    version="0.1.0",
    install_requires=["requests"],
    packages=setuptools.find_packages(),
    entry_points={"console_scripts": ["lorem.py = lorem_ipsum.lorem:main"]},
)
