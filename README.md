# milestone-project-four

# E-Commerce Site for Reson Interiors

Contents
- [Project Goals](#project-goals)
- [Business Goals](#business-goals)
- [User Personas](#user-personas)
- [User Stories](#user-stories)
- [Data Base Schema](#db-models)

##UX

### Project Goals
The goal of the project is to create a full-stack e-commerce django site comprised of multiple apps that include a well structured relational database, CRUD operations, authentication, authorisation, permission bondaries and a real e-commerce payment flow. The project will demonstrate excellent UX design, featuring a clean seperation of concerns with a well organised directory structure with reliably structured and accurately maintained content across all files, as well as robust and graceful error handling.

---------------------------------------

### Business goals
- Increase Sales by adding an online revenue stream  
- Increase Footfall In-Store by conveying information about us and our store  
- Reach a national market for a selection of our products
- [Could have some kind business metric tracking goal]

### User Personas
The Casual Browser:  
Goal - Browse the site to see everything the shop has to offer
Context - Didn't arrive to buy anything specific but is interested to see what they can find by casualy browsing while at home, at work or on the go.  
Frustrations - Poor Site Layout, Unclear Navigation, unresponsive on different devices  
Needs - Clear site navigation and Informative, Intuitive Product Navigation. Help in discovering Flagship items or best selling products to help new/casual browsers find our best products.  

The Regular/Repeat Customer:
Goal - Buy something Again with ease   
Context - Regular customer who knows what they want to buy.  
Frustration - Not being able to quickly identify the items they know that they are looking for   
Needs - Easy and Intuitive Navigation, Easy to Access previous orders seciton    

The Gift Buyer:  
Goal - Find a gift for a specific occasion or stock up on gift supplies  
Context - Someone who may be looking for an item for a specific occasion or someone who is just looking to stock up on their gift supplies.    
Frustrations - Unclear Occasion Categories, Difficult to find Gift Card Seciton.  
Needs - Ability to search by occasion and Buy a Gift Card.  

The Vintage Collector:  
Goal - Find one of a kind vintage products not available elsewhere.  
Context - Someone who enjoys spending time hunting for one of a kind vintage products.  
Frustration - Unclear Photographs/Condition of items. Bad Product Navigation.  
Needs - Vintage Site Section. Vintage Product Category with Comprehensive Attributes to Provide Clarity.  

### User Stories
🟢 MUST HAVE
🟡 SHOULD HAVE
🔵 COULD HAVE

(from casual browser)  
🟢 As a visitor, I want to browse products without needing to create an account so that I can explore the site freely.  
🟢 As a visitor, I want clear navigation menus and categories so that I can easily find products of interest.  
🟢 As a visitor, I want search and filtering tools so that I can refine product listings easily.  
🟡 As a visitor, I want to see featured and best-selling products so that I can quickly understand what the store offers.  
🟢 As a visitor, I want the site to work well on mobile and desktop so that I can browse comfortably on any device.  
🟢 As a visitor, I want product pages to load quickly and display clear information so that I can make informed browsing decisions.  

(from regular customer)  
🟡 As a customer, I want an “Order History” section so that I can view past purchases and track what I have already bought.  
🟡 As a customer, I want the checkout process to be fast and pre-filled with my saved details so that I can complete purchases efficiently.  
🟢 As a customer, I want my basket updates to appear instantly so that I always know what I am about to purchase.  

(from gift giver)   
🟡 As a customer, I want to browse products by occasion (e.g. birthdays, anniversaries) so that I can quickly find suitable gifts.    
🟡 As a customer, I want a gift card option so that I can purchase flexible gifts when I am unsure what to buy.   
🟢 As a customer, I want filtering options such as price range and category so that I can stay within my budget.  
🟢 As a customer, I want clear delivery information so that I can ensure gifts arrive on time.  

(from vintage hunter)  
🔵 As a customer, I want detailed product descriptions including condition and known history and high-quality images so that I can assess authenticity and value.  
🔵 As a customer, I want a dedicated vintage category so that I can easily browse rare items.  
🔵 As a customer, I want accurate stock availability so that I know when an item is truly one-of-a-kind.  
🔵 As a customer, I want advanced filtering (era, type, rarity) so that I can find specific collectibles.  

(authentication)  
🟢 As a user, I want to register an account so that I can access personalised features.  
🟢 As a user, I want to securely log in and log out so that my data is protected.  
🟢 As a user, I want role-based access (customer/admin) so that only authorised users can manage products and orders.  

(checkout and basket)  
🟢 As a user, I want to add and remove items from my basket so that I can control my purchase before checkout.  
🟢 As a user, I want cart updates to update immediately in the UI so that I always see accurate totals.  
🟡 As a user, I want a smooth checkout process so that I can complete purchases quickly.  
🟢 As a user, I want to pay securely using an integrated payment system so that I can trust the transaction.  
🟢 As a user, I want an order confirmation page so that I know my purchase was successful.  

(admin)  
🟢 As an admin, I want to create, update, and delete products so that I can manage the store catalogue.  
🟢 As an admin, I want to manage stock levels so that availability is always accurate.  
🟢 As an admin, I want to view and manage customer orders so that I can fulfil purchases efficiently.  
🟢 As an admin, I want to categorise products so that users can navigate the store easily.  

(general)  
🟢 As a user, I want the interface to be intuitive so that I can navigate without instructions.  
🟢 As a user, I want consistent layout and design across pages so that the experience feels professional.  
🟡 As a user, I want immediate feedback when I perform actions (add to cart, update quantity, delete item) so that I know the system has responded.  
🟡 As a user, I want error messages that are clear and helpful so that I can fix problems easily.  
🟢 As a user, I want accessibility support so that I can use the site regardless of ability.  

### Features  
When these are completed the main features the site will have will be:  
User Authentication & Roles - Register, Log in, Log out and role based access(customer/admin).  
Admin Product & Stock Management - Create/update/delete products, manage stock levels, categorise products.  
Product Browsing & Navigation - Products page and navigation present.  
Search & Filtering - Search bar and filtering using EAV.  
Product Detail Pages - Page for the details of the prdouct and a place for size/colour selection to take place.  
Homepage/Merchandising - Homepage section with best products.  
Basket Management - update or remove items in basket,  total updates.  
Checkout & Payments - Secure checkout page with robust process and checkout succcess oage.  
Order Management - Customer see past orders and manage orders in admin panel.  
Gift Shopping Experienece - gift card purchasing, search by occasion.  
Vintage Collector Experience - Vintage category, enhanced attributes.  
UX Quality & Accessibility - Intuitive interface, consistent design, action feedback, clear error messages, accessibility support.  


### DB Models
Given the type of products we stock at Reason an Entity-Attribute-Value was chosen here to allow the site admins alot of control over the categories of data attatched to the products without having to make migrations to the database. We have made some compromises and mitigations filtering through the Attribute Value Column can be lengthy as it is just one big long column so I have indexed it for faster queries. We also loose the native data type checking which may lead to bugs across the website like two cnaldes one having '40hrs' burntime while the other has 'fourty hours' or breaks in numerical logic. This is mitigated by adding a Value Type Field which will validate our input and, while being stored as a string will allow the admin to select a Data Type Label for each Attribute.

```
User Profile:  
    User(From Djangos User Model, OnetoOneField) 
    Name(CharField)
    Phone Number(CharField)  
    Address(CharfFeld)  
    Country(CountryField)

Product(EAV):   
    Category:    
        Category(CharField)   

    Product Type:  
        Category(fk)  
        name  
 
    Product:   
        Category(fk) 
        Sku(CharField)   
        Name(CharField)   
        Description(TextField)   
        Price(DecimalField)  
        Brand(CharField/Choices)   
        Rating(DecimalField)  
        ImageURL(URLField)  
        Image(ImageField)

    Attribute:
        "  
        ValueType(models.TextChoices):  
            TEXT = 'text', 'Text'  
            NUMBER = 'number', 'Number'  
            BOOLEAN = 'boolean', 'Boolean'  
        "
        Category(fk)  
        Attribute(CharField)  
        Value Type(choices=ValueType.choices, default='text') 

    Product Attribute Value:  
        Product(fk)  
        Attribute(fk)  
        Value(CharField, db_index=True) [db_index=True indexs the database for faster reads as this is going to be along column]  
        # Unique Together (Product, Attribute) [only one of each attribute:value pair is added to each product]  


Order:  
    Order Number(CharField)  
    User Profile(fk)  
    Name(CharField)   
    Email(CharField)  
    Phone Number(CharField)  
    Address(charField)  
    Country(CountryField)  
    Date(DateTimeField)  
    Delivery Cost(DecimalField)  
    Order Total(DecimalField)  
    Grand Total(DecimalField) [Order Total + Delivery]  
    Stripe PIID(CharField) [Stores the payment intent created by stripe]  

Order Line Item:  
    Order(fk)  
    Product(fk)
    Quantity(IntegerField)
    Line Item Total(DecimalField)

```  

#### Product Categories/Types
- Home Fragrence & Candles
  - Candles
  - Candle Holders
  - Diffusers
  - Wax Melts 

- Kitchen & Dining
  - Mugs 
  - Bowls
  - Tea Towels
  - Jugs

- Cards & Gift Wrap
  - Cards
  - Wrapping paper
  - Gift bags
  - Tape & Ribbon

- Home Decor
  - Photo Frames
  - Book Ends
  - baskets & Matts

- Soft Furnishings
  - Cushions
  - Throws 

- Perfume & Body
  - Perfume
  - Soap
  - Moisteriser


- Stationary
  - Notebooks
  - Journals 
  - Paper Weights


### Wireframes