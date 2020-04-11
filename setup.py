from setuptools import setup

setup(
    name='lsra-scraper',
    version='0.1.0',
    packages=['lsra_scraper'],
    url='',
    license='MIT License',
    author='houfu',
    author_email='houfu@outlook.sg',
    description='A command that scrapes the LSRA website for a list of law firms in Singapore',
    install_requires=[
        "bs4", "requests", "beautifulsoup4", 'Click', 'html5lib', 'selenium'
    ],
    entry_points='''
    [console_scripts]
    lsra_scraper=lsra_scraper.lsra_scraper:lsra_scraper
    ''',
)
