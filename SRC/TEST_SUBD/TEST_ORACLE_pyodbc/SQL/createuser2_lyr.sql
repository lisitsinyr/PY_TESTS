alter session set "_ORACLE_SCRIPT"=true;
CREATE USER lyr identified by lyr;
CREATE USER LYR IDENTIFIED BY lyr
DEFAULT TABLESPACE USERS QUOTA 100M ON USERS;

grant create session to lyr;
grant create table to lyr;
grant create procedure to lyr;
grant create trigger to lyr;
grant create view to lyr;
grant create sequence to lyr;

grant alter any table to lyr;
grant alter any procedure to lyr;
grant alter any trigger to lyr;
grant alter profile to lyr;

grant delete any table to lyr;
grant drop any table to lyr;
grant drop any procedure to lyr;
grant drop any trigger to lyr;
grant drop any view to lyr;

grant drop profile to lyr;
grant select on sys.v_$session to lyr;
grant select on sys.v_$sesstat to lyr;
grant select on sys.v_$statname to lyr;
grant SELECT ANY DICTIONARY to lyr;
