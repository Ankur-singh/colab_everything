# colab_everything
> Python library to run streamlit, flask, fastapi, etc on google colab.


## Install

`pip install colab-everything`

## Introduction

We cannot access the localhost on Google Colab, as we do on our local machine because Google Colab provides a VM(virtual machine). Hence, we will have to expose it to a public URL to access it. We can use [ngrok](https://ngrok.com/). **Ngrok** exposes local servers behind NATs and firewalls to the public internet over secure tunnels.

This library hides away all the complexity and provides you simple interface to run your webapps on colab. The library can be used in the following scenario:
- To test your web app before deploying it into production. 
- To share the app with peers, friends, and clients; so that they can use/test your app and provide feedbacks.

## How to use

**Note:** The library is only responsible for port tunneling. So, you will have setup everything required to run your web app. For example; installing all the dependecies, setting up all the environment varibles, etc.

#### Streamlit app

```python
from colab_everything import ColabStreamlit
ColabStreamlit('app.py') # streamlit app path
```

#### Flask app

```python
from colab_everything import ColabFlask
ColabFlask('app.py') # Flask app path
```

#### FastAPI app

**Note:** FastAPI uses `uvicorn`, so the syntax is a bit different. You will have to pass only the file name (without extention). For example, pass `main` if your app is `main.py`.

```python
from colab_everything import ColabFastapi
ColabFastapi('app') # FastAPI app file name
```

#### Any other Custom app or command

You can use `ColabCustom` to easily run an other app or command.

To be very honest, you will never have to use `http.server` because colab already provides a file explorer. The example below is just for demonstration purposes.

**Note:** The default port is 9999. If you are using any other port then you will have specify it twice; in the command and also in the argument.

```python
## Using default port
from colab_everything import ColabCustom
cmd = 'python -m http.server 9999'
ColabCustom(cmd)
```

```python
## Using non-default port
from colab_everything import ColabCustom
cmd = 'python -m http.server 10000'
ColabCustom(cmd, port=10000)
```

I am actively looking for feedbacks and contributions. Feel free to contact me at *as.ankursingh3.1@gmail.com*.
