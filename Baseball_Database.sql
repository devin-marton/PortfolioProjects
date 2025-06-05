CREATE DATABASE IF NOT EXISTS Minot_Pitchers;
USE Minot_Pitchers;

-- Table to store Minot pitchers
DROP TABLE IF EXISTS Pitchers CASCADE;
CREATE TABLE Pitchers (
    pitcher_id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    handedness ENUM('L', 'R') NOT NULL, -- Left or Right handed
    freshman_year YEAR NOT NULL
);

-- Table to store stat history of pitchers
DROP TABLE IF EXISTS Stats CASCADE;
CREATE TABLE Stats (
    stat_id INT AUTO_INCREMENT PRIMARY KEY  NOT NULL,
    pitcher_id INT NOT NULL,
    season YEAR NOT NULL,
    school VARCHAR(50),
	WAR FLOAT,
    FIP FLOAT,
    IP FLOAT,
    KBB FLOAT,
    ERA FLOAT,
    W FLOAT,
    WHIP FLOAT,
    K9 FLOAT
);

-- Sample data for pitchers
INSERT INTO Pitchers (first_name, last_name, handedness, freshman_year) VALUES
('Hayden', 'Bode', 'R', 2022),
('Griffin', 'Shearon', 'R', 2021),
('Ian', 'Bauer', 'L', 2023),
('Connor', 'Meldrim', 'R', 2024),
('Gage', 'Eastlick', 'R', 2022),
('Anthony', 'Disantis', 'R', 2023),
('Ayden', 'Sauerbrei', 'R', 2024),
('Bryson', 'Reif', 'L', 2022),
('Colton', 'Bagshaw', 'R', 2023),
('Connor', 'Hill', 'L', 2022),
('Joshua', 'Czyz', 'R', 2023),
('Jack', 'Bright', 'L', 2023),
('Jacob', 'Thompson', 'R', 2024),
('Nolan', 'Craddock', 'L', 2022),
('Noah', 'Balandran', 'R', 2020),
('Alex', 'Engel', 'R', 2024),
('Anthony','Chatwood','R',2023),
('Devin','Marton','R',2020),
('Seth','Dietz','R',2023);

