from setuptools import setup, find_packages

setup(
    name="stockscraper",
    version="1.0",
    description="Stock Scraper",
    url="http://github.com/davidjura/stockscraper",
    author="David Jura",
    license="MIT",
    packages=find_packages(),
    install_requires=[
        "requests",
        "pandas",
        "fake-useragent"
    ],
    entry_points = {
        "console_scripts": ["stock-scraper=stockscraper.cli:main"],
    }
)
