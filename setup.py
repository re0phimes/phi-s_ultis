from setuptools import setup, find_packages

print(find_packages())

requires = [
    'requests>=2.27.1',
    'loguru>=0.6.0',
    'lxml==4.6.3',
    'pydantic==1.9.1',
    'tqdm==4.62.2',
]


setup(
    name="Encrawler",
    version="0.1.14",
    packages=find_packages(),
    description="增加境外bing news search",
    author="phimes",
    author_email="phimes@163.com",
)
