![Peer Logo](https://github.com/Kasneci-Lab/AI-assisted-writing/blob/ui/img/Peer_logo.png?raw=true)

Try PEER on [https://peer.edu.sot.tum.de](https://peer.edu.sot.tum.de/)

## Requirements
- python=3.10
- ```
  apt install packages.txt
  pip install requirements.txt
  ```

### 1. create an api json file
Create a `secrects.toml` file under in a `.streamlit` directory.
An example:
```
[openai_secrets]
openai_key =  "sk-..."

[ocr_secrets]
ocr_app_id =  "..."
ocr_app_key = "..."
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
