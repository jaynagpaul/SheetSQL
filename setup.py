from setuptools import setup

setup(
    name="SheetsDB",
    version="0.0.1",
    description="Google Sheets as a SQL Database",
    author="SpiesWithin",
    author_email="spieswithin@gmail.com",
    url="https://github.com/SpiesWithin/SheetsDB",
    packages=["sheetsdb"],
    install_requires=["pygsheets"],
    setup_requires=["pytest-runner"],
    tests_require=["pytest"]
)
