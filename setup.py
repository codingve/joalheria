from setuptools import setup, find_packages


def read(filename):
    return [
        req.strip()
        for req
        in open(filename).readlines()
    ]


setup(
    name='joalheria',
    version='0.1.0',
    description='An "Audsat" test for developer interview.',
    author='Veronica Toledo',
    author_email='vntoledo30@gmail.com',
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=read("requirements.txt"),
    extras_require={
        "dev": read("requirements-dev.txt")
    }
)
