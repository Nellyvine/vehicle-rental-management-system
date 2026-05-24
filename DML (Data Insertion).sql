-- ─── Customers ──────────────────────────────────────────
INSERT INTO Customer (customer_name, customer_contact, customer_license, customer_address, registered_date) VALUES
    ('Brian Otieno',       '+254712345678', 'KNB-2023-001', 'Nairobi, Kenya',      '2023-03-12'),
    ('Nellyvine Mizero',   '+2305912345',   'MU-2022-0441', 'Quatre Bornes, MU',   '2023-05-20'),
    ('Amara Diallo',       '+221771234567', 'SN-2021-7823', 'Dakar, Senegal',       '2023-06-18'),
    ('Fatuma Wanjiku',     '+255789012345', 'TZ-2020-3341', 'Dar es Salaam, TZ',   '2023-08-04'),
    ('Jean-Pierre Habimana','+250788123456','RW-2023-5590', 'Kigali, Rwanda',       '2024-01-09');


-- ─── Vehicles ───────────────────────────────────────────
INSERT INTO Vehicle (vehicle_type, vehicle_brand, vehicle_model, rental_rate, vehicle_status, current_mileage, license_plate, year) VALUES
    ('SUV',   'Toyota',  'Land Cruiser', 8500.00, 'Available',    34200, 'KBZ 123A', 2019),
    ('Sedan', 'Honda',   'Civic',        4500.00, 'Rented',       21100, 'MU-A 4421', 2021),
    ('Truck', 'Isuzu',   'D-Max',        6000.00, 'Maintenance',  58700, 'TZ-DM-007', 2018),
    ('SUV',   'Nissan',  'X-Trail',      7000.00, 'Available',    12300, 'RW-NX-991', 2022),
    ('Sedan', 'Mazda',   'CX-5',         5500.00, 'Available',     8900, 'KBZ 778B', 2023);


-- ─── Mechanics ──────────────────────────────────────────
INSERT INTO Mechanic (mechanic_name, mechanic_specialty) VALUES
    ('James Kamau',    'Engine & Transmission'),
    ('Patrick Nzinga', 'Electrical Systems'),
    ('Sylvie Umubyeyi','Brakes & Suspension'),
    ('Mohamed Issa',   'Air Conditioning'),
    ('Grace Odhiambo', 'Body & Paint');


-- ─── Rentals ────────────────────────────────────────────
INSERT INTO Rental (customer_id, vehicle_id, rental_date, expected_return, return_date) VALUES
    (1, 2, '2024-01-10', '2024-01-15', '2024-01-15'),
    (2, 1, '2024-02-01', '2024-02-07', '2024-02-08'),
    (3, 4, '2024-03-05', '2024-03-10', '2024-03-10'),
    (4, 5, '2024-04-12', '2024-04-16', NULL),         -- still active
    (5, 2, '2024-05-01', '2024-05-05', '2024-05-05');


-- ─── Payments ───────────────────────────────────────────
-- total_cost calculated as DATEDIFF(return_date, rental_date) * rental_rate
-- R1: 5 days * 4500 = 22500, R2: 7 days * 8500 = 59500, etc.
INSERT INTO Payment (rental_id, payment_amount, payment_date) VALUES
    (1, 22500.00, '2024-01-15'),
    (2, 59500.00, '2024-02-08'),
    (3, 35000.00, '2024-03-10'),
    (5, 18000.00, '2024-05-05'),
    (1,  2500.00, '2024-01-16');  -- late penalty payment for rental 1


-- ─── Maintenance ────────────────────────────────────────
INSERT INTO Maintenance (vehicle_id, maintenance_date, maintenance_type, maintenance_cost, mechanic_id, next_service_due) VALUES
    (3, '2024-01-05', 'Oil Change',         3500.00, 1, '2024-04-05'),
    (2, '2024-02-20', 'Brake Pad Replacement', 8200.00, 3, '2024-08-20'),
    (1, '2024-03-15', 'Full Service',        15000.00, 1, '2024-09-15'),
    (3, '2024-03-28', 'Electrical Fault Fix', 6700.00, 2, NULL),
    (4, '2024-04-10', 'Tyre Rotation',        2500.00, 3, '2024-10-10');
