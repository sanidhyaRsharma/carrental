CREATE TABLE IF NOT EXISTS vehicle
(plate_num VARCHAR(10) NOT NULL PRIMARY KEY,
 make VARCHAR (20) NOT NULL,
 model VARCHAR (20) NOT NULL,
 built_year INT NOT NULL,
 color VARCHAR (20) NOT NULL,
 vehicle_class VARCHAR (20) NOT NULL,
 price_per_day NUMERIC(6,2) NOT NULL,
 is_active BOOLEAN NOT NULL
);

CREATE TYPE STATUS AS ENUM ('BOOKED', 'CANCELLED', 'IN PROGRESS', 'COMPLETED');
CREATE TABLE IF NOT EXISTS booking
(booking_id INT NOT NULL PRIMARY KEY,
 booking_date DATE NOT NULL DEFAULT CURRENT_DATE, 
 booking_status STATUS NOT NULL,
 start_time DATE NOT NULL,
 end_time DATE NOT NULL,
 final_cost NUMERIC(7,2) NOT NULL,
 user_id BIGINT NOT NULL,
 plate_num VARCHAR(10) NOT NULL,
 CONSTRAINT fk_user_id
    FOREIGN KEY(user_id) 
    REFERENCES users_newuser(id)
    ON DELETE CASCADE,
 CONSTRAINT fk_vehicle_num
    FOREIGN KEY(plate_num) 
    REFERENCES vehicle(plate_num)
    ON DELETE RESTRICT
);

CREATE TABLE IF NOT EXISTS payment_details
(user_id BIGINT NOT NULL,
 bank_name VARCHAR (20) NOT NULL,
 card_number VARCHAR(20),
 routing_number VARCHAR(9),
 account_number VARCHAR(20),
 card_expiry DATE,
 billing_address VARCHAR,
 account_name VARCHAR,
 CONSTRAINT fk_user_id
    FOREIGN KEY(user_id) 
    REFERENCES users_newuser(id)
    ON DELETE CASCADE
);