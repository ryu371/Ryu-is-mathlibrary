from setuptools import setup, find_packages

setup(
    name="RyuEngine",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        # 依存するライブラリを記述
        "requests",
    ],
    author="ryu371",
    description="A brief description",
)
