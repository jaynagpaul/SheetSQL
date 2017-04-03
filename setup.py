from setuptools import setup

setup(
    name="sheetsql",
    version="0.0.1",
    description="Google Sheets as a SQL Database",
    author="SpiesWithin",
    author_email="spieswithin@gmail.com",
    url="https://github.com/SpiesWithin/SheetSQL",
    packages=["sheetsql"],
    install_requires=["gspread", "oauth2client", "sqlparse"],
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
    license="MIT"
)
