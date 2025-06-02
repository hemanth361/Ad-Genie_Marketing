CREATE TABLE campaigns (
    id SERIAL PRIMARY KEY,
    title TEXT,
    scheduled_at TIMESTAMP,
    status TEXT
);