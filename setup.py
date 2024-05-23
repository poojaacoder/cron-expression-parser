from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="cron-parser",
    version="2.0.0",
    author="Pooja Deshmukh",
    author_email="pooja.deshmukh7745@gmail.com",
    description="Cron expression parser",
    long_description=long_description,
    packages=["cron_parser"],
    entry_points={
        "console_scripts": [
            "cron-parser = cron_parser.cli:cli"
        ]
    },
    python_requires='>=3.12',
)
