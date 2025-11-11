 CS50-Final-Project

Developer notes:-

Monthly finances tracking application, designed to effectively aid you into timely paying your credit card bills.
what should the features be for the application.
let us analyze the finances for a month and all the things that we have to do to effectively manage our finances.

Styling is the last step of the application

First implementation !
first comes the intake of money or deposits into you account in the form of income from various sources, ammounting to one full bank balance.
By creating a separate index template, I can use input fields to add income, incoming from varous streams, while stating each of the source's names in a text box alont side the int income stream box.
I should aim to somehow create a add row link button to add an empty row containing input fields to enter you extra income sources.
Second implementation is to add up all of these imcomes in to one net pay, with an add button.
Third I need the addition of sources name alongside their amounts, like all these sources amount up to this much total, together with their individual contributions.
so we took a turn on our plan. Now i am removing the add another source button, because i was trying the implementation of
individual source and their income listing, and it was not adding the remaining extra source amounts. I do not know why but it
sure is adding and projecting the individual and total amount with sources when i click add income after adding each source and
income, individually. The data base is working fine as well.

My next goal is to some how, make a clear buffer button to clear the database's values of incomes and sources, for a fresh start, if you made a mistake while adding incomes, may be!
We need a clear the previous buffer as well for new financial analysis !

Now that we are done with the income part. What is left is the expenses part. Same like income entries, we can use the same algorithm to wite out our expenses, with all the add and remove buffer functionallity. Though I am confused whether creating all these routes will effect the functionallity of the program or not? Or is it a bad practice or not.

After listing the expenses, comes the subtraction part, where we should potentially create a button for subtracting all the expenses from the incomes and give out the fun money etc. We can play with the remaining money as well, by using some alogorithm to divide it among a number of categories including fun-money or may be savings.