import setuptools

setuptools.setup(
    name="pyschool",
    version="0.0.1",
    author="Shigeru Kitazaki",
    # author_email="author@example.com",
    description="A small example package",
    url="https://github.com/skitazaki/python-school-ja/",
    packages=setuptools.find_packages("src"),
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
