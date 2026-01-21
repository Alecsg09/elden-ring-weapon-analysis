CREATE TABLE armas (
    nome TEXT,
    tipo TEXT,
    dano_base INTEGER,
    peso REAL,
    atributo_principal TEXT
);

INSERT INTO armas (nome, tipo, dano_base, peso, atributo_principal) VALUES
('Greatsword', 'Colossal Sword', 164, 23.0, 'Strength'),
('Claymore', 'Greatsword', 138, 9.0, 'Strength'),
('Uchigatana', 'Katana', 115, 5.5, 'Dexterity'),
('Longsword', 'Straight Sword', 110, 3.5, 'Strength'),
('Reduvia', 'Dagger', 79, 2.5, 'Dexterity');


SELECT * FROM armas;


SELECT 
    nome, 
    tipo, 
    (dano_base / peso) AS eficiencia
FROM armas
ORDER BY eficiencia DESC;


SELECT 
    atributo_principal,
    AVG(dano_base / peso) AS media_eficiencia
FROM armas
GROUP BY atributo_principal;