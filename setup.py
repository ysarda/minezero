import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="minezero",
    version="0.0.1",
    author="Yash Sarda",
    author_email="ysarda9@gmail.com",
    description="Deep Reinforcement Learning in Minecraft",
    long_description=long_description,
    long_description_content_type="text/markdown",
    project_urls={},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    package_data={"": ["*.xml"]},
    python_requires=">=3.8",
    include_package_data=True,
)