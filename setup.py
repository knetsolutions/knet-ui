from setuptools import setup
from setuptools import find_packages

install_requires = [
    'flask',
]
test_requires = []

setup(
    name='knet-ui',
    version='0.1',
    description="KNet Next UI",
    author="S.Suresh Kumar",
    author_email="sureshkumarr.s@gmail.com",
    url="https://github.com/knetsolutions/knet-ui",
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    keywords='knet',
    scripts=[],
    license="Apache",
    entry_points={
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: User Interfaces',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7'
    ]
)
