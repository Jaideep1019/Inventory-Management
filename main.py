from store.products import get_all_products,add_product,update_product,record_sale,delete_product,view_product_details
from store.supply import add_supplier
def main():
    print('''
          
1. Add New Product #complete
2. Update Product Stock #complete
3. Record a Sale #partial complete
4. Add Supplier #complete
5. View Supplier's Products 
6. Generate Inventory Report
7. Check Reorder Alerts
8. View Product Details #complete
9. Delete a Product #complete
10. Exit
11. View All product Details

''')
    while True:
        choice = int(input('Enter an option: '))
        if choice == 1:
            p_id = int(input('Enter product id: '))
            p_category = input('Enter product category: ')
            p_name = input('Enter product name: ')
            p_price = int(input('Enter product price: '))
            p_quantity = input('Enter no.of products: ')
            a = add_product(p_id,p_category,p_name,p_price,p_quantity)
            print(a)
        elif choice == 2:
            p_id = int(input('Enter product id: '))
            u_quantity = int(input('Enter no.of products to update: '))
            b = update_product(p_id,u_quantity)
            print(b)
        elif choice == 3:
            p_id = int(input('Enter product id: '))
            u_quantity = int(input('Enter sold quantity: '))
            c = record_sale(p_id,u_quantity)
            print(c)
        elif choice == 4:
            s_id = int(input('Enter Supplier ID: '))
            s_name = input('Enter Supplier Name: ')
            s_contact = input('Enter Supplier Phone number: ')
            d = add_supplier(s_id,s_name,s_contact)
            print(d)
        elif choice == 5:

            pass
        elif choice == 6:
            pass
        elif choice == 7:
            pass
        elif choice == 8:
            p_id = int(input('Enter the Product ID: '))
            f = view_product_details(p_id)
            print(f)
        elif choice == 9:
            p_id = int(input('Enter the Product ID to remove: '))
            e = delete_product(p_id)
            print(e)
        elif choice == 10:
            break
        elif choice ==11:
            p = get_all_products()
            print(p)

if __name__ == '__main__':
    main()