# Milestone Project 4: E-Commerce Site for Reason Interiors
[Live Site](https://reason-interiors-157a3dc5010c.herokuapp.com/)

[GitHub Repository](https://github.com/Gruheem/milestone-project-four)

## Table of Contents

- [Purpose/Project Goals](#purposeproject-goals)
- [UX](#ux)
  - [Business Goals](#business-goals)
  - [User Personas](#user-personas)
  - [User Stories](#user-stories)
  - [Wireframes](#wireframes)
  - [Style Choices](#style-choices)
- [Features](#features)
  - [Homepage/Merchandising](#homepagemerchandising)
  - [User Authentication & Roles](#user-authentication--roles)
  - [Admin Product & Stock Management](#admin-product--stock-management)
  - [Product Browsing & Navigation](#product-browsing--navigation)
  - [Search & Filtering](#search--filtering)
  - [Product Detail Pages](#product-detail-pages)
  - [Basket Management](#basket-management)
  - [Checkout & Payments](#checkout--payments)
  - [Order Management](#order-management)
  - [UX Quality & Accessibility](#ux-quality--accessibility)
- [Data Schema & Design Rationale](#data-schema--design-rationale)
  - [EAV Model](#eav-model)
- [Technologies & Technical Decisions](#technologies--technical-decisions)
  - [Django](#django)
  - [BootStrap](#bootstrap)
  - [Approaches Used](#approaches-used)
  - [Stripe/Checkout Flow](#stripecheckout-flow)
  - [Custom Filter](#custom-filter)
  - [Avoiding the 'n+1 probem'](#avoiding-the-n1-probem)
  - [Shell](#shell)
  - [Authentication (Django AllAuth)](#authentication-django-allauth)
  - [Defensive Programming](#defensive-programming)
- [Testing](#testing)
  - [Bugs Encounters & resolutions](#bugs-encounters--resolutions)
  - [Manual Testing](#manual-testing)
  - [Validator Testing](#validator-testing)
  - [Colour Testing](#colour-testing)
  - [Lighthouse Testing](#ligthouse-testing)
  - [User Story Testing](#user-story-testing)
- [Security](#security)
- [Deployment](#deployment)
- [Future Features and Development](#future-features-and-developement)
- [Credits & Attribution](#credits--attribution)
- [Appendix: Categories, Product Types & Attributes](#appendix-categories-product-types--attributes)


## Purpose/Project Goals
The goal of the project is to create a full-stack e-commerce django site comprised of multiple apps that include a well structured relational database, CRUD operations, authentication, authorisation, permission bondaries and a real e-commerce payment flow. The project will demonstrate excellent UX design, featuring a clean seperation of concerns with a well organised directory structure with reliably structured and accurately maintained content across all files, as well as robust and graceful error handling.

Its purpose is to increase the value of the business through increasing sales by reaching a larger audience and new markets.


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
🟢 As a user, I want to pay securely using an integrated payment system so that I can trust the  transaction.  
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

### Wireframes
Wire frames were made using paint, I chose this software because its familiarity eliminated technical friction, letting me focus straight away on the creative process. Here are the wireframes I made for the project: 

**Home Page**:  
<img src="static/images/d-home.png" width="300" alt="Desktop home page wireframe">
<img src="static/images/m-home.png" width="300" alt="Mobile home page wireframe">

**Products**:  
<img src="static/images/d-products.png" width="300" alt="Desktop products page wireframe">
<img src="static/images/m-products.png" width="300" alt="Mobile products page wireframe">

**Product Detail**:  
<img src="static/images/d-product-detail.png" width="300" alt="Desktop product detail page wireframe">
<img src="static/images/m-product-detail.png" width="300" alt="Mobile product detail page wireframe">

**Bag**:   
<img src="static/images/d-bag.png" width="300" alt="Desktop shopping bag page wireframe">
<img src="static/images/m-bag.png" width="300" alt="Mobile shopping bag page wireframe">

**Checkout**:  
<img src="static/images/d-checkout.png" width="300" alt="Desktop checkout page wireframe">
<img src="static/images/m-checkout.png" width="300" alt="Mobile checkout page wireframe">

**Profile**:  
<img src="static/images/d-profile.png" width="300" alt="Desktop user profile page wireframe">
<img src="static/images/m-profile.png" width="300" alt="Mobile user profile page wireframe">



### Style Choices
I have kept the colour palette small in order to create a strong sense of the brand and really trying to keep the design decisions quantafiably justifiable.  

This is the pallette I chose:  

<img src="static/images/colour-pallette.png">  
  
`#FFFFFF` - This was chosen as the background to the product cards and toasts to make them stand out from the page.  
`#FCFCFC` - This was chosen as the background colour as pain white was too harsh.  
`D0D0DC` - This was chosen as a colour for the disabled buttons in the project. A faded colour but one that still meets accessibility standards.  
`#757575` - This was chosen as a placeholder. I wanted something that was noticably lighter than the text inkeeping with convention but still meets accessibility standards.  
`#18221F` - This was chosen as the text colour. It is softer than pure black and has a slight green tint to it to make it feel cohesive with the hero colour.  
`#02271B` - This is the companies hero colour, used for brand recognition. We also want to introduce colour as we do not want a monochrome site as this would feel too cold.


## Features

### Homepage/Merchandising 
Homepage section with welcome:  
<img src="static/images/hero.png" width="450" alt="Homepage hero section">
<img src="static/images/welcome.png" width="450" alt="Homepage welcome section">
<img src="static/images/cateories-shop.png" width="450" alt="Homepage shop categories section">
<img src="static/images/testimonies.png" width="450" alt="Homepage customer testimonials section">
<img src="static/images/google-maps.png" width="450" alt="Homepage Google Maps location section">
<img src="static/images/footer.png" width="450" alt="Homepage footer section"> 
  
### User Authentication & Roles 
Register, Log in, Log out and role based access(customer/admin):  

<img src="static/images/sign-in.png" width="450" alt="User sign-in page">
<img src="static/images/sign-out.png" width="450" alt="User sign-out confirmation">
<img src="static/images/register.png" width="450" alt="User registration page">


### Admin Product & Stock Management 
Create/update/delete products, manage stock levels, categorise products:  

<img src="static/images/admin-pannel.png" width="450" alt="Admin panel dashboard">
<img src="static/images/admin-products-one.png" width="450" alt="Admin product management page">
 
I have made it so that when you are on a the add a product page that when you select is product type all existing attributes populate the form with dropdown for you to pick from the existing values. From here you can also create new Attributes and Values to fit the product the user is adding. Adding these attribute and values here is what creates the search filter on theproducts page.  

<img src="static/images/admin-products-two.png" width="450" alt="Admin product attributes and values form">
 

### Product Browsing & Navigation 
Products page and navigation present:   

Navigation:  
<img src="static/images/nav-one.png" width="400" alt="Main navigation menu">
<img src="static/images/nav-two.png" width="400" alt="Expanded product navigation menu">
<img src="static/images/nav-three.png" width="400" alt="Product category navigation menu">
Navigation result:  
<img src="static/images/products.png" width="400" alt="Products page displaying filtered product results"> 


### Search & Filtering
Search bar and filtering using EAV:  
The search bar is a drop down revealed once the icon is clcicked and activated when clicked again. There is feedback for an empty search prompting users to try again.  
<img src="static/images/search-icon.png" width="400" alt="Search icon in the navigation bar">
<img src="static/images/search-bar.png" width="400" alt="Expanded search bar">

The filter is dynamically generated from my EAV Model to suit the varied nature of them items in stock.
<img src="static/images/filter.png" width="400" alt="Dynamically generated product filters">  
  
### Product Detail Pages 
Page for the details of the prdouct and a place for size/colour selection to take place:  
<img src="static/images/product-detail.png" width="400" alt="Product detail page with product information and options">

### Basket Management 
Update or remove items in basket, total updates:  
<img src="static/images/bag-one.png" width="400" alt="Shopping bag displaying selected products">
<img src="static/images/bag-two.png" width="400" alt="Shopping bag with updated product quantity and total"> 

### Checkout & Payments 
Secure checkout page with robust process and checkout succcess page:  
<img src="static/images/checkout.png" width="400" alt="Checkout page with customer and payment details">
<img src="static/images/checkout-return.png" width="400" alt="Checkout return page">
<img src="static/images/checkout-success.png" width="400" alt="Successful checkout confirmation page"> 
    
### Order Management 
Customer see past orders and manage orders in admin panel:  
<img src="static/images/order-admin.png" width="400" alt="Admin order management page">
<img src="static/images/profile.png" width="400" alt="Customer profile displaying previous orders"> 

### UX Quality & Accessibility 
Intuitive interface, consistent design, action feedback, clear error messages, accessibility support.   
Toasts happen at every point an action is taken here are examples of a success toast and an info toast.  
<img src="static/images/success-toast.png" width="400" alt="Success toast notification confirming a completed action">
<img src="static/images/info-toast.png" width="400" alt="Information toast notification providing user feedback">  


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

I have also Created a table for the UserProfile which will be linked to the django user table and utalised for saving inforamtion and tracking order history.   

The final Database Schema used for the project is as follows:  

<img src="static/images/database-erd.webp">


## Technologies & Technical Decisions

### Django  
Django was chosen as the framework to support the MVT architecture chosen for the project. Django's clearly seperated MVT architecture and appropriate functionality for an e-commerce website. The Built in security provides layers of protection and has a customisable admin section that works very well.  

### BootStrap  
BootStrap 5.3 was used for creating this project  

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
I used the Python Shell for various operation and tests during the development process. An example was when I added a slug field to my db models and used the shell to populate that slug field for al enties based fo the entries name.

I used it check the existance of database entries and the values of variables at different stages of different data flows.

### Authentication (Django AllAuth)

I used django-AllAuth for my authenitication as it has some good security features such as password hashing, csrf protection, email verification and reset password fetaures. Aswell as its own template system. The templates that were adapted for the project to use were:
- log_in
- log_out
- sign-up
- verification_sent
- verification_email_required  

### Defensive Programming  

Defensive programming is an approach to development that anticipates unexpected, invalid, or potentially manipulated input and adds checks to prevent it from causing errors or compromising the application.  

In this project, defensive programming is used in several areas:

- Performing multiple checks to control button presses and user inputs when submitting quantity changes to the bag, including disabling buttons where appropriate and validating quantity selections. 
- Validating forms before passing the data to the Stripe checkout view.
- Checking that a bag exists and contains items before allowing the user to proceed to checkout, returning an appropriate error if it does not.
- Calculating the final price to be charged from the bag_contents and product data stored on the server, rather than relying on prices or values supplied by the user's browser.
- Using server-side validation to ensure that submitted data is valid and cannot be manipulated to bypass checkout rules.


## Testing


### Bugs Encounters & resolutions

| # | Feature/Area | What was tested | Bug found | Fix |
|---|---|---|---|---|
| 1 | Product filter (checkboxes) | Ticking a filter checkbox where two different attributes shared the same value (e.g. two attributes both having a value of "15cm") | Template logic ticked both checkboxes since they shared the same value, and once ticked there was no way to untick just one — a page reload would re-tick the other | Paired attribute + value together as key:value pairs in a dictionary (rather than tracking values alone) using a custom template filter (`get_item`) to look them up in the template |
| 2 | Product filter ('id's) | generating the `<li>` dynamically leaves room for two list items to have the same 'id' attribute | This is semantically incorrect html and could cause bugs with JS and CSS element selectors | Attatched the attribute id to the attribute to create a unique identifier |
| 3 | Bag — remove item | Removing an item from the shopping bag session dict using its `item_id` | Silently failed — `if item_id in bag: bag.pop(item_id)` never matched because the bag dict stores keys as strings but the incoming `item_id` was an integer | Cast `item_id = str(item_id)` before comparing/popping |
| 4 | Checkout return / webhook race condition | Completing a Stripe payment and observing the return redirect | User could be redirected to the success page before the `checkout.session.completed` webhook had fired and created the Order, meaning the confirmation page had no order to display | Added a polling mechanism (`checkout_return.html` + `order_check.js` + `check_order` view) that checks every second for the order to exist by `stripe_pid`/`payment_intent`, then reloads the page once it's ready |
| 5 | Custom 404 page | Setting `DEBUG = False` locally to preview the styled custom 404 page | Static files stopped resolving entirely with `DEBUG = False`, so the custom 404 template couldn't be previewed in its styled form | Created a temporary view/URL/template in the `home` app (`test-404`) to preview and style the 404 page while `DEBUG = True`, then removed it once styling was confirmed |


### Manual Testing

| Feature | Steps | Expected result | Actual result | Pass/Fail |
|---|---|---|---|---|
| Add to bag | 1. Navigate to a product detail page. 2. Adjust quantity using +/- buttons. 3. Click "Add to Bag" | Product is added to bag with correct quantity, success toast displays with product image, name, qty, running bag total, and free delivery message if under threshold | As expected | Pass |
| Adjust bag quantity | 1. Go to Bag page. 2. Click + or - buttons on an item's quantity input | Quantity updates and form auto-submits, bag total and subtotal update, buttons disable correctly at 1 and 99 | As expected | Pass |
| Remove from bag | 1. On Bag page, click "Remove" link next to an item | Item is removed from bag, page redirects back to bag view, success toast confirms removal, totals update | As expected | Pass |
| Guest checkout (no account) | 1. Add items to bag while not logged in. 2. Go to Checkout. 3. Fill in delivery/payment details manually (no pre-fill, no save-info checkbox shown). 4. Complete Stripe payment | Order form is blank, "Create an account or login to save this information" message shown instead of save-info checkbox, order is still created successfully via webhook | As expected | Pass |
| Checkout with saved profile info pre-filled | 1. Log in as a user with saved profile defaults. 2. Go to Checkout | All fields except full name populate correctly from `UserProfile` defaults, "Save this delivery information to my profile" checkbox is checked by default | As expected | Pass |
| Stripe payment success | 1. Complete checkout with Stripe test card. 2. Wait on `checkout_return` polling page | `checkout.session.completed` webhook fires, order is created in DB linked to bag/profile metadata, polling detects the order and reloads to `checkout_success.html` showing order number, items, and shipping address | As expected | Pass |
| Stripe payment failure/decline | 1. Complete checkout with a Stripe test decline card | Stripe's embedded Payment Element surfaces the decline error inline before redirect, no order is created since `checkout.session.completed` never fires for a failed payment | As expected | Pass |
| Order confirmation email received | 1. Complete a successful test payment | `_send_confirmation_email` fires from the webhook handler with order number, date, totals, and delivery address | As expected | Pass |
| Product filter by attribute | 1. Go to Products page filtered by a product type. 2. Tick attribute checkboxes in the filter panel | URL updates with `product_types` and attribute slug/value query params preserved, only matching products display, filter checkboxes remain ticked on reload | As expected | Pass |
| Product search | 1. Use the search bar in the desktop header and or mobile dropdown. 2. Enter a search term matching a product name or description | Products matching `product_name` or `description` are returned, empty search shows an error message and redirects back to the home page | As expected | Pass |
| Product sort | 1. On Products page, select each sort option from the dropdown | Product list re-orders correctly for each option, name sort ignores case via `Lower()` annotation, "Sort by..." reset option clears sort/direction params from URL | As expected | Pass |
| Register / login / logout | 1. Register a new account via signup form. 2. Confirm email if required. 3. Log out. 4. Log back in with credentials | Account created via allauth, `UserProfile` auto-created, login/logout succeed with appropriate success messages, user redirected  | As expected | Pass |
| Profile update | 1. Log in. 2. Go to Profile page. 3. Update delivery fields. 4. Submit form | `UserProfileForm` validates and saves, success message "Profile updated successfully" displays, updated values persist and pre-fill on the checkout page  | As expected | Pass |
| Order history view | 1. Log in as a user with past orders. 2. Go to Profile page. 3. Click an order number in the order history table | Order history table lists order number, date, line items, and grand total, clicking order number navigates to `order_history` view rendering `checkout_success.html` with an info message noting it's a past confirmation | As expected | Pass |
| 404 page on invalid URL | 1. Navigate to a non-existent URL | Custom 404 page renders with site header/footer, 404 message, Home and Back buttons | As expected | Pass |
| Responsive layout — mobile nav, filters, bag table | 1. View site at mobile breakpoint. 2. Open hamburger nav menu. 3. Open product filters via filter button. 4. View bag page | Mobile nav toggles via Bootstrap collapse, mobile header/search/icons display in place of desktop header row, filter panel toggles visibility below `lg` breakpoint via `filter-button` click, bag switches from table layout to stacked card layout on mobile | As expected | Pass |


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

### User Story Testing
Testing reveals all but 6 user stories passed their tests and this creates the foundation for our next steps of developement.  

'x' = Pass, '-' = Fail

(from casual browser)  
🟢 [x] As a visitor, I want to browse products without needing to create an account so that I can explore the site freely.  
🟢 [x] As a visitor, I want clear navigation menus and categories so that I can easily find products of interest.  
🟢 [x] As a visitor, I want search and filtering tools so that I can refine product listings easily.  
🟡 [-] As a visitor, I want to see featured and best-selling products so that I can quickly understand what the store offers.  
🟢 [x] As a visitor, I want the site to work well on mobile and desktop so that I can browse comfortably on any device.  
🟢 [x] As a visitor, I want product pages to load quickly and display clear information so that I can make informed browsing decisions.  

(from regular customer)  
🟡 [x] As a customer, I want an “Order History” section so that I can view past purchases and track what I have already bought.  
🟡 [x] As a customer, I want the checkout process to be fast and pre-filled with my saved details so that I can complete purchases efficiently.  
🟢 [x] As a customer, I want my basket updates to appear instantly so that I always know what I am about to purchase.  
  
(from gift giver)  
🟡 [-] As a customer, I want to browse products by occasion (e.g. birthdays, anniversaries) so that I can quickly find suitable gifts.  
🟡 [-] As a customer, I want a gift card option so that I can purchase flexible gifts when I am unsure what to buy.  
🟢 [x] As a customer, I want filtering options such as price range and category so that I can stay within my budget.  
🟢 [x] As a customer, I want clear delivery information so that I can ensure gifts arrive on time.  
  
(from vintage hunter)  
🔵 [-] As a customer, I want detailed product descriptions including condition and known history and high-quality images so that I can assess authenticity and value.  
🔵 [-] As a customer, I want a dedicated vintage category so that I can easily browse rare items.  
🔵 [-] As a customer, I want accurate stock availability so that I know when an item is truly one-of-a-kind.  
🔵 [-] As a customer, I want advanced filtering (era, type, rarity) so that I can find specific collectibles.  

(authentication)  
🟢 [x] As a user, I want to register an account so that I can access personalised features.  
🟢 [x] As a user, I want to securely log in and log out so that my data is protected.  
🟢 [x] As a user, I want role-based access (customer/admin) so that only authorised users can manage products and orders.  

(checkout and basket)  
🟢 [x] As a user, I want to add and remove items from my basket so that I can control my purchase before checkout.  
🟢 [x] As a user, I want cart updates to update immediately in the UI so that I always see accurate totals.  
🟡 [x] As a user, I want a smooth checkout process so that I can complete purchases quickly.  
🟢 [x] As a user, I want to pay securely using an integrated payment system so that I can trust the  transaction.  
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


### Colour Testing

[EightShapes]() Contrast Checker  
  
<img src="static/images/contrast-grid.png" width="500" alt="Colour Contrast Grid">   
  
Colour testing has pass WCEG standards for Text Readability Contrast 

## Lighthouse Testing

Initial Testing:  

<img src="static/images/lighthouse-one.png" width="300">  

Some improvements wera able to be made through image loading priority adjustments. A LCP issue was identified but not fully resolved within the project timeframe. Further optimisation would focus on getting the load time down through image optimisation and other exploration.

<img src="static/images/lighthouse-two.png" width="300">  

## Security

- There are no Scret keys in the settings on anywhere on GitHub they are safely stored as Environment Variables.
- DEBUG is False on the deployed app.
- Log in permissions are set so only a superuser can access the admin.  Log in requirements are set of profile pages to keep the views secured.
- Force HTTPS to keep the connection secure in settings.py.
- .gitignore used to keep sensitive files local.
- Rate Limiting used on certain views add to bag for bots scraping inventory levels, log in/ registration to try to help against brute force attacks and on checkout creation to limit testing stolen cards.



## Deployment
Steps taken to deploy:
Live deployment -  
- Prepare settings.py for production deployment
  - DEBUG > False
  - Removing Secret Keys
- Create Procfile
- Add gunicorn
- Push deployment-ready commit to GitHub
- Make a json back up of our database to be used as a fixture to upload our data
- Create the PostgreSQL database, configure the deployed application to use it, and run Django migrations to create the required database tables- load the json file into the database
- Create a Heroku app
- Set Environment Variables in Heroku Settings
- Link to GitHub
- Deploy app from main branch
- Create an S3 AWS Bucket to serve the static files with a group and a user 
- Assign the correct Bucket policy and user permissions
- Get secrets from stripe and put them in the stripe config
- Update Environment Variables

Local deployment -  
To run this project locally, make sure you have your virtual environment activated and the correct version of Python running. Then install dependencies using requirements.txt (`pip3 install -r requirements.txt`). After this has successfully completed, run `python3 manage.py runserver` in the terminal. Hold Control/Command and click on the link created to launch the app in your default browser.

## Future Features and Development  

Features to complete our user stories would be:  
Gift Shopping Experienece - gift card purchasing, search by occasion. 
Vintage Collector Experience - Vintage category, enhanced attributes.  

I was quite ambitious with the scope of the project and one or two things didn't quite make intot the final submission. Once I could see their complexity they were decided to be left out like the sort by occaision and gift card sale of different amounts.

The next steps for the project would be to comlete these outstanding user stories section and I would very much like to add a best sellers/what 'in' at the moment section on the homepage. I woukd also add a fully custom page outside of the admin to add/edit/delete products mirroring logic from the products admin.  

Optimization is something I would have liked to have spent more time on and making some automated tests for the payment taking part of the site.

Something else I would do is to make a suite of automated tesitng than ran regularly and informed me with an alert if any feature on the site wsn't working.


## Credits & Attribution
There are some code attributions that need to be made:

The loading wheel(css spinner) on the checkout_return.html page was found on https://cssloaders.github.io/

The loading spinner as you press the confirm pament button wwas adapted from [The Code Institute](https://lms.codeinstitute.net/).

admin_attributes.js is not original code. It was generated by an LLM(claude).

The Boutique Ado tutorial informed the work flow of the project but as it was writtena few years ago now several things had changed and updated making the code substantially different in most areas e.g. checkout flow, db schemas.

design inspiration was taken from other similar shops such as [domestic science](https://domesticsciencehome.co.uk/?srsltid=AfmBOorxd7XfITr37hcJsb-h9dYANKWNgiltKruAirGYriprLu5WadEv) and [mon pote](https://monpote.co.uk/).

## Appendix: Categories, Product Types & Attributes

[Initial Categories, Product Types & Attributes](appendix.txt)