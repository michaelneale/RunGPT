# Run code that ChatGPT generates

You can ask ChatGPT to write snippets of code, and with this plugin you can tell it to evaluate or test the code it writes without leaving ChatGPT. 
You need to have access to ChatGPT plugins to use this (and python installed). 

### Usage: 
![example](https://github.com/michaelneale/RunGPT/assets/14976/9485645b-3013-42af-88c3-8be95eb2e5f7)

## How it works

ChatGPT has a reasonable idea of what language it is generating, so an appropriate docker container can be used to evaluate the code. Note that containerizing is for convenience, not for security. Buyer beware. 
This could be how the machines take over.

## Installing

To install the required packages for this plugin, run the following command:

```bash
pip install -r requirements.txt
```

To run the plugin, enter the following command:

```bash
python main.py
```

Once the local server is running:

1. Navigate to https://chat.openai.com. 
2. In the Model drop down, select "Plugins" (note, if you don't see it there, you don't have access yet).
3. Select "Plugin store"
4. Select "Develop your own plugin"
5. Enter in `localhost:5003` since this is the URL the server is running on locally, then select "Find manifest file".

The plugin should now be installed and enabled! You can start with a question like "What is on my todo list" and then try adding something to it as well! 

## Getting help

Open an issue or fork it. 

## Warning

This will evaluate code in a container that matches the language, so be careful. 
