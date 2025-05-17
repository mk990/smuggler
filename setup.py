from setuptools import setup

setup(
    name='smuggler',
    version='1.1.0',
    description='HTTP Request Smuggling Detection Tool',
    long_description="""
    Smuggler is a tool for detecting HTTP request smuggling vulnerabilities.
    It works by sending crafted requests to test for CL.TE and TE.CL desync behaviors.
    """,
    url='https://github.com/mk990/smuggler ',
    license='MIT',
    py_modules=['smuggler'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Security',
        'Topic :: Internet :: WWW/HTTP'
    ],
    packages=['configs','payloads','lib'],  # Include configs as a package
    entry_points={
        'console_scripts': [
            'smuggler = smuggler:main',
        ],
    },
    python_requires='>=3.6',
)
