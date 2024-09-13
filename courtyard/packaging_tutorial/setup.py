import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="DingTalkLoginTool",
    version="0.0.2",
    author="samplecatalina",
    author_email="",
    description="DingTalkLoginTool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/samplecatalina-ai/courtyard/tree/master/courtyardMall/courtyardMall/utils",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

# 在当前目录下打包并上传
# python3 setup.py sdist
# python3 setup.py sdist upload
