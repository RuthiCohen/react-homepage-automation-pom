# react-homepage-automation-pom

This test suite uses Python and Selenium WebDriver to test the React.js homepage.

---

### Setup Instructions

1. Clone the project
```bash
git clone https://github.com/RuthiCohen/react-homepage-automation-pom.git
```
2. create & activate a venv
```bash
cd react-homepage-automation-pom
python3 -m venv .venv
source .venv/bin/activate
```

3. Install required packages
```bash
pip install -r requirements.txt
```
---
### Running tests

- Running all tests: 
```bash
pytest tests/ -v
``` 

- Running specific test:
```bash
pytest tests/test_homepage.py -v
```



