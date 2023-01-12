# ai-assisted-writing

## Requirements
- python=3.7
- ```
  pip install requirements.txt
  ```

## Usage
> passcode: abc
### use Docker
```angular2html
sudo docker build -t ai-assisted-writting:0.1.0 .
sudo docker run -p 8501:8501 --name aaw ai-assisted-writting:0.1.0
```

### run locally
```angular2html
streamlit run app.py
```