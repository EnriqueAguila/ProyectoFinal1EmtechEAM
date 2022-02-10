# Mil gracias por tanta pasciencia Maestro Jimmy
" " "
lifestore_searches = [ id_search , id product ]
lifestore_sales= [ id_sale , id_product , score ( from 1 to 5) , date , refund (1 for true or 0 to false ) ]
lifestore_products = [ id_product , name , price , category , stock ]
 " " "
from sre_parse import CATEGORIES
from unicodedata import category
from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches 

#−−−−−−−−−−−−−−−−−−−LOGIN−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−#
 username = " kikitos "
 password = " felino "
 tries = 0 ; Acces = False

while not Acces :
    tries += 1

    if tries == 4 :
        exit ( )
    if input ( ’ Username : ’ ) == username and input ( ’ Password : ’ ) == password :
        Acces = True
        print ( ’ Acces Granted ’ )
else :
     print (f ’You have {3 − tries } tries lefts’ )

#−−−−−−−−−−−−−−−−−−−−−−−−−Ventas−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−#
soldproduct = [ ] ; timesold = [ ]

soldproduct = [ sale [1] for sale in lifestore_sales ]

for sale in lifestore_products : # Creación de lista anidada
    nested =[]
    timesold . append ( nested )
    for k in range (1) :
        nested . append ( sale [0] )
        nested . append ( sale [1] )
        nested . append ( soldproduct . count (sale [0])) #Conteo de veces vendidas
        nested . append ( sale  [−2])

def Sort ( timesold ) : #tiempo de estancia antiguo [ id_product , name , time_sold , category ]
    timesold . s o r t ( key = lambda x : x [ 2 ] )
    return timesold

timesold = Sort ( timesold ) # Orden ascendente

print ( " \n MOST SOLD PRODUCTS" )
for i in [−1,−2,−3,−4,−5]:
    print ( F ’ID : { timesold [ i ] [ 0 ] } \ t NAME: { timesold [i] [1] } \ t SALES: { timesold [i] [2] } ’ )

#print ("\ n LEAST SOLD PRODUCTS" )

#for i in range (0 ,5) :
#print ( F ’ID : { timesold [i] [0]} \ t NAME: { timesold [i] [1] } \ t SALES: { timesold [i] [2] } ’ )

#−−−−−−−−−−−−−−−−−−−−−−−−−Ventas por categoria−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−#
categories= [ ]
procesors = [ ] ; gpus = [ ] ; motherboards = [ ] ; drives = [ ] ; usb = [ ] ; screns = [ ] ; speakers = [ ] ; headphones = [ ]

CATEGORIES= [ item [−2] for item in lifestore_products]

category = list ( dict.from keys ( CATEGORIES ) )

for item in timesold :
    if CATEGORIES [0] in item :
        processors.append ( item [:3] )
    elif CATEGORIES [1] in item :
        gpus.append ( item [:3] )
    elif CATEGORIES [2] in item :
        motherboards.append ( item [:3] )
    elif CATEGORIES [3] in item :
        drives. append ( item [:3] )
    elif CATEGORIES [4] in item :
        usb.append ( item [:3] )
    elif CATEGORIES [5] in item :
        screens.append ( item [:3] )
    elif CATEGORIES [6] in item :
        speakers.append ( item [:3] )
    elif CATEGORIES [7] in item :
        headphones.append ( item [:3] )

print ( " \n LEAST SOLD PROCESSORS" )
for i in range (5) :
    print ( f "ID : { processors [i] [0] } \ t NAME: { processors [i] [1] } \ t TIMES SOLD: {processors [i][ −1]} " )

print ( " \n LEAST SOLD GPUS" )
for i in range (5) :
    print ( f "ID : {gpus [i] [0] } \ t NAME: {gpus [i] [1] } \ t TIMES SOLD: {gpus [i][−1]} ")

print ( " \n LEAST SOLD MOTHERBOARDS" )
for i in range (5) :
    print ( f "ID : { motherboards [i] [0] } \ t NAME: { motherboards [i] [1] } \ t TIMES SOLD: {motherboards [ i ][ −1]} " )

print ( " \n LEAST SOLD DRIVES" )
for i in range (5) :
    print ( f "ID : { drives [i] [0] } \ t NAME: { drives [i] [1] } \ t TIMES SOLD: { d r i v e s [i][ −1]}" )

