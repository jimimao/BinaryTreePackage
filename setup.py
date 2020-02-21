# from distutils.core import setup
# # # from setuptools import setup, find_packages
# # # setup(
# # #     name="BinaryTreeVisual",
# # #     keywords = ('Visual', 'BinaryTree'),
# # #     version="0.0.1",
# # #     author= "JimiMao",
# # #     author_email = '381682386@qq.com',
# # #     long_description=" a test package of visualization of Binary Tree",
# # #     # py_modules=['BinaryTreeVisual'],
# # #     license = 'MIT License',
# # #     packages = find_packages(),
# # #     platforms= 'any',
# # #     )
# # setup(
# #     name="BinaryTreeVisual",
# #     version="0.0.1",
# #     py_modules=['BinaryTreeVisual'],
# #     )

import setuptools
#
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="BinaryTreeVisual",
    version="0.0.1",
    author="Example Author",
    author_email="author@example.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)