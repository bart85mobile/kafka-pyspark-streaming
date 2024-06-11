# Introduction

## Project directory
    .
    ├── local                # Contains python files to run locally
    │   └── config.py        # Contains Kafka cluster connection details used by the consumer & producer
    │   └── consumer.py      # Consumes messages to the sink topic
    │   └── producer.py      # Produces messages to the source topic
    │   └── requirements.txt # Contains libraries needed to run local .py files
    └── Kafka PySpark.ipynb  # Notebook to be imported and run on Databricks

# Usage
## Prerequisites
* Python 3.9+
* Upstash account
* Databricks account

## Setting up
1. Make a virtual environment in your project directory by running `python -m venv .venv`
2. Activate the virtual environment by running `source .venv/bin/activate`
3. Install the necessary libraries on your virtual environment by running `pip install -r local/requirements.txt`
4. Update `local/config.py` with your Kafka cluster connection details from Upstash
5. Update `Kafka PySpark Notebook.ipynb` with your Kafka cluster connection details from Upstash
6. Import `Kafka PySpark Notebook.ipynb` to Databricks

## Running
1. Run `producer.py` in your local machine to write to the `source` topic
2. Run `Kafka PySpark Notebook.ipynb` on Databricks to consume from `source`, process, then write to the `sink` topic
3. Run `consumer.py` in your local machine to consume the processed messages from `sink` topic