print ( " \n LEAST SOLD USB" )
for i in range (2) :
    print ( f "ID : {usb [i] [0] } \ t NAME: {usb [i] [1] } \ t TIMES SOLD: {usb [i][ −1]} " )

print ( " \n LEAST SOLD SCREENS" )
for i in range (5) :
    print ( f "ID : { screens [i] [0] } \ t NAME: { screens [i] [1] } \ t TIMES SOLD: { screens [i][ −1]} " )

print ( " \n LEAST SOLD SPEAKERS" )
for i in range (5) :
    print ( f "ID : { speakers [i] [0] } \ t NAME: { speakers [i] [1] } \ t TIMES SOLD: { speakers [i][ −1]} " )

print ( " \n LEAST SOLD HEADPHONES" )
for i in range (5) :
    print ( f "ID : {headphones [i] [0] } \ t NAME: {headphones [i] [1] } \ t TIMES SOLD: {headphones [ i ][ −1]} " )

#−−−−−−−−−−−−−−−−−−−−−−−−−Searches−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−#
searchedproduct = [ ] ; timesearched = [ ]

searchedproduct = [ search [ 1 ] for search in lifestore_searches]

for search in lifestore_products : # Creación de una lista anidada
    nested =[]
    timesearched.append ( nested )
    for k in range (1) :
        nested.append ( search [0] ) #Saving ID
        nested.append ( search [1] ) #Saving Name
        nested.append ( searchedproduct . count ( search [ 0 ] ) ) #Contando las veces buscadas
        nested.append ( search [−2]) # Guardar categoria

def Sort ( timesearched ) :
    timesearched.sort ( key = lambda x : x [ 2 ] )
    return timesearched

timesearched = Sort ( timesearched )

print ( " \n MOST SEARCHED PRODUCTS" )
for i in [−1,−2,−3,−4,−5]:
    print ( F ’ID : { timesearched [i] [0] } \ t NAME: {timesearched [i] [1]} \ t SEARCHES: {timesearched [i][ −2]} ’ )

#print ("\ n LEAST SEARCHED PRODUCTS" )
#for i in range (0 ,10) :
# print ( F ’ID : { timesearched [i] [0] } \ t NAME: { timesearched [i] [1] } \ t SEARCHES: {timesearched [i][−1]} ’ )

#−−−−−−−−−−−−−−−−−−−−−−−−−Busquedas por Categorias−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−#
processors 2 = [ ] ; gpus2 = [ ] ; motherboards2 = [ ] ; drives2 = [ ] ; usb2 = [ ] ; screens2= [ ] ; speakers2 = [ ] ; headphones2 = [ ]

for item in timesearched :
    if CATEGORIES [0] in item :
        processors 2.append ( item [:3])
    elif CATEGORIES [1] in item 
        gpus2.append ( item [:3] )
    elif CATEGORIES [2] in item :
        motherboards2.append ( item [:3])
    elif CATEGORIES [3] in item :
        drives2 . append ( item [:3] )
    elif CATEGORIES [4] in item :
        usb2.append ( item [:3] )
    elif CATEGORIES [5] in item :
        screens2.append (item [:3] )
    elif CATEGORIES [6] in item :
        speakers2.append (item [:3] )
    elif CATEGORIES [7] in item :
        headphones2.append (item [:3] )

print ( " \n LEAST SEARCHED PROCESSORS" )
for i in range (9) :
    print ( f "ID : { processors 2 [i] [0] } \ t NAME: { processors 2 [i] [1] } \ t TIMES SEARCHED: {processors 2 [i][−1]} " )

print ( " \n LEAST SEARCHED GPUS" )
for i in range (10) :
    print ( f "ID : {gpus2 [i] [0] } \ t NAME: {gpus2 [i] [1] } \ t TIMES SEARCHED: {gpus2 [i] [2] }" )

print ( " \n LEAST SEARCHED MOTHERBOARDS" )
for i in range (10) :
    print ( f "ID : { motherboards2 [i] [0] } \ t NAME: { motherboards2 [i] [1] } \ t TIMES SEARCHED: { motherboards2 [i][ −1]} " )

print ( " \n LEAST SEARCHED DRIVES" )
for i in range (10) :
    print ( f "ID : { drives2 [i] [0] } \ t NAME: { drives2 [i] [1] } \ t TIMES SEARCHED: { drives2 [i][ −1]} " )

