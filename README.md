# onemt
onemt

export PYTHONPATH=$PYTHONPATH:/home/vandan/work/research/translation/repos/onemt_big/fairseq

 2172  git checkout v0.12.2
 2173  pip install --editable ./
 2174  pip3 install --upgrade pip==24.0.0
 2175  pip install --editable ./



# LOCAL INSTALL

bash install_server.sh

# LOCAL START

sh start.sh

# Docker Build

bash docker_build.sh 

# Docker Run

bash docker_run.sh 

# Docker check

docker container ls

# Docker Stop/Delete Container

docker rm -f <container-id>



# API URL 

http://0.0.0.0:8084/onemtapi/v1/translateulca

# Input (ULCA)

{
    "input": [
        {
            "source": "नमस्ते"
        }
    ],
    "config": {
        "modelId":101,
        "language": {
            "sourceLanguage": "hin",
            "targetLanguage": "eng"
            }
    }
}

# Output (ULCA)

{
    "output": [
        {
            "source": "नमस्ते",
            "target": "Hi."
        }
    ],
    "config": {
        "modelId": 101,
        "language": {
            "sourceLanguage": "hin",
            "targetLanguage": "eng"
        }
    }
}
