C:\Users\User\AppData\Local\Programs\Python\Python38-32\python.exe C:\Users\User\PycharmProjects\Dbase_SQLAlchemy_HMWK\sql_alchemy_db.py
Engine(sqlite:///C:\Users\User\PycharmProjects\Dbase_SQLAlchemy_HMWK\sql_alch.db)
session.query(Customer).all()= [<Customer:1-tmiller>, <Customer:2-scottharvey>, <Customer:3-tmiller>, <Customer:4-scottharvey>, <Customer:5-tmiller>, <Customer:6-scottharvey>, <Customer:7-johnlara>, <Customer:8-sarahtomlin>, <Customer:9-tmiller>, <Customer:10-scottharvey>, <Customer:11-tmiller>, <Customer:12-scottharvey>, <Customer:13-johnlara>, <Customer:14-sarahtomlin>, <Customer:15-tmiller>, <Customer:16-scottharvey>, <Customer:17-johnlara>, <Customer:18-sarahtomlin>, <Customer:19-tmiller>, <Customer:20-scottharvey>, <Customer:21-tmiller>, <Customer:22-scottharvey>, <Customer:23-johnlara>, <Customer:24-sarahtomlin>, <Customer:25-tmiller>, <Customer:26-scottharvey>, <Customer:27-tmiller>, <Customer:28-scottharvey>, <Customer:29-tmiller>, <Customer:30-scottharvey>, <Customer:31-johnlara>, <Customer:32-sarahtomlin>, <Customer:33-tmiller>, <Customer:34-scottharvey>, <Customer:35-tmiller>, <Customer:36-scottharvey>, <Customer:37-johnlara>, <Customer:38-sarahtomlin>, <Customer:39-tmiller>, <Customer:40-scottharvey>, <Customer:41-tmiller>, <Customer:42-scottharvey>, <Customer:43-johnlara>, <Customer:44-sarahtomlin>, <Customer:45-tmiller>, <Customer:46-scottharvey>, <Customer:47-tmiller>, <Customer:48-scottharvey>, <Customer:49-johnlara>, <Customer:50-sarahtomlin>, <Customer:51-tmiller>, <Customer:52-scottharvey>, <Customer:53-tmiller>, <Customer:54-scottharvey>, <Customer:55-johnlara>, <Customer:56-sarahtomlin>, <Customer:57-tmiller>, <Customer:58-scottharvey>, <Customer:59-tmiller>, <Customer:60-scottharvey>, <Customer:61-johnlara>, <Customer:62-sarahtomlin>, <Customer:63-tmiller>, <Customer:64-scottharvey>, <Customer:65-tmiller>, <Customer:66-scottharvey>, <Customer:67-johnlara>, <Customer:68-sarahtomlin>, <Customer:69-tmiller>, <Customer:70-scottharvey>, <Customer:71-tmiller>, <Customer:72-scottharvey>, <Customer:73-johnlara>, <Customer:74-sarahtomlin>, <Customer:75-tmiller>, <Customer:76-scottharvey>, <Customer:77-tmiller>, <Customer:78-scottharvey>, <Customer:79-johnlara>, <Customer:80-sarahtomlin>, <Customer:81-tmiller>, <Customer:82-scottharvey>, <Customer:83-tmiller>, <Customer:84-scottharvey>, <Customer:85-tmiller>, <Customer:86-scottharvey>, <Customer:87-tmiller>, <Customer:88-scottharvey>, <Customer:89-tmiller>, <Customer:90-scottharvey>, <Customer:91-johnlara>, <Customer:92-sarahtomlin>, <Customer:93-tmiller>, <Customer:94-scottharvey>, <Customer:95-tmiller>, <Customer:96-scottharvey>, <Customer:97-johnlara>, <Customer:98-sarahtomlin>, <Customer:99-tmiller>, <Customer:100-scottharvey>, <Customer:101-tmiller>, <Customer:102-scottharvey>, <Customer:103-johnlara>, <Customer:104-sarahtomlin>, <Customer:105-tmiller>, <Customer:106-scottharvey>, <Customer:107-tmiller>, <Customer:108-scottharvey>, <Customer:109-johnlara>, <Customer:110-sarahtomlin>, <Customer:111-tmiller>, <Customer:112-scottharvey>, <Customer:113-tmiller>, <Customer:114-scottharvey>, <Customer:115-tmiller>, <Customer:116-scottharvey>, <Customer:117-tmiller>, <Customer:118-scottharvey>, <Customer:119-tmiller>, <Customer:120-scottharvey>, <Customer:121-tmiller>, <Customer:122-scottharvey>, <Customer:123-tmiller>, <Customer:124-scottharvey>]
C:\Users\User\AppData\Local\Programs\Python\Python38-32\lib\site-packages\sqlalchemy\sql\sqltypes.py:659: SAWarning: Dialect sqlite+pysqlite does *not* support Decimal objects natively, and SQLAlchemy must convert from floating point - rounding errors and other issues may occur. Please consider storing Decimal numbers as strings or integers on this platform for lossless storage.
  util.warn(
session.query(Item).all() session.query(Order).all()= [<Item:1-Chair>, <Item:2-Pen>, <Item:3-Headphone>, <Item:4-Travel Bag>, <Item:5-Keyboard>, <Item:6-Monitor>, <Item:9-Chair>, <Item:10-Pen>, <Item:11-Headphone>, <Item:12-Travel Bag>, <Item:13-Keyboard>, <Item:14-Monitor>, <Item:17-Chair>, <Item:18-Pen>, <Item:19-Headphone>, <Item:20-Travel Bag>, <Item:21-Keyboard>, <Item:22-Monitor>, <Item:25-Chair>, <Item:26-Pen>, <Item:27-Headphone>, <Item:28-Travel Bag>, <Item:29-Keyboard>, <Item:30-Monitor>, <Item:33-Chair>, <Item:34-Pen>, <Item:35-Headphone>, <Item:36-Travel Bag>, <Item:37-Keyboard>, <Item:38-Monitor>, <Item:41-Chair>, <Item:42-Pen>, <Item:43-Headphone>, <Item:44-Travel Bag>, <Item:45-Keyboard>, <Item:46-Monitor>, <Item:49-Chair>, <Item:50-Pen>, <Item:51-Headphone>, <Item:52-Travel Bag>, <Item:53-Keyboard>, <Item:54-Monitor>, <Item:57-Chair>, <Item:58-Pen>, <Item:59-Headphone>, <Item:60-Travel Bag>, <Item:61-Keyboard>, <Item:62-Monitor>, <Item:65-Chair>, <Item:66-Pen>, <Item:67-Chair>, <Item:68-Pen>, <Item:69-Headphone>, <Item:70-Travel Bag>, <Item:71-Keyboard>, <Item:72-Monitor>, <Item:73-Chair>, <Item:74-Pen>, <Item:75-Headphone>, <Item:76-Travel Bag>, <Item:77-Keyboard>, <Item:78-Monitor>, <Item:79-Chair>, <Item:80-Pen>, <Item:81-Headphone>, <Item:82-Travel Bag>, <Item:83-Keyboard>, <Item:84-Monitor>, <Item:85-Chair>, <Item:86-Pen>, <Item:87-Chair>, <Item:88-Pen>, <Item:89-Chair>, <Item:90-Pen>, <Item:91-Chair>, <Item:92-Pen>, <Item:93-Chair>, <Item:94-Pen>, <Item:95-Chair>, <Item:96-Pen>, <Item:97-Headphone>, <Item:98-Travel Bag>, <Item:99-Keyboard>, <Item:100-Monitor>, <Item:103-Chair>, <Item:104-Pen>, <Item:105-Headphone>, <Item:106-Travel Bag>, <Item:107-Keyboard>, <Item:108-Monitor>, <Item:111-Chair>, <Item:112-Pen>, <Item:113-Chair>, <Item:114-Pen>, <Item:115-Chair>, <Item:116-Pen>, <Item:117-Chair>, <Item:118-Pen>, <Item:119-Chair>, <Item:120-Pen>, <Item:121-Chair>, <Item:122-Pen>] [<Order:1>, <Order:2>, <Order:3>, <Order:4>, <Order:5>, <Order:6>, <Order:7>, <Order:8>, <Order:9>, <Order:10>, <Order:11>, <Order:12>, <Order:13>, <Order:14>, <Order:15>, <Order:16>, <Order:17>, <Order:18>, <Order:19>, <Order:20>, <Order:21>, <Order:22>, <Order:23>, <Order:24>, <Order:25>, <Order:26>, <Order:27>, <Order:28>, <Order:29>, <Order:30>, <Order:31>, <Order:32>, <Order:33>, <Order:34>, <Order:35>, <Order:36>, <Order:37>, <Order:38>, <Order:39>, <Order:40>, <Order:41>, <Order:42>, <Order:43>, <Order:44>, <Order:45>, <Order:46>, <Order:47>, <Order:48>, <Order:49>, <Order:50>, <Order:51>, <Order:52>, <Order:53>, <Order:54>, <Order:55>, <Order:56>, <Order:57>, <Order:58>, <Order:59>, <Order:60>, <Order:61>, <Order:62>, <Order:63>, <Order:64>, <Order:65>, <Order:66>, <Order:67>, <Order:68>, <Order:69>, <Order:70>]
SELECT customers.id AS customers_id, customers.first_name AS customers_first_name, customers.last_name AS customers_last_name, customers.username AS customers_username, customers.email AS customers_email, customers.address AS customers_address, customers.town AS customers_town, customers.created_on AS customers_created_on, customers.updated_on AS customers_updated_on 
FROM customers
1 Toby
2 Scott
3 Toby
4 Scott
5 Toby
6 Scott
7 John
8 Sarah
9 Toby
10 Scott
11 Toby
12 Scott
13 John
14 Sarah
15 Toby
16 Scott
17 John
18 Sarah
19 Toby
20 Scott
21 Toby
22 Scott
23 John
24 Sarah
25 Toby
26 Scott
27 Toby
28 Scott
29 Toby
30 Scott
31 John
32 Sarah
33 Toby
34 Scott
35 Toby
36 Scott
37 John
38 Sarah
39 Toby
40 Scott
41 Toby
42 Scott
43 John
44 Sarah
45 Toby
46 Scott
47 Toby
48 Scott
49 John
50 Sarah
51 Toby
52 Scott
53 Toby
54 Scott
55 John
56 Sarah
57 Toby
58 Scott
59 Toby
60 Scott
61 John
62 Sarah
63 Toby
64 Scott
65 Toby
66 Scott
67 John
68 Sarah
69 Toby
70 Scott
71 Toby
72 Scott
73 John
74 Sarah
75 Toby
76 Scott
77 Toby
78 Scott
79 John
80 Sarah
81 Toby
82 Scott
83 Toby
84 Scott
85 Toby
86 Scott
87 Toby
88 Scott
89 Toby
90 Scott
91 John
92 Sarah
93 Toby
94 Scott
95 Toby
96 Scott
97 John
98 Sarah
99 Toby
100 Scott
101 Toby
102 Scott
103 John
104 Sarah
105 Toby
106 Scott
107 Toby
108 Scott
109 John
110 Sarah
111 Toby
112 Scott
113 Toby
114 Scott
115 Toby
116 Scott
117 Toby
118 Scott
119 Toby
120 Scott
121 Toby
122 Scott
123 Toby
124 Scott
session.query(Customer.id, Customer.first_name).all()= [(1, 'Toby'), (2, 'Scott'), (3, 'Toby'), (4, 'Scott'), (5, 'Toby'), (6, 'Scott'), (7, 'John'), (8, 'Sarah'), (9, 'Toby'), (10, 'Scott'), (11, 'Toby'), (12, 'Scott'), (13, 'John'), (14, 'Sarah'), (15, 'Toby'), (16, 'Scott'), (17, 'John'), (18, 'Sarah'), (19, 'Toby'), (20, 'Scott'), (21, 'Toby'), (22, 'Scott'), (23, 'John'), (24, 'Sarah'), (25, 'Toby'), (26, 'Scott'), (27, 'Toby'), (28, 'Scott'), (29, 'Toby'), (30, 'Scott'), (31, 'John'), (32, 'Sarah'), (33, 'Toby'), (34, 'Scott'), (35, 'Toby'), (36, 'Scott'), (37, 'John'), (38, 'Sarah'), (39, 'Toby'), (40, 'Scott'), (41, 'Toby'), (42, 'Scott'), (43, 'John'), (44, 'Sarah'), (45, 'Toby'), (46, 'Scott'), (47, 'Toby'), (48, 'Scott'), (49, 'John'), (50, 'Sarah'), (51, 'Toby'), (52, 'Scott'), (53, 'Toby'), (54, 'Scott'), (55, 'John'), (56, 'Sarah'), (57, 'Toby'), (58, 'Scott'), (59, 'Toby'), (60, 'Scott'), (61, 'John'), (62, 'Sarah'), (63, 'Toby'), (64, 'Scott'), (65, 'Toby'), (66, 'Scott'), (67, 'John'), (68, 'Sarah'), (69, 'Toby'), (70, 'Scott'), (71, 'Toby'), (72, 'Scott'), (73, 'John'), (74, 'Sarah'), (75, 'Toby'), (76, 'Scott'), (77, 'Toby'), (78, 'Scott'), (79, 'John'), (80, 'Sarah'), (81, 'Toby'), (82, 'Scott'), (83, 'Toby'), (84, 'Scott'), (85, 'Toby'), (86, 'Scott'), (87, 'Toby'), (88, 'Scott'), (89, 'Toby'), (90, 'Scott'), (91, 'John'), (92, 'Sarah'), (93, 'Toby'), (94, 'Scott'), (95, 'Toby'), (96, 'Scott'), (97, 'John'), (98, 'Sarah'), (99, 'Toby'), (100, 'Scott'), (101, 'Toby'), (102, 'Scott'), (103, 'John'), (104, 'Sarah'), (105, 'Toby'), (106, 'Scott'), (107, 'Toby'), (108, 'Scott'), (109, 'John'), (110, 'Sarah'), (111, 'Toby'), (112, 'Scott'), (113, 'Toby'), (114, 'Scott'), (115, 'Toby'), (116, 'Scott'), (117, 'Toby'), (118, 'Scott'), (119, 'Toby'), (120, 'Scott'), (121, 'Toby'), (122, 'Scott'), (123, 'Toby'), (124, 'Scott')]
session.query(Customer).count() 124
session.query(Item).count() 102
session.query(Order).count() 70
session.query(Customer).first() <Customer:1-tmiller>
session.query(Item).first() <Item:1-Chair>
session.query(Order).first() <Order:1>
session.query(Customer).get(1) <Customer:1-tmiller>
session.query(Item).get(1) <Item:1-Chair>
session.query(Order).get(100) None
session.query(Customer).filter(Customer.first_name == 'John').all() [<Customer:7-johnlara>, <Customer:13-johnlara>, <Customer:17-johnlara>, <Customer:23-johnlara>, <Customer:31-johnlara>, <Customer:37-johnlara>, <Customer:43-johnlara>, <Customer:49-johnlara>, <Customer:55-johnlara>, <Customer:61-johnlara>, <Customer:67-johnlara>, <Customer:73-johnlara>, <Customer:79-johnlara>, <Customer:91-johnlara>, <Customer:97-johnlara>, <Customer:103-johnlara>, <Customer:109-johnlara>]
SELECT customers.id AS customers_id, customers.first_name AS customers_first_name, customers.last_name AS customers_last_name, customers.username AS customers_username, customers.email AS customers_email, customers.address AS customers_address, customers.town AS customers_town, customers.created_on AS customers_created_on, customers.updated_on AS customers_updated_on 
FROM customers 
WHERE customers.first_name = ?
session.query(Customer).filter(Customer.id <= 7, Customer.town == 'Norfolk').all() [<Customer:7-johnlara>]
SELECT customers.id AS customers_id, customers.first_name AS customers_first_name, customers.last_name AS customers_last_name, customers.username AS customers_username, customers.email AS customers_email, customers.address AS customers_address, customers.town AS customers_town, customers.created_on AS customers_created_on, customers.updated_on AS customers_updated_on 
FROM customers 
WHERE customers.id <= ? AND customers.town LIKE ?
-----------
[<Customer:7-johnlara>, <Customer:8-sarahtomlin>, <Customer:13-johnlara>, <Customer:14-sarahtomlin>, <Customer:17-johnlara>, <Customer:18-sarahtomlin>, <Customer:23-johnlara>, <Customer:24-sarahtomlin>, <Customer:31-johnlara>, <Customer:32-sarahtomlin>, <Customer:37-johnlara>, <Customer:38-sarahtomlin>, <Customer:43-johnlara>, <Customer:44-sarahtomlin>, <Customer:49-johnlara>, <Customer:50-sarahtomlin>, <Customer:55-johnlara>, <Customer:56-sarahtomlin>, <Customer:61-johnlara>, <Customer:62-sarahtomlin>, <Customer:67-johnlara>, <Customer:68-sarahtomlin>, <Customer:73-johnlara>, <Customer:74-sarahtomlin>, <Customer:79-johnlara>, <Customer:80-sarahtomlin>, <Customer:91-johnlara>, <Customer:92-sarahtomlin>, <Customer:97-johnlara>, <Customer:98-sarahtomlin>, <Customer:103-johnlara>, <Customer:104-sarahtomlin>, <Customer:109-johnlara>, <Customer:110-sarahtomlin>]
[<Customer:7-johnlara>, <Customer:13-johnlara>, <Customer:17-johnlara>, <Customer:23-johnlara>, <Customer:31-johnlara>, <Customer:37-johnlara>, <Customer:43-johnlara>, <Customer:49-johnlara>, <Customer:55-johnlara>, <Customer:61-johnlara>, <Customer:67-johnlara>, <Customer:73-johnlara>, <Customer:79-johnlara>, <Customer:91-johnlara>, <Customer:97-johnlara>, <Customer:103-johnlara>, <Customer:109-johnlara>]
[<Customer:7-johnlara>, <Customer:13-johnlara>, <Customer:17-johnlara>, <Customer:23-johnlara>, <Customer:31-johnlara>, <Customer:37-johnlara>, <Customer:43-johnlara>, <Customer:49-johnlara>, <Customer:55-johnlara>, <Customer:61-johnlara>, <Customer:67-johnlara>, <Customer:73-johnlara>, <Customer:79-johnlara>, <Customer:91-johnlara>, <Customer:97-johnlara>, <Customer:103-johnlara>, <Customer:109-johnlara>]
session.query(Order).filter(Order.date_shipped == None).all() [<Order:2>, <Order:3>, <Order:4>, <Order:5>, <Order:6>, <Order:7>, <Order:8>, <Order:9>, <Order:10>, <Order:11>, <Order:12>, <Order:13>, <Order:14>, <Order:15>, <Order:16>, <Order:17>, <Order:18>, <Order:19>, <Order:20>, <Order:21>, <Order:22>, <Order:23>, <Order:24>, <Order:25>, <Order:26>, <Order:27>, <Order:28>, <Order:29>, <Order:30>, <Order:31>, <Order:32>, <Order:33>, <Order:34>, <Order:35>, <Order:36>, <Order:37>, <Order:38>, <Order:39>, <Order:40>, <Order:41>, <Order:42>, <Order:43>, <Order:44>, <Order:45>, <Order:46>, <Order:47>, <Order:48>, <Order:49>, <Order:50>, <Order:51>, <Order:52>, <Order:53>, <Order:54>, <Order:55>, <Order:56>, <Order:57>, <Order:58>, <Order:59>, <Order:60>, <Order:61>, <Order:62>, <Order:63>, <Order:64>, <Order:65>, <Order:66>, <Order:67>, <Order:68>, <Order:69>, <Order:70>]
session.query(Order).filter(Order.date_shipped != None).all() [<Order:1>]
session.query(Customer).filter(Customer.first_name.in_(['Toby', 'Sarah'])).all() [<Customer:1-tmiller>, <Customer:3-tmiller>, <Customer:5-tmiller>, <Customer:8-sarahtomlin>, <Customer:9-tmiller>, <Customer:11-tmiller>, <Customer:14-sarahtomlin>, <Customer:15-tmiller>, <Customer:18-sarahtomlin>, <Customer:19-tmiller>, <Customer:21-tmiller>, <Customer:24-sarahtomlin>, <Customer:25-tmiller>, <Customer:27-tmiller>, <Customer:29-tmiller>, <Customer:32-sarahtomlin>, <Customer:33-tmiller>, <Customer:35-tmiller>, <Customer:38-sarahtomlin>, <Customer:39-tmiller>, <Customer:41-tmiller>, <Customer:44-sarahtomlin>, <Customer:45-tmiller>, <Customer:47-tmiller>, <Customer:50-sarahtomlin>, <Customer:51-tmiller>, <Customer:53-tmiller>, <Customer:56-sarahtomlin>, <Customer:57-tmiller>, <Customer:59-tmiller>, <Customer:62-sarahtomlin>, <Customer:63-tmiller>, <Customer:65-tmiller>, <Customer:68-sarahtomlin>, <Customer:69-tmiller>, <Customer:71-tmiller>, <Customer:74-sarahtomlin>, <Customer:75-tmiller>, <Customer:77-tmiller>, <Customer:80-sarahtomlin>, <Customer:81-tmiller>, <Customer:83-tmiller>, <Customer:85-tmiller>, <Customer:87-tmiller>, <Customer:89-tmiller>, <Customer:92-sarahtomlin>, <Customer:93-tmiller>, <Customer:95-tmiller>, <Customer:98-sarahtomlin>, <Customer:99-tmiller>, <Customer:101-tmiller>, <Customer:104-sarahtomlin>, <Customer:105-tmiller>, <Customer:107-tmiller>, <Customer:110-sarahtomlin>, <Customer:111-tmiller>, <Customer:113-tmiller>, <Customer:115-tmiller>, <Customer:117-tmiller>, <Customer:119-tmiller>, <Customer:121-tmiller>, <Customer:123-tmiller>]
session.query(Customer).filter(Customer.first_name.notin_(['Toby', 'Sarah'])).all() [<Customer:2-scottharvey>, <Customer:4-scottharvey>, <Customer:6-scottharvey>, <Customer:7-johnlara>, <Customer:10-scottharvey>, <Customer:12-scottharvey>, <Customer:13-johnlara>, <Customer:16-scottharvey>, <Customer:17-johnlara>, <Customer:20-scottharvey>, <Customer:22-scottharvey>, <Customer:23-johnlara>, <Customer:26-scottharvey>, <Customer:28-scottharvey>, <Customer:30-scottharvey>, <Customer:31-johnlara>, <Customer:34-scottharvey>, <Customer:36-scottharvey>, <Customer:37-johnlara>, <Customer:40-scottharvey>, <Customer:42-scottharvey>, <Customer:43-johnlara>, <Customer:46-scottharvey>, <Customer:48-scottharvey>, <Customer:49-johnlara>, <Customer:52-scottharvey>, <Customer:54-scottharvey>, <Customer:55-johnlara>, <Customer:58-scottharvey>, <Customer:60-scottharvey>, <Customer:61-johnlara>, <Customer:64-scottharvey>, <Customer:66-scottharvey>, <Customer:67-johnlara>, <Customer:70-scottharvey>, <Customer:72-scottharvey>, <Customer:73-johnlara>, <Customer:76-scottharvey>, <Customer:78-scottharvey>, <Customer:79-johnlara>, <Customer:82-scottharvey>, <Customer:84-scottharvey>, <Customer:86-scottharvey>, <Customer:88-scottharvey>, <Customer:90-scottharvey>, <Customer:91-johnlara>, <Customer:94-scottharvey>, <Customer:96-scottharvey>, <Customer:97-johnlara>, <Customer:100-scottharvey>, <Customer:102-scottharvey>, <Customer:103-johnlara>, <Customer:106-scottharvey>, <Customer:108-scottharvey>, <Customer:109-johnlara>, <Customer:112-scottharvey>, <Customer:114-scottharvey>, <Customer:116-scottharvey>, <Customer:118-scottharvey>, <Customer:120-scottharvey>, <Customer:122-scottharvey>, <Customer:124-scottharvey>]
session.query(Item).filter(Item.cost_price.between(10, 50)).all() [<Item:3-Headphone>, <Item:4-Travel Bag>, <Item:5-Keyboard>, <Item:11-Headphone>, <Item:12-Travel Bag>, <Item:13-Keyboard>, <Item:19-Headphone>, <Item:20-Travel Bag>, <Item:21-Keyboard>, <Item:27-Headphone>, <Item:28-Travel Bag>, <Item:29-Keyboard>, <Item:35-Headphone>, <Item:36-Travel Bag>, <Item:37-Keyboard>, <Item:43-Headphone>, <Item:44-Travel Bag>, <Item:45-Keyboard>, <Item:51-Headphone>, <Item:52-Travel Bag>, <Item:53-Keyboard>, <Item:59-Headphone>, <Item:60-Travel Bag>, <Item:61-Keyboard>, <Item:69-Headphone>, <Item:70-Travel Bag>, <Item:71-Keyboard>, <Item:75-Headphone>, <Item:76-Travel Bag>, <Item:77-Keyboard>, <Item:81-Headphone>, <Item:82-Travel Bag>, <Item:83-Keyboard>, <Item:97-Headphone>, <Item:98-Travel Bag>, <Item:99-Keyboard>, <Item:105-Headphone>, <Item:106-Travel Bag>, <Item:107-Keyboard>]
session.query(Item).filter(not_(Item.cost_price.between(10, 50))).all() [<Item:1-Chair>, <Item:2-Pen>, <Item:6-Monitor>, <Item:9-Chair>, <Item:10-Pen>, <Item:14-Monitor>, <Item:17-Chair>, <Item:18-Pen>, <Item:22-Monitor>, <Item:25-Chair>, <Item:26-Pen>, <Item:30-Monitor>, <Item:33-Chair>, <Item:34-Pen>, <Item:38-Monitor>, <Item:41-Chair>, <Item:42-Pen>, <Item:46-Monitor>, <Item:49-Chair>, <Item:50-Pen>, <Item:54-Monitor>, <Item:57-Chair>, <Item:58-Pen>, <Item:62-Monitor>, <Item:65-Chair>, <Item:66-Pen>, <Item:67-Chair>, <Item:68-Pen>, <Item:72-Monitor>, <Item:73-Chair>, <Item:74-Pen>, <Item:78-Monitor>, <Item:79-Chair>, <Item:80-Pen>, <Item:84-Monitor>, <Item:85-Chair>, <Item:86-Pen>, <Item:87-Chair>, <Item:88-Pen>, <Item:89-Chair>, <Item:90-Pen>, <Item:91-Chair>, <Item:92-Pen>, <Item:93-Chair>, <Item:94-Pen>, <Item:95-Chair>, <Item:96-Pen>, <Item:100-Monitor>, <Item:103-Chair>, <Item:104-Pen>, <Item:108-Monitor>, <Item:111-Chair>, <Item:112-Pen>, <Item:113-Chair>, <Item:114-Pen>, <Item:115-Chair>, <Item:116-Pen>, <Item:117-Chair>, <Item:118-Pen>, <Item:119-Chair>, <Item:120-Pen>, <Item:121-Chair>, <Item:122-Pen>]
session.query(Item).filter(Item.name.like('%r')).all() [<Item:1-Chair>, <Item:6-Monitor>, <Item:9-Chair>, <Item:14-Monitor>, <Item:17-Chair>, <Item:22-Monitor>, <Item:25-Chair>, <Item:30-Monitor>, <Item:33-Chair>, <Item:38-Monitor>, <Item:41-Chair>, <Item:46-Monitor>, <Item:49-Chair>, <Item:54-Monitor>, <Item:57-Chair>, <Item:62-Monitor>, <Item:65-Chair>, <Item:67-Chair>, <Item:72-Monitor>, <Item:73-Chair>, <Item:78-Monitor>, <Item:79-Chair>, <Item:84-Monitor>, <Item:85-Chair>, <Item:87-Chair>, <Item:89-Chair>, <Item:91-Chair>, <Item:93-Chair>, <Item:95-Chair>, <Item:100-Monitor>, <Item:103-Chair>, <Item:108-Monitor>, <Item:111-Chair>, <Item:113-Chair>, <Item:115-Chair>, <Item:117-Chair>, <Item:119-Chair>, <Item:121-Chair>]
session.query(Item).filter(Item.name.ilike('w%')).all() []
session.query(Item).filter(not_(Item.name.like('W%'))).all() [<Item:1-Chair>, <Item:2-Pen>, <Item:3-Headphone>, <Item:4-Travel Bag>, <Item:5-Keyboard>, <Item:6-Monitor>, <Item:9-Chair>, <Item:10-Pen>, <Item:11-Headphone>, <Item:12-Travel Bag>, <Item:13-Keyboard>, <Item:14-Monitor>, <Item:17-Chair>, <Item:18-Pen>, <Item:19-Headphone>, <Item:20-Travel Bag>, <Item:21-Keyboard>, <Item:22-Monitor>, <Item:25-Chair>, <Item:26-Pen>, <Item:27-Headphone>, <Item:28-Travel Bag>, <Item:29-Keyboard>, <Item:30-Monitor>, <Item:33-Chair>, <Item:34-Pen>, <Item:35-Headphone>, <Item:36-Travel Bag>, <Item:37-Keyboard>, <Item:38-Monitor>, <Item:41-Chair>, <Item:42-Pen>, <Item:43-Headphone>, <Item:44-Travel Bag>, <Item:45-Keyboard>, <Item:46-Monitor>, <Item:49-Chair>, <Item:50-Pen>, <Item:51-Headphone>, <Item:52-Travel Bag>, <Item:53-Keyboard>, <Item:54-Monitor>, <Item:57-Chair>, <Item:58-Pen>, <Item:59-Headphone>, <Item:60-Travel Bag>, <Item:61-Keyboard>, <Item:62-Monitor>, <Item:65-Chair>, <Item:66-Pen>, <Item:67-Chair>, <Item:68-Pen>, <Item:69-Headphone>, <Item:70-Travel Bag>, <Item:71-Keyboard>, <Item:72-Monitor>, <Item:73-Chair>, <Item:74-Pen>, <Item:75-Headphone>, <Item:76-Travel Bag>, <Item:77-Keyboard>, <Item:78-Monitor>, <Item:79-Chair>, <Item:80-Pen>, <Item:81-Headphone>, <Item:82-Travel Bag>, <Item:83-Keyboard>, <Item:84-Monitor>, <Item:85-Chair>, <Item:86-Pen>, <Item:87-Chair>, <Item:88-Pen>, <Item:89-Chair>, <Item:90-Pen>, <Item:91-Chair>, <Item:92-Pen>, <Item:93-Chair>, <Item:94-Pen>, <Item:95-Chair>, <Item:96-Pen>, <Item:97-Headphone>, <Item:98-Travel Bag>, <Item:99-Keyboard>, <Item:100-Monitor>, <Item:103-Chair>, <Item:104-Pen>, <Item:105-Headphone>, <Item:106-Travel Bag>, <Item:107-Keyboard>, <Item:108-Monitor>, <Item:111-Chair>, <Item:112-Pen>, <Item:113-Chair>, <Item:114-Pen>, <Item:115-Chair>, <Item:116-Pen>, <Item:117-Chair>, <Item:118-Pen>, <Item:119-Chair>, <Item:120-Pen>, <Item:121-Chair>, <Item:122-Pen>]
session.query(Customer).limit(2).all() [<Customer:1-tmiller>, <Customer:2-scottharvey>]
session.query(Customer).filter(Customer.address.ilike('%avenue')).limit(2).all() [<Customer:8-sarahtomlin>, <Customer:14-sarahtomlin>]
SELECT customers.id AS customers_id, customers.first_name AS customers_first_name, customers.last_name AS customers_last_name, customers.username AS customers_username, customers.email AS customers_email, customers.address AS customers_address, customers.town AS customers_town, customers.created_on AS customers_created_on, customers.updated_on AS customers_updated_on 
FROM customers
 LIMIT ? OFFSET ?
SELECT customers.id AS customers_id, customers.first_name AS customers_first_name, customers.last_name AS customers_last_name, customers.username AS customers_username, customers.email AS customers_email, customers.address AS customers_address, customers.town AS customers_town, customers.created_on AS customers_created_on, customers.updated_on AS customers_updated_on 
FROM customers 
WHERE lower(customers.address) LIKE lower(?)
 LIMIT ? OFFSET ?
session.query(Customer).limit(2).offset(2).all() [<Customer:3-tmiller>, <Customer:4-scottharvey>]
SELECT customers.id AS customers_id, customers.first_name AS customers_first_name, customers.last_name AS customers_last_name, customers.username AS customers_username, customers.email AS customers_email, customers.address AS customers_address, customers.town AS customers_town, customers.created_on AS customers_created_on, customers.updated_on AS customers_updated_on 
FROM customers
 LIMIT ? OFFSET ?
session.query(Item).filter(Item.name.ilike('wa%')).all() []
session.query(Item).filter(Item.name.ilike('wa%')).order_by(Item.cost_price).all() []
[]
SELECT customers.id AS customers_id, customers.first_name AS customers_first_name, customers.last_name AS customers_last_name, customers.username AS customers_username, customers.email AS customers_email, customers.address AS customers_address, customers.town AS customers_town, customers.created_on AS customers_created_on, customers.updated_on AS customers_updated_on 
FROM customers JOIN orders ON customers.id = orders.customer_id
[(11, 'tmiller', 1), (11, 'tmiller', 2), (21, 'tmiller', 3), (21, 'tmiller', 4), (27, 'tmiller', 5), (27, 'tmiller', 6), (29, 'tmiller', 7), (29, 'tmiller', 8), (35, 'tmiller', 9), (35, 'tmiller', 10), (41, 'tmiller', 11), (41, 'tmiller', 12), (41, 'tmiller', 13), (47, 'tmiller', 14), (47, 'tmiller', 15), (47, 'tmiller', 16), (53, 'tmiller', 17), (53, 'tmiller', 18), (53, 'tmiller', 19), (59, 'tmiller', 20), (59, 'tmiller', 21), (59, 'tmiller', 22), (65, 'tmiller', 23), (65, 'tmiller', 24), (65, 'tmiller', 25), (71, 'tmiller', 26), (71, 'tmiller', 27), (71, 'tmiller', 28), (77, 'tmiller', 29), (77, 'tmiller', 30), (77, 'tmiller', 31), (83, 'tmiller', 32), (83, 'tmiller', 33), (83, 'tmiller', 34), (85, 'tmiller', 35), (85, 'tmiller', 36), (85, 'tmiller', 37), (87, 'tmiller', 38), (87, 'tmiller', 39), (87, 'tmiller', 40), (89, 'tmiller', 41), (89, 'tmiller', 42), (89, 'tmiller', 43), (95, 'tmiller', 44), (95, 'tmiller', 45), (95, 'tmiller', 46), (101, 'tmiller', 47), (101, 'tmiller', 48), (101, 'tmiller', 49), (107, 'tmiller', 50), (107, 'tmiller', 51), (107, 'tmiller', 52), (113, 'tmiller', 53), (113, 'tmiller', 54), (113, 'tmiller', 55), (115, 'tmiller', 56), (115, 'tmiller', 57), (115, 'tmiller', 58), (117, 'tmiller', 59), (117, 'tmiller', 60), (117, 'tmiller', 61), (119, 'tmiller', 62), (119, 'tmiller', 63), (119, 'tmiller', 64), (121, 'tmiller', 65), (121, 'tmiller', 66), (121, 'tmiller', 67), (123, 'tmiller', 68), (123, 'tmiller', 69), (123, 'tmiller', 70)]
[('Wolfden',), ('Beckinsdale',), ('Wolfden',), ('Beckinsdale',), ('Wolfden',), ('Beckinsdale',), ('Norfolk',), ('Norfolk',), ('Wolfden',)]
[('Wolfden',), ('Beckinsdale',), ('Norfolk',)]
[(3, 124)]
[(2, 'Pen'), (3, 'Headphone'), (4, 'Travel Bag'), (5, 'Keyboard'), (10, 'Pen'), (11, 'Headphone'), (12, 'Travel Bag'), (13, 'Keyboard'), (18, 'Pen'), (19, 'Headphone'), (20, 'Travel Bag'), (21, 'Keyboard'), (26, 'Pen'), (27, 'Headphone'), (28, 'Travel Bag'), (29, 'Keyboard'), (34, 'Pen'), (35, 'Headphone'), (36, 'Travel Bag'), (37, 'Keyboard'), (42, 'Pen'), (43, 'Headphone'), (44, 'Travel Bag'), (45, 'Keyboard'), (50, 'Pen'), (51, 'Headphone'), (52, 'Travel Bag'), (53, 'Keyboard'), (58, 'Pen'), (59, 'Headphone'), (60, 'Travel Bag'), (61, 'Keyboard'), (66, 'Pen'), (68, 'Pen'), (69, 'Headphone'), (70, 'Travel Bag'), (71, 'Keyboard'), (74, 'Pen'), (75, 'Headphone'), (76, 'Travel Bag'), (77, 'Keyboard'), (80, 'Pen'), (81, 'Headphone'), (82, 'Travel Bag'), (83, 'Keyboard'), (86, 'Pen'), (88, 'Pen'), (90, 'Pen'), (92, 'Pen'), (94, 'Pen'), (96, 'Pen'), (97, 'Headphone'), (98, 'Travel Bag'), (99, 'Keyboard'), (104, 'Pen'), (105, 'Headphone'), (106, 'Travel Bag'), (107, 'Keyboard'), (112, 'Pen'), (114, 'Pen'), (116, 'Pen'), (118, 'Pen'), (120, 'Pen'), (122, 'Pen')]
[(2, 'Pen'), (3, 'Headphone'), (4, 'Travel Bag'), (5, 'Keyboard'), (10, 'Pen'), (11, 'Headphone'), (12, 'Travel Bag'), (13, 'Keyboard'), (18, 'Pen'), (19, 'Headphone'), (20, 'Travel Bag'), (21, 'Keyboard'), (26, 'Pen'), (27, 'Headphone'), (28, 'Travel Bag'), (29, 'Keyboard'), (34, 'Pen'), (35, 'Headphone'), (36, 'Travel Bag'), (37, 'Keyboard'), (42, 'Pen'), (43, 'Headphone'), (44, 'Travel Bag'), (45, 'Keyboard'), (50, 'Pen'), (51, 'Headphone'), (52, 'Travel Bag'), (53, 'Keyboard'), (58, 'Pen'), (59, 'Headphone'), (60, 'Travel Bag'), (61, 'Keyboard'), (66, 'Pen'), (68, 'Pen'), (69, 'Headphone'), (70, 'Travel Bag'), (71, 'Keyboard'), (74, 'Pen'), (75, 'Headphone'), (76, 'Travel Bag'), (77, 'Keyboard'), (80, 'Pen'), (81, 'Headphone'), (82, 'Travel Bag'), (83, 'Keyboard'), (86, 'Pen'), (88, 'Pen'), (90, 'Pen'), (92, 'Pen'), (94, 'Pen'), (96, 'Pen'), (97, 'Headphone'), (98, 'Travel Bag'), (99, 'Keyboard'), (104, 'Pen'), (105, 'Headphone'), (106, 'Travel Bag'), (107, 'Keyboard'), (112, 'Pen'), (114, 'Pen'), (116, 'Pen'), (118, 'Pen'), (120, 'Pen'), (122, 'Pen')]
0
[<Customer:7-johnlara>, <Customer:13-johnlara>, <Customer:17-johnlara>, <Customer:23-johnlara>, <Customer:31-johnlara>, <Customer:37-johnlara>, <Customer:43-johnlara>, <Customer:49-johnlara>, <Customer:55-johnlara>, <Customer:61-johnlara>, <Customer:67-johnlara>, <Customer:73-johnlara>, <Customer:79-johnlara>, <Customer:91-johnlara>, <Customer:97-johnlara>, <Customer:103-johnlara>, <Customer:109-johnlara>]
[<Customer:7-johnlara>, <Customer:8-sarahtomlin>, <Customer:13-johnlara>, <Customer:14-sarahtomlin>, <Customer:17-johnlara>, <Customer:18-sarahtomlin>, <Customer:23-johnlara>, <Customer:24-sarahtomlin>, <Customer:31-johnlara>, <Customer:32-sarahtomlin>, <Customer:37-johnlara>, <Customer:38-sarahtomlin>, <Customer:43-johnlara>, <Customer:44-sarahtomlin>, <Customer:49-johnlara>, <Customer:50-sarahtomlin>, <Customer:55-johnlara>, <Customer:56-sarahtomlin>, <Customer:61-johnlara>, <Customer:62-sarahtomlin>, <Customer:67-johnlara>, <Customer:68-sarahtomlin>, <Customer:73-johnlara>, <Customer:74-sarahtomlin>, <Customer:79-johnlara>, <Customer:80-sarahtomlin>, <Customer:91-johnlara>, <Customer:92-sarahtomlin>, <Customer:97-johnlara>, <Customer:98-sarahtomlin>, <Customer:103-johnlara>, <Customer:104-sarahtomlin>, <Customer:109-johnlara>, <Customer:110-sarahtomlin>]
[<Customer:109-johnlara>, <Customer:103-johnlara>, <Customer:97-johnlara>, <Customer:91-johnlara>, <Customer:79-johnlara>, <Customer:73-johnlara>, <Customer:67-johnlara>, <Customer:61-johnlara>, <Customer:55-johnlara>, <Customer:49-johnlara>, <Customer:43-johnlara>, <Customer:37-johnlara>, <Customer:31-johnlara>, <Customer:23-johnlara>, <Customer:17-johnlara>, <Customer:13-johnlara>, <Customer:7-johnlara>, <Customer:110-sarahtomlin>, <Customer:104-sarahtomlin>, <Customer:98-sarahtomlin>, <Customer:92-sarahtomlin>, <Customer:80-sarahtomlin>, <Customer:74-sarahtomlin>, <Customer:68-sarahtomlin>, <Customer:62-sarahtomlin>, <Customer:56-sarahtomlin>, <Customer:50-sarahtomlin>, <Customer:44-sarahtomlin>, <Customer:38-sarahtomlin>, <Customer:32-sarahtomlin>, <Customer:24-sarahtomlin>, <Customer:18-sarahtomlin>, <Customer:14-sarahtomlin>, <Customer:8-sarahtomlin>]
Order already shipped.

Process finished with exit code 0
