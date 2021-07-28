create table car (
    id bigserial not null primary key,
    make varchar(100) not null,
    model varchar(100) not null,
    price numeric(19, 2) not null
);

create table person (
    id bigserial not null primary key,
    first_name varchar(50) not null,
    last_name varchar(50) not null,
    gender varchar(7) not null,
    email varchar(100),
    date_of_birth date not null,
    country_of_birth varchar(50) not null,
    car_id bigint references car (id),
    unique(car_id),
    UNIQUE(email)
);

insert into person (first_name, last_name, gender, email, date_of_birth, country_of_birth) 
values ('Joshua', 'Henriques', 'Male', 'henriques.joshua@gmail.com', '1995-03-03', 'CA');
insert into person (first_name, last_name, gender, email, date_of_birth, country_of_birth) 
values ('Nica', 'Henriques', 'Female', 'henriques.nica@gmail.com', '1998-01-05', 'US');
insert into person (first_name, last_name, gender, email, date_of_birth, country_of_birth) 
values ('Adam', 'Ali', 'Male', 'ali.adam@gmail.com', '1995-02-19', 'CA');

insert into car (make, model, price) values ('Land Rover', 'Sterling', '87665.38');
insert into car (make, model, price) values ('Audi', 'A7', '27762.38');
insert into car (make, model, price) values ('Honda', 'Civic', '57263.38');