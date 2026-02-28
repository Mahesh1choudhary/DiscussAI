--- users table creation
CREATE TABLE users (
                       user_id SERIAL PRIMARY KEY,
                       user_name VARCHAR NOT NULL,
                       email VARCHAR NOT NULL UNIQUE,
                       created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
                       updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- indices
CREATE INDEX ix_users_user_id ON users (user_id);
CREATE INDEX ix_users_user_name ON users (user_name);



