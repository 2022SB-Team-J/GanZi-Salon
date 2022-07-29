CREATE TABLE user (
    user_idx INT NOT NULL AUTO_INCREMENT,
    id VARCHAR(20) NOT NULL unique,
    pswd varchar(20) NOT NULL,
    gender varchar(1) default 'N' NOT NULL,
    create_at datetime default now(),
    upload_at datetime default now(),
    is_active boolean default 0,
    PRIMARY KEY (user_idx)
);

CREATE TABLE image (
    img_idx INT NOT NULL AUTO_INCREMENT,
    user_idx VARCHAR(20) NOT NULL unique,
    img_url VARCHAR(200) NOT NULL,
    create_at datetime default now(),
    PRIMARY KEY (img_idx),
    FOREIGN KEY (user_idx) REFERENCES `user` (`user_idx`)
);
