from setuptools import setup, find_packages

setup(
    name="charbot_app",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'django>=3.0,<4.0',
        # Add other dependencies if needed
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)
