
CREATE LOGIN bglcap
with Password = '48Gheq0Iz9t'

CREATE USER bglcap from login bglcap;

EXEC sp_addrolemember 'db_owner', 'bglcap'


CREATE TABLE iii
(
    Payout_Category NVARCHAR(100),
    amt_2016 int,
    amt_2017 int,
    amt_2018 int,
    amt_2019 int,
    amt_2020 int
)

CREATE TABLE rates
(
    gender NVARCHAR(20),
    age int,
    lowest float,
    low float,
    high float,
    highest float
)

CREATE TABLE life_insured
(
    year int,
    portion int
)

CREATE TABLE ownership_gap
(
    year int,
    portion int
)

CREATE TABLE why_insured
(
    reason NVARCHAR(100),
    year1 int,
    year2 int,
    change int
)


CREATE TABLE why_not_insured
(
    reason NVARCHAR(100),
    portion int
)

CREATE TABLE cdc_state
(
    year NVARCHAR(20),
    state_val NVARCHAR(20),
    expectancy float
)
