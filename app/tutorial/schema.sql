create table if not exists search (
    id integer primary key autoincrement,
    date datetime  not null
    name char(100) not null
    some char(100) not null
);

insert or ignore into search (id, date, name, some) values (0, '1000-01-01 00:00:00', 'Start learning Pyramid', 'Something');
