Mathematics behind Credit/Debit card numbering

All credit and debit cards have numbers printed on them (generally 16 digits). This signifies a unique account number for a card and reveals some information about the card issuer and its associated account. For obvious reasons, just any randomly generated numbers will not work, they follow pattern.

Let’s break it down
1. Card Number
Credit/Debit card numbers are all numeric. These numbers count ranges from 12 to 19 digits.
For example, MasterCard has 16 digits and American Express has 15 digits.
2. Major Industry Identifier (MII)
The first digit of the credit/debit card is the Major Industry Identifier (MII). It indicates the category of the entity which issued the card.
* 1 and 2: Airlines
* 3: Travel and Entertainment
* 4 and 5: Banking and Financial Services
* 6: Merchandising and Banking
* 7: Petroleum
* 8: Health care, Telecommunications
* 9: National Assignment
3. Issuer Identification Number (IIN)
The first six digits are the Issuer Identification Number (IIN). These denotes the institution that issued the card.
For example, Visa cards begin with a 4, while MasterCard ones start with number between 51 and 55.

3. Issuer Identification Number (IIN)
The first six digits are the Issuer Identification Number (IIN). These denotes the institution that issued the card.
For example, Visa cards begin with a 4, while MasterCard ones start with number between 51 and 55.
The Mathematics behind the Card Numbering
In a typical sixteen-digit credit card number, the first fifteen digits are determined by the issuing bank, but the last digit, called the check digit, is mathematically determined based on all other digits.
5333619503715702
Account Number: 533361950371570
Check Digit: 2
Credit/Debit card numbers are often typed in, input, transferred and quoted. All of this transmission can cause errors, especially considering that humans are involved. Humans often make mistakes in transferal. To try and minimize this, credit card numbers contain a check digit.
Although, not all errors can be detected with a single check digit, one can still find out if one digit is wrong. Whenever an e-commerce application, for example, has to validate a card number, it checks this last digit before sending the rest of the information to the bank.
The exact mathematic formula for its generation was invented by Hans Peter Luhn, an engineer at IBM in 1954. Originally patented, the algorithm is now in the public domain and a Worldwide standard ISO/IEC 7812–1.
The Luhn Algorithm or modulo-10 Algorithm
The Luhn algorithm is based around the principle of modulo arithmetic and digital roots.
1. Start from the rightmost digit (i.e. check digit)
2. Multiply every second digit by 2 (i.e. digit at even positions)
3. If the result in step 2 is more than one digit, add them up (E.g. 12: 1+2 = 3)
4. Add the resulting digits to digits at the odd positions
Let’s consider below account number for example.
Note: Number generated randomly from online website.
533361950371570

Example for calculating check digit for any Credit/Debit card
https://miro.medium.com/max/972/1*VwP_mnBs0D7XTbC-rS9R3A.png
The total obtained is 48+x, should be divisible by 10, only then this number is a valid card number.
Thus, the check digit (x) should be calculated accordingly, so that the final total is divisible by 10.
Therefore, x must be 2, so that the total will be 48+2 = 50. (“x” can only be a single digit)
x = 2 is the check digit for the above example.
You can go ahead and try with your own Credit/Debit card numbers.



References: 
    - https://medium.com/@ma.juber/mathematics-behind-credit-debit-card-numbering-340bf68d27d2
    - https://www.discoverglobalnetwork.com/downloads/IPP_VAR_Compliance.pdf



