{
  
  # App information
   
    'name': 'Easy Stock Reservation Management',
    'version': '11.0',
    'category': 'stock',
    'license': 'OPL-1',
    'summary': """Manage Stock Reservation and Release of stock easily.""",
    
   # Dependencies
   
   'depends': ['sale','sale_stock'],
   
    # Views
   
    'data': [
          'views/product_product.xml'
	],
   
   # Odoo Store Specific
    
    'images': ['static/description/stock_reservation.png'],      
    
    
    
    # Author

    'author': 'Craftsync Technologies',
    'website': 'https://www.craftsync.com',
    'maintainer': 'Craftsync Technologies',
       
       
    # Technical 
    
    'installable': True,
    'currency': 'EUR',
    'price': 29.00,
    'auto_install': False,
    'application': True,
          
    
}
