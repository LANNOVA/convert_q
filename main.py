import re

def convert_quantity(product_name, quantity_unit):
    # Define regular expression pattern to match quantity and unit
    #pattern = r'(\d+(?:\.\d+)?)\s*(\w+)'
    pattern = r'(\d+(?:\.\d+)?)\s*(oz|ounce|ct|lb|lbs|g|kg|fl|mg|ml|gal|l|cups|quart|pint|count|pounds|pound|-oz|-ct|-lb|-lbs|-g|-kg|-fl|-mg|-ml|-gal|-l|-cups|-quart|-pint|-count|-pounds|-pound|-ounce)\b'
    # Extract quantity and unit from product name using regular expression
    lowername = product_name.lower()
    match = re.search(pattern, lowername)
    if not match:
        return None

    # Convert quantity to desired unit
    quantity, unit = match.groups()
    quantity = float(quantity)
    if (unit.lower() == 'oz' or unit.lower() == 'ounce'  or unit.lower() == '-ounce' or unit.lower() == 'fl' or unit.lower() == '-fl' or unit.lower() == '-oz' ) and quantity_unit.lower() == 'lb':
        quantity /= 16.0  
    elif (unit.lower() == 'lb' or unit.lower() == 'lbs' or unit.lower() == 'pound'  or quantity_unit.lower() == 'pounds' or unit.lower() == '-lb' or unit.lower() == '-lbs' or unit.lower() == '-pound'  or quantity_unit.lower() == '-pounds') and quantity_unit.lower() == 'oz':
        quantity *= 16.0  
    elif  unit.lower() == 'g' or unit.lower() == '-g' or unit.lower() == '-g'and quantity_unit.lower() == 'g':
        quantity *= 1.0  
    elif unit.lower() == 'kg' or unit.lower() == '-kg'  and quantity_unit.lower() == 'kg':
        quantity *= 1.0  
    elif (unit.lower() == 'oz' or unit.lower() == 'ounce'  or unit.lower() == '-ounce' or unit.lower() == 'fl' or unit.lower() == '-fl' or unit.lower() == '-oz' ) and quantity_unit.lower() == 'oz':
        quantity *= 1.0   
    elif (unit.lower() == 'oz' or unit.lower() == 'ounce'  or unit.lower() == '-ounce' or unit.lower() == 'fl' or unit.lower() == '-fl' or unit.lower() == '-oz' ) and quantity_unit.lower() == 'kg':
        quantity /= 35.274 
    elif (unit.lower() == 'oz' or unit.lower() == 'ounce'  or unit.lower() == '-ounce' or unit.lower() == 'fl' or unit.lower() == '-fl' or unit.lower() == '-oz' ) and quantity_unit.lower() == 'g':
        quantity /= 0.035274 
    elif (unit.lower() == 'lb' or unit.lower() == 'lbs'or unit.lower() == 'pound') and quantity_unit.lower() == 'lb':
        quantity *= 1.0  
    elif unit.lower() == 'mg'  or unit.lower() == '-mg' and quantity_unit.lower() == 'mg':
        quantity *= 1.0 
    elif unit.lower() == 'ml' or  unit.lower() == '-ml' and quantity_unit.lower() == 'ml':
        quantity *= 1.0   
    elif unit.lower() == 'gal'  or unit.lower() == '-gal' and quantity_unit.lower() == 'gal':
        quantity *= 1.0   
    elif unit.lower() == 'l' or  unit.lower() == '-l' and quantity_unit.lower() == 'l':
        quantity *= 1.0 
    elif unit.lower() == 'count' or unit.lower() == '-ct' and quantity_unit.lower() == 'count':
        quantity *= 1.0  
    elif unit.lower() == 'cups' or  unit.lower() == '-cups'  and quantity_unit.lower() == 'cups':
        quantity *= 1.0
    
    elif unit.lower() == 'kg' or unit.lower() == '-kg' and quantity_unit.lower() == 'g':
        quantity *= 1000.0  
    elif  unit.lower() == 'g' or unit.lower() == '-g' and quantity_unit.lower() == 'kg':
        quantity /= 1000.0  
    elif unit.lower() == 'mg' or unit.lower() == '-mg' and quantity_unit.lower() == 'g':
        quantity /= 1000.0 
    elif  unit.lower() == 'g' or unit.lower() == '-g' and quantity_unit.lower() == 'mg':
        quantity *= 1000.0 
    elif (unit.lower() == 'oz' or unit.lower() == 'ounce'  or unit.lower() == '-ounce' or unit.lower() == 'fl' or unit.lower() == '-fl' or unit.lower() == '-oz' ) and quantity_unit.lower() == 'ml':
        quantity *= 29.5735 
    elif unit.lower() == 'gal'  or unit.lower() == '-gal' and quantity_unit.lower() == 'l':
        quantity *= 3.78541 
    elif unit.lower() == 'pt' and quantity_unit.lower() == 'oz':
        quantity *= 16.0  
    elif (unit.lower() == 'lb' or unit.lower() == 'lbs' or unit.lower() == 'pound'  or unit.lower()=='pounds') and quantity_unit.lower() == 'kg':
        quantity /= 2.20462  
    elif (unit.lower() == 'lb' or unit.lower() == 'lbs' or unit.lower() == 'pound'  or unit.lower()== 'pounds') and quantity_unit.lower() == 'g':
        quantity *= 453.592  
    elif  unit.lower() == 'g' or unit.lower() == '-g' and quantity_unit.lower() == 'lb':
        quantity /= 453.592
    elif  (unit.lower() == 'lb' or unit.lower() == 'lbs' or unit.lower() == 'pound'  or unit.lower()== 'pounds') and quantity_unit.lower() == 'mg':
        quantity *= 453592.0  
    elif unit.lower() == 'mg' or unit.lower() == '-mg' and (quantity_unit.lower() == 'lb' or quantity_unit.lower() == 'lbs'):
        quantity /= 453592.0  
    elif (unit.lower() == 'oz' or unit.lower() == 'ounce'  or unit.lower() == '-ounce' or unit.lower() == 'fl' or unit.lower() == '-fl' or unit.lower() == '-oz' ) and quantity_unit.lower() == 'g':
        quantity *= 28.3495 
    elif  unit.lower() == 'g' or unit.lower() == '-g' and quantity_unit.lower() == 'oz':
        quantity /= 28.3495 
    elif (unit.lower() == 'oz' or unit.lower() == 'ounce'  or unit.lower() == '-ounce' or unit.lower() == 'fl' or unit.lower() == '-fl' or unit.lower() == '-oz' )  and quantity_unit.lower() == 'mg':
        quantity *= 28349.5  
    elif unit.lower() == 'mg' or unit.lower() == '-mg' and quantity_unit.lower() == 'oz':
        quantity /= 28349.5
    elif unit.lower() == 'kg' or unit.lower() == '-kg' and quantity_unit.lower() == 'lb':
        quantity *= 2.20462 
    elif (unit.lower() == 'oz' or unit.lower() == 'ounce'  or unit.lower() == '-ounce' or unit.lower() == 'fl' or unit.lower() == '-fl' or unit.lower() == '-oz' ) and quantity_unit.lower() == 'pt':
        quantity /= 16.0  
    elif unit.lower() == 'qt' or unit.lower() == '-qt' and quantity_unit.lower() == 'oz':
        quantity *= 32.0  #
    elif (unit.lower() == 'oz' or unit.lower() == 'ounce'  or unit.lower() == '-ounce' or unit.lower() == 'fl' or unit.lower() == '-fl' or unit.lower() == '-oz' ) and quantity_unit.lower() == 'qt' or unit.lower() == '-qt':
        quantity /= 32.0  
    elif unit.lower() == 'cup' and quantity_unit.lower() == 'oz':
        quantity *= 8.0  
    elif (unit.lower() == 'oz' or unit.lower() == 'ounce'  or unit.lower() == '-ounce' or unit.lower() == 'fl' or unit.lower() == '-fl' or unit.lower() == '-oz' ) and quantity_unit.lower() == 'cup':
        quantity /= 8.0  
    elif unit.lower() == 'l' or  unit.lower() == '-l' and quantity_unit.lower() == 'gal':
        quantity /= 3.78541  
    elif unit.lower() == 'ml' or  unit.lower() == '-ml' and quantity_unit.lower() == 'oz':
        quantity /= 29.5735  
    elif  (unit.lower() == 'lb' or unit.lower() == 'lbs' or unit.lower() == 'pound'  or unit.lower()== 'pounds') and quantity_unit.lower() == 'ml':
        quantity *= 453.59237 
    elif  (unit.lower() == 'lb' or unit.lower() == 'lbs' or unit.lower() == 'pound'  or unit.lower()== 'pounds') and quantity_unit.lower() == 'l':
        quantity *= 0.45359237  
    elif  (unit.lower() == 'lb' or unit.lower() == 'lbs' or unit.lower() == 'pound'  or unit.lower()== 'pounds') and quantity_unit.lower() == 'gal':
        quantity *= 0.119826427317 
    elif  (unit.lower() == 'lb' or unit.lower() == 'lbs' or unit.lower() == 'pound'  or unit.lower()== 'pounds') and quantity_unit.lower() == 'qt' or unit.lower() == '-qt':
        quantity /= 2.086351 
    elif  (unit.lower() == 'lb' or unit.lower() == 'lbs' or unit.lower() == 'pound'  or unit.lower()== 'pounds') and quantity_unit.lower() == 'pint':
        quantity /= 1.043176  
    elif  (unit.lower() == 'lb' or unit.lower() == 'lbs' or unit.lower() == 'pound'  or unit.lower()== 'pounds') and quantity_unit.lower() == 'cups':
        quantity *= 1.917222837193
        #skdhakhdksahdk
    elif  unit.lower() == 'ml' or  unit.lower() == '-ml' and quantity_unit.lower() == 'lb':
        quantity /= 453.59237 
    elif  unit.lower() == 'l' or  unit.lower() == '-l' and quantity_unit.lower() == 'lb':
        quantity /= 0.45359237  
    elif  unit.lower() == 'gal'  or unit.lower() == '-gal'and quantity_unit.lower() == 'lb':
        quantity /= 0.119826427317 
    elif  unit.lower() == 'qt' or unit.lower() == '-qt' and quantity_unit.lower() == 'lb':
        quantity *= 2.086351 
    elif  unit.lower() == 'pint' or  unit.lower() == '-pint'and quantity_unit.lower() == 'lb':
        quantity *= 1.043176  
    elif  unit.lower() == 'cups' or  unit.lower() == '-cups' and quantity_unit.lower() == 'lb':
        quantity /= 1.917222837193
        #skdhakhdksahdk
    elif  (unit.lower() == 'oz' or unit.lower() == 'ounce'  or unit.lower() == '-ounce' or unit.lower() == 'fl' or unit.lower() == '-fl' or unit.lower() == '-oz' )  and quantity_unit.lower() == 'ml':
        quantity *= 29.574
    elif  (unit.lower() == 'oz' or unit.lower() == 'ounce'  or unit.lower() == '-ounce' or unit.lower() == 'fl' or unit.lower() == '-fl' or unit.lower() == '-oz' )  and quantity_unit.lower() == 'l':
        quantity /= 33.814 
    elif  (unit.lower() == 'oz' or unit.lower() == 'ounce'  or unit.lower() == '-ounce' or unit.lower() == 'fl' or unit.lower() == '-fl' or unit.lower() == '-oz' )  and quantity_unit.lower() == 'gal':
        quantity /= 128 
    elif  (unit.lower() == 'oz' or unit.lower() == 'ounce'  or unit.lower() == '-ounce' or unit.lower() == 'fl' or unit.lower() == '-fl' or unit.lower() == '-oz' )  and quantity_unit.lower() == 'qt' or unit.lower() == '-qt':
        quantity /= 32 
    elif  (unit.lower() == 'oz' or unit.lower() == 'ounce'  or unit.lower() == '-ounce' or unit.lower() == 'fl' or unit.lower() == '-fl' or unit.lower() == '-oz' )  and quantity_unit.lower() == 'pint':
        quantity /= 16 
    elif  (unit.lower() == 'oz' or unit.lower() == 'ounce'  or unit.lower() == '-ounce' or unit.lower() == 'fl' or unit.lower() == '-fl' or unit.lower() == '-oz' )  and quantity_unit.lower() == 'cups':
        quantity /= 8 
        #skdhakhdksahdk
    elif  unit.lower() == 'ml' or  unit.lower() == '-ml'  and quantity_unit.lower() == 'oz':
        quantity /= 29.574
    elif  unit.lower() == 'l' or  unit.lower() == '-l'  and quantity_unit.lower() == 'oz':
        quantity *= 33.814 
    elif  unit.lower() == 'gal'  or unit.lower() == '-gal' and quantity_unit.lower() == 'oz':
        quantity *= 128 
    elif  unit.lower() == 'qt' or unit.lower() == '-qt'  and quantity_unit.lower() == 'oz':
        quantity *= 32 
    elif  unit.lower() == 'pint' or  unit.lower() == '-pint'  and quantity_unit.lower() == 'oz':
        quantity *= 16 
    elif  unit.lower() == 'cups' or  unit.lower() == '-cups' and quantity_unit.lower() == 'oz':
        quantity *= 8
        #skdhakhdksahdk 
    elif   unit.lower() == 'g' or unit.lower() == '-g' and quantity_unit.lower() == 'ml':
        quantity *= 1   
    elif   unit.lower() == 'g' or unit.lower() == '-g' and quantity_unit.lower() == 'l':
        quantity /= 1000 
    elif   unit.lower() == 'g' or unit.lower() == '-g' and quantity_unit.lower() == 'gal':
        quantity /= 3785.41178  
    elif   unit.lower() == 'g' or unit.lower() == '-g' and quantity_unit.lower() == 'qt' or unit.lower() == '-qt':
        quantity /= 946.352946 
    elif   unit.lower() == 'g' or unit.lower() == '-g' and quantity_unit.lower() == 'pint':
        quantity /= 473.176473 
    elif   unit.lower() == 'g' or unit.lower() == '-g' and quantity_unit.lower() == 'cups':
        quantity /= 236.5882 
        #skdhakhdksahdk 
    elif  unit.lower() == 'ml' or  unit.lower() == '-ml' and quantity_unit.lower() == 'g' :
        quantity /= 1   
    elif  unit.lower() == 'l' or  unit.lower() == '-l' and quantity_unit.lower() == 'g' :
        quantity *= 1000 
    elif  unit.lower() == 'gal'  or unit.lower() == '-gal' and quantity_unit.lower() == 'g' :
        quantity *= 3785.41178  
    elif  unit.lower() == 'qt' or unit.lower() == '-qt' and quantity_unit.lower() == 'g' :
        quantity *= 946.352946 
    elif  unit.lower() == 'pint' or  unit.lower() == '-pint' and quantity_unit.lower() == 'g' :
        quantity *= 473.176473 
    elif  unit.lower() == 'cups' or  unit.lower() == '-cups' and quantity_unit.lower() == 'g' :
        quantity *= 236.5882
        #skdhakhdksahdk
    elif  unit.lower() == 'kg' or unit.lower() == '-kg' and quantity_unit.lower() == 'ml':
        quantity *= 1/1000 
    elif  unit.lower() == 'kg' or unit.lower() == '-kg' and quantity_unit.lower() == 'l':
        quantity /= 1000/1000  
    elif  unit.lower() == 'kg' or unit.lower() == '-kg' and quantity_unit.lower() == 'gal':
        quantity /= 3785.41178/1000   
    elif  unit.lower() == 'kg' or unit.lower() == '-kg' and quantity_unit.lower() == 'qt' or unit.lower() == '-qt':
        quantity /= 946.352946/1000  
    elif  unit.lower() == 'kg' or unit.lower() == '-kg' and quantity_unit.lower() == 'pint':
        quantity /= 473.176473/1000 
    elif  unit.lower() == 'kg' or unit.lower() == '-kg' and quantity_unit.lower() == 'cups':
        quantity /= 236.5882/1000
        #skdhakhdksahdk 
    elif  unit.lower() == 'ml' or  unit.lower() == '-ml' and quantity_unit.lower() == 'kg':
        quantity /= 1/1000 
    elif  unit.lower() == 'l' or  unit.lower() == '-l' and quantity_unit.lower() == 'kg':
        quantity *= 1000/1000  
    elif  unit.lower() == 'gal'  or unit.lower() == '-gal' and quantity_unit.lower() == 'kg':
        quantity *= 3785.41178/1000   
    elif  unit.lower() == 'qt' or unit.lower() == '-qt' and quantity_unit.lower() == 'kg':
        quantity *= 946.352946/1000  
    elif  unit.lower() == 'pint' or  unit.lower() == '-pint' and quantity_unit.lower() == 'kg':
        quantity *= 473.176473/1000 
    elif  unit.lower() == 'cups' or  unit.lower() == '-cups' and quantity_unit.lower() == 'kg':
        quantity *= 236.5882/1000
        #skdhakhdksahdk 
    elif  unit.lower() == 'mg' or unit.lower() == '-mg' and quantity_unit.lower() == 'ml':
        quantity *= 1*1000  
    elif  unit.lower() == 'mg' or unit.lower() == '-mg' and quantity_unit.lower() == 'l':
        quantity /= 1000*1000 
    elif  unit.lower() == 'mg' or unit.lower() == '-mg' and quantity_unit.lower() == 'gal':
        quantity /= 3785.41178*1000  
    elif  unit.lower() == 'mg' or unit.lower() == '-mg' and quantity_unit.lower() == 'qt' or unit.lower() == '-qt':
        quantity /= 946.352946*1000
    elif  unit.lower() == 'mg' or unit.lower() == '-mg' and quantity_unit.lower() == 'pint':
        quantity /= 473.176473*1000
    elif  unit.lower() == 'mg' or unit.lower() == '-mg' and quantity_unit.lower() == 'cups':
        quantity /= 236.5882*1000
    elif unit.lower() == 'ml' or  unit.lower() == '-ml' and quantity_unit.lower() == 'mg':
        quantity *= 1000
    elif unit.lower() == 'l' or  unit.lower() == '-l' and quantity_unit.lower() == 'mg':
        quantity *= 1000*1000
    elif unit.lower() == 'gal'  or unit.lower() == '-gal' and quantity_unit.lower() == 'mg':
        quantity *= 3785.41178*1000
    elif unit.lower() == 'qt' or unit.lower() == '-qt' and quantity_unit.lower() == 'mg':
        quantity *= 946.352946*1000
    elif unit.lower() == 'pint' or  unit.lower() == '-pint' and quantity_unit.lower() == 'mg':
        quantity *= 473.176473*1000
    elif unit.lower() == 'cups' or  unit.lower() == '-cups' and quantity_unit.lower() == 'mg':
        quantity *= 236.5882*1000
    
    else:
        return None
    
    return quantity
