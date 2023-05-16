import json

import quart
import quart_cors
from quart import request

app = quart_cors.cors(quart.Quart(__name__), allow_origin="https://chat.openai.com")

import docker

import subprocess
import tempfile
import os

def run_code_in_container(language, code):
    # select docker image based on language
    if language.lower() == 'javascript' or language.lower() == 'typescript':
        image = 'node'
        file_extension = '.js'
    elif language.lower() == 'ruby':
        image = 'ruby'
        file_extension = '.rb'
    elif language.lower() == 'python':
        image = 'python'
        file_extension = '.py'
    else:
        raise ValueError(f'Unsupported language: {language}')

    # create a temporary file and write the code to it
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=file_extension)
    temp_file.write(code.encode())
    temp_file.close()

    # build and run the docker command
    try:
        command = f'docker run --rm -v {os.path.dirname(temp_file.name)}:/tmp {image} {image} /tmp/{os.path.basename(temp_file.name)}'
        process = subprocess.run(command, shell=True, check=True, capture_output=True)
    finally:
        os.unlink(temp_file.name)  # clean up the temporary file

    return process.stdout.decode()

# Example usage:
#print(run_code_in_container('python', 'print("Hello, world!")'))

@app.post("/eval")
async def eval():
    request = await quart.request.get_json(force=True)
    print(request)
    code = request['code']
    

    out = run_code_in_container(request['lang'], code)
    response = {"stdout": out}

    return quart.Response(response=json.dumps(response), status=200)



@app.get("/logo.png")
async def plugin_logo():
    filename = 'logo.png'
    return await quart.send_file(filename, mimetype='image/png')

@app.get("/.well-known/ai-plugin.json")
async def plugin_manifest():
    host = request.headers['Host']
    with open("./.well-known/ai-plugin.json") as f:
        text = f.read()
        return quart.Response(text, mimetype="text/json")

@app.get("/openapi.yaml")
async def openapi_spec():
    host = request.headers['Host']
    with open("openapi.yaml") as f:
        text = f.read()
        return quart.Response(text, mimetype="text/yaml")

def main():
    app.run(debug=True, host="0.0.0.0", port=5003)

if __name__ == "__main__":
    main()


