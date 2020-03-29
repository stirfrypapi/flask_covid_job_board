INSERT INTO accounts(email, password, account_type, created)
VALUES
('pangr@gmail.com', 'password123', 'Applicant', CURRENT_TIMESTAMP),
('pango@gmail.com', 'password123', 'Applicant', CURRENT_TIMESTAMP),
('nypresbyterian@gmail.com', 'password123', 'Employer', CURRENT_TIMESTAMP);

INSERT INTO applicants(email, profession, first_name, last_name, school, grad_date, exp_position, exp_description, exp_from, exp_to, created)
VALUES
('pangr@gmail.com', 'student', 'Ray', 'Pang', 'Univ of Michigan', CURRENT_TIMESTAMP, 'Nurse', 'nused people back to health', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('pango@gmail.com', 'student', 'Ray', 'Pang', 'Univ of Michigan', CURRENT_TIMESTAMP, 'Nurse', 'nused people back to health', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

INSERT INTO applications(email, opening_id, status)
VALUES
('pangr@gmail.com', '1', 'submitted'),
('pango@gmail.com', '1', 'submitted');

INSERT INTO employers(email, name, address_1, address_2, city, state, zipcode)
VALUES
('nypresbyterian@gmail.com', 'NY Presbyterian', '123 Park Ave', NULL, 'NY', 'NY', '11364');

INSERT INTO openings(opening_id, date_posted, urgency, title, description, email, deadline)
VALUES
('1', CURRENT_TIMESTAMP, 'urgent', 'Need nurses ASAP', 'Nurse Covid19 patients', 'nypresbyterian@gmail.com', CURRENT_TIMESTAMP);

