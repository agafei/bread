
products = {
    "americano":{"name":"Americano","price":150.00},
    "brewedcoffee":{"name":"Brewed Coffee","price":110.00},
    "cappuccino":{"name":"Cappuccino","price":170.00},
    "dalgona":{"name":"Dalgona","price":170.00},
    "espresso":{"name":"Espresso","price":140.00},
    "frappuccino":{"name":"Frappuccino","price":170.00},
}

def get_product(code):

    return products[code]


def get_property(code,property):

    return float(products[code][property])


def main():
    with open('receipt01.txt','a+') as f:
        total=0
        y=0
        final={}
        f.write('\n==\n')
        f.write('CODE\t\t\tNAME\t\t\tQUANTITY\t\t\tSUBTOTAL\n')

        while True:
            order=input('{product_code},{quantity}: ')
            if order!='/':
                code=order.split(',')[0]
                quantity=order.split(',')[1]
                subtotal=get_property(code,'price')*float(quantity)
                check=code in final
                total=total+subtotal
                if check==True:
                    final[code]['quantity']+=quantity
                    final[code]['subtotal']+=subtotal
                else:
                    final[code]=get_product(code)
                    final[code]['quantity']=quantity
                    final[code]['subtotal']=subtotal
            else:
                sorted_final=sorted(final)

                while y<len(final):
                    f.write(sorted_final[y]+'\t\t')
                    if len(list(final[sorted_final[y]]['name']))>8:
                        f.write(final[sorted_final[y]]['name']+'\t\t')
                    else:
                        f.write('\t'+final[sorted_final[y]]['name']+'\t\t\t')
                    f.write(str(final[sorted_final[y]]['quantity'])+'\t\t\t')
                    f.write(str(final[sorted_final[y]]['subtotal'])+'\n')
                    y+=1
                f.write('\nTotal:\t\t\t\t\t\t\t\t\t'+str(total))
                f.write('\n==')
                f.close()
                break
main()
