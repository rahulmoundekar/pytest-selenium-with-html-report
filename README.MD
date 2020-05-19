# PYTEST-SELENIUM WITH HTML REPORTS :

![python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)

#### Pre Requisites

  - Making the project as :
    ```
    mkdir pytest-selenium-with-html-report
	cd pytest-selenium-with-html-report
    ```
  - Web Scraping installation:
     ```
     open command prompt type 
        pip install virtualenv
     create virtualenv
    	>>virtualenv venv
     we need to activate virtualenv for use
    	>>venv\scripts\activate
    ```
  - Run the following command in your command line:
    ```
    pip install -U pytest OR pip install pytest
    pip install pytest-html
    pip install selenium
    ```
  - Way of execute program as below :
     >pytest -v -s --html=reports.html --self-contained-html
     
     >pytest -v -s --html=.\reports\report.html --self-contained-html
