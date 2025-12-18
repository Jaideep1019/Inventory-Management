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
        'price':899,
        'quantity':30
    },
    {
        'id':3,
        'category':'spectacles',
        'name':'Raybon Polarized oval glasses',
        'price':10_999,
        'quantity':14
    }
]

# def delete_product(p_id):
#     for p in products:
#         if p['id'] == p_id:
#             del p
#             return 'Product deleted successfully'
#     return 'Invalid Product ID'

# loop with remove for dictionaries in list
def delete_product(p_id):
    for d in products:
        if d.get('id') == p_id:
            products.remove(d)
            return 'Product Removed Successfully'
            break  # Stops after finding and removing the first match


print(delete_product(2))
print(products)