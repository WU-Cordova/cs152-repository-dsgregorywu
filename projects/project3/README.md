This is my Bearcat Bistro Project!
Some Data Structure choices I made:
- For menus, I used a series of lists and dictionaries with prices on them. I used these because it was a good way of being able to easily access and iterate through each menu while also having a designated price. A linkedlist might've been better for complexity since I'm not ever changing the size of these menus, but linkedlists don't interact as well with dictionaries.
- For Customer Orders, I made a class with a bunch of properties that vary between tracking what the customer wants in their order, to the price, to the customer name, and lots more. This was helpful because it let me treat each class as an object that I am able to access from wherever in my program. This was the only data structure that I felt would be good, as nothing else allows me to store as many variables within it.
- For the Orders Queue, I used a Deque. I chose this because it allowed me to track which orders came when. It was either this or the original Queue, and I figured I would rather have the option of adding things to the front of the queue (which I haven't implemented, but definitely could be useful in a "Rush Order" feature) than the ability to wrap around from the Circular Queue.
- For Completed Orders, I used another Deque for very similar reasons. What was frustrating about using the Deque was that they are not iterable, so I had to do a pretty large workaround for a few of my main functions, but it ended up working pretty well.
- For building drinks, I used a ListStack. This was incredibly useful, as it allowed me to add in a "Back" feature for my custom drink ordering. I could've used something like a circularqueue for this, but I thought that using a stack would allow me for better, quick access to what pages. It also is better for complexity!

- Running the program: Right now, you need to log in as an employee with a password (I only have myself lol). You are then prompted to a home screen, where you can view each section of the ginormous bistro menu, place a new order, view open orders, close an order, view daily reports, or exit the program. The navigation of this is pretty easy, type in whatever you are prompted to. When ordering drinks or snacks, you can use B for back, or Q to quit. 

- If I had more time to work on this, I would likely implement a Rush Order system, as well as time based automatic order preparation. I also would like to split this up into a few different files, but I tried and it didn't work. Hopefully by May this will be fixed!! I also would fix a bunch of formatting things, just to make the text read back more like a coffee shop. Unfortunately this is WAY more trouble than what its worth, so I'm just gonna let it be.

Here's the output of one run through the simulator!

Welcome, Bearcat Bistro Employee! Please Enter Your Username: Derec
Please enter your password: CS152
Welcome to the Bearcat Bistro, Derec!
    
1. Display Menu
2. Take New Order
3. View Open Orders
4. Mark Order as Complete
5. View End of Day Report
6. Exit
    
Please select an option. 1
Menus: 1: Add Ons, 2: Bases, 3: Drip Options, 4: Espresso Drinks, 5: Fruity Flavors, 6: Milks, 7: Non Coffee, 8: Savory Flavors, 9: Snacks, 10: Teas, 11: Sizes, 12: Temperatures
Which Menu would you like to view? [B]ack to options, [Q]uit: 5
   
Fruity Flavors
  - Blackberry
  - Blueberry
  - Blue Raspberry
  - Grape
  - Grapefruit
  - Lavender
  - Lime
  - Mango
  - Passionfruit
  - Peach
  - Pear
  - Pomegranate
  - Pineapple
  - Raspberry
  - Strawberry
  - Watermelon

Menus: 1: Add Ons, 2: Bases, 3: Drip Options, 4: Espresso Drinks, 5: Fruity Flavors, 6: Milks, 7: Non Coffee, 8: Savory Flavors, 9: Snacks, 10: Teas, 11: Sizes, 12: Temperatures
Which Menu would you like to view? [B]ack to options, [Q]uit: 2
   
Bases
  - Drip
  - Espresso
  - Lemonade
  - Redbull
  - Tea

Menus: 1: Add Ons, 2: Bases, 3: Drip Options, 4: Espresso Drinks, 5: Fruity Flavors, 6: Milks, 7: Non Coffee, 8: Savory Flavors, 9: Snacks, 10: Teas, 11: Sizes, 12: Temperatures
Which Menu would you like to view? [B]ack to options, [Q]uit: b
   
Going back to the previous menu.
Welcome to the Bearcat Bistro, Derec!
    
1. Display Menu
2. Take New Order
3. View Open Orders
4. Mark Order as Complete
5. View End of Day Report
6. Exit
    
Please select an option. 2
 
What name would you like to use for your order? Derec
 
Would you like a (D)rink or (S)nack? D
    
Bases
  1. Drip
  2. Espresso
  3. Lemonade
  4. Redbull
  5. Tea

Please select a base. 4
You chose: Redbull
 
Fruity Flavors
  1. Blackberry
  2. Blueberry
  3. Blue Raspberry
  4. Grape
  5. Grapefruit
  6. Lavender
  7. Lime
  8. Mango
  9. Passionfruit
  10. Peach
  11. Pear
  12. Pomegranate
  13. Pineapple
  14. Raspberry
  15. Strawberry
  16. Watermelon

Which flavor would you like? 15
You chose Strawberry.
  
Would you like to add another flavor? Y
Fruity Flavors
  1. Blackberry
  2. Blueberry
  3. Blue Raspberry
  4. Grape
  5. Grapefruit
  6. Lavender
  7. Lime
  8. Mango
  9. Passionfruit
  10. Peach
  11. Pear
  12. Pomegranate
  13. Pineapple
  14. Raspberry
  15. Strawberry
  16. Watermelon

Which flavor would you like? 11
You chose Pear.
  
Would you like to add another flavor? N
Add Ons
  1. Cold Foam
  2. Espresso Shot
  3. Whipped Cream

Would you like an Add On? Press N for None. b
Removing last fruity flavor choice: Pear
Fruity Flavors
  1. Blackberry
  2. Blueberry
  3. Blue Raspberry
  4. Grape
  5. Grapefruit
  6. Lavender
  7. Lime
  8. Mango
  9. Passionfruit
  10. Peach
  11. Pear
  12. Pomegranate
  13. Pineapple
  14. Raspberry
  15. Strawberry
  16. Watermelon

Which flavor would you like? 8
You chose Mango.
  
Would you like to add another flavor? N
Add Ons
  1. Cold Foam
  2. Espresso Shot
  3. Whipped Cream

Would you like an Add On? Press N for None. 3
You chose Whipped Cream.
Would you like to add another Add On? N
 
Sizes
  1. Small
  2. Medium
  3. Large

What size would you like? 2
You chose Medium
 
Your drink: Medium Strawberry, Mango Redbull with Whipped Cream
Would you like to add this to your order? (Y)es or (N)o? Y
 
Item added to your order!
Order for Derec: Medium Strawberry, Mango Redbull with Whipped Cream
   
Would you like a (D)rink, a (S)nack, or to (C)omplete your order? s
    
Available Snacks:
1. Bagel
2. Chocolate Chip Cookie
3. Curry Pocket
4. Sugar Cookie
5. Quesadilla
6. Pizza
   
Please select a snack by number, or choose (B)ack or (Q)uit: 4
You chose: Sugar Cookie
Would you like to add Sugar Cookie to your order? (Y)es or (N)o? Y
Order for Derec: Medium Strawberry, Mango Redbull with Whipped Cream, Sugar Cookie
   
Would you like a (D)rink, a (S)nack, or to (C)omplete your order? C
    
Order for Derec Confimed! Your Reciept:
Medium Strawberry, Mango Redbull with Whipped Cream
Sugar Cookie
You Paid: $8.25
Your Barista: Derec
 
Welcome to the Bearcat Bistro, Derec!
    
1. Display Menu
2. Take New Order
3. View Open Orders
4. Mark Order as Complete
5. View End of Day Report
6. Exit
    
Please select an option. 2
 
What name would you like to use for your order? Joe
 
Would you like a (D)rink or (S)nack? D
    
Bases
  1. Drip
  2. Espresso
  3. Lemonade
  4. Redbull
  5. Tea

Please select a base. 5
You chose: Tea
 
Teas
  1. Chai
  2. Chamomile
  3. Darjeeling
  4. Earl Grey
  5. Jasmine
  6. Lemongrass
  7. Matcha
  8. Oolong
  9. Rooibos

Which tea would you like? 4
You chose Earl Grey.
   
Add Ons
  1. Cold Foam
  2. Espresso Shot
  3. Whipped Cream

Would you like an Add On? Press N for None. N
No Add Ons selected.
 
Sizes
  1. Small
  2. Medium
  3. Large

What size would you like? 2
You chose Medium
 
Your drink: Medium Earl Grey Tea
Would you like to add this to your order? (Y)es or (N)o? Y
 
Item added to your order!
Order for Joe: Medium Earl Grey Tea
   
Would you like a (D)rink, a (S)nack, or to (C)omplete your order? C
    
Order for Joe Confimed! Your Reciept:
Medium Earl Grey Tea
You Paid: $3.25
Your Barista: Derec
 
Welcome to the Bearcat Bistro, Derec!
    
1. Display Menu
2. Take New Order
3. View Open Orders
4. Mark Order as Complete
5. View End of Day Report
6. Exit
    
Please select an option. 3
 
Order for Derec - $8.25
Medium Strawberry, Mango Redbull with Whipped Cream - $6.25
Sugar Cookie - $2.0
 
Order for Joe - $3.25
Medium Earl Grey Tea - $3.25
 
Welcome to the Bearcat Bistro, Derec!
    
1. Display Menu
2. Take New Order
3. View Open Orders
4. Mark Order as Complete
5. View End of Day Report
6. Exit
    
Please select an option. 4
Order Up for Derec!

Sugar Cookie
Welcome to the Bearcat Bistro, Derec!
    
1. Display Menu
2. Take New Order
3. View Open Orders
4. Mark Order as Complete
5. View End of Day Report
6. Exit
    
Please select an option. 4
Order Up for Joe!

Welcome to the Bearcat Bistro, Derec!
    
1. Display Menu
2. Take New Order
3. View Open Orders
4. Mark Order as Complete
5. View End of Day Report
6. Exit
    
Please select an option. 5
 
Today's Sales
 
Order for Derec - $8.25:
Medium Strawberry, Mango Redbull with Whipped Cream - $6.25
Sugar Cookie - $2.0
 
Order for Joe - $3.25:
Medium Earl Grey Tea - $3.25
 
Account User: Derec
 
Welcome to the Bearcat Bistro, Derec!
    
1. Display Menu
2. Take New Order
3. View Open Orders
4. Mark Order as Complete
5. View End of Day Report
6. Exit
    
Please select an option. 6
Exiting Bearcat Bistro.


- After Debugging Phase 1, I removed all of the glaring issues that I could find, this being issues with the back function where it didn't accurately subtract the cost of certain items, as well as refining what prints during the display_drink function based on the base of the drink if the user used the back function. I also had an issue where drink names weren't listed when orders were marked as complete, but I got that fixed.
- Some things I still would like to fix/change: When the price ends in .x0, it doesn't show the zero. This is likely a simple change, I just haven't gotten around to it. Also, I would like to add more character to the UI to make it seem more coffee shop-esque.

An updated run though of the program:

Welcome, Bearcat Bistro Employee! Please Enter Your Username: Derec
Please enter your password: CS152
Welcome to the Bearcat Bistro, Derec!
    
1. Display Menu
2. Take New Order
3. View Open Orders
4. Mark Order as Complete
5. View End of Day Report
6. Exit
    
Please select an option. 2
 
What name would you like to use for your order? Derec
 
Would you like a (D)rink or (S)nack? D
    
Bases
  1. Drip
  2. Espresso
  3. Lemonade
  4. Redbull
  5. Tea

Please select a base. 4
You chose: Redbull
 
Fruity Flavors
  1. Blackberry
  2. Blueberry
  3. Blue Raspberry
  4. Grape
  5. Grapefruit
  6. Lavender
  7. Lime
  8. Mango
  9. Passionfruit
  10. Peach
  11. Pear
  12. Pomegranate
  13. Pineapple
  14. Raspberry
  15. Strawberry
  16. Watermelon

Which flavor would you like? 11
You chose Pear.
  
Would you like to add another flavor? N
Add Ons
  1. Cold Foam
  2. Espresso Shot
  3. Whipped Cream

Would you like an Add On? Press N for None. b
Removing last fruity flavor choice: Pear
Fruity Flavors
  1. Blackberry
  2. Blueberry
  3. Blue Raspberry
  4. Grape
  5. Grapefruit
  6. Lavender
  7. Lime
  8. Mango
  9. Passionfruit
  10. Peach
  11. Pear
  12. Pomegranate
  13. Pineapple
  14. Raspberry
  15. Strawberry
  16. Watermelon

Which flavor would you like? 13
You chose Pineapple.
  
Would you like to add another flavor? Y
Fruity Flavors
  1. Blackberry
  2. Blueberry
  3. Blue Raspberry
  4. Grape
  5. Grapefruit
  6. Lavender
  7. Lime
  8. Mango
  9. Passionfruit
  10. Peach
  11. Pear
  12. Pomegranate
  13. Pineapple
  14. Raspberry
  15. Strawberry
  16. Watermelon

Which flavor would you like? 9
You chose Passionfruit.
  
Would you like to add another flavor? N
Add Ons
  1. Cold Foam
  2. Espresso Shot
  3. Whipped Cream

Would you like an Add On? Press N for None. 3
You chose Whipped Cream.
Would you like to add another Add On? N
 
Sizes
  1. Small
  2. Medium
  3. Large

What size would you like? 2
You chose Medium
 
Your drink: Medium Pineapple, Passionfruit Redbull with Whipped Cream
Would you like to add this to your order? (Y)es or (N)o? Y
 
Item added to your order!
Order for Derec: Medium Pineapple, Passionfruit Redbull with Whipped Cream
   
Would you like a (D)rink, a (S)nack, or to (C)omplete your order? S
    
Available Snacks:
1. Bagel
2. Chocolate Chip Cookie
3. Curry Pocket
4. Sugar Cookie
5. Quesadilla
6. Pizza
   
Please select a snack by number, or choose (B)ack or (Q)uit: 5
You chose: Quesadilla
Would you like to add Quesadilla to your order? (Y)es or (N)o? Y
Order for Derec: Medium Pineapple, Passionfruit Redbull with Whipped Cream, Quesadilla
   
Would you like a (D)rink, a (S)nack, or to (C)omplete your order? C
    
Order for Derec Confimed! Your Reciept:
Medium Pineapple, Passionfruit Redbull with Whipped Cream
Quesadilla
You Paid: $9.0
Your Barista: Derec
 
Welcome to the Bearcat Bistro, Derec!
    
1. Display Menu
2. Take New Order
3. View Open Orders
4. Mark Order as Complete
5. View End of Day Report
6. Exit
    
Please select an option. 2
 
What name would you like to use for your order? Joe
 
Would you like a (D)rink or (S)nack? D
    
Bases
  1. Drip
  2. Espresso
  3. Lemonade
  4. Redbull
  5. Tea

Please select a base. 2
You chose: Espresso
 
Espresso Drinks
  1. Americano
  2. Latte
  3. Mocha
  4. White Mocha

Which drink would you like? 2
You chose Latte.
  
Temperatures
  1. Iced
  2. Hot

Would you like that (I)ced or (H)ot? 2
You chose Hot
 
Milks
  1. Almond
  2. Coconut
  3. Nonfat
  4. Oat
  5. Soy
  6. Whole

Which milk would you like? 4
You chose Oat.
    
Savory Flavors
  1. Chocolate
  2. Caramel
  3. Hazelnut
  4. Pumpkin Spice
  5. Vanilla
  6. Irish Cream
  7. White Chocolate

Which flavor would you like? 4
You chose Pumpkin Spice.
   
Would you like to add another flavor? N
Add Ons
  1. Cold Foam
  2. Espresso Shot
  3. Whipped Cream

Would you like an Add On? Press N for None. 2
You chose Espresso Shot.
Would you like to add another Add On? N
 
Sizes
  1. Small
  2. Medium
  3. Large

What size would you like? 3
You chose Large
 
Your drink: Large Hot Pumpkin Spice Latte with Oat Milk and Espresso Shot
Would you like to add this to your order? (Y)es or (N)o? Y
 
Item added to your order!
Order for Joe: Large Hot Pumpkin Spice Latte with Oat Milk and Espresso Shot
   
Would you like a (D)rink, a (S)nack, or to (C)omplete your order? s
    
Available Snacks:
1. Bagel
2. Chocolate Chip Cookie
3. Curry Pocket
4. Sugar Cookie
5. Quesadilla
6. Pizza
   
Please select a snack by number, or choose (B)ack or (Q)uit: 1
You chose: Bagel
Would you like to add Bagel to your order? (Y)es or (N)o? Y
Order for Joe: Large Hot Pumpkin Spice Latte with Oat Milk and Espresso Shot, Bagel
   
Would you like a (D)rink, a (S)nack, or to (C)omplete your order? C
    
Order for Joe Confimed! Your Reciept:
Large Hot Pumpkin Spice Latte with Oat Milk and Espresso Shot
Bagel
You Paid: $13.75
Your Barista: Derec
 
Welcome to the Bearcat Bistro, Derec!
    
1. Display Menu
2. Take New Order
3. View Open Orders
4. Mark Order as Complete
5. View End of Day Report
6. Exit
    
Please select an option. 3
 
Order for Derec - $9.0
Medium Pineapple, Passionfruit Redbull with Whipped Cream - $5.75
Quesadilla - $3.25
 
Order for Joe - $13.75
Large Hot Pumpkin Spice Latte with Oat Milk and Espresso Shot - $11.0
Bagel - $2.75
 
Welcome to the Bearcat Bistro, Derec!
    
1. Display Menu
2. Take New Order
3. View Open Orders
4. Mark Order as Complete
5. View End of Day Report
6. Exit
    
Please select an option. 4
Order Up for Derec!
Medium Pineapple, Passionfruit Redbull with Whipped Cream
Quesadilla
Welcome to the Bearcat Bistro, Derec!
    
1. Display Menu
2. Take New Order
3. View Open Orders
4. Mark Order as Complete
5. View End of Day Report
6. Exit
    
Please select an option. 4
Order Up for Joe!
Large Hot Pumpkin Spice Latte with Oat Milk and Espresso Shot
Bagel
Welcome to the Bearcat Bistro, Derec!
    
1. Display Menu
2. Take New Order
3. View Open Orders
4. Mark Order as Complete
5. View End of Day Report
6. Exit
    
Please select an option. 3
 
There are no open orders.
Welcome to the Bearcat Bistro, Derec!
    
1. Display Menu
2. Take New Order
3. View Open Orders
4. Mark Order as Complete
5. View End of Day Report
6. Exit
    
Please select an option. 5
 
Today's Sales
 
Order for Derec - $9.0:
Medium Pineapple, Passionfruit Redbull with Whipped Cream - $5.75
Quesadilla - $3.25
 
Order for Joe - $13.75:
Large Hot Pumpkin Spice Latte with Oat Milk and Espresso Shot - $11.0
Bagel - $2.75
 
Account User: Derec
 
Welcome to the Bearcat Bistro, Derec!
    
1. Display Menu
2. Take New Order
3. View Open Orders
4. Mark Order as Complete
5. View End of Day Report
6. Exit
    
Please select an option. 6
Exiting Bearcat Bistro.