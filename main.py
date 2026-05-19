import click
from rich.console import Console
from rich.table import Table
import json
import os
from datetime import date

console = Console()
DATA_FILE = "log.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE) as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

@click.group()
def cli():
    pass

if __name__ == "__main__":
    cli()