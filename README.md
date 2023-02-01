# ai-assisted-writing

## Requirements
- python=3.10
- ```
  pip install requirements.txt
  ```

## Usage
> passcode: abc

### 1. create an api json file
create a `.api.json` file under the project root.
An example:
```
{
  "openai": "sk-...",
  "ocr_app_id": "...",
  "ocr_app_key": "..."
}
```

### 2. use Docker
```angular2html
sudo docker build -t ai-assisted-writting:0.1.0 .
sudo docker run -p 8501:8501 --name aaw ai-assisted-writting:0.1.0
```

### 2. run locally
```angular2html
streamlit run app.py
```