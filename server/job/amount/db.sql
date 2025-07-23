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
    aid    char(8)   primary key, -- 識別子

    yymmdd date      not null, -- 使用日
    dnum   int       not null, -- 日毎の連番

    dord   int       not null, -- 日毎の表示順

    useful text      not null, -- 用途
    cid    char(8)   not null, -- 支払い方法
    amount int       not null, -- 金額

    paydate date     not null, -- 支払い集計日

    udate  TIMESTAMP default CURRENT_TIMESTAMP, -- 更新日時
    delflg boolean   not null default false     -- 削除フラグ
);

create table card_rec (
    cid       char(8)   primary key, -- 識別子
    cname     text      not null,    -- 名称
    due       int       not null,    -- 締め日
    pay_month int       not null,    -- 支払い月
    pay_day   int       not null,    -- 支払い日
    udate     TIMESTAMP default CURRENT_TIMESTAMP
);
insert into card_rec
(cid, cname, due, pay_month, pay_day)
values
  ('C0000001', 'cache',   0, 0, 0)
, ('C0000002', 'PayPay', 29, 1, 27)
, ('C0000003', 'auPay',  15, 1, 10)
;

alter table amt_rec add constraint fk_cid
foreign key (cid) references card_rec(cid);





-- 集計用SQL


-- 種別毎の支払い日算出
with
tmp_tgt as (
    select
        '2025-07-15'::date as tgt,
        'C0000003' as cid
),
tmp_pay as (
	-- 支払い種別毎の支払日（今日、支出した場合の支払日）
	select
	  C.cid,           -- 識別子
	  C.cname,         -- 名称
	  case when C.due = 0
	       then D.tgt
	       when extract(day from D.tgt)::int <= C.due
	       then make_date( extract( year from D.tgt + (C.pay_month || ' month')::interval)::int,
	                       extract(month from D.tgt + (C.pay_month || ' month')::interval)::int,
	                       C.pay_day )
	       else make_date( extract( year from D.tgt + ((C.pay_month + 1) || ' month')::interval)::int,
	                       extract(month from D.tgt + ((C.pay_month + 1) || ' month')::interval)::int,
	                       C.pay_day )
	  end as pay_date  -- 支払日
	from card_rec as C, tmp_tgt as D
)

select * from tmp_pay, tmp_tgt where tmp_pay.cid = tmp_tgt.cid



-- 当日基準での集計対象期間算出
with tmp_pay as (
	-- 支払い種別毎の支払日（今日、支出した場合の支払日）
	select
	  C.cid,           -- 識別子
	  C.cname,         -- 名称
	  case when C.due = 0
	       then make_date( extract(year from now())::int,
	                       extract(month from now())::int,
	                       extract(day from now())::int )
	       when extract(day from now())::int <= C.due
	       then make_date( extract( year from now() + (C.pay_month || ' month')::interval)::int,
	                       extract(month from now() + (C.pay_month || ' month')::interval)::int,
	                       C.pay_day )
	       else make_date( extract( year from now() + ((C.pay_month + 1) || ' month')::interval)::int,
	                       extract(month from now() + ((C.pay_month + 1) || ' month')::interval)::int,
	                       C.pay_day )
	  end as pay_date  -- 支払日
	from card_rec as C
),

tmp_calc_limit as (
    -- 一番未来の支払日基準で集計対象限界を取得
	select
	  case when extract(day from max(pay_date)) <= 22
	       then make_date( extract( year from max(pay_date))::int,
	                       extract(month from max(pay_date))::int,
	                       22 )
	       else make_date( extract( year from max(pay_date) + interval '1 month')::int,
	                       extract(month from max(pay_date) + interval '1 month')::int,
	                       22 )
	  end as to_date
	from tmp_pay
),

tmp_list as (
    -- リスト作成用の連番
	select -1 as n
	union
	select 0 as n
	union
	select 1 as n
	union
	select 2 as n
	union
	select 3 as n
),
tmp_between_list as (
    -- 集計対象候補
	select make_date( extract( year from now() + (N.n || ' month')::interval)::int,
	                  extract(month from now() + (N.n || ' month')::interval)::int,
	                  23 ) as st,
	       make_date( extract( year from now() + ((N.n + 1) || ' month')::interval)::int,
	                  extract(month from now() + ((N.n + 1) || ' month')::interval)::int,
	                  22 ) as ed
	from tmp_list as N
)

select
  BTW.st,  -- 集計開始日
  BTW.ed   -- 集計終了日
from tmp_between_list as BTW, tmp_calc_limit as CLC
where now() <= BTW.ed
  and BTW.st <= CLC.to_date
order by BTW.st
