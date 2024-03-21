drop database if exists rentalDB;
create database rentalDB;

CREATE TABLE Rental_Room
(
    PID VARCHAR (16) NOT NULL,
    RentalGroupID VARCHAR (16) NOT NULL,
    OwnerID VARCHAR (16) NOT NULL,
    ManagerID VARCHAR (16) NOT NULL,
    Accessibility VARCHAR (16) NOT NULL,
    Laundry_Type VARCHAR(32) NOT NULL,
    Cost_Per_Month INT NOT NULL,
    PARKING BOOLEAN NOT NULL,
    Num_Bathrooms INT NOT NULL,
    Num_Bedrooms INT NOT NULL,
    Province VARCHAR (2) NOT NULL,
    Street VARCHAR (32) NOT NULL,
    City VARCHAR (32) NOT NULL,
    Postal_Code VARCHAR (32) NOT NULL,
    Date_Of_Listing DATE,
    Num_Residents INT NOT NULL,
    Kitchen_Privs BOOLEAN NOT NULL,
    PRIMARY KEY (PID)
    FOREIGN KEY (RentalGroupID) REFERENCES Rental_Group(GroupCode),
    FOREIGN KEY (OwnerID) REFERENCES Owns(PhoneNum),
    FOREIGN KEY (ManagerID) REFERENCES Manages(PhoneNum),
    
);

CREATE TABLE Rental_Apartment
(
    PID VARCHAR (16) NOT NULL,
    RentalGroupID VARCHAR (16) NOT NULL,
    OwnerID VARCHAR (16) NOT NULL,
    ManagerID VARCHAR (16) NOT NULL,
    Accessibility BOOLEAN NOT NULL,
    Laundry_Type VARCHAR(32) NOT NULL,
    Cost_Per_Month INT NOT NULL,
    PARKING BOOLEAN NOT NULL,
    Num_Bathrooms INT NOT NULL,
    Num_Bedrooms INT NOT NULL,
    Province VARCHAR (2) NOT NULL,
    Street VARCHAR (32) NOT NULL,
    City VARCHAR (32) NOT NULL,
    Postal_Code VARCHAR (32) NOT NULL,
    Date_Of_Listing DATE,
    Elevator BOOLEAN NOT NULL,
    Floor_Num TINYINT NOT NULL,
    Apt_Num VARCHAR (16) NOT NULL,
    PRIMARY KEY (PID)
    FOREIGN KEY (RentalGroupID) REFERENCES Rental_Group(GroupCode),
    FOREIGN KEY (OwnerID) REFERENCES Owns(PhoneNum),
    FOREIGN KEY (ManagerID) REFERENCES Manages(PhoneNum),
    
);

CREATE TABLE Rental_House
(
    PID VARCHAR (16) NOT NULL,
    RentalGroupID VARCHAR (16) NOT NULL,
    OwnerID VARCHAR (16) NOT NULL,
    ManagerID VARCHAR (16) NOT NULL,
    Accessibility BOOLEAN NOT NULL,
    Laundry_Type VARCHAR(32) NOT NULL,
    Cost_Per_Month INT NOT NULL,
    PARKING BOOLEAN NOT NULL,
    Num_Bathrooms INT NOT NULL,
    Num_Bedrooms INT NOT NULL,
    Province VARCHAR (2) NOT NULL,
    Street VARCHAR (32) NOT NULL,
    City VARCHAR (32) NOT NULL,
    Postal_Code VARCHAR (32) NOT NULL,
    Date_Of_Listing DATE,
    Fenced BOOLEAN NOT NULL,
    Attachment_Type VARCHAR (32) NOT NULL,
    PRIMARY KEY (PID)
    FOREIGN KEY (RentalGroupID) REFERENCES Rental_Group(GroupCode),
    FOREIGN KEY (OwnerID) REFERENCES Owns(PhoneNum),
    FOREIGN KEY (ManagerID) REFERENCES Manages(PhoneNum),
    
);

CREATE TABLE Room_Furnishing
(
    RoomID INT NOT NULL,
    Furniture VARCHAR(256) NOT NULL,
    PRIMARY KEY (RoomID, Furniture),
    FOREIGN KEY (RoomID) REFERENCES Rental_Room(PID) ON DELETE CASCADE
);

CREATE TABLE Renter
(
    ID VARCHAR (5) NOT NULL,
    GroupCode VARCHAR (4) NOT NULL,
    Fname VARCHAR (32) NOT NULL,
    Lname VARCHAR (32) NOT NULL,
    PhoneNum VARCHAR (16) NOT NULL,
    StudentID VARCHAR (8) NOT NULL,
    ExpectedGrad DATE,
    ProgramOfStudy VARCHAR (32) NULL,
    PRIMARY KEY (ID)
    FOREIGN KEY (GroupCode) REFERENCES Rental_Group(GroupCode)
);

CREATE TABLE Manager
(
    ID VARCHAR (5) NOT NULL,
    PhoneNum VARCHAR (16) NOT NULL,
    Fname VARCHAR (32) NOT NULL,
    Lname VARCHAR (32) NOT NULL,
    PRIMARY KEY (ID,PhoneNum),
);

CREATE TABLE PropertyOwner
(
    ID VARCHAR (5) NOT NULL,
    PhoneNum VARCHAR (16) NOT NULL,
    Fname VARCHAR (32) NOT NULL,
    Lname VARCHAR (32) NOT NULL,
    PRIMARY KEY (ID,PhoneNum),
);

CREATE TABLE Rental_Group
(
    GroupCode VARCHAR (4) NOT NULL,
    Accommodation VARCHAR (16) NULL,
    Num_Bedrooms INT NULL,
    Num_Bathrooms INT NULL,
    Parking BOOLEAN NULL,
    Laundry VARCHAR (32) NULL,
    MaxPay INT NULL,
    Accessibility VARCHAR (16) NULL,
    PRIMARY KEY (GroupCode)
);

CREATE TABLE Rents
(   
    GroupCode VARCHAR (4) NOT NULL,
    PropertyID VARCHAR (16) NOT NULL,
    MonthlyRent INT NOT NULL,
    LeaseSignDate DATE NOT NULL,
    FOREIGN KEY (GroupCode) REFERENCES Rental_Group(GroupCode) ON DELETE CASCADE
);

CREATE TABLE Manages
(
    PhoneNum VARCHAR (16) NOT NULL,
    StartDate DATE,
    PRIMARY KEY (PhoneNum)
    FOREIGN KEY (PhoneNum) REFERENCES Manager(PhoneNum)  ON DELETE CASCADE
);

CREATE TABLE Owns
(
    PhoneNum VARCHAR (16) NOT NULL,
    PRIMARY KEY (PhoneNum)
    FOREIGN KEY (PhoneNum) REFERENCES PropertyOwner(PhoneNum)  ON DELETE CASCADE
);