print(r"""
      ___           ___           ___
     /\  \         /\  \         /\  \
    /::\  \       /::\  \       /::\  \
   /:/\:\  \     /:/\:\  \     /:/\:\  \
  /:/  \:\  \   /:/  \:\  \   /:/  \:\  \
 /:/__/ \:\__\ /:/__/ \:\__\ /:/__/ \:\__\
 \:\  \ /:/  / \:\  \ /:/  / \:\  \ /:/  /
  \:\  /:/  /   \:\  /:/  /   \:\  /:/  /
   \:\/:/  /     \:\/:/  /     \:\/:/  /
    \::/  /       \::/  /       \::/  /
     \/__/         \/__/         \/__/

        S E C R E T   A U C T I O N
""")


print("\n\n\n\nWelcome to the secret auction program. \n\n\n")

auction_dictionary = {}


def find_highest_bidder(auction_dictionary):
    highest_bid = 0
    highest_bidder = ""
    for key in auction_dictionary:
        if auction_dictionary[key] >= highest_bid:
            highest_bid = auction_dictionary[key]
            highest_bidder = key

    print(f"\n \n \n ******************* Highest bid is {highest_bid}€ made by {highest_bidder}   *******************")


def find_highest_bidder_with_max_function(auction_dictionary):
    highest_bidder = max(auction_dictionary, key=auction_dictionary.get)
    highest_bid = auction_dictionary[highest_bidder]
    print(f"\n \n \n ******************* Highest bid is {highest_bid}€ made by {highest_bidder}   *******************")



auction_active = True

while auction_active:

    name = input("What is your name? ")
    bid = int(input("What is your bid?  €"))
    auction_dictionary[name] = bid
    if input("Are there any other bidders? Type 'yes' or 'no': ").lower() == "no":
        auction_active = False
        find_highest_bidder(auction_dictionary)
        find_highest_bidder_with_max_function(auction_dictionary)
    else:
        print("\n" * 100)               # clears screen --> for bidder discretion


