# python3 setup.py build
# python3 setup.py sdist upload
import setuptools

setuptools.setup(
    name='python-xml2dict',
    version='0.1.1',
    url='https://github.com/gotthardp/python-xml2dict.git',
    author='Petr Gotthard',
    author_email='petr.gotthard@centrum.cz',
    description='Flexible XML to dict Converter',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Development Status :: 4 - Beta"
    ],
    py_modules = ['xml2dict']
)

# end of file
