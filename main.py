import requests
from pyscript import document, when


@when("click", "#getSettings")
def settings_get(event) -> dict:
    APIUrl = "your api url"
    idInstance = document.querySelector("#idInstance")
    idInstance = idInstance.value
    apiTokenInstance = document.querySelector("#apiTokenInstance")
    apiTokenInstance = apiTokenInstance.value
    url = f"{APIUrl}/waInstance{idInstance}/getSettings/{apiTokenInstance}"
    response = requests.get(url, verify=False)
    response_data = response.json()
    output_div = document.querySelector("#output")
    output_div.innerText = response_data


@when("click", "#getStateInstance")
def state_instance_get(event) -> dict:
    APIUrl = "your api url"
    idInstance = document.querySelector("#idInstance")
    idInstance = idInstance.value
    apiTokenInstance = document.querySelector("#apiTokenInstance")
    apiTokenInstance = apiTokenInstance.value
    url = f"{APIUrl}/waInstance{idInstance}/getStateInstance/{apiTokenInstance}"
    response = requests.get(url, verify=False)
    response_data = response.json()
    output_div = document.querySelector("#output")
    output_div.innerText = response_data


@when("click", "#sendMessage")
def message_send(event) -> dict:
    APIUrl = "your api url"
    idInstance = document.querySelector("#idInstance")
    idInstance = idInstance.value
    apiTokenInstance = document.querySelector("#apiTokenInstance")
    apiTokenInstance = apiTokenInstance.value
    chatId = document.querySelector("#chatId")
    chatId = chatId.value
    message = document.querySelector("#message")
    message = message.value
    data = {
    "chatId": f"{chatId}@c.us",
    "message": message,
    
        }
    url = f"{APIUrl}/waInstance{idInstance}/sendMessage/{apiTokenInstance}"
    response = requests.post(url, verify=False, json=data)
    response_data = response.json()
    output_div = document.querySelector("#output")
    output_div.innerText = response_data


@when("click", "#sendFileByUrl")
def file_send(event) -> dict:
    APIUrl = "your api url"
    idInstance = document.querySelector("#idInstance")
    idInstance = idInstance.value
    apiTokenInstance = document.querySelector("#apiTokenInstance")
    apiTokenInstance = apiTokenInstance.value
    chatIdfile = document.querySelector("#chatIdfile")
    chatIdfile = chatIdfile.value
    urlFile = document.querySelector("#urlFile")
    urlFile = urlFile.value
    data = {
    "chatId": f"{chatIdfile}@c.us",
    "urlFile": urlFile,
    "fileName": "cat.png",
    "caption": "Кот"
        }
    url = f"{APIUrl}/waInstance{idInstance}/sendFileByUrl/{apiTokenInstance}"
    response = requests.post(url, verify=False, json=data)
    response_data = response.json()
    output_div = document.querySelector("#output")
    output_div.innerText = response_data
    