drop table if exists items;
create table items (
      id integer primary key autoincrement,
      name text not null
);
drop table if exists fridge_items;
create table fridge_items (
      item_id integer not null,
      count real not null
);
drop table if exists lists;
create table lists (
      id integer primary key autoincrement,
      name text not null,
      created_at date not null,
      finished_at date
);
drop table if exists list_items;
create table list_items (
      list_id integer not null,
      item_id integer not null,
      count integer not null
);
