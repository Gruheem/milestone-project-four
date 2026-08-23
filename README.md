# milestone-project-four

# E-Commerce Site for Reson Interiors

## Table of Contents
- [Purpose & Value Proposition](#purpose--value-proposition)
- [UX](#ux)
  - [Business Goals](#business-goals)
  - [User Personas](#user-personas)
  - [User Stories](#user-stories)
  - [Wireframes](#wireframes)
- [Features](#features)
- [Data Schema & Design Rationale](#data-schema--design-rationale)
  - [Database Models](#database-models)
- [Technologies & Key Technical Decisions](#technologies--key-technical-decisions)
  - [Technologies and Approaches Used](#technologies-and-approaches-used)
  - [Stripe/Checkout Flow](#stripecheckout-flow)
  - [Defensive Programming](#defensive-programming)
  - [APIs](#apis)
  - [Authentication (Django AllAuth)](#authentication-django-allauth)
  - [Stripe Integration Notes](#stripe-integration-notes)
- [Testing](#testing)
- [Bugs / Known Issues](#bugs--known-issues)
- [Deployment](#deployment)
- [Security](#security)
- [Credits & Attribution](#credits--attribution)
- [Appendix: Product Categories, Types & Attributes](#appendix-product-categories-types--attributes)

---

<!-- To do look at expanding this maybe-->

### Purpose/Project Goals
The goal of the project is to create a full-stack e-commerce django site comprised of multiple apps that include a well structured relational database, CRUD operations, authentication, authorisation, permission bondaries and a real e-commerce payment flow. The project will demonstrate excellent UX design, featuring a clean seperation of concerns with a well organised directory structure with reliably structured and accurately maintained content across all files, as well as robust and graceful error handling.

---

## UX

### Business Goals
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
🟢 [x] As a visitor, I want to browse products without needing to create an account so that I can explore the site freely.
🟢 [x] As a visitor, I want clear navigation menus and categories so that I can easily find products of interest.
🟢 [x] As a visitor, I want search and filtering tools so that I can refine product listings easily.
🟡 [ ] As a visitor, I want to see featured and best-selling products so that I can quickly understand what the store offers.
🟢 [x] As a visitor, I want the site to work well on mobile and desktop so that I can browse comfortably on any device.
🟢 [x] As a visitor, I want product pages to load quickly and display clear information so that I can make informed browsing decisions.

(from regular customer)
🟡 [x] As a customer, I want an “Order History” section so that I can view past purchases and track what I have already bought.
🟡 [x] As a customer, I want the checkout process to be fast and pre-filled with my saved details so that I can complete purchases efficiently.
🟢 [x] As a customer, I want my basket updates to appear instantly so that I always know what I am about to purchase.

(from gift giver)
🟡 [ ] As a customer, I want to browse products by occasion (e.g. birthdays, anniversaries) so that I can quickly find suitable gifts.
🟡 [ ] As a customer, I want a gift card option so that I can purchase flexible gifts when I am unsure what to buy.
🟢 [x] As a customer, I want filtering options such as price range and category so that I can stay within my budget.
🟢 [ ] As a customer, I want clear delivery information so that I can ensure gifts arrive on time.

(from vintage hunter)
🔵 [ ] As a customer, I want detailed product descriptions including condition and known history and high-quality images so that I can assess authenticity and value.
🔵 [ ] As a customer, I want a dedicated vintage category so that I can easily browse rare items.
🔵 [ ] As a customer, I want accurate stock availability so that I know when an item is truly one-of-a-kind.
🔵 [ ] As a customer, I want advanced filtering (era, type, rarity) so that I can find specific collectibles.

(authentication)
🟢 [x] As a user, I want to register an account so that I can access personalised features.
🟢 [x] As a user, I want to securely log in and log out so that my data is protected.
🟢 [x] As a user, I want role-based access (customer/admin) so that only authorised users can manage products and orders.

(checkout and basket)
🟢 [x] As a user, I want to add and remove items from my basket so that I can control my purchase before checkout.
🟢 [x] As a user, I want cart updates to update immediately in the UI so that I always see accurate totals.
🟡 [x] As a user, I want a smooth checkout process so that I can complete purchases quickly.
🟢 [x] As a user, I want to pay securely using an integrated payment system so that I can trust the transaction.
🟢 [x] As a user, I want an order confirmation page so that I know my purchase was successful.

(admin)
🟢 [x] As an admin, I want to create, update, and delete products so that I can manage the store catalogue.
🟢 [x] As an admin, I want to manage stock levels so that availability is always accurate.
🟢 [x] As an admin, I want to view and manage customer orders so that I can fulfil purchases efficiently.
🟢 [x] As an admin, I want to categorise products so that users can navigate the store easily.

(general)
🟢 [x] As a user, I want the interface to be intuitive so that I can navigate without instructions.
🟢 [x] As a user, I want consistent layout and design across pages so that the experience feels professional.
🟡 [x] As a user, I want immediate feedback when I perform actions (add to cart, update quantity, delete item) so that I know the system has responded.
🟡 [x] As a user, I want error messages that are clear and helpful so that I can fix problems easily.
🟢 [x] As a user, I want accessibility support so that I can use the site regardless of ability.

### Wireframes
<!-- To Do add wireframes -->

---

## Features
When these are completed the main features the site will have will be:
User Authentication & Roles - Register, Log in, Log out and role based access(customer/admin).
Admin Product & Stock Management - Create/update/delete products, manage stock levels, categorise products.
Product Browsing & Navigation - Products page and navigation present.
Search & Filtering - Search bar and filtering using EAV.
Product Detail Pages - Page for the details of the prdouct and a place for size/colour selection to take place.
Homepage/Merchandising - Homepage section with best products.
Basket Management - update or remove items in basket,  total updates.
Checkout & Payments - Secure checkout page with robust process and checkout succcess oage.
  - Loading wheel css loading wheel on redirect page
Order Management - Customer see past orders and manage orders in admin panel.
Gift Shopping Experienece - gift card purchasing, search by occasion.
Vintage Collector Experience - Vintage category, enhanced attributes.
UX Quality & Accessibility - Intuitive interface, consistent design, action feedback, clear error messages, accessibility support.

<!-- To do add screenshots -->

---

## Data Schema & Design Rationale

### EAV Model
Given the varied types of products we stock at Reason an Entity-Attribute-Value was chosen here to allow the site admins alot of control over the categories of data attatched to the products without having to make migrations to the database. We have made some compromises and mitigations filtering through the Attribute Value Column can be lengthy as it is just one big long column so I have indexed it for faster queries. We also loose the native data type checking which may lead to bugs across the website like two cnaldes one having '40hrs' burntime while the other has 'fourty hours' or breaks in numerical logic. This is mitigated by adding a Value Type Field which will validate our input and, while being stored as a string will allow the admin to select a Data Type Label for each Attribute.

Initial plan:
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

Fixtures were used to load starting data into the Category, ProductType, Attribute and AttributeValue Tables.

When it came to adding the products through the admin I realised I would neet an extra table to combine the product with its attributes and values so I created the ProductAttributeValue table.

For the filter I chose the approach of Using JavaScript to create url based on the filter lists state. The state is decided by which chekcboxes are ticked at any given moment. As I was creating the logic for the filter I realised I was going to need to give the Attribute and AttributeValue tables a slug in order to avoid any potential bugs. For example some of the values have the character '&' in them. I also chose to make the slug non-unique, this was because I wanted to create a page where you can filter through all the products in a category and be able to see all the products with the same scent/colour in the category, without having multiple of the same atttribute to tick multiple of the same value, temporarily parting them from their product type. Initialy I have chosen to develope a page reload rather than use AJAX API in order to keep the project more managable.

I am using PROTECT on Product.product_type so on delete the products linked to it won't all just get deleted if a product type were to be deleted by mistake.

The final Database Schema used for the project is as follows:  
[Database Schema](static/images/database-erd.webp)

---

## Technologies & Key Technical Decisions

### Django
Django was chosen as the framework to support the MVT architecture chosen for the project. Django's clearly seperated MVT architecture and appropriate functionality for an e-commerce website. The Built in security provides layers of protection and has a customisable admin section thatw orks very well.

### Approaches Used

EAV Model:  
Entity Attribute Value Style Schema
For creating dynamic filters and product listings.

Dispatch Table Pattern:  
Verify - Route - Handle
Approach used for recieving webhooks.

The checkout flow:  
capture info using our checkout form - validate it, to makesure its trustworthy before handing it to stripe - use it to start a checkout session, this renders the stripe payment widget - payment is made - meta data from the webhook we recieve back creates our order, this is most reliable way of knowing a successfulll payment has been made hearing from stripe rather than the users web browser - return to success/confirmation page.  

### Stripe/Checkout Flow

Used version Clover for a balance of being new and not be the newest to have more support. I chose to use Stripes newer checkout sessions feature as this is what thier documentation strongly recommends. Imbedding the checkout session so it uses Stripes payment element. This makes manualy handling payment intents and mounting unnecassery. Our order is then created by the webhook handler on recipt of the checkout.session.success webhook. Stripes payment element gives alot of user error feedback instantly before the return redirect, eliminating the need to create lots of different webhook error handlers. Aswell as my core checout.session.success I have chosen to build one to try and measure cart abandonment using checkout.session.expired. 

Stripe:  
https://docs.stripe.com/payments/accept-a-payment?payment-ui=checkout&ui=embedded-page&lang=python  
https://docs.stripe.com/api  

### Custom Filter
I made a cutom filter to safely retrieve a keys value from a dictionary as django templates don't allow normal Python dictionary look ups with a a variable key.

### Avoiding the 'n+1 probem'
he N+1 problem is a database performance problem that happens when you retrieve a collection of objects with one query, and then accidentally make an database query for each individual object in that collection. This happened in this project when it comes to fetching a list of attribute then fetching each set of values for each attribute. Prefetch here drasticaly cuts the number of queries on the database within our iteration nested inside another iteration while dynamically creating our product filters, from our attributes and values.

```python
attributes = Attribute.objects.filter(
    product_type__in=product_types,
    values__productattributevalue__product__in=products
).distinct().prefetch_related(
    Prefetch(
        'values',
        queryset=AttributeValue.objects.filter(
            productattributevalue__product__in=products
        ).distinct()
    )
)
```


### Shell 
I used the Python Shell for various operation and tests during the developement process. an example was when i added a slug field to my db models and used the shell to populate that slug field for al enties based fo the entries name.

I used it check the existance of database entries and the values of variables at different stages of different data flows.

### Authentication (Django AllAuth)

I used django-AllAuth for my authenitication as it bosts a suite of security features such as password hashing, csrf protection, email verification and reset password fetaures. Aswell as its own template system. The templates that were adapted for the project to use were:
- log_in
- log_out
- sign-up
- verification_sent
- verification_email_required  

---

## Testing
<!-- To do manual testing, colour testing, lighthouse testing-->

---

### Bugs / Known Issues

| # | Feature/Area | What was tested | Bug found | Fix |
|---|---|---|---|---|
| 1 | Product filter (checkboxes) | Ticking a filter checkbox where two different attributes shared the same value (e.g. two attributes both having a value of "15cm") | Template logic ticked both checkboxes since they shared the same value, and once ticked there was no way to untick just one — a page reload would re-tick the other | Paired attribute + value together as key:value pairs in a dictionary (rather than tracking values alone) using a custom template filter (`get_item`) to look them up in the template |
| 2 | Product filter ('id's) | generating the `<li>` dynamically leaves room for two list items to have the same 'id' attribute | This is semantically incorrect html and could cause bugs with JS and CSS element selectors | Attatched the attribute id to the attribute to create a unique identifier |
| 3 | Bag — remove item | Removing an item from the shopping bag session dict using its `item_id` | Silently failed — `if item_id in bag: bag.pop(item_id)` never matched because the bag dict stores keys as strings but the incoming `item_id` was an integer | Cast `item_id = str(item_id)` before comparing/popping |
| 4 | Checkout return / webhook race condition | Completing a Stripe payment and observing the return redirect | User could be redirected to the success page before the `checkout.session.completed` webhook had fired and created the Order, meaning the confirmation page had no order to display | Added a polling mechanism (`checkout_return.html` + `order_check.js` + `check_order` view) that checks every second for the order to exist by `stripe_pid`/`payment_intent`, then reloads the page once it's ready |
| 5 | Custom 404 page | Setting `DEBUG = False` locally to preview the styled custom 404 page | Static files stopped resolving entirely with `DEBUG = False`, so the custom 404 template couldn't be previewed in its styled form | Created a temporary view/URL/template in the `home` app (`test-404`) to preview and style the 404 page while `DEBUG = True`, then removed it once styling was confirmed |

### Manual Testing — Feature Checklist

| Feature | Steps | Expected result | Actual result | Pass/Fail |
|---|---|---|---|---|
| Add to bag | | | | |
| Adjust bag quantity | | | | |
| Remove from bag | | | | |
| Guest checkout (no account) | | | | |
| Checkout with saved profile info pre-filled | | | | |
| Stripe payment success | | | | |
| Stripe payment failure/decline | | | | |
| Order confirmation email received | | | | |
| Product filter by attribute | | | | |
| Product search | | | | |
| Product sort (price/rating/name) | | | | |
| Register / login / logout | | | | |
| Profile update (save delivery info) | | | | |
| Order history view | | | | |
| 404 page on invalid URL | | | | |
| Responsive layout — mobile nav, filters, bag table | | | | |


### Validator Testing
W3C HTML Validator - html files encountred some erros for the Django Template Language usedi n them. I am discounting these errors as they shouldnot be addressed. Pages that couldn't be validated as there was too much DTL were manualy reviewed.
| File | Result |
|---|---|
| base.html | Pass |
| main-nav.html | Pass |
| mobile_header | Pass |
| index.html | Pass |
| products.html | Pass |
| product_detail | Pass |
| bag.html | Manual Pass | - DTL Error to severe to process properly
| checkout.html | Pass |
| checkout_return.html | Pass |
| checkout_success.html | Manual Pass | - DTL Error to severe to process properly
| profile.html | Manual Pass | - DTL Error to severe to process properly


W3C CSS Validator - Errors were raised regarding the use of nested css how ever this is somehting i have chosen not to change right now. In future I could change that to ensue backwards compatibility.
| File | Result |
|---|---|
| base.css | Pass |
| products.css | Pass |
| checkout.css | Pass |


JSHint Validation - Errors were raised regarding some missing semi-colons. These have been addressed and rectified.
| File | Result |
|---|---|
| base.js | Pass |
| checkout.js | Pass |
| check_order.js | Pass |
| admin_attributes.js | Pass |
| filters.js | Pass |
| products.js | Pass |
| quantity_input_script | Pass |
| profile.js | Pass |

https://docs.astral.sh/ruff/
PEP8 adhereance testing with Ruff was carried out on all .py files. it raised some formatting errors which I have fixed, mostly wanting things to wrap after 79 chars for code and 72 chars for docstrings and comments. Ruff wanted me to hange all the `"` to `'` to fully pass the tests, this seemed like a long, drawn out and slightly unnecassery task so the agent in vs code completed this swap for me.  

All Python files acheieved PASS Status.


### Colour Testing


---
## Ligthouse Testing

---
## Deployment
<!-- To do -->

---

## Security

- There are no Scret keys in the settings on anywhere on GitHub they are safely stored as Environment Variables.
- DEBUG is False on the deployed app.
- Log in permissions are set so only a superuser can access the admin.  Log in requirements are set of profile pages to keep the views secured.
- Rate limiting to protect from brute force/DDOS attacks.
- Force HTTPS to keep the connection secure.
- .gitignore used to keep sensitive files local.

### Defensive Programming
<!-- to do redo -->
Perorming multiple checks to control button presses and inputs when submitting quantity changes for bag and button disabling on quantity select forms:

form validation before passing it to stripe checkout/views.py

checking if there is a bag before continuing with chekcout and throing an error if not.

creating final price to be charged from the bag_contents and product models, not reallying on the wat the users browser is telling us.

---

## Future Features and Developement
<!-- to do -->

---

## Credits & Attribution
<!-- To do -->

---

## Appendix: Product Categories, Types & Attributes

- Home Fragrence & Candles
  - Candles
    - Candle Type
    - Burn Time
    - Wax Type
    - Scent
    - Colour
    - Patterned
    - Height
    - Diameter
  - Candle Holders
   - Holds Candle Type
   - Height
   - Length
   - Material
  - Diffusers
   - Scent
   - Reeds Included
  - Wax Melts
   - Burn Time(hrs)
   - Scent
   - Wax Type

- Kitchen & Dining
  - Mugs
    - Colour
    - Capacity
    - Material
  - Bowls
    - Colour
    - Width
    - Material
  - Tea Towels
    - Colour
    - Patterned
    - Material
  - Jugs
    - Material
    - Volume

- Cards & Gift Wrap
  - Cards
   - Occasion
  - Wrapping paper
   - Format
  - Gift bags
   - Gift Bag
   - Bottle Bag
   - Size
  - Tape & Ribbon
   - Colour
   - Type

- Home Decor
  - Photo Frames
    - Size
    - Material
  - Book Ends
    - Height
    - Length
    - Depth
    - Material
  - baskets & Matts
    - Material
    - Length
    - Width

- Soft Furnishings
  - Cushions
    - Colour
    - Patterned
    - Material
    - Removable Cover
  - Throws
    - Colour
    - Patterned
    - Length(cm)
    - Width(cm)
    - Material
- Perfume & Body
  - Perfume
    - Scent
    - Volume
  - Soap
    - Scent
  - Moisteriser
    - Scent
    - Volume

- Stationary
  - Notebooks
    - Lined
    - Cover Type
    - Page count
  - Journals
    - Cover type
    - Page Count
  - Paper Weights

Candle Type:
- Tin
- Pot
- Tealight
- Dinner
- Taper

Burn Time:
- 2.5hrs
- 5hrs
- 10hrs
- 20hrs
- 30hrs
- 40hrs

Wax Type:
- Parafin
- Soy
- Beeswax
- Steerin

Scent:
- Bay & Rosemary
- Bergamot & Nettle
- Embers
- Fig
- Geranium Leaf
- Granite & Moss
- Grapefruit & Lime
- Inspiritus
- Moss
- Orange & Cinnamon
- Orange Blossom
- Potager
- Sandalwood
- Sandalwood & Cedar
- Sea Garden
- Sea Moss & Driftwood
- Sea Salt
- Sweet Pea
- Thyme & Mint
- Tranquillity
- Vintage Rose
- Walled Garden
- Wild Gorse
- Wild Rhubarb
- Winter Thyme

Colour:
- White
- Ivory
- Cream
- Natural
- Beige
- Taupe
- Grey
- Black
- Brown
- Gold
- Silver
- Copper
- Yellow
- Orange
- Terracotta
- Red
- Burgundy
- Pink
- Blush Pink
- Purple
- Lavender
- Blue
- Navy
- Teal
- Green
- Sage Green
- Olive Green
- Forest Green

Patterned:
(True / False)

Height:
- 10cm
- 15cm
- 20cm
- 25cm
- 30cm

Diameter:
- 1cm
- 2cm
- 3cm
- 4cm
- 5cm
- 10cm
- 15cm
- 20cm

Holds Candle Type:
- Dinner Candle
- Taper Candle
- Pillar Candle

Length:
- 5cm
- 10cm
- 20cm
- 30cm
- 50cm
- 100cm
- 150cm
- 200cm
- 250cm

Material:
- Glass
- Ceramic
- Brass
- Mixed Metal
- Porcelaine
- Stonewear

Reeds Included:
(True / False)

Capacity:
- 100ml
- 200ml
- 300ml
- 400ml
- 500ml

Width:
- 5cm
- 10cm
- 15cm
- 20cm
- 30cm
- 40cm
- 50cm

Volume:
- 50ml
- 100ml
- 150ml
- 200ml
- 300ml
- 400ml
- 500ml
- 750ml
- 1000ml

Occasion:
- Birthday
- Wedding
- Thankyou
- Congratulations
- New Home
- New Baby
- Sympathy

Format:
- Wrap Sheet
- Roll
- Tissue Paper

Bag Type:
- Gift Bag
- Bottle Bag

Size:
- Small
- Medium
- Large

Type:
- Tape
- Ribbon

Depth:
- 5cm
- 10cm
- 15cm
- 20cm
- 30cm
- 40cm
- 50cm

Removable Cover:
(True / False)

Lined:
(True / False)

Cover Type:
- Soft Back
- Hard Back

Page Count:
- 30
- 50
- 100
- 150
- 200