from django import template
register = template.Library()

@register.filter
def checkoutTotal(value):
    result = 100
    for i in value:
        result += (i.cart_product.product_price * i.quantity) 
    return result

@register.filter
def totalPrice(value):
    result = 0
    for i in value:
        result += (i.cart_product.product_price * i.quantity)
    return result