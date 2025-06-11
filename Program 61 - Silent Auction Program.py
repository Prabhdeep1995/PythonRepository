import os

print("**** Welcome to Silent Auction Program ****")
list1 = []

def inputs():
    name = input("What is your Name? ")
    bid = input("What is your bid? ")
    bid=float(bid)
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no' ").lower()
    data = {'name':name,
            'bid':bid,'other_bidders' : other_bidders}
    list1.append(data)
    return list1

def calculate_maximum(auctionDataList):
    print("In max function")
    maxBid = auctionDataList[0].get('bid')
    for i in auctionDataList:
        if i.get('bid')>maxBid:
            maxBid= i.get('bid')
            maxBidName= i.get('name')
    print(f"The winner of Silent auction is {maxBidName} with bid amount {maxBid}")
    return maxBidName


def auction():
    auctionDataList= inputs()

    for i in auctionDataList:
        if i.get('other_bidders') == 'yes':
            # os.system('cls')
            inputs()
        else:
            print(auctionDataList)
            # print(i)
            calculate_maximum(auctionDataList)

auction()







