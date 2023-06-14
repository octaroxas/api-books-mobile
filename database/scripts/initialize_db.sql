CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    password TEXT NOT NULL,
    nickname TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS friends (
    id SERIAL PRIMARY KEY,
    user_id INT,
    friend_id INT,
    FOREIGN KEY (user_id) REFERENCES users,
    FOREIGN KEY (friend_id) REFERENCES users
);

CREATE TABLE IF NOT EXISTS books (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    pages INT NOT NULL,
    isbn TEXT DEFAULT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    favorited BOOL DEFAULT FALSE,
    user_id INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users
);

CREATE TABLE IF NOT EXISTS readRecords (
    id SERIAL PRIMARY KEY,
    start_page INT NOT NULL,
    end_page INT NOT NULL,
    description TEXT DEFAULT NULL,
    book_id INT,
    FOREIGN KEY (book_id) REFERENCES books
);

CREATE TABLE IF NOT EXISTS readRecordComments (
    id SERIAL PRIMARY KEY,
    comment TEXT NOT NULL,
    readRecordId INT,
    user_id INT,
    FOREIGN KEY (readRecordId) REFERENCES readRecords,
    FOREIGN KEY (user_id) REFERENCES users
);

CREATE TABLE IF NOT EXISTS collections (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS collectionBooks (
    id SERIAL NOT NULL,
    collectionId INT,
    book_id INT,
    FOREIGN KEY (collectionId) REFERENCES collections,
    FOREIGN KEY (book_id) REFERENCES books
);

CREATE TABLE IF NOT EXISTS categories (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS bookCategories (
    categoryId INT,
    bookId INT,
    FOREIGN KEY (categoryId) REFERENCES categories,
    FOREIGN KEY (bookId) REFERENCES books
);

CREATE TABLE IF NOT EXISTS friendRequests (
    id SERIAL PRIMARY KEY,
    srcUserId INT,
    destUserId INT,
    FOREIGN KEY (srcUserId) REFERENCES users,
    FOREIGN KEY (destUserId) REFERENCES users
);
