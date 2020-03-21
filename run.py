# pylint: disable=no-value-for-parameter

from utils import utils as u
import click
import time

DATE_RANGE = u.get_date_range()
STRING_DATE_RANGE = u.get_string_date_range(DATE_RANGE)
UNDERSCORE_DATE_RANGE = u.get_underscore_date_range(DATE_RANGE)


@click.command()
@click.help_option('-h', '--help')
def main():

    # raw data
    casos, fallecidos, uci, altas = u.get_datasets()
    raw_data = {
        "casos": casos,
        "fallecidos": fallecidos,
        "uci": uci,
        "altas": altas
    }
    u.import_datasets_to_carto(raw_data)
    time.sleep(60)

    # unnested data
    unnested_casos, unnested_fallecidos, unnested_uci, unnested_altas = u.get_unnested_datasets(
        STRING_DATE_RANGE,
        UNDERSCORE_DATE_RANGE
    )
    unnested_data = {
        "unnested_casos": unnested_casos,
        "unnested_fallecidos": unnested_fallecidos,
        "unnested_uci": unnested_uci,
        "unnested_altas": unnested_altas,
    }
    time.sleep(60)
    u.import_datasets_to_carto(unnested_data)
    time.sleep(60)
    u.update_geoms()

    # centroids data
    centroids_casos, centroids_fallecidos, centroids_uci, centroids_altas = u.get_centroids_datasets(
        STRING_DATE_RANGE,
        UNDERSCORE_DATE_RANGE
    )
    centroids_data = {
        "centroids_casos": centroids_casos,
        "centroids_fallecidos": centroids_fallecidos,
        "centroids_uci": centroids_uci,
        "centroids_altas": centroids_altas,
    }
    time.sleep(60)
    u.import_datasets_to_carto(centroids_data)


if __name__ == "__main__":
    main()
