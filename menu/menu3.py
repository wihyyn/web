import firebase_admin
from firebase_admin import credentials, firestore
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

docs = [
{
"name":"咖啡星冰樂 Coffee Frappuccino Blended Beverage",
"size":"中杯",
"price":"$115",
"calo":"224大卡" 
},

{
"name":"咖啡星冰樂 Coffee Frappuccino Blended Beverage",
"size":"大杯",
"price":"$135",
"calo":"289大卡" 
},

{
"name":"咖啡星冰樂 Coffee Frappuccino Blended Beverage",
"size":"特大杯",
"price":"$155",
"calo":"512大卡" 
},

{
"name":"焦糖星冰樂 Caramel Frappuccino Blended Beverage",
"size":"中杯",
"price":"$140",
"calo":"427大卡" 
},

{
"name":"焦糖星冰樂 Caramel Frappuccino Blended Beverage",
"size":"大杯",
"price":"$160",
"calo":"587大卡" 
},

{
"name":"焦糖星冰樂 Caramel Frappuccino Blended Beverage",
"size":"特大杯",
"price":"$180",
"calo":"675大卡" 
},

{
"name":"摩卡可可碎片星冰樂 Java Chip Frappuccino Blended Beverage",
"size":"中杯",
"price":"$155",
"calo":"353大卡" 
},

{
"name":"摩卡可可碎片星冰樂 Java Chip Frappuccino Blended Beverage",
"size":"大杯",
"price":"$175",
"calo":"562大卡" 
},

{
"name":"摩卡可可碎片星冰樂 Java Chip Frappuccino Blended Beverage",
"size":"特大杯",
"price":"$195",
"calo":"620大卡" 
},

{
"name":"焦糖可可碎片星冰樂 Caramel Java Chip Frappuccino Blended Beverage",
"size":"中杯",
"price":"$155",
"calo":"486大卡" 
},

{
"name":"焦糖可可碎片星冰樂 Caramel Java Chip Frappuccino Blended Beverage",
"size":"大杯",
"price":"$175",
"calo":"656大卡" 
},

{
"name":"焦糖可可碎片星冰樂 Caramel Java Chip Frappuccino Blended Beverage",
"size":"特大杯",
"price":"$195",
"calo":"783大卡" 
},

{
"name":"巧克力可可碎片星冰樂 Chocolate Cream Java Chip Frappuccino Blended Beverage",
"size":"中杯",
"price":"$130",
"calo":"371大卡" 
},

{
"name":"巧克力可可碎片星冰樂 Chocolate Cream Java Chip Frappuccino Blended Beverage",
"size":"大杯",
"price":"$150",
"calo":"494大卡" 
},

{
"name":"巧克力可可碎片星冰樂 Chocolate Cream Java Chip Frappuccino Blended Beverage",
"size":"特大杯",
"price":"$170",
"calo":"583大卡" 
},

{
"name":"醇濃抹茶星冰樂 Pure Matcha Cream Frappuccino Blended Beverage",
"size":"中杯",
"price":"$155",
"calo":"345大卡" 
},

{
"name":"醇濃抹茶星冰樂 Pure Matcha Cream Frappuccino Blended Beverage",
"size":"大杯",
"price":"$175",
"calo":"487大卡" 
},

{
"name":"醇濃抹茶星冰樂 Pure Matcha Cream Frappuccino Blended Beverage",
"size":"特大杯",
"price":"$195",
"calo":"559大卡" 
},

{
"name":"香草風味星冰樂 Vanilla Cream Frappuccino Blended Beverage",
"size":"中杯",
"price":"$105",
"calo":"347大卡" 
},

{
"name":"香草風味星冰樂 Vanilla Cream Frappuccino Blended Beverage",
"size":"大杯",
"price":"$125",
"calo":"480大卡" 
},

{
"name":"香草風味星冰樂 Vanilla Cream Frappuccino Blended Beverage",
"size":"特大杯",
"price":"$145",
"calo":"561大卡" 
},

{
"name":"雙果果汁星冰樂 Mango Passion Fruit Blended Juice Drink",
"size":"中杯",
"price":"$125",
"calo":"182大卡" 
},

{
"name":"雙果果汁星冰樂 Mango Passion Fruit Blended Juice Drink",
"size":"大杯",
"price":"$145",
"calo":"239大卡" 
},

{
"name":"雙果果汁星冰樂 Mango Passion Fruit Blended Juice Drink",
"size":"特大杯",
"price":"$165",
"calo":"319大卡" 
}

]

collection_ref = db.collection("星巴克星冰樂咖啡菜單")
for doc in docs:
  collection_ref.add(doc)






