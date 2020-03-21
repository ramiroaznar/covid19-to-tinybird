with data as (
  select 
    d.cartodb_id as original_id,
    to_timestamp(
      unnest(
        array [
          '04/03/2020', '05/03/2020', '06/03/2020', 
          '09/03/2020', '10/03/2020', '11/03/2020', 
          '12/03/2020', '13/03/2020', '16/03/2020',
          '17/03/2020', '18/03/2020', '19/03/2020',
          {string_date_range}
          ]
      ),
      'DD/MM/YYYY'
    ) AS date,
    unnest(
      array [
        d._04_03_2020, d._05_03_2020, d._06_03_2020,
        d._09_03_2020, d._10_03_2020, d._11_03_2020, 
        d._12_03_2020, d._13_03_2020, d._16_03_2020, 
        d._17_03_2020, d._18_03_2020, d._19_03_2020,
        {underscore_date_range}
        
    ]
    ) AS value,
    d.ccaa,
    s.population,
    'Datadista' as source,
    'https://github.com/datadista/datasets/tree/master/COVID%2019' as source_url 
  from 
    uci d,
    spain_regions s
  where 
    d.ccaa = s.nom_ccaa
) 
select 
  *,
  (value / population) as value_density 
from 
  data
  