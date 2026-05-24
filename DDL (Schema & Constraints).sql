-- Create and select the database
DROP DATABASE IF EXISTS vehicle_rental_db;

CREATE DATABASE vehicle_rental_db
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

USE vehicle_rental_db;

-- ─── Customer ───────────────────────────────────────────
CREATE TABLE Customer (
    customer_id      INT            NOT NULL AUTO_INCREMENT,
    customer_name    VARCHAR(100)   NOT NULL,
    customer_contact VARCHAR(20)    NOT NULL,
    customer_license VARCHAR(50)    NOT NULL,
    customer_address VARCHAR(255)   NULL,
    registered_date  DATE           NOT NULL DEFAULT (CURDATE()),
    CONSTRAINT pk_customer   PRIMARY KEY (customer_id),
    CONSTRAINT uq_contact    UNIQUE (customer_contact),
    CONSTRAINT uq_license    UNIQUE (customer_license)
);


-- ─── Vehicle ────────────────────────────────────────────
CREATE TABLE Vehicle (
    vehicle_id      INT            NOT NULL AUTO_INCREMENT,
    vehicle_type    VARCHAR(50)    NOT NULL,
    vehicle_brand   VARCHAR(50)    NOT NULL,
    vehicle_model   VARCHAR(50)    NOT NULL,
    rental_rate     DECIMAL(10,2)  NOT NULL,
    vehicle_status  VARCHAR(20)    NOT NULL DEFAULT 'Available',
    current_mileage INT            NOT NULL DEFAULT 0,
    license_plate   VARCHAR(20)    NOT NULL,
    year            YEAR           NOT NULL,
    CONSTRAINT pk_vehicle       PRIMARY KEY (vehicle_id),
    CONSTRAINT uq_plate         UNIQUE (license_plate),
    CONSTRAINT chk_rate         CHECK (rental_rate > 0),
    CONSTRAINT chk_mileage      CHECK (current_mileage >= 0),
    CONSTRAINT chk_year         CHECK (year >= 1990),
    CONSTRAINT chk_status       CHECK (vehicle_status IN ('Available','Rented','Maintenance'))
);


-- ─── Mechanic ───────────────────────────────────────────
CREATE TABLE Mechanic (
    mechanic_id        INT          NOT NULL AUTO_INCREMENT,
    mechanic_name      VARCHAR(100) NOT NULL,
    mechanic_specialty VARCHAR(100) NOT NULL,
    CONSTRAINT pk_mechanic PRIMARY KEY (mechanic_id)
);


-- ─── Rental ─────────────────────────────────────────────
CREATE TABLE Rental (
    rental_id       INT  NOT NULL AUTO_INCREMENT,
    customer_id     INT  NOT NULL,
    vehicle_id      INT  NOT NULL,
    rental_date     DATE NOT NULL DEFAULT (CURDATE()),
    expected_return DATE NOT NULL,
    return_date     DATE NULL,
    CONSTRAINT pk_rental         PRIMARY KEY (rental_id),
    CONSTRAINT fk_rental_cust    FOREIGN KEY (customer_id)
        REFERENCES Customer(customer_id)
        ON DELETE RESTRICT ON UPDATE CASCADE,
    CONSTRAINT fk_rental_veh     FOREIGN KEY (vehicle_id)
        REFERENCES Vehicle(vehicle_id)
        ON DELETE RESTRICT ON UPDATE CASCADE,
    CONSTRAINT chk_exp_return    CHECK (expected_return >= rental_date),
    CONSTRAINT chk_ret_date      CHECK (return_date IS NULL OR return_date >= rental_date)
);


-- ─── Payment ────────────────────────────────────────────
CREATE TABLE Payment (
    payment_id     INT           NOT NULL AUTO_INCREMENT,
    rental_id      INT           NOT NULL,
    payment_amount DECIMAL(10,2) NOT NULL,
    payment_date   DATE          NOT NULL DEFAULT (CURDATE()),
    CONSTRAINT pk_payment       PRIMARY KEY (payment_id),
    CONSTRAINT fk_payment_rent  FOREIGN KEY (rental_id)
        REFERENCES Rental(rental_id)
        ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT chk_pay_amount   CHECK (payment_amount > 0)
);


-- ─── Maintenance ────────────────────────────────────────
CREATE TABLE Maintenance (
    maintenance_id   INT           NOT NULL AUTO_INCREMENT,
    vehicle_id       INT           NOT NULL,
    maintenance_date DATE          NOT NULL DEFAULT (CURDATE()),
    maintenance_type VARCHAR(100)  NOT NULL,
    maintenance_cost DECIMAL(10,2) NOT NULL,
    mechanic_id      INT           NULL DEFAULT NULL,
    next_service_due DATE          NULL,
    CONSTRAINT pk_maintenance    PRIMARY KEY (maintenance_id),
    CONSTRAINT fk_maint_veh      FOREIGN KEY (vehicle_id)
        REFERENCES Vehicle(vehicle_id)
        ON DELETE RESTRICT ON UPDATE CASCADE,
    CONSTRAINT fk_maint_mech     FOREIGN KEY (mechanic_id)
        REFERENCES Mechanic(mechanic_id)
        ON DELETE SET NULL ON UPDATE CASCADE,
    CONSTRAINT chk_maint_cost    CHECK (maintenance_cost >= 0)
);


-- ─── Indexes for common lookups ─────────────────────────
CREATE INDEX idx_rental_customer ON Rental(customer_id);
CREATE INDEX idx_rental_vehicle  ON Rental(vehicle_id);
CREATE INDEX idx_payment_rental  ON Payment(rental_id);
CREATE INDEX idx_maint_vehicle   ON Maintenance(vehicle_id);
