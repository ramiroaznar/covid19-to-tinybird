# pylint: disable=no-value-for-parameter

from utils import utils as u
import click


DATASETS = ['casos', 'fallecidos', 'uci', 'altas']


@click.command()
@click.help_option('-h', '--help')
def main():

    imports = [
        u.import_and_replace(dset) for dset in DATASETS
    ] 

    return imports

if __name__ == "__main__":
    main()
