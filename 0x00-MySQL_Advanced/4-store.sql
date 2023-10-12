-- script that creates a trigger that decreases
-- the quantity of an item after adding a new order.

CREATE TRIGGER update_item_quantity
BEFORE INSERT ON orders
FOR EACH ROW UPDATE items
SET quantity = quantity - NEW.quantity
WHERE items.id = NEW.item_id;
