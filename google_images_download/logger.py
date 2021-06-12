import typer
import json
from typing import Dict, Any


def raise_error(msg: str):
    typer.echo(msg, err=True)
    raise typer.Abort()


def log_info(msg: str):
    typer.echo(msg)


def pretty_log_info(dict_object: Dict[str, Any]):
    log_info(json.dumps(dict_object, indent=True))
