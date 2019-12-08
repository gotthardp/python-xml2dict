# python3 setup.py build
# python3 setup.py sdist upload
import setuptools

setuptools.setup(
    name='xml2dict',
    version='0.1.0',
    url='https://github.com/gotthardp/python-xml2dict.git',
    author='Petr Gotthard',
    author_email='petr.gotthard@centrum.cz',
    description='Flexible XML to dict Converter',
    packages=setuptools.find_packages(),
    install_requires=[],
)

# end of file
