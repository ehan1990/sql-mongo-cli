import json
import click


@click.command(name="version")
def version_cmd():
    data = {
        "version": "1.0.0",
    }
    print(json.dumps(data, indent=2))
