-- script that lists all bands with Glam rock as

SELECT band_name, COALESCE(split, 2022) - formed AS lifespan
     FROM metal_bands
     WHERE main_style LIKE '%Glam rock%'
     ORDER BY lifespan DESC;
