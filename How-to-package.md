## How to install
  - Make sure you have the latest versions of `setuptools` and `wheel` installed:
      - `python3 -m pip install --user --upgrade setuptools wheel`
  - Now run this command from the same directory where `setup.py` is located: 
      - `python3 setup.py sdist bdist_wheel`
  - The first thing you’ll need to do is register an account on Test PyPI. Test PyPI is a separate instance of the package index intended for testing and experimentation. It’s great for things like this tutorial where we don’t necessarily want to upload to the real index. To register an account, go to https://test.pypi.org/account/register/ and complete the steps on that page. You will also need to verify your email address before you’re able to upload any packages. For more details on Test PyPI, see Using TestPyPI.
  - You’ll need to install Twine:
      - `python3 -m pip install --user --upgrade twine`
  - Once installed, run Twine to upload all of the archives under dist:
      - `twine upload --repository-url https://test.pypi.org/legacy/ dist/*`
  - Once uploaded your package should be viewable on TestPyPI, in your programs:
      - https://test.pypi.org/manage/projects/
	  
	  
**Go to the 'How-to-install.md' guidelines for installing your newly uploaded package.**
