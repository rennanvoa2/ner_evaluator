import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ner_evaluator",
    version="1.0.1",
    author="Rennan Valadares",
    author_email="rennanvoa2@gmail.com",
    description="Evaluate Named Entity Recognition (NER) models",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rennanvoa2/evaluate_ner_models",
    project_urls={
        "Bug Tracker": "https://github.com/rennanvoa2/evaluate_ner_models/issues"
    },
    license="None",
    packages=["ner_evaluator"],
    install_requires=["rapidfuzz"],
)
