This is a customer database
+-----------------+     +---------------------+     +------------------------+     +-------------+
|     Category    |     |       Product       |     |         Order          |     |   Customer  |
+-----------------+     +---------------------+     +------------------------+     +-------------+
| - id: PK        |     | - id: PK            |     | - id: PK               |     | - id: PK    |
| - name: Char     |     | - name: Char        |     | - order_date: Date     |     | - name: Char|
| - created_at     |     | - description: Text |     | - total_amount: Decimal|     | - email: Email|
| - updated_at     |     | - image: ImageField |     | - created_at           |     | - created_at |
|                 |     | - price: Decimal    |     | - updated_at           |     | - updated_at |
|                 |     | - category: FK      |     |                        |     | - orders: M2M|
+-----------------+     +---------------------+     +------------------------+     +-------------+
                                    |
                                    |
                                    v
                             +-------------------+
                             |      BaseModel    |
                             +-------------------+
                             | - id: PK          |
                             | - created_at      |
                             | - updated_at      |
                             +-------------------+
Category (One-to-Many with Product): The Category model has a one-to-many relationship with the Product model. Each category can have multiple products, but each product belongs to only one category.

Product (Many-to-One with Category and Many-to-Many with Order): The Product model has a many-to-one relationship with the Category model (each product belongs to one category), and a many-to-many relationship with the Order model (a product can be in multiple orders, and an order can contain multiple products).

Order (Many-to-Many with Product and Many-to-Many with Customer): The Order model has a many-to-many relationship with the Product model (an order can contain multiple products, and a product can be in multiple orders) and a many-to-many relationship with the Customer model (an order can be associated with multiple customers, and a customer can have multiple orders).

Customer (Many-to-Many with Order): The Customer model has a many-to-many relationship with the Order model. A customer can be associated with multiple orders, and an order can have multiple customers.

BaseModel (No direct table): The BaseModel is an abstract model serving as a base for other models. It includes common fields like id, created_at, and updated_at. It doesn't create its own table but provides these fields to other models through inheritance.
