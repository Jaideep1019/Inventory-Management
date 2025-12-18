#CRUD operations on Suppliers

supply = [
    {
        'id':1,
        'name':'Samsung',
        'contact':'9320456785'
    },
    {
        'id':2,
        'name':'CityStyle',
        'contact':'8520369741'
    },
    {
        'id':3,
        'name':'Lenskart',
        'contact':'7509548631'
    }
    ]

def add_supplier(s_id,s_name,s_contact):
    supply.append({
        'id':s_id,
        'name':s_name,
        'contact':s_contact
    })
    return 'Supplier Added Successfully'