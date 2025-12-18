#CRUD operations on Suppliers

supply_details = [
    {
        'supplier_id':1,
        'name':'Samsung',
        'contact':'9320456785'
    },
    {
        'supplier_id':2,
        'name':'CityStyle',
        'contact':'8520369741'
    },
    {
        'supplier_id':3,
        'name':'Lenskart',
        'contact':'7509548631'
    }]

supply_products = [
    {
        'supplier_id':1,
        'products':{
            'product_id':'M17',
            'product_name':'Samsung M17 5g',
            'product_price':13_999,
            'product_quantity':1250
        }
    },
    {
        'supplier_id':2,
        'products':{
            'product_id':158,
            'product_name':'Grey Cotton Jeans "36"',
            'product_price':799,
            'product_quantity':350
        }
    },
    {
        'supplier_id':3,
        'products':{
            'product_id':92,
            'product_name':'Blue Square Frame',
            'product_price':800,
            'product_quantity':80
        }
    }

]

def add_supplier(s_id,s_name,s_contact):
    supply_details.append({
        'supplier_id':s_id,
        'name':s_name,
        'contact':s_contact
    })
    return 'Supplier Added Successfully'

def view_supplier_products(s_id):
    for s in supply_products:
        if s['supplier_id'] == s_id:
            return s['products']
    pass