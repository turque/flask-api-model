from setuptools import find_packages, setup

__version__ = "0.1"

setup(
    name="my_api",
    version=__version__,
    packages=find_packages(exclude=["tests"]),
    install_requires=[
        "Flask",
        "Flask-RESTful",
        "Werkzeug",
        "Flask-SQLAlchemy",
        "SQLAlchemy",
        "psycopg2-binary",
        "Flask-Migrate",
        'gevent',
        'gunicorn',
        'supervisor',
        "Flask-Login",
        "Flask-Bcrypt",
        "flask-jwt-extended",
        "environs",
        "flask-loguru",
        "apispec[yaml]",
        "apispec-webframeworks",
    ]
)
