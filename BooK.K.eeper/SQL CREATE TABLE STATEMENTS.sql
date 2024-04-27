DROP TABLE Checked_Out;
DROP TABLE Students;
DROP TABLE Copies;
DROP TABLE Books;

CREATE TABLE Books(
    ISBN CHAR(13) PRIMARY KEY,
    title VARCHAR(200),
    authors VARCHAR(200),
	summary VARCHAR(2000)
);

CREATE TABLE Copies(
    ISBN CHAR(13) REFERENCES Books ON DELETE CASCADE,
    copyNum INT,
    condition VARCHAR(10),
    PRIMARY KEY(ISBN, copyNum)
);

CREATE TABLE Students(
    sID CHAR(8) PRIMARY KEY,
    sName VARCHAR(50)
);

CREATE TABLE Checked_Out(
    sID CHAR(8) REFERENCES Students,
    ISBN CHAR(13) REFERENCES Books,
	dateCheckedOut DATE,
    PRIMARY KEY(sID, ISBN)
);
