# pylint: disable=no-value-for-parameter

from utils import utils as u
import click

@click.command()
@click.help_option('-h', '--help')
def main():

    # raw data
    casos, fallecidos = u.get_datasets()
    raw_data = {
        "casos": casos,
        "fallecidos": fallecidos
    }
    u.import_datasets_to_carto(raw_data)

    # unnested data
    unnested_casos, unnested_fallecidos = u.get_unnested_datasets()
    unnested_data = {
        "unnested_casos": unnested_casos,
        "unnested_fallecidos": unnested_fallecidos
    }
    u.import_datasets_to_carto(unnested_data)

    # centroids data
    centroids_casos, centroids_fallecidos = u.get_centroids_datasets()
    centroids_data = {
        "centroids_casos": centroids_casos,
        "centroids_fallecidos": centroids_fallecidos
    }
    u.import_datasets_to_carto(centroids_data)

if __name__ == "__main__":
    main()
