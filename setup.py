from setuptools import setup
import json

with open("metadata.json", encoding="utf-8") as fp:
    metadata = json.load(fp)

setup(
    name='lexibank_idssegmented',
    py_modules=['lexibank_idssegmented'],
    include_package_data=True,
    url=metadata.get("url", ""),
    zip_safe=False,
    install_requires=[
        "pylexibank>=3.2.0",
        "collabutils",
        "idspy"
    ],
    extras_require={
        'test': [
            'pytest-cldf',
        ],
    },
)
