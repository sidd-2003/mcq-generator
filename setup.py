from setuptools import find_packages,setup

setup(
    name='mcqgenrator',
    version='0.0.1',
    author='Siddhant Dnyane',
    author_email='siddhantdnyane2003@gmail.com',
    install_requires=["groq","langchain","streamlit","python-dotenv","PyPDF2"],
    packages=find_packages()
)