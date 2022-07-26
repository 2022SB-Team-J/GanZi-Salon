CREATE TABLE user (
    user_idx INT NOT NULL AUTO_INCREMENT,
    id VARCHAR(20) NOT NULL unique,
    pswd varchar(20) NOT NULL,
    gender varchar(1) default 'N',
    create_at datetime default now(),
    upload_at datetime default now(),
    is_active boolean default 0,
    PRIMARY KEY (user_idx)
);
