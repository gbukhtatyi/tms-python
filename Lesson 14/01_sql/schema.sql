DROP DATABASE IF EXISTS `lesson-14`;

CREATE DATABASE `lesson-14`;

USE `lesson-14`;

create table seller (
	id int unsigned primary key auto_increment,
	company varchar(255) not null,
	phone varchar(255) not null
);

create table products (
	id int unsigned primary key auto_increment,
	seller_id int unsigned not null,
	username varchar(255) not null,
	price int unsigned not null,
	`count` int unsigned default 0,

	foreign key (seller_id) references seller (id)
);

create table users (
	id int unsigned primary key auto_increment,
	username varchar(255) not null,
	password varchar(255) not null,
	email varchar(255) not null
);

create table orders (
	id int unsigned primary key auto_increment,
	user_id int unsigned not null,
	product_id int unsigned not null,
	`count` int unsigned not null,

	foreign key (user_id) references users (id),
	foreign key (product_id) references products (id)
);
