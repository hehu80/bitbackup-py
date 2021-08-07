import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pybitbackup",
    author="Henning Voss",
    author_email="henning@huhehu.com",
    description="A Python tool to download all your BitBucket projects",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hehu80/bitbackup-py",
    project_urls={
        "Bug Tracker": "https://github.com/hehu80/bitbackup-py/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.9",
    scripts=['src/pybitbackup'],
)