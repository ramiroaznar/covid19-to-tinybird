select 
  original_id,
  date,
  value,
  ccaa,
  st_y(st_pointonsurface(the_geom)) as latitude,
  st_x(st_pointonsurface(the_geom)) as longitude,
  st_pointonsurface(the_geom) as the_geom,
  population,
  source,
  source_url,
  value_density 
from 
  unnested_{dataset}
