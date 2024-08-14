from setuptools import setup, find_packages

setup(
    name="elections-scraper",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests",
        "beautifulsoup4"
    ],
    entry_points={
        "console_scripts": [
            "elections_scraper=elections_scraper.scraper:main"
        ],
    },
    description="A tool to scrape election results from volby.cz.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Vasyl Burov",
    author_email="vasylburov@gmail.com",
    url="https://github.com/vasburov/project",
    license="MIT"
)
