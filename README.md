# Implementation of Graph RAG from Microsoft

## Env

### OS

Currently, this git repo has tried under both Windows and Ubuntu.

### Python version

Python 3.10 - 3.12

### Wheel requirement (Ubuntu users skip this step)

C++ compilor and Visual Studio tools.

You can download VS tools from the site below:

The VS tools need about 9 GB of storage in your computer.

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

```graphrag init --root ./ragtest```

This action will build up two files ```.env``` and ```settings.yaml``` and one folder ```prompts```.

If you clone this git repo, you have to delete ```.env``` and ```settings.yaml``` before run the command.

### Step 3 :

Change the value of ```GRAPHRAG_API_KEY``` in ```.env``` to your own OpenAI API key or Azure OpenAI key.

If you use Azure OpenAI, it is suggested to follow the steps in the site below:

https://www.cnblogs.com/gaocong/p/18299221

### Step 4 :

Run the command below:

```python -m graphrag.index```

A series of parquet files will be created according to our document ```book.txt``` after the action.

By now, our Graph RAG has been set up successfully and is ready to be used.

## Source Site

[GraphRAG Getting Started](https://microsoft.github.io/graphrag/get_started/)
