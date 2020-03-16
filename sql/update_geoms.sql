update unnested_{dataset} d 
set the_geom = s.the_geom 
from spain_regions s 
where s.nom_ccaa = d.ccaa 