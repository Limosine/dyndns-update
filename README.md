# dyndns-update

## Installation

Clone the repository and install with pip:

```console
$ git clone git@github.com:Limosine/dyndns-update
$ pip install ./dyndns-update
```

## Usage

### Command-line

    usage: dyndns-update [-h] [-c CONFIG] [-f] [{sp,noip}]

    positional arguments:
      {sp,noip}             Update a hostname by provider

    options:
      -h, --help            show this help message and exit
      -c CONFIG, --config CONFIG
                            Specify a config file
      -f, --force           Disable cache

### Python module

```python
import dyndns_update

dyndns_update.update(provider, username, password, hostname)
```

## Configuaration

Syntax of the configuration file:

    force = False
    update {
    <name> {
    provider = noip
    username = <username>
    password = <password>
    hostname = <hostname>
    }
    <name> {
    provider = sp
    username = <username>
    password = <password>
    hostname = <hostname> 
    }
    }

## License
Licensed under the [EUPL-1.2-or-later](./LICENSE).
