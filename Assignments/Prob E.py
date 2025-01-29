def maximum_bags_sold(customers, rice_bags):
    # Sort customers and rice bags based on price and quantity (in reverse order)
    customers.sort(key=lambda x: (x[0], x[1]), reverse=True)
    rice_bags.sort(key=lambda x: (x[1], x[0]), reverse=True)

    sold_bags = 0
    bag_taken = [False] * len(rice_bags)

    for customer_price, customer_quantity in customers:
        for j, (bag_price, bag_quantity) in enumerate(rice_bags):
            if not bag_taken[j] and bag_price <= customer_price and bag_quantity >= customer_quantity:
                # Sell the bag to the customer
                sold_bags += 1
                bag_taken[j] = True
                break

    return sold_bags

# Example usage:
customers = [(5, 10), (8, 5), (7, 8)]
rice_bags = [(3, 12), (7, 10), (4, 8), (6, 15)]

result = maximum_bags_sold(customers, rice_bags)
print("Maximum bags sold:", result)

