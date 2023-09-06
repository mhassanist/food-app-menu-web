menu = [{
  "name": "Burger",
  "price": 5.0,
  "available": True
}, {
  "name": "Pizza",
  "price": 8.0,
  "available": True
}, {
  "name": "Pasta",
  "price": 6.0,
  "available": True
}, {
  "name": "Salad",
  "price": 4.0,
  "available": True
}]

order = []


def get_menu_items():
 return menu


def get_order_total():
  total = 0
  for item in order:
    total += item['price'] * item['qty']

  print("total: ", total)
  return total


def add_order_item(item, qty):
  new_order_item = {"name": item['name'], "price": item['price'], "qty": qty}

  #new_order_item_tuple = (item['name'], item['name'], qty)
  #new_order_item_list = [item['name'], item['name'], qty]

  order.append(new_order_item)

  print("order", order)
