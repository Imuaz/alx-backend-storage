--  script that creates an index on the table k`names` and the first letter of `name`
-- Add a new column to store the first letter of the name
ALTER TABLE names
ADD COLUMN first_letter CHAR(1) GENERATED ALWAYS AS (LEFT(name, 1)) STORED;

CREATE INDEX idx_name_first ON names (first_letter);
