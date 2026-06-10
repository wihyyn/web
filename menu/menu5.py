import firebase_admin
from firebase_admin import credentials, firestore
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

docs = [
{
"name":"草莓巴西莓風味冰雪星沁爽 Frozen Strawberry Acai Lemonade Starbucks Refreshers Beverage",
"size":"中杯",
"price":"$115",
"calo":"176大卡" 
},

{
"name":"草莓巴西莓風味冰雪星沁爽 Frozen Strawberry Acai Lemonade Starbucks Refreshers Beverage",
"size":"大杯",
"price":"$130",
"calo":"228大卡" 
},

{
"name":"草莓巴西莓風味冰雪星沁爽 Frozen Strawberry Acai Lemonade Starbucks Refreshers Beverage",
"size":"特大杯",
"price":"$145",
"calo":"281大卡" 
},

{
"name":"芒果火龍果冰雪星沁爽 Frozen Mango Dragonfruit Lemonade Starbucks Refreshers Beverage",
"size":"中杯",
"price":"$115",
"calo":"200大卡" 
},

{
"name":"芒果火龍果冰雪星沁爽 Frozen Mango Dragonfruit Lemonade Starbucks Refreshers Beverage",
"size":"大杯",
"price":"$130",
"calo":"256大卡" 
},

{
"name":"芒果火龍果冰雪星沁爽 Frozen Mango Dragonfruit Lemonade Starbucks Refreshers Beverage",
"size":"特大杯",
"price":"$145",
"calo":"313大卡" 
},

{
"name":"蘋果山竹風味爆爆檸檬星沁爽 APPLE MANGOSTEEN WITH GLITTER POP LEMONADE STARBUCKS REFRESHERS BEVERAGE",
"size":"中杯",
"price":"$110",
"calo":"153大卡" 
},

{
"name":"蘋果山竹風味爆爆檸檬星沁爽 APPLE MANGOSTEEN WITH GLITTER POP LEMONADE STARBUCKS REFRESHERS BEVERAGE",
"size":"大杯",
"price":"$125",
"calo":"224大卡" 
},

{
"name":"蘋果山竹風味爆爆檸檬星沁爽 APPLE MANGOSTEEN WITH GLITTER POP LEMONADE STARBUCKS REFRESHERS BEVERAGE",
"size":"特大杯",
"price":"$140",
"calo":"264大卡" 
},

{
"name":"蘋果山竹風味爆爆椰奶星沁爽 PURPLE RUBY POP DRINK WITH APPLE MANGOSTEEN STARBUCKS REFRESHERS BEVERAGE (made with coconutmilk)",
"size":"中杯",
"price":"$120",
"calo":"175大卡" 
},

{
"name":"蘋果山竹風味爆爆椰奶星沁爽 PURPLE RUBY POP DRINK WITH APPLE MANGOSTEEN STARBUCKS REFRESHERS BEVERAGE (made with coconutmilk)",
"size":"大杯",
"price":"$135",
"calo":"240大卡" 
},

{
"name":"蘋果山竹風味爆爆椰奶星沁爽 PURPLE RUBY POP DRINK WITH APPLE MANGOSTEEN STARBUCKS REFRESHERS BEVERAGE (made with coconutmilk)",
"size":"特大杯",
"price":"$150",
"calo":"305大卡" 
},

{
"name":"芒果火龍果檸檬星沁爽 Mango Dragonfruit with Lemonade Starbucks Refreshers Beverage",
"size":"中杯",
"price":"$95",
"calo":"175大卡" 
},

{
"name":"芒果火龍果檸檬星沁爽 Mango Dragonfruit with Lemonade Starbucks Refreshers Beverage",
"size":"大杯",
"price":"$110",
"calo":"224大卡" 
},

{
"name":"芒果火龍果檸檬星沁爽 Mango Dragonfruit with Lemonade Starbucks Refreshers Beverage",
"size":"特大杯",
"price":"$125",
"calo":"273大卡" 
},

{
"name":"芒果火龍果椰奶星沁爽 Dragon Drink with Mango Dragonfruit Starbucks Refreshers Beverage (made with coconutmilk)",
"size":"中杯",
"price":"$105",
"calo":"162大卡" 
},

{
"name":"芒果火龍果椰奶星沁爽 Dragon Drink with Mango Dragonfruit Starbucks Refreshers Beverage (made with coconutmilk)",
"size":"大杯",
"price":"$120",
"calo":"207大卡" 
},

{
"name":"芒果火龍果椰奶星沁爽 Dragon Drink with Mango Dragonfruit Starbucks Refreshers Beverage (made with coconutmilk)",
"size":"特大杯",
"price":"$135",
"calo":"252大卡" 
},

{
"name":"草莓巴西莓檸檬風味星沁爽 Strawberry Acai with Lemonade Starbucks Refreshers",
"size":"中杯",
"price":"$95",
"calo":"155大卡" 
},

{
"name":"草莓巴西莓檸檬風味星沁爽 Strawberry Acai with Lemonade Starbucks Refreshers",
"size":"大杯",
"price":"$110",
"calo":"201大卡" 
},

{
"name":"草莓巴西莓檸檬風味星沁爽 Strawberry Acai with Lemonade Starbucks Refreshers",
"size":"特大杯",
"price":"$125",
"calo":"246大卡" 
},

{
"name":"草莓巴西莓椰奶風味星沁爽 Pink Drink with Strawberry Acai Starbucks Refreshers (made with coconut milk)",
"size":"中杯",
"price":"$105",
"calo":"250大卡" 
},

{
"name":"草莓巴西莓椰奶風味星沁爽 Pink Drink with Strawberry Acai Starbucks Refreshers (made with coconut milk)",
"size":"大杯",
"price":"$120",
"calo":"328大卡" 
},

{
"name":"草莓巴西莓椰奶風味星沁爽 Pink Drink with Strawberry Acai Starbucks Refreshers (made with coconut milk)",
"size":"特大杯",
"price":"$135",
"calo":"403大卡" 
}

]

collection_ref = db.collection("星巴克星星沁爽菜單")
for doc in docs:
  collection_ref.add(doc)






