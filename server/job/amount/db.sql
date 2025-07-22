-- postgres

create user amtusr;
alter role amtusr with password 'AMTAMT';

create database amtdb encoding 'UTF8' owner amtusr;


-- amtusr
psql -h 127.0.0.1 -p 5432 -d amtdb -U amtusr

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
    aid    char(8)   primary key, -- システム上の主キー

    yymmdd date      not null, -- 使用日
    dnum   int       not null, -- 日毎の連番

    dord   int       not null, -- 日毎の表示順

    useful text      not null, -- 用途
    amount int       not null, -- 金額

    udate  TIMESTAMP default CURRENT_TIMESTAMP, -- 更新日時
    delflg boolean   not null default false     -- 削除フラグ
);
