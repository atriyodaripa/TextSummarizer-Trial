import setuptools

with open("TextSummarizer\TextSummarizer-Trial\README.md", 'r', encoding='utf-8') as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "Text_Summarizer"
AUTHOR_USER_NAME = "atriyo.daripa"
SRC_REPO = "text_summarizer"
AUTHOR_EMAIL = "atriyo.daripa@gmail.com"


setuptools.setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A text summarizer application",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
)
