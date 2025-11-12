create database produtos_db;

use produtos_db;

create table produtos (
 id int auto_increment primary key,
 nome varchar(100),
 preco decimal(10,2),
 quantidade int
);
