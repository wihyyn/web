import firebase_admin
from firebase_admin import credentials, firestore
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

docs = [
{
"name":"紅心芭樂冷萃咖啡 Guava Lemonade Cold Brew",
"size":"中杯",
"price":"$140",
"calo":"169大卡" 
},

{
"name":"紅心芭樂冷萃咖啡 Guava Lemonade Cold Brew",
"size":"大杯",
"price":"$160",
"calo":"247大卡" 
},

{
"name":"紅心芭樂冷萃咖啡 Guava Lemonade Cold Brew",
"size":"特大杯",
"price":"$180",
"calo":"324大卡" 
},

{
"name":"冷萃咖啡 Cold Brew",
"size":"中杯",
"price":"$125",
"calo":"16大卡" 
},

{
"name":"冷萃咖啡 Cold Brew",
"size":"大杯",
"price":"$145",
"calo":"32大卡" 
},

{
"name":"冷萃咖啡 Cold Brew",
"size":"特大杯",
"price":"$165",
"calo":"33大卡" 
},

{
"name":"經典特調冷萃咖啡 Vanilla Sweet Cream Cold Brew",
"size":"中杯",
"price":"$150",
"calo":"163大卡" 
},

{
"name":"經典特調冷萃咖啡 Vanilla Sweet Cream Cold Brew",
"size":"大杯",
"price":"$170",
"calo":"218大卡" 
},

{
"name":"經典特調冷萃咖啡 Vanilla Sweet Cream Cold Brew",
"size":"特大杯",
"price":"$190",
"calo":"274大卡" 
},

{
"name":"香檸蜜柚冷萃咖啡 Ruby Grapefruit and Honey Lemonade Cold Brew",
"size":"中杯",
"price":"$140",
"calo":"168大卡" 
},

{
"name":"香檸蜜柚冷萃咖啡 Ruby Grapefruit and Honey Lemonade Cold Brew",
"size":"大杯",
"price":"$160",
"calo":"202大卡" 
},

{
"name":"香檸蜜柚冷萃咖啡 Ruby Grapefruit and Honey Lemonade Cold Brew",
"size":"特大杯",
"price":"$180",
"calo":"236大卡" 
},

{
"name":"夏日冰柚冷萃咖啡 Honey Ruby Grapefruit Cold Brew",
"size":"中杯",
"price":"$140",
"calo":"332大卡" 
},

{
"name":"夏日冰柚冷萃咖啡 Honey Ruby Grapefruit Cold Brew",
"size":"大杯",
"price":"$160",
"calo":"453大卡" 
},

{
"name":"夏日冰柚冷萃咖啡 Honey Ruby Grapefruit Cold Brew",
"size":"特大杯",
"price":"$180",
"calo":"568大卡" 
},

{
"name":"檸檬冷萃咖啡 Lemonade Cold Brew",
"size":"中杯",
"price":"$140",
"calo":"130大卡" 
},

{
"name":"檸檬冷萃咖啡 Lemonade Cold Brew",
"size":"大杯",
"price":"$160",
"calo":"164大卡" 
},

{
"name":"檸檬冷萃咖啡 Lemonade Cold Brew",
"size":"特大杯",
"price":"$180",
"calo":"198大卡" 
},

{
"name":"鹹焦糖風味氮氣歐蕾 Salted Caramel Flavored Nitro Cold Brew with Milk",
"size":"中杯",
"price":"$170",
"calo":"120大卡" 
},

{
"name":"鹹焦糖風味氮氣歐蕾 Salted Caramel Flavored Nitro Cold Brew with Milk",
"size":"大杯",
"price":"$190",
"calo":"156大卡" 
},

{
"name":"鹹焦糖風味氮氣歐蕾 Salted Caramel Flavored Nitro Cold Brew with Milk",
"size":"特大杯",
"price":"$210",
"calo":"193大卡" 
},

{
"name":"經典特調氮氣冷萃咖啡 Nitro Cold Brew with Vanilla Sweet Cream",
"size":"中杯",
"price":"$180",
"calo":"130大卡" 
},

{
"name":"經典特調氮氣冷萃咖啡 Nitro Cold Brew with Vanilla Sweet Cream",
"size":"大杯",
"price":"$200",
"calo":"174大卡" 
},

{
"name":"經典特調氮氣冷萃咖啡 Nitro Cold Brew with Vanilla Sweet Cream",
"size":"特大杯",
"price":"$220",
"calo":"214大卡" 
},

{
"name":"氮氣冷萃咖啡 Nitro Cold Brew",
"size":"中杯",
"price":"$155",
"calo":"16大卡" 
},

{
"name":"氮氣冷萃咖啡 Nitro Cold Brew",
"size":"大杯",
"price":"$175",
"calo":"21大卡" 
},

{
"name":"氮氣冷萃咖啡 Nitro Cold Brew",
"size":"特大杯",
"price":"$195",
"calo":"26大卡" 
},

{
"name":"氮氣冷萃咖啡歐蕾 Nitro Cold Brew Coffee with Milk",
"size":"中杯",
"price":"$155",
"calo":"64大卡" 
},

{
"name":"氮氣冷萃咖啡歐蕾 Nitro Cold Brew Coffee with Milk",
"size":"大杯",
"price":"$175",
"calo":"82大卡" 
},

{
"name":"氮氣冷萃咖啡歐蕾 Nitro Cold Brew Coffee with Milk",
"size":"特大杯",
"price":"$195",
"calo":"100大卡" 
}

]

collection_ref = db.collection("星巴克星冷萃咖啡菜單")
for doc in docs:
  collection_ref.add(doc)






