-- use vegetables_and_fruit;
-- insert vegetables_and_fruit (fruit_name, fruit_type, color, caloric_content, fruit_description) values ('watermelon', 'fruit', 'green', 15, 'healthy and to more water');
-- #Exrecise 1
-- SELECT * FROM vegetables_and_fruit.vegetables_and_fruit where fruit_type = 'vegetable' and caloric_content < 120;
-- #Exrecise 2
-- SELECT * FROM vegetables_and_fruit.vegetables_and_fruit where caloric_content between 100 and 300 and fruit_type like 'fruit'
-- #Exrecise 3
-- SELECT * FROM vegetables_and_fruit.vegetables_and_fruit where fruit_type = 'fruit' and fruit_name like '%melon%';
-- #Exrecise 4
-- SELECT * FROM vegetables_and_fruit.vegetables_and_fruit where fruit_description like '%healthy%';
-- #Exrecise 5
-- SELECT * FROM vegetables_and_fruit.vegetables_and_fruit where color = 'red' || color = 'green'
-- SELECT * FROM vegetables_and_fruit.vegetables_and_fruit where color in('red','green')