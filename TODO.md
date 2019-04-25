# Data Privacy Project
1. Clean up login page
  * Adding multi-user support (account creation) - incorporate createAccount.py (IN PROGRESS)
  * Change config.ini to read from Dict { userEncrypted: passwordEncrypted } (DONE)
  * Add generation of private/public key on LOGIN (NEARLY DONE)

2. Create fake auction page (with list of 5 auctions and option to bid on them)

3. Backend for Auction bidding
  * Upon receiving bids, server will hold list of top X bids (# of items) along with encrypted User information
  * If a bid is higher than the current one, replace it and (maybe) notify the user (and let them rebid)

4. Treat like silent auction, keep list of bids silent (but notify users when outbid)
  * When auction is over (timer), notify the winner and losers

* Server is treated as "Bob" and dishes out public/private keys to user
* User is "Alice", sends in encrypted bid data and server can decrypt it
