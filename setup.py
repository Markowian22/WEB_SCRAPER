from setuptools import find_packages, setup

setup(
    name="WEB_SCRAPER_EASY",
    version="0.2",
    description="Library to facviliate webscraping",
    packages=find_packages("src"),
    package_dir={"": "src"},
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Marek Budzicz",
    author_email="budziczmarek@gmail.com",
    url="https://github.com/Markowian22/WEB_SCRAPER",
    install_requires=["selenium"],
    python_requires=">=3.10",
)
