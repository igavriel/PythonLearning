# This class represents a product entity in a system.
# auto increment of p_id as static member
class Product():
    next_id = 0
    
    def __init__(self, name, price):
        self.p_id = Product.next_id
        Product.next_id = Product.next_id + 1
        self.name = name
        self.price = float(price)

    def __str__(self):
        return f"Prod: {self.p_id} name: {self.name} price: {self.price}"


# This class contains attributes related to a marketing campaign.
# assign the product list to the campaign as a static member
class Campaign():
    product_list = None

    def __init__(self, name, p_id, amount, discount):
        self.name = name
        self.p_id = p_id
        self.amount = amount
        self.discount = discount
        
    def __str__(self):
        prd = ShoppingCart.product_list[self.p_id]
        return f"Name: {self.name} Prod: ({self.p_id}) {prd.name} Amount: {self.amount} discount: {self.discount}%"


# This class represents a shopping cart. with product list and campaign list static members
class ShoppingCart():
    product_list = None
    campaign_list = None

    def __init__(self):
        self.shop_list = set()

    def add(self, p_id, amount):
        self.shop_list.add((p_id, amount))

    def __str__(self):
        return "\n".join(str(ShoppingCart.product_list[item[0]]) + 
                         str(" Amount=") + 
                         str(item[1]) for item in self.shop_list)
        
    def __calc_cmp_item(self, item, cmp):
        prd = ShoppingCart.product_list[item[0]]
        amount=int(item[1])
        price = 0
        while amount>=cmp.amount:
            local_price = cmp.amount * prd.price - (cmp.amount * prd.price)*(cmp.discount/100)
            price = price+local_price
            amount = amount - cmp.amount
            #print(f"price {price} local_price={local_price}")
            
        if amount > 0:
            price = price + amount * prd.price
        
        #print(f"price {price}")
        return price    


    def __calc_item(self, item):
        calc_amount = 0
        prd = ShoppingCart.product_list[item[0]]
        for cmp in ShoppingCart.campaign_list:
            if cmp.p_id == prd.p_id:
                calc_amount = self.__calc_cmp_item(item, cmp)
        
        amount=int(item[1])
        price =float(prd.price)
        item_total = amount*price
        
        if calc_amount != item_total:
            print(f"{prd.name}: {amount}x{price} = {item_total} = New Price = {calc_amount} ")
            return calc_amount

        print(f"{prd.name}: {amount}x{price} = {item_total} ")
        return item_total


    def calc(self):
        total = 0
        for item in self.shop_list:
            total = total + self.__calc_item(item)
            
        print(f"Total: {total}")

#############################################################

product_list = [
    Product("Milk", 10),    #0
    Product("Butter", 5),   #1
    Product("Bread", 4),    #2
    Product("Flower", 8),   #3
    Product("Soda", 3),     #4
]

# assign the product list to the campaign as a static member
Campaign.product_list = product_list
campaign_list = [
    Campaign("1+1", 0, 2, 50),
    Campaign("2+1", 1, 3, 33),
    Campaign("9+1", 2, 10, 10),
    Campaign("5+1", 4, 6, 16),
]

ShoppingCart.product_list = product_list
ShoppingCart.campaign_list = campaign_list

shopping_cart = ShoppingCart()
shopping_cart.add(0, 3)
shopping_cart.add(1, 6)
shopping_cart.add(2, 4)
shopping_cart.add(4, 6)

print("\nProducts")
print("\n".join(str(item) for item in product_list))

print("\nCampaign")
print("\n".join(str(item) for item in campaign_list))

print("\nShoppingCart\n", shopping_cart)

print("\nBill\n")
shopping_cart.calc()
