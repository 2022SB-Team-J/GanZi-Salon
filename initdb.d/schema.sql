CREATE TABLE user (
    user_index INT NOT NULL AUTO_INCREMENT,
    id VARCHAR(20) NOT NULL unique,
    user_name varchar(20) NOT NULL,
    user_password varchar(20) NOT NULL,
    gender varchar(1) default 'N' NOT NULL,
    is_active boolean default 0,
    create_at datetime default now(),
    upload_at datetime default now(),
    PRIMARY KEY (user_index)
);
CREATE TABLE image (
    image_index INT NOT NULL AUTO_INCREMENT,
    user_index INT NOT NULL unique,
    image_url VARCHAR(200) NOT NULL,
    create_at datetime default now(),
    PRIMARY KEY (image_index),
    FOREIGN KEY (user_index) REFERENCES user (user_index)
);
