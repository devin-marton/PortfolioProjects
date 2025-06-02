import mysql.connector

# Connect to mysql and create the database and then close the connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
)

cursor = db.cursor()

cursor.execute("""DROP DATABASE IF EXISTS Holiday_Gifts_Python;
               CREATE DATABASE IF NOT EXISTS Holiday_Gifts_Python;""")
db.close()

# Reconnect to MySQL, this time connecting the database that was just created and add tables and data
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="Holiday_Gifts_Python"
)

cursor = db.cursor()
cursor.execute("""

DROP TABLE IF EXISTS recipients CASCADE;
CREATE TABLE IF NOT EXISTS recipients 
    (id INT NOT NULL AUTO_INCREMENT,
    recipient_name VARCHAR(50),
    relationship INT,
    age_range INT,
    PRIMARY KEY (id),
    FOREIGN KEY (relationship) REFERENCES relationships (relationship));
        INSERT INTO recipients (recipient_name, relationship, age_range)
            VALUES 
                ('Katrina',1,1),
                ('Katrina from kids',1,1),
                ('Perry',1,1),
                ('Perry from kids',1,1),
                ('Thomas',1,2),
                ('Chloe',1,2),
                ('Janel',2,1),
                ('Alan',2,1),
                ('Jim',3,1),
                ('Ros',3,1),
                ('Angela',3,1),
                ('Rob',3,1),
                ('Annabel',3,3),
                ('Fay',3,1),
                ('Steve',3,1),
                ('Sasha',3,2),
                ('Philip',2,1),
                ('Mimi',2,1),
                ('Trixy',2,3),
                ('Olivia',4,4),
                ('Sienna',4,2),
                ('Kiera',4,2),
                ('Millie',4,2),
                ('Megan',4,2);
              
DROP TABLE IF EXISTS age_range CASCADE;
CREATE TABLE IF NOT EXISTS age_range 
    (id INT NOT NULL AUTO_INCREMENT,
    age_range VARCHAR(50),
    PRIMARY KEY (id));
        INSERT INTO age_range (age_range)
            VALUES 
                ('Adult'),
                ('Toddler'),
                ('Baby'),
                ('Child');
                
DROP TABLE IF EXISTS relationships CASCADE;
CREATE TABLE IF NOT EXISTS relationships 
    (id INT NOT NULL AUTO_INCREMENT,
    relationship VARCHAR(50),
    PRIMARY KEY (id));
        INSERT INTO relationships (relationship)
            VALUES 
                ('our family'),
                ('Sara side'),
                ('my side'),
                ('Friends');
                
                
DROP TABLE IF EXISTS budget_amount CASCADE;
CREATE TABLE IF NOT EXISTS budget_amount 
    (id INT NOT NULL AUTO_INCREMENT,
    amount VARCHAR(50),
    PRIMARY KEY (id));
        INSERT INTO budget_amount (amount)
            VALUES 
                ('$10.00'),
                ('$15.00'),
                ('$20.00'),
                ('$30.00'),
                ('$40.00');

DROP TABLE IF EXISTS money CASCADE;
CREATE TABLE IF NOT EXISTS money 
    (id INT NOT NULL AUTO_INCREMENT,
    recipient_id INT,
    budget_id INT,
    amount_spent VARCHAR(50),
    PRIMARY KEY (id),
    FOREIGN KEY (recipient_id) REFERENCES recipients (id),
    FOREIGN KEY (budget_id) REFERENCES budget_amount (id));
        INSERT INTO money (recipient_id, budget_id, amount_spent)
            VALUES 
                (1,4,'$0.00'),
                (2,1,'$0.00'),
                (3,4,'$0.00'),
                (4,1,'$0.00'),
                (5,5,'$10.00'),
                (6,5,'$31.00'),
                (7,3,'$28.00'),
                (8,3,'$30.00'),
                (9,3,'$13.00'),
                (10,3,'$1.00'),
                (11,3,'$0.00'),
                (12,3,'$0.00'),
                (13,2,'$12.00'),
                (14,3,'$25.00'),
                (15,2,'$0.00'),
                (16,2,'$13.75'),
                (17,3,'$0.00'),
                (18,2,'$10.00'),
                (19,2,'$12.00'),
                (20,1,'$6.50'),
                (21,1,'$6.50'),
                (22,1,'$6.50'),
                (23,1,'$6.75'),
                (24,1,'$8.00');

DROP TABLE IF EXISTS gifts CASCADE;
CREATE TABLE IF NOT EXISTS gifts 
    (id INT NOT NULL AUTO_INCREMENT,
    gift_name VARCHAR(50),
    bought VARCHAR(50),
    url VARCHAR(100),
    PRIMARY KEY (id));
        INSERT INTO gifts (gift_name, bought, url)
            VALUES 
                ('Billie train','Yes', 'billietrain.com'),
                ('Sunshine Chair','Yes','amazon.com/sunshinechair'),
                ('Electronic photo frame','Yes','bestbuy.com/photoframe'),
                ('Magazine subsciption', 'Yes', 'totalmagazines.com'),
                ('Backgamon', 'Yes','amazon.com/backgamon'),
                ('After shaves','Yes', 'target.com/aftershave'),
                ('Travel Hair Dryer', 'Yes','won with raffle ticket'),
                ('Shirts', 'No', 'target.com/shirts'),
                ('Gift Vouchers', 'No', 'amazon.com'),
                ('Buncing Tiger', 'Yes', 'amazon.com/bouncingtiger'),
                ('Painting', 'Yes', 'mypaint.com'),
                ('Gadgets', 'No', 'amazon.com/gadets'),
                ('DVD', 'Yes', 'blockbuster.com'),
                ('Game', 'Yes', 'games.com'),
                ('Make Up', 'Yes', 'sophora.com'),
                ('Books', 'Yes', 'barnesandnoble.com'),
                ('Tea Set', 'Yes', 'amazon.com/teaset');
                
DROP TABLE IF EXISTS gift_ideas CASCADE;
CREATE TABLE IF NOT EXISTS gift_ideas 
    (id INT NOT NULL AUTO_INCREMENT,
    recipient_id INT,
    gift_idea_1 INT,
    gift_idea_2 INT,
    PRIMARY KEY (id),
    FOREIGN KEY (recipient_id) REFERENCES recipients (id),
    FOREIGN KEY (gift_idea_1) REFERENCES gifts (id),
    FOREIGN KEY (gift_idea_2) REFERENCES gifts (id));
        INSERT INTO gift_ideas (recipient_id,gift_idea_1,gift_idea_2)
            VALUES 
                (1,0,0),
                (2,0,0),
                (3,0,0),
                (4,0,0),
                (5,1,0),
                (6,2,0),
                (7,3,0),
                (8,4,0),
                (9,5,6),
                (10,7,0),
                (11,0,0),
                (12,8,9),
                (13,10,0),
                (14,11,0),
                (15,12,0),
                (16,13,14),
                (17,0,0),
                (18,15,0),
                (19,10,0),
                (20,16,0),
                (21,16,0),
                (22,16,0),
                (23,13,0),
                (24,16,17);     
                
#Views and Queries

CREATE VIEW gift_summary AS
SELECT 
    r.recipient_name AS Recipient,
    TRIM(
        CONCAT(
            COALESCE(g1.gift_name, ''),
            CASE 
                WHEN g2.gift_name IS NOT NULL THEN CONCAT(', ', g2.gift_name) 
                ELSE '' 
            END
        )
    ) AS Gift_Ideas,
    rel.relationship AS "Friend/Family",
    ar.age_range AS "Age Range",
    ba.amount AS Budget,
    m.amount_spent AS Actual
FROM 
    recipients r
LEFT JOIN relationships rel ON r.relationship = rel.id
LEFT JOIN age_range ar ON r.age_range = ar.id
LEFT JOIN money m ON r.id = m.recipient_id
LEFT JOIN budget_amount ba ON m.budget_id = ba.id
LEFT JOIN gift_ideas gi ON r.id = gi.recipient_id
LEFT JOIN gifts g1 ON gi.gift_idea_1 = g1.id
LEFT JOIN gifts g2 ON gi.gift_idea_2 = g2.id;

CREATE VIEW query1 AS
SELECT 
    recipients.recipient_name, 
    relationships.relationship, 
    age_range.age_range
FROM 
    recipients
JOIN 
    relationships ON recipients.relationship = relationships.id
JOIN 
    age_range ON recipients.age_range = age_range.id;

CREATE VIEW query2 AS
SELECT 
    recipients.recipient_name, 
    gifts.gift_name AS gift_idea,
    gifts.bought AS is_bought,
    gifts.url
FROM 
    gift_ideas
JOIN 
    recipients ON gift_ideas.recipient_id = recipients.id
LEFT JOIN 
    gifts ON gift_ideas.gift_idea_1 = gifts.id OR gift_ideas.gift_idea_2 = gifts.id
WHERE 
    gifts.id IS NOT NULL;

CREATE VIEW query3 AS
SELECT 
    recipients.recipient_name, 
    budget_amount.amount AS budget, 
    money.amount_spent
FROM 
    money
JOIN 
    recipients ON money.recipient_id = recipients.id
JOIN 
    budget_amount ON money.budget_id = budget_amount.id;

""")
db.close()


