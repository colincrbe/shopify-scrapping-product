import requests
import json 
import pandas as pd
url = 'https://shopURL/products.json?limit=250&page=4'

r = requests.get(url)

data = r.json()

product_list = []
tag_product = ''
for item in data['products']:
    title = item['title']
    handle = item['handle']
    body_html = item['body_html']
    created = item['created_at']
    product_type = item['product_type']
    tags = item['tags']
    all_images = []
    for image in item['images']:
        try:
            imagesrc = image['src']
            all_images.append(image['src'])
        except:
            imagesrc = 'None'
            all_images.append('None')
    image_position = 1
    option_list = []
    option_main = []
    option_name = []
    for option in item['options']:
        op_name = option['name']
        op_position = option['position']
        option_name.append(op_name) 
        for value in option['values']:
            option_list.append(value)
        option_main.append(option_list)  
        option_list = []  
    final_list = []
    if len(item['options']) == 3:
        for taille in option_main[0]: 
            for couleur in option_main[1]:
                for autre in option_main[2]:
                    temp_list = []
                    temp_list.append(taille)
                    temp_list.append(couleur)
                    temp_list.append(autre)
                    final_list.append(temp_list)
    elif len(item['options']) == 2:
        for taille in option_main[0]: 
            for couleur in option_main[1]:
                temp_list = []      
                temp_list.append(taille)
                temp_list.append(couleur)
                final_list.append(temp_list)
    elif len(item['options']) == 1:
        for taille in option_main[0]: 
            temp_list = []      
            temp_list.append(taille)
            final_list.append(temp_list)         
    for variant in item['variants']:
        price = variant['price']
        sku = variant['sku']
        available = variant['available']
        weight = variant['grams']
        if variant['featured_image'] is not None:
            featured_image = variant['featured_image'] 
            if len(item['options']) == 3:
                product = {
                'Handle': handle,
                'Title': title,
                'Body (HTML)': body_html,
                'product_type': product_type,
                'price': price,
                'Variant Inventory Policy': 'deny',
                'Variant Taxable': 'VRAI',
                'Tags': tags,
                'sku': sku,
                'Variant Grams': weight,
                'Option1 Name': option_name[0],
                'Option1 Value': final_list[image_position - 1][0],
                'Option2 Name': option_name[1],
                'Option2 Value': final_list[image_position - 1][1],
                'Option3 Name': option_name[2],
                'Option3 Value': final_list[image_position - 1][2],
                'available': available,
                'Image Src': featured_image['src'],
                'Variant Image': featured_image['src'],
                'Image Position': image_position,
                'Status': 'active'
            }
            elif len(item['options']) == 2:
                product = {
                'Handle': handle,
                'Title': title,
                'Body (HTML)': body_html,
                'product_type': product_type,
                'price': price,
                'Variant Inventory Policy': 'deny',
                'Variant Taxable': 'VRAI',
                'Tags': tags,
                'sku': sku,
                'Variant Grams': weight,
                'Option1 Name': option_name[0],
                'Option1 Value': final_list[image_position - 1][0],
                'Option2 Name': option_name[1],
                'Option2 Value': final_list[image_position - 1][1],
                'Option3 Name': '',
                'Option3 Value': '',
                'available': available,
                'Image Src': featured_image['src'],
                'Variant Image': featured_image['src'],
                'Image Position': image_position,
                'Status': 'active'
                }
            elif len(item['options']) == 1:
                temp_index = 0
                if temp_index == 0:
                    product = {
                    'Handle': handle,
                    'Title': title,
                    'Body (HTML)': body_html,
                    'product_type': product_type,
                    'price': price,
                    'Variant Inventory Policy': 'deny',
                    'Variant Taxable': 'VRAI',
                    'Tags': tags,
                    'sku': sku,
                    'Variant Grams': weight,
                    'Option1 Name': option_name[0],
                    'Option1 Value': final_list[image_position - 1][0],
                    'Option2 Name': '',
                    'Option2 Value': '',
                    'Option3 Name': '',
                    'Option3 Value': '',
                    'available': available,
                    'Image Src': featured_image['src'],
                    'Variant Image': featured_image['src'],
                    'Image Position': image_position,
                    'Status': 'active'
                    }
                else:
                    product = {
                    'Handle': handle,
                    'Title': title,
                    'Body (HTML)': body_html,
                    'product_type': product_type,
                    'price': price,
                    'Variant Inventory Policy': 'deny',
                    'Variant Taxable': 'VRAI',
                    'Tags': tags,
                    'sku': sku,
                    'Variant Grams': weight,
                    'Option1 Name': '',
                    'Option1 Value': '',
                    'Option2 Name': '',
                    'Option2 Value': '',
                    'Option3 Name': '',
                    'Option3 Value': '',
                    'available': available,
                    'Image Src': featured_image['src'],
                    'Variant Image': featured_image['src'],
                    'Image Position': image_position,
                    'Status': 'active'
                    }
        else:
            position_index = 1
            for imagePro in item['images']:
                if position_index == 1:
                    product = {
                    'Handle': handle,
                    'Title': title,
                    'Body (HTML)': body_html,
                    'product_type': product_type,
                    'price': price,
                    'Variant Inventory Policy': 'deny',
                    'Variant Taxable': 'VRAI',
                    'Variant Grams': weight,
                    'Option1 Name': 'Title',
                    'Option1 Value': 'Default Title',
                    'Option2 Name': '',
                    'Option2 Value': '',
                    'Option3 Name': '',
                    'Option3 Value': '',
                    'Variant Requires Shipping': 'VRAI',
                    'Tags': tags,
                    'sku': sku,
                    'available': available,
                    'Image Src': imagePro['src'],
                    'Variant Image': imagePro['src'],
                    'Image Position': position_index,
                    'Status': 'active'
                }
                else:
                    product = {
                    'Handle': handle,
                    'Image Src': imagePro['src'],
                }
                position_index = position_index + 1
                product_list.append(product)
        image_position = image_position + 1
        product_list.append(product)

df = pd.DataFrame(product_list)
df.to_csv('allproducts.csv')
print('save to file.')
