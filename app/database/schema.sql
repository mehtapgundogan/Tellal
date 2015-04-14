drop table if exists Mails;
create table Mails(
  id integer primary key autoincrement,
  title text not null,
  mailText text not null	  	
);

drop table if exists Users;
create table Users(
  userID integer primary key autoincrement,
  mailAdress text not null,
  userStatus text not null
);
drop table if exists Issues;
create table Issues(
  issueID integer primary key autoincrement,
  issueName text not null
);
