-- script that lists all bands with Glam rock as
-- their main style, ranked by their longevity

WITH longevity AS (
  SELECT band_name, split - formed AS lifespan
  FROM metal_bands
  WHERE main_style = 'Glam rock'
)
SELECT band_name, lifespan
FROM longevity
ORDER BY lifespan DESC;
