## How it is distributed :
  - You’ll need to install Twine:
      - `pip install twine`
  - Now run this command from the same directory where `setup.py` is located (this creates the files in the dist folder): 
      - `python setup.py sdist`
  - Register an account at PyPI:
      - https://pypi.org/
  - Once installed, run Twine to upload all of the archives under dist:
      - `twine upload dist/*`
  - You will be asked to provide your username and password. Provide the credentials you used to register to PyPi earlier.
  - **Note:** if the project name has already been registered on test.pypi.org and pypi.org you will get the following error 'his filename has already been used, use a different version'.

**The package is now uploaded: visit https://pypi.org/project/AD-cs207/ to see your package online.**
  
**Go to the 'How-to-install.md' guidelines for installing your newly uploaded package.**
