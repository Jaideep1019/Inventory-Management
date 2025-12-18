#CRUD operations of Products

#Products requirements
# product_name, qunatities
# suppliers
# stock alerts

products = [
    {
        'id':1,
        'category':'electronics',
        'name':'Samsung M07',
        'price':6_999,
        'quantity':100
    },
    {
        'id':2,
        'category':'clothes',
        'name':'Brown Jeans',
        'size':'S,M,L,XL',
        'price':899,
        'quantity':40
    },
    {
        'id':3,
        'category':'spectacles',
        'name':'Raybon Polarized oval glasses',
        'price':10_999,
        'quantity':15
    }
]

#features
# add product
# update product stock
# delete product

def get_all_products():
    return products

def add_product(p_id,p_category,p_name,p_price,p_quantity):
    products.append(
        {
            'id':p_id,
            'category':p_category,
            'name':p_name,
            'price':p_price,
            'quantity':p_quantity
        }
    )
    return 'Product Added Successfully'

def update_product_quantity(p_id,u_quantity):
    for p in products:
        if p['id'] == p_id:
            p['quantity'] += u_quantity
            return p
    return 'Invalid product ID'

records = []
def update_records(h):
    records.append(h)
    return 'Product sale is recorded' 
#f'Product sale is recorded {records}' - code for verifying records list

def record_sale(p_id,u_quantity):
    for p in products:
        if p['id'] == p_id and p['quantity']>0:
            p['quantity'] -= u_quantity
            return p
    return 'Ivalid ID/ No stock available'

# loop with remove for dictionaries in list
def delete_product(p_id):
    for d in products:
        if d.get('id') == p_id:
            products.remove(d)
            return 'Product Removed Successfully'
            break  # Stops after finding and removing the first match

def view_product_details(p_id):
    for p in products:
        if p.get('id') == p_id:
            return p

alerts = []
def check_reoder_alerts():
    for p in products:
        if p['quantity']<=10:
            alerts.append(f'alert "{p['name']}" is low in quantity')
    return alerts

# calculating all the products sold by referring sales record 
def generate_inventory_report():
    total_revenue = 0
    total_products_sold = 0
    for r in records:
        total_revenue += (r['price']*r['quantity'])
        total_products_sold += r['quantity']
    return f'Total Products Sold = {total_products_sold} and Total Revenue generated = {total_revenue}'