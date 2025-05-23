-- postgres

create user amtusr;
alter role amtusr with password 'AMTAMT';

create database amtdb encoding 'UTF8' owner amtusr;

-- amtusr
create table pln_rec (
    pid     char(8)   primary key,

    yymmdd  date      not null,
    dnum    int       not null,

    dord    int       not null,

    useful  text      not null,
    income  int       not null,
    expense int       not null,

    udate   TIMESTAMP default CURRENT_TIMESTAMP,
    delflg  boolean   not null default false
);

create table amt_rec (
    aid    char(8)   primary key,

    yymmdd date      not null,
    dnum   int       not null,

    dord   int       not null,

    useful text      not null,
    amount int       not null,

    udate  TIMESTAMP default CURRENT_TIMESTAMP,
    delflg boolean   not null default false
);
