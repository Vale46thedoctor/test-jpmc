from distutils.core import setup

setup(
    name='test-jpmc',
    version='1.0',
    packages=['RestClient', 'RestServer'],
    url='',
    license='',
    author='supersyro',
    author_email='',
    #py_modules=["unittest" ],
    install_requires=["uvicorn" , "fastapi", "pydantic", "python-dotenv"],
    description='setup.py for jpmc project'
)
