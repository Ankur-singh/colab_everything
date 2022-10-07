# AUTOGENERATED! DO NOT EDIT! File to edit: ../00_core.ipynb.

# %% auto 0
__all__ = ['ColabBase', 'ColabStreamlit', 'ColabFlask', 'ColabFastapi', 'ColabCustom']

# %% ../00_core.ipynb 3
import os
import subprocess
from pyngrok import ngrok

# %% ../00_core.ipynb 4
class ColabBase():
    def __init__(self, port=9999):
        self.port = port
        self._start_server()
        
    def _start_server(self):
        active_tunnels = ngrok.get_tunnels()
        for tunnel in active_tunnels:
            public_url = tunnel.public_url
            ngrok.disconnect(public_url)
        url = ngrok.connect(addr=self.port, options={"bind_tls": True}, return_ngrok_tunnel=True)
        print(f'Web App can be accessed on: {url.public_url}')

# %% ../00_core.ipynb 5
class ColabStreamlit(ColabBase):
    def __init__(self, path, port=9999):
        super().__init__(port)
        self.path = path
        self.run_app()

    def run_app(self, debug=True):
        os.system(f"fuser -n tcp -k {self.port}")
        cmd = f'streamlit run {self.path} --server.port {self.port}'
        with subprocess.Popen(
            [cmd],
            shell=True,
            stdout=subprocess.PIPE,
            bufsize=1,
            universal_newlines=True,
            ) as proc:
                for line in proc.stdout:
                    if debug: print(line, end="")

# %% ../00_core.ipynb 6
class ColabFlask(ColabBase):
    def __init__(self, path, port=9999):
        super().__init__(port)
        self.path = path
        self.run_app()

    def run_app(self, debug=True):
        os.system(f"fuser -n tcp -k {self.port}")
        cmd = f'FLASK_APP={self.path} flask run --host=0.0.0.0 --port={self.port}'
        with subprocess.Popen(
            [cmd],
            shell=True,
            stdout=subprocess.PIPE,
            bufsize=1,
            universal_newlines=True,
            ) as proc:
                for line in proc.stdout:
                    if debug: print(line, end="")

# %% ../00_core.ipynb 7
class ColabFastapi(ColabBase):
    def __init__(self, path, app='app', port=9999):
        super().__init__(port)
        self.path = path
        self.app = app
        self.run_app()

    def run_app(self, debug=True):
        os.system(f"fuser -n tcp -k {self.port}")
        cmd = f'uvicorn {self.path}:{self.app} --reload --port {self.port}'
        with subprocess.Popen(
            [cmd],
            shell=True,
            stdout=subprocess.PIPE,
            bufsize=1,
            universal_newlines=True,
            ) as proc:
                for line in proc.stdout:
                    if debug: print(line, end="")

# %% ../00_core.ipynb 8
class ColabCustom(ColabBase):
    def __init__(self, cmd, port=9999):
        super().__init__(port)
        self.cmd = cmd
        self.run_app()

    def run_app(self, debug=True):
        os.system(f"fuser -n tcp -k {self.port}")
        with subprocess.Popen(
            [self.cmd],
            shell=True,
            stdout=subprocess.PIPE,
            bufsize=1,
            universal_newlines=True,
            ) as proc:
                for line in proc.stdout:
                    if debug: print(line, end="")
