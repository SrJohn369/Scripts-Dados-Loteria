CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(50) UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS quina (
    concurso    PRIMARY KEY,
    data        DATE,
    bola1       SMALLINT,
    bola2       SMALLINT,
    bola3       SMALLINT,
    bola4       SMALLINT,
    bola5       SMALLINT
);