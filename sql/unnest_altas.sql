with data as (
  select 
    d.cartodb_id as original_id,
    to_timestamp(
      unnest(
        array [
            '16/03/2020', '17/03/2020', '18/03/2020', '19/03/2020'
          ]
      ),
      'DD/MM/YYYY'
    ) AS date,
    unnest(
      array [
        d._16_03_2020, d._17_03_2020, d._18_03_2020, d._19_03_2020
    ]
    ) AS value,
    d.ccaa,
    s.population,
    'Datadista' as source,
    'https://github.com/datadista/datasets/tree/master/COVID%2019' as source_url 
  from 
    altas d,
    spain_regions s
  where 
    d.ccaa = s.nom_ccaa
) 
select 
  *,
  (value / population) as value_density 
from 
  data
  