print ( " \n LEAST SEARCHED USB" )
for i in range (2) :
    print ( f "ID : {usb2 [i] [0] } \ t NAME: {usb2 [i] [1] } \ t TIMES SEARCHED: {usb2 [i][ −1]} " )

print ( " \n LEAST SEARCHED SCREENS" )
for i in range (10) :
    print ( f "ID : { screens2 [i] [0] } \ t NAME: { screens2 [i] [1] } \ t TIMES SEARCHED: {screens2 [i][ −1]} " )

print ( " \n LEAST SEARCHED SPEAKERS" )
for i in range (10) :
    print ( f "ID : { speakers2 [i] [0] } \ t NAME: { speakers2 [i] [1] } \ t TIMES SEARCHED: {speakers2 [i][ −1]} " )

print ( " \n LEAST SEARCHED HEADPHONES" )
for i in range (10) :
    print ( f "ID : {headphones2 [i] [0] } \ t NAME: {headphones2 [i] [1] } \ t TIMES SEARCHED: {headphones2 [1][ −1]} " )

#−−−−−−−−−−−−−−−−−−−−−−REVIEWS-NOW−−−−−−−−−−−−−−−−−−−−−−−−−−#
tempsum=0; t o t a l s c o r e = [ ] ; averagescore = [ ]

" " " 
for i in range (0 , len ( l i f e s t o r e _ p r o d u c t s )): for k in range (0, len ( lifestore_sales ) ) :
 if lifestore_sales [ k][1]== timesold [i] [0] :
tempsum += lifestore_sales[ k ] [2] #Sumar puntajes de revisión

totalscore.append (tempsum)
tempsum=0 
" " "

for product in lifestore_products:
    for review in lifestore_sales:
        if product [0]== review [ 1 ]:
            tempsum += review [ 2 ] #Sumar puntajes de revisión

totalscore.append (tempsum) 
tempsum=0 

#timesold i s [ id_product , name , time_sold , category ]

" " " for review in lifestore_products: # Creación de una lista anidada " " "
       nested =[]
       if timesold [review [ 0 ] − 1 ] [2] > 0 : # Obtener reseñas de productos vendidos al menos una vez
            averagescore . append (nested)
            for k in range (1) :
                nested.append ( review [0] )
                nested.append ( review [1] )
                nested.append ( timesold [ review [0]−1] [2] ) # Tiempos revisados
                nested.append ( totalscore [review [0]−1]/ timesold [ review [0] −1] [2] ) 
     # Obteniendo promedio
" " "
for review in timesold : # Creación de una lista anidada
    nested =[]
    if review [2] > 0 : # Obtener reseñas de productos vendidos al menos una vez
        averagescore.append ( nested )
        for k in range (1) :
            nested.append ( review [0] )
            nested.append ( review [1] )
            nested.append ( review [2] ) # Tiempos revisados
            nested.append ( totalscore [review [0]−1]/ review[2] ) #se hace la inteaccion

def Sort ( averagescore ) :
    averagescore . s o r t ( key = lambda x : x [ −1])
    return averagescore

averagescore = Sort ( averagescore )

print ( " \n BEST RATED PRODUCTS" )
for i in range (−1,−11,−1) :
    print ( F ’ID : {averagescore [i] [0] } \ t NAME: { averagescore [i] [1] } \ t SCORE: {averagescore [i][−1]}\ t TIMES REVIEWED: { averagescore [ i ] [ 2 ] } ’ )

print ( " \n WORST RATED PRODUCTS" )
for i in range (0 ,10) :
print ( F ’ID : { averagescore [i] [0] } \ t NAME: { averagescore [ i ] [ 1 ] } \ t SCORE: {averagescore [i][−1]}\ t TIMES REVIEWED: {averagescore [i] [2] } ’ )

#−−−−−−−−−−−−−−−−−−−−−−Ventas por mes−−−−−−−−−−−−−−−−−−−−−−−−−−#
from datetime import datetime ; import calendar
date = [ sale [3] for sale in lifestore_sales ]
date.sort ( key = lambda date : datetime.strptime ( date , ’%d/%m/%Y’ ) ) # Ordenar las fechas en orden

month =calendar.month_name [1:]

refundeditem = [ ] ; total refunds = 0 ; average ticket = [ ]
totalsales = 0 ; monthsales = [ 0 ] ∗ 1 2 ; monthprofit = [0] ∗ 1 2

soldproduct = [ sale [1] for sale in lifestore_sales ]

