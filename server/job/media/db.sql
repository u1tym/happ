-- postgres

create user mdausr;
alter role mdausr with password 'MEDIAMEDIA';

create database mdadb encoding 'UTF8' owner mdausr;

-- mdausr
create table person (
    pid      char(8)  primary key,
    pname    text     not null
);

create table media (
    mid      char(8)  primary key,
    mname    text     not null
);

insert into person ( pid, pname )
values
 ('P0000001', '悠木碧')
,('P0000002', '田村ゆかり')
;

insert into media ( mid, mname )
values
 ('M0000001', 'CD')
,('M0000002', 'DVD')
,('M0000003', 'BD')
;

create table mda_rec (
    rid     char(8)   primary key,

    pid     char(8)   not null,
    mid     char(8)   not null,

    title   text      not null,

    release date      not null,
    own     boolean   not null default false,

    udate   TIMESTAMP default CURRENT_TIMESTAMP,
    delflg  boolean   not null default false,

    foreign key (pid) references person(pid)
        on delete no action
        on update cascade,
    foreign key (mid) references media(mid)
        on delete no action
        on update cascade
);
