CREATE database em;
use em;
show tables;
SELECT * FROM employees;
UPDATE employees SET is_admin=1 WHERE id=1;

SELECT * FROM employees;
SELECT * FROM departments;
SELECT * FROM grades;
SELECT * FROM roles;

INSERT INTO employees (email, username, first_name, last_name, password_hash, department_id, role_id, grade_id, is_admin, created_at, updated_at) 
VALUES
('john.doe@example.com', 'johndoe', 'John', 'Doe', 'pbkdf2:sha256:600000$example1', NULL, NULL, NULL, 0, '2024-12-02 16:30:00', '2024-12-02 16:30:00'),
('jane.smith@example.com', 'janesmith', 'Jane', 'Smith', 'pbkdf2:sha256:600000$example2', NULL, NULL, NULL, 0, '2024-12-02 16:31:00', '2024-12-02 16:31:00'),
('michael.johnson@example.com', 'michaelj', 'Michael', 'Johnson', 'pbkdf2:sha256:600000$example3', NULL, NULL, NULL, 0, '2024-12-02 16:32:00', '2024-12-02 16:32:00'),
('emily.davis@example.com', 'emilydavis', 'Emily', 'Davis', 'pbkdf2:sha256:600000$example4', NULL, NULL, NULL, 0, '2024-12-02 16:33:00', '2024-12-02 16:33:00'),
('daniel.brown@example.com', 'danbrown', 'Daniel', 'Brown', 'pbkdf2:sha256:600000$example5', NULL, NULL, NULL, 0, '2024-12-02 16:34:00', '2024-12-02 16:34:00');
INSERT INTO employees (email, username, first_name, last_name, password_hash, department_id, role_id, grade_id, is_admin, created_at, updated_at) 
VALUES
('alice.green@example.com', 'alicegreen', 'Alice', 'Green', 'pbkdf2:sha256:600000$example6', NULL, NULL, NULL, 0, '2024-12-02 16:35:00', '2024-12-02 16:35:00'),
('bob.white@example.com', 'bobwhite', 'Bob', 'White', 'pbkdf2:sha256:600000$example7', NULL, NULL, NULL, 0, '2024-12-02 16:36:00', '2024-12-02 16:36:00'),
('chris.martin@example.com', 'chrismartin', 'Chris', 'Martin', 'pbkdf2:sha256:600000$example8', NULL, NULL, NULL, 0, '2024-12-02 16:37:00', '2024-12-02 16:37:00'),
('susan.clark@example.com', 'susanclark', 'Susan', 'Clark', 'pbkdf2:sha256:600000$example9', NULL, NULL, NULL, 0, '2024-12-02 16:38:00', '2024-12-02 16:38:00'),
('robert.king@example.com', 'robertk', 'Robert', 'King', 'pbkdf2:sha256:600000$example10', NULL, NULL, NULL, 0, '2024-12-02 16:39:00', '2024-12-02 16:39:00'),
('julia.harris@example.com', 'juliaharris', 'Julia', 'Harris', 'pbkdf2:sha256:600000$example11', NULL, NULL, NULL, 0, '2024-12-02 16:40:00', '2024-12-02 16:40:00'),
('david.miller@example.com', 'davidmiller', 'David', 'Miller', 'pbkdf2:sha256:600000$example12', NULL, NULL, NULL, 0, '2024-12-02 16:41:00', '2024-12-02 16:41:00'),
('sarah.moore@example.com', 'sarahmoore', 'Sarah', 'Moore', 'pbkdf2:sha256:600000$example13', NULL, NULL, NULL, 0, '2024-12-02 16:42:00', '2024-12-02 16:42:00'),
('george.taylor@example.com', 'georgetaylor', 'George', 'Taylor', 'pbkdf2:sha256:600000$example14', NULL, NULL, NULL, 0, '2024-12-02 16:43:00', '2024-12-02 16:43:00'),
('lisa.jackson@example.com', 'lisajackson', 'Lisa', 'Jackson', 'pbkdf2:sha256:600000$example15', NULL, NULL, NULL, 0, '2024-12-02 16:44:00', '2024-12-02 16:44:00');


INSERT INTO departments (id, name, description, created_at, updated_at)
VALUES
(7, 'Human Resources', 'Manages hiring and employee policies.', '2024-12-02 17:10:00', '2024-12-02 17:10:00'),
(8, 'Engineering', 'Develops and maintains software.', '2024-12-02 17:11:00', '2024-12-02 17:11:00'),
(9, 'Marketing', 'Promotes products and services.', '2024-12-02 17:12:00', '2024-12-02 17:12:00'),
(10, 'Sales', 'Drives revenue and client relations.', '2024-12-02 17:13:00', '2024-12-02 17:13:00'),
(11, 'Customer Support', 'Assists customers with issues.', '2024-12-02 17:14:00', '2024-12-02 17:14:00');


INSERT INTO grades (id, paygrade, amount, created_at, updated_at)
VALUES
(1, 'Grade A', 75000, '2024-12-02 17:20:00', '2024-12-02 17:20:00'),
(2, 'Grade B', 60000, '2024-12-02 17:21:00', '2024-12-02 17:21:00'),
(3, 'Grade C', 50000, '2024-12-02 17:22:00', '2024-12-02 17:22:00'),
(4, 'Grade D', 40000, '2024-12-02 17:23:00', '2024-12-02 17:23:00'),
(5, 'Grade E', 30000, '2024-12-02 17:24:00', '2024-12-02 17:24:00');

INSERT INTO roles (id, name, description, created_at, updated_at)
VALUES
(1, 'Manager', 'Oversees team operations and ensures project delivery.', '2024-12-02 17:30:00', '2024-12-02 17:30:00'),
(2, 'Developer', 'Responsible for coding and software development.', '2024-12-02 17:31:00', '2024-12-02 17:31:00'),
(3, 'Designer', 'Handles UI/UX and graphic design tasks.', '2024-12-02 17:32:00', '2024-12-02 17:32:00'),
(4, 'Analyst', 'Analyzes data and provides insights for decision-making.', '2024-12-02 17:33:00', '2024-12-02 17:33:00'),
(5, 'Tester', 'Performs software testing to ensure quality.', '2024-12-02 17:34:00', '2024-12-02 17:34:00');

INSERT INTO roles (id, name, description, created_at, updated_at)
VALUES
(6, 'Product Owner', 'Defines product vision and prioritizes features.', '2024-12-02 17:35:00', '2024-12-02 17:35:00'),
(7, 'Support Specialist', 'Provides customer support and resolves issues.', '2024-12-02 17:36:00', '2024-12-02 17:36:00');

UPDATE grades SET amount = 90000  WHERE id = 2 ;
