-- sqlite3 db.sqlite < blog-schema.sql
drop table if exists country;
create table country (
  id integer primary key autoincrement,
  name text not null
);

drop table if exists post;
create table post (
  id integer primary key autoincrement,
  title text not null,
  body text not null,
  pub_date text
);

