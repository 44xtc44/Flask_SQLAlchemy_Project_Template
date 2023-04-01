import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

# ###############################################

pack_name = "Flask_SQLAlchemy_Project_Template"
pack_version = "1.4"
pack_description = "Simple and ready to grow template. Understand Flask SQLAlchemy basics, with examples. Uses " \
                   "Blueprints and application factory. Avoid circular imports."

INSTALL_REQUIRES = [
    'setuptools~=59.2.0',
    'Flask~=2.0.3',
    'flask-sqlalchemy~=2.5'
]
PYTHON_REQUIRES = '>=3.6'

setuptools.setup(

    name=pack_name,  # project name /folder
    version=pack_version,
    author="René Horn",
    author_email="rene_horn@gmx.net",
    description=pack_description,
    long_description=long_description,
    license='MIT License',
    long_description_content_type="text/markdown",
    url="",
    include_package_data=True,
    packages=setuptools.find_packages(),
    install_requires=INSTALL_REQUIRES,
    classifiers=[
        # How mature is this project? Common values are
        # https://packaging.python.org/guides/distributing-packages-using-setuptools/
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable",
        "Framework :: Flask",
    ],
    python_requires=PYTHON_REQUIRES,
)
