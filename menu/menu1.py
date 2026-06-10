import firebase_admin
from firebase_admin import credentials, firestore
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

docs = [
{
"name":"那堤 Caffè Latte",
"size":"小杯",
"price":"$115",
"calo":"139大卡" 
},

{
"name":"那堤 Caffè Latte",
"size":"中杯",
"price":"$125",
"calo":"202大卡" 
},

{
"name":"那堤 Caffè Latte",
"size":"大杯",
"price":"$140",
"calo":"295大卡" 
},

{
"name":"那堤 Caffè Latte",
"size":"特大杯",
"price":"$155",
"calo":"325大卡" 
},

{
"name":"美式咖啡 Caffè Americano",
"size":"小杯",
"price":"$85",
"calo":"6大卡" 
},

{
"name":"美式咖啡 Caffè Americano",
"size":"中杯",
"price":"$100",
"calo":"12大卡" 
},

{
"name":"美式咖啡 Caffè Americano",
"size":"大杯",
"price":"$115",
"calo":"18大卡" 
},

{
"name":"美式咖啡 Caffè Americano",
"size":"特大杯",
"price":"$130",
"calo":"34大卡" 
},

{
"name":"焦糖瑪奇朵 Caramel Macchiato",
"size":"中杯",
"price":"$145",
"calo":"264大卡" 
},

{
"name":"焦糖瑪奇朵 Caramel Macchiato",
"size":"大杯",
"price":"$160",
"calo":"355大卡" 
},

{
"name":"焦糖瑪奇朵 Caramel Macchiato",
"size":"特大杯",
"price":"$175",
"calo":"400大卡" 
},

{
"name":"卡布奇諾 Cappuccino",
"size":"中杯",
"price":"$125",
"calo":"152大卡" 
},

{
"name":"卡布奇諾 Cappuccino",
"size":"大杯",
"price":"$140",
"calo":"190大卡" 
},

{
"name":"卡布奇諾 Cappuccino",
"size":"特大杯",
"price":"$155",
"calo":"257大卡" 
},

{
"name":"摩卡 Caffè Mocha",
"size":"中杯",
"price":"$140",
"calo":"455大卡" 
},

{
"name":"摩卡 Caffè Mocha",
"size":"大杯",
"price":"$155",
"calo":"576大卡" 
},

{
"name":"摩卡 Caffè Mocha",
"size":"特大杯",
"price":"$170",
"calo":"710大卡" 
},

{
"name":"特選馥郁那堤 Espresso Choice Extra Shot Latte",
"size":"中杯",
"price":"$150",
"calo":"216大卡" 
},

{
"name":"特選馥郁那堤 Espresso Choice Extra Shot Latte",
"size":"大杯",
"price":"$165",
"calo":"297大卡" 
},

{
"name":"特選馥郁那堤 Espresso Choice Extra Shot Latte",
"size":"特大杯",
"price":"$180",
"calo":"345大卡" 
},

{
"name":"馥列白 Flat White",
"size":"中杯",
"price":"$140",
"calo":"217大卡" 
},

{
"name":"馥列白 Flat White",
"size":"大杯",
"price":"$155",
"calo":"274大卡" 
},

{
"name":"馥列白 Flat White",
"size":"特大杯",
"price":"$170",
"calo":"361大卡" 
},

{
"name":"可可瑪奇朵 Cocoa Macchiato",
"size":"中杯",
"price":"$145",
"calo":"300大卡" 
},

{
"name":"可可瑪奇朵 Cocoa Macchiato",
"size":"大杯",
"price":"$160",
"calo":"383大卡" 
},

{
"name":"可可瑪奇朵 Cocoa Macchiato",
"size":"特大杯",
"price":"$175",
"calo":"499大卡" 
},

{
"name":"冰那堤 Iced Caffè Latte",
"size":"中杯",
"price":"$125",
"calo":"146大卡" 
},

{
"name":"冰那堤 Iced Caffè Latte",
"size":"大杯",
"price":"$140",
"calo":"189大卡" 
},

{
"name":"冰那堤 Iced Caffè Latte",
"size":"特大杯",
"price":"$155",
"calo":"234大卡" 
},

{
"name":"冰美式咖啡 Iced Caffè Americano",
"size":"中杯",
"price":"$100",
"calo":"12大卡" 
},

{
"name":"冰美式咖啡 Iced Caffè Americano",
"size":"大杯",
"price":"$115",
"calo":"18大卡" 
},

{
"name":"冰美式咖啡 Iced Caffè Americano",
"size":"特大杯",
"price":"$130",
"calo":"24大卡" 
},

{
"name":"冰焦糖瑪奇朵 Iced Caramel Macchiato",
"size":"中杯",
"price":"$145",
"calo":"223大卡" 
},

{
"name":"冰焦糖瑪奇朵 Iced Caramel Macchiato",
"size":"大杯",
"price":"$160",
"calo":"330大卡" 
},

{
"name":"冰焦糖瑪奇朵 Iced Caramel Macchiato",
"size":"特大杯",
"price":"$175",
"calo":"362大卡" 
},

{
"name":"雲朵冰搖濃縮咖啡 Cold Foam Iced Espresso",
"size":"中杯",
"price":"$135",
"calo":"118大卡" 
},

{
"name":"雲朵冰搖濃縮咖啡 Cold Foam Iced Espresso",
"size":"大杯",
"price":"$150",
"calo":"131大卡" 
},

{
"name":"雲朵冰搖濃縮咖啡 Cold Foam Iced Espresso",
"size":"特大杯",
"price":"$165",
"calo":"153大卡" 
},

{
"name":"冰摩卡 Iced Caffè Mocha",
"size":"中杯",
"price":"$140",
"calo":"382大卡" 
},

{
"name":"冰摩卡 Iced Caffè Mocha",
"size":"大杯",
"price":"$155",
"calo":"514大卡" 
},

{
"name":"冰摩卡 Iced Caffè Mocha",
"size":"特大杯",
"price":"$170",
"calo":"574大卡" 
},

{
"name":"冰特選馥郁那堤 Espresso Choice Extra Shot Iced Latte",
"size":"中杯",
"price":"$150",
"calo":"162大卡" 
},

{
"name":"冰特選馥郁那堤 Espresso Choice Extra Shot Iced Latte",
"size":"大杯",
"price":"$165",
"calo":"217大卡" 
},

{
"name":"冰特選馥郁那堤 Espresso Choice Extra Shot Iced Latte",
"size":"特大杯",
"price":"$180",
"calo":"239大卡" 
},

{
"name":"冰馥列白 Iced Flat White",
"size":"中杯",
"price":"$140",
"calo":"164大卡" 
},

{
"name":"冰馥列白 Iced Flat White",
"size":"大杯",
"price":"$155",
"calo":"231大卡" 
},

{
"name":"冰馥列白 Iced Flat White",
"size":"特大杯",
"price":"$170",
"calo":"267大卡" 
},

{
"name":"冰可可瑪奇朵 Iced Cocoa Macchiato",
"size":"中杯",
"price":"$145",
"calo":"231大卡" 
},

{
"name":"冰可可瑪奇朵 Iced Cocoa Macchiato",
"size":"大杯",
"price":"$160",
"calo":"302大卡" 
},

{
"name":"冰可可瑪奇朵 Iced Cocoa Macchiato",
"size":"特大杯",
"price":"$175",
"calo":"351大卡" 
},

{
"name":"每日精選咖啡 Brewed Coffee",
"size":"小杯",
"price":"$80",
"calo":"14大卡" 
},

{
"name":"每日精選咖啡 Brewed Coffee",
"size":"中杯",
"price":"$90",
"calo":"23大卡" 
},

{
"name":"每日精選咖啡 Brewed Coffee",
"size":"大杯",
"price":"$100",
"calo":"23大卡" 
},

{
"name":"每日精選咖啡 Brewed Coffee",
"size":"特大杯",
"price":"$110",
"calo":"37大卡" 
},

{
"name":"咖啡密斯朵 Caffè Misto",
"size":"小杯",
"price":"$80",
"calo":"86大卡" 
},

{
"name":"咖啡密斯朵 Caffè Misto",
"size":"中杯",
"price":"$90",
"calo":"131大卡" 
},

{
"name":"咖啡密斯朵 Caffè Misto",
"size":"大杯",
"price":"$100",
"calo":"171大卡" 
},

{
"name":"咖啡密斯朵 Caffè Misto",
"size":"特大杯",
"price":"$110",
"calo":"219大卡" 
}

]

collection_ref = db.collection("星巴克咖啡及那堤菜單")
for doc in docs:
  collection_ref.add(doc)