-- data for sats
INSERT INTO Stats (pitcher_id, season, school, WAR, FIP, IP, KBB, ERA, W, WHIP, K9) VALUES
(1, 2022, 'Butte College',-0.45,8.36 , 8.1, 0.9, 5.4, 0, 2.40, 9.72),
(1, 2023, 'Butte College',0.08, 2.64,18.2, 0.9, 0.96, 1, 0.96, 8.68),
(1, 2024, 'Minot State',-1.46, 8.4,5.1, 3, 15.19, 0, 2.54, 10.59),
(2, 2021, 'Minot State',-0.97,9.2 ,2.2, 0.57, 10.12, 0, 7.27, 16.36),
(2, 2023, 'Minot State',-1.09,7.35 ,4.2, 1.17, 11.57, 0, 2.38, 15),
(3, 2023, 'Centralia College',-3.79,3.99 ,69, 2.22, 3.91, 4, 1.26, 7.83),
(3, 2024, 'Shasta College',-4.23, 4.66,68.2, 1.26, 7.08, 2, 2.04, 6.42),
(4, 2024, 'Minot State',-0.86 ,3.9 ,5, 2, 9, 0, 2.4, 10.8),
(5, 2022, 'Sacramento City College',-1.05 , 2.98,22.1, 6.33, 2.42, 1, 1.12, 7.66),
(5, 2023, 'Sacramento City College',-0.03 ,3.56 ,46.2, 2.67, 3.47, 2, 1.26, 6.17),
(5, 2024, 'Minot State',-1.60,4.52 ,9, 2, 7, 0, 1.89, 10),
(6, 2023, 'Cosumnes River College',-71.46 , 10.00,11.2, 0.53, 15.43, 0, 2.57, 6.17),
(6, 2024, 'Cosumnes River College',2.15,4.86 ,66, 1.78, 4.09, 4, 1.61, 7.77),
(7, 2024, 'Minot State',-0.82 ,2.8 ,12.0, 3.0, 9.75, 1, 2.25, 13.5),
(8, 2022, 'Butte College',-0.80 ,3.63 ,9.2, 1.88, 9.31, 1, 2.38, 13.97),
(8, 2023, 'Butte College', 5.23, 3.03,48.1, 3.18, 2.98, 6, 1.12, 10.06),
(9, 2023, 'Minot State',-0.30 ,17.35 ,4.2, 0.71, 13.50, 1, 3.09, 10.71),
(9, 2023, 'Minot State', -0.27,4.21 ,12.1, 1.22, 3.65, 0, 1.65, 8.18),
(10, 2022, 'Point Loma', 0.49,4.59 ,10.1, 1.00, 6.10, 1, 1.49, 8.91),
(10, 2023, 'Point Loma', -1.88,8.9 ,5.0, 1.00, 9.00, 0, 2.00, 3.6),
(10, 2024, 'Point Loma', 0.00, 2.47,1.2, 2.00, 0.00, 0, 1.67, 15.00),
(11, 2023, 'Cosumnes River College', -0.22,7.53 ,20.1, 0.68, 3.54, 0, 2.11, 5.75),
(11, 2024, 'Cosumnes River College', -2.45,6.55 ,27.1, 1.05, 6.59, 0, 1.68, 6.91),
(12, 2023, 'Minot State', 0.01,73.3 ,0.1, 0.33, 0.00, 0, 30.00, 90.00),
(12, 2024, 'Minot State', -1.17, 10.3,8.0, 1.00, 12.38, 0, 2.50, 9.00),
(13, 2024, 'Minot State', -0.42,4.05 ,4.0, 1.50, 4.50, 0, 1.50, 6.75),
(14, 2022, 'Santa Barbara City College', -1.16, 2.15,5.2, 2.00, 12.71, 0, 2.82, 19.06),
(14, 2024, 'Cosumnes River College', -0.62,5.15 ,21.1, 1.08, 7.59, 0, 1.78, 5.91),
(15, 2020, 'Moorpark College', 1.89,3.00 ,37.0, 3.11, 3.89, 3, 1.24, 6.81),
(15, 2021, 'Moorpark College', 1.84,3.55 ,40.1, 2.42, 4.46, 4, 1.30, 6.47),
(15, 2022, 'Moorpark College', -0.06,3.79 ,80.0, 1.89, 4.16, 5, 1.31, 4.05),
(15, 2023, 'Minot State', -2.46,7.69 ,8.2,3.00, 5.19, 0, 1.34, 6.59),
(15, 2024, 'Minot State', -0.61,4.91 ,8.1, 1.25, 6.48, 0, 1.85, 5.56),
(16, 2024, 'Minot State', -4.03,19.66 ,1.1, 2.00, 40.50, 0, 6.36, 16.36),
(17, 2023, 'Colby Community College' ,-4.83,7.36, 25.1, 0.84, 10.30, 0, 2.21, 7.46),
(17, 2024, 'Colby Community College' ,-3.83,7.3, 25.0, 0.86, 10.08, 0, 2.12, 6.84),
(18, 2020, 'Sierra College', 0.10,3.06 ,8.2, 2.5, 0.00, 0, 0.92, 10.38),
(18, 2021, 'Sierra College', -0.35,6.57 ,5.2, 0.89, 14.29, 1, 3.08, 12.71),
(18, 2022, 'Sierra College', 2.00,3.24 ,50.1, 2.63, 5.01, 4, 1.45, 8.94),
(18, 2024, 'Minot State', -2.07,9.73 ,4.2, 0.71, 21.21, 0, 4.29, 10.71),
(19, 2023, 'Williston State College',-0.31,6.08, 7.2, 1.67, 14.09, 1, 2.74, 11.74),
(19, 2024, 'Williston State College' ,-1.68,3.4, 10.1, 1.90, 8.71, 0, 2.03, 16.55);

CREATE OR REPLACE VIEW Pitchers_Stats
AS
SELECT
p.first_name AS 'First Name',
p.last_name AS 'Last Name',
p.handedness AS 'Handedness',
p.freshman_year AS 'Freshman Year',
s.season AS 'Season', 
s.school AS 'School', 
s.WAR,
s.FIP,
s.IP, 
s.KBB, 
s.ERA, 
s.W, 
s.WHIP, 
s.K9
FROM pitchers p
JOIN Stats s ON s.pitcher_id=p.pitcher_id;
