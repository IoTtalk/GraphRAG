# Implementation of Graph RAG from Microsoft

## Env

### OS

Currently, this git repo has just tried under Windows OS.

### Python version

Python 3.10 - 3.12

### Wheel requirement

C++ compilor and Visual Studio tools.

You can download VS tools from the site below:

https://visualstudio.microsoft.com/visual-cpp-build-tools/

The VS tools need about 9GB of storage in your computer.

### Python package

```pip install graphrag```

or

```pip install -r requirement.txt```

## How to run Graph RAG

### Step 1 : Download Dataset

The command in Microsoft tutorial cannot successfully download the text file we need, so I write a python file to download and stored the text file.

Run the command below:

```python3 grab.py```

This action will build a folder ```input``` and stored the text file into ```book.txt``` in this folder.


### Step 2 : 

Run the command below:

```python -m graphrag.index --init```

This action will build up two files ```.env``` and ```settings.yaml```

If you clone this git repo, you can skip this step.

### Step 3 :

Change the value of ```GRAPHRAG_API_KEY``` in ```.env``` to your own OpenAI API key or Azure API key.

### Step 4 :

Run the command below:

```python -m graphrag.index```

A series of parquet files will be created according to our document ```book.txt``` after the action.

By now, our Graph RAG has been set up successfully and is ready to be used.

## Source Site

https://microsoft.github.io/graphrag/posts/get_started/
