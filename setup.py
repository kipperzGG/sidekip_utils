from setuptools import setup, find_packages

VERSION = '0.0.1'

# Setting up
setup(
    name="sidekip_utils",
    version=VERSION,
    author="kipperz",
    author_email="<kip@kipperz.gg>",
    description="sidekip Utilities",
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[],
    python_requires='>=3.8.0',
    classifiers=[
        'Natural Language :: English',
    ]
)