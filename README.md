# onemt (HimangY-IIITH)



### LOCAL INSTALL

bash install_server.sh

### LOCAL START

sh start.sh

### Docker Build

bash docker_build.sh 

### Docker Run

bash docker_run.sh 

### Docker check

docker container ls

### Docker Stop/Delete Container

docker rm -f <container-id>




## API URL 

http://0.0.0.0:8084/onemtapi/v1/translateulca

### Input (ULCA)
```
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
```
### Output (ULCA)
```
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
```
# Training Code
- https://ssmt.iiit.ac.in/meitygit/ssmt/mt-model-deploy-dhruva/-/tree/master/training-code

### supported language pairs

| Source - Target (Bi-direction)| 
|-------------------------------|
|Hindi, English <-> Dogri, Kashmiri, Kannada, Sindhi|



## Citation
```bash
@inproceedings{mujadia-sharma-2022-ltrc,
    title = "The {LTRC} {H}indi-{T}elugu Parallel Corpus",
    author = "Mujadia, Vandan  and Sharma, Dipti",
    booktitle = "Proceedings of the Thirteenth Language Resources and Evaluation Conference",
    month = jun,
    year = "2022",
    address = "Marseille, France",
    publisher = "European Language Resources Association",
    url = "https://aclanthology.org/2022.lrec-1.365",
    pages = "3417--3424",
}

@inproceedings{mujadia-sharma-2021-english,
title = "{E}nglish-{M}arathi Neural Machine Translation for {L}o{R}es{MT} 2021",
author = "Mujadia, Vandan  and Sharma, Dipti Misra",
booktitle = "Proceedings of the 4th Workshop on Technologies for MT of Low Resource Languages (LoResMT2021)",
month = aug,
year = "2021",
address = "Virtual",
publisher = "Association for Machine Translation in the Americas",
url = "https://aclanthology.org/2021.mtsummit-loresmt.16",
pages = "151--157",
}
```