for i in range (0 , len ( lifestore_sales ) ) :
    if int ( lifestore_sales [ i ][ −1]) == 0: # Verificando que no fue un reembolso
        total sales += lifestore_products [ soldproduct [i]] [2] # sumando las ventas totales
        if " /01/ " in date [i] :
             monthprofit [0]+= lifestore_products [ soldproduct [ ]] [2]
             monthsales [0]+=1
        elif " /02/ " in date [i] :
             monthprofit [1]+= lifestore_products [ soldproduct [i]] [2]
             monthsales [1]+=1
        elif " /03/ " in date [i] :
             monthprofit [2]+= lifestore_products [ soldproduct [i]] [2]
             monthsales [2]+=1
        elif " /04/ " in date [i] :
             monthprofit [3]+= lifestore_products [ soldproduct [i]] [2]
             monthsales [3]+=1
        elif " /05/ " in date [i] :
             monthprofit [4]+= lifestore_products [ soldproduct [i]] [2]
             monthsales [4]+=1
        elif " /06/ " in date [i] :
             monthprofit [5]+= lifestore_products [ soldproduct [i]] [2]
             monthsales [5]+=1
        elif " /07/ " in date [i] :
             monthprofit [6]+= lifestore_products [ soldproduct [i]] [2]
             monthsales [6]+=1
        elif " /08/ " in date [i] :
             monthprofit [7]+= lifestore_products [ soldproduct [i]] [2]
             monthsales [7]+=1
        elif " /09/ " in date [i] :
             monthprofit [8]+= lifestore_products [ soldproduct [i]] [2]
             monthsales [8]+=1
        elif " /10/ " in date [i] :
             monthsales [9]+= lifestore_products [ soldproduct [i]] [2]
             monthsales [9]+=1
        elif " /11/ " in date [ i ] :
             monthprofit [10]+= lifestore_products [ soldproduct [i]] [2]
             monthsales [10]+=1
        elif " /12/ " in date [ i ] :
             monthprofit [11]+= lifestore_products [ soldproduct [i]] [2]
             monthsales [11]+=1
    else:
        refundeditem.append ( soldproduct [i] )   # ID deProducto reembolsado
        total refunds+=lifestore_products [ soldproduct [i] ] [2] # Total perdida en reembolsos
303
for i in range (12) :
    if monthsales [ i ] > 0 :
        averageticket.append(monthprofit [i] /monthsales [i] ) # Obteniendo promedio
    else:
        averageticket.append (0)

salesxmonth = [list (l) for l in zip (month , monthprofit , monthsales , averageticket) ]

def Sort (salesxmonth) : # ordenar con fin de lucro
    salesxmonth.sort (key = lambda x : x [1])
    return salesxmonth
salesxmonth = Sort (salesxmonth)

print ( " \n MOST PROFITABLE MONTHS" )
for i in [−1,−2,−3,−4,−5]:
    print (F ’MONTH: {salesxmonth [i] [0]} \ t PROFIT: {" $ { : ,. 2 f } ". format ( salesxmonth [i] [1] ) }\ t SALES: { salesxmonth [ i ] [ 2 ] } \ t AVERAGE: { salesxmonth [ i ][ −1]} ’ )

def Sort (salesxmonth ) : # ordenar por ventas
    salesxmonth.sort ( key = lambda x : x [2] )
    return salesxmonth
salesxmonth = Sort ( salesxmonth )

print ( " \n MOST SALES PER MONTHS" )
for i in [−1,−2,−3,−4,−5]:
    print (F ’MONTH: { salesxmonth [i] [0] } \ t PROFIT: {" $ { : , . 2 f } ". format ( salesxmonth [i] [1] ) }\ t SALES: {salesxmonth [i] [2] } \ t AVERAGE: {salesxmonth [i][−1]} ’)

def Sort (salesxmonth) : # Ordenar por promedio
    salesxmonth.sort (key = lambda x : x [ −1])
    return salesxmonth
salesxmonth = Sort (salesxmonth)

print (" \n HIGHEST AVERAGE TICKET PER MONTH")
for i in [−1,−2,−3,−4,−5]:
    print (F ’MONTH:{ salesxmonth [i] [0] } \ t PROFIT: {" $ { : ,. 2 f } ". format (salesxmonth [i] [1])}\ t SALES: {salesxmonth [i] [2] } \ t AVERAGE: { salesxmonth [i][ −1]} ’)

