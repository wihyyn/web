import firebase_admin
from firebase_admin import credentials, firestore
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

docs = [
{
"name":"福吉茶那堤 Hojicha Tea Latte",
"size":"中杯",
"price":"$140",
"calo":"376大卡" 
},

{
"name":"福吉茶那堤 Hojicha Tea Latte",
"size":"大杯",
"price":"$155",
"calo":"509大卡" 
},

{
"name":"福吉茶那堤 Hojicha Tea Latte",
"size":"特大杯",
"price":"$170",
"calo":"656大卡" 
},

{
"name":"經典紅茶那堤 Black Tea Latte",
"size":"中杯",
"price":"$140",
"calo":"203大卡" 
},

{
"name":"經典紅茶那堤 Black Tea Latte",
"size":"大杯",
"price":"$155",
"calo":"279大卡" 
},

{
"name":"經典紅茶那堤 Black Tea Latte",
"size":"特大杯",
"price":"$170",
"calo":"344大卡" 
},

{
"name":"醇濃抹茶那堤 Pure Matcha Latte",
"size":"中杯",
"price":"$145",
"calo":"331大卡" 
},

{
"name":"醇濃抹茶那堤 Pure Matcha Latte",
"size":"大杯",
"price":"$160",
"calo":"443大卡" 
},

{
"name":"醇濃抹茶那堤 Pure Matcha Latte",
"size":"特大杯",
"price":"$175",
"calo":"570大卡" 
},

{
"name":"伯爵茶那堤 Earl Grey Tea Latte",
"size":"中杯",
"price":"$140",
"calo":"226大卡" 
},

{
"name":"伯爵茶那堤 Earl Grey Tea Latte",
"size":"大杯",
"price":"$155",
"calo":"296大卡" 
},

{
"name":"伯爵茶那堤 Earl Grey Tea Latte",
"size":"特大杯",
"price":"$170",
"calo":"373大卡" 
},

{
"name":"玫瑰蜜香茶那堤 Rose Fancy Tea Latte",
"size":"中杯",
"price":"$140",
"calo":"203大卡" 
},

{
"name":"玫瑰蜜香茶那堤 Rose Fancy Tea Latte",
"size":"大杯",
"price":"$155",
"calo":"279大卡" 
},

{
"name":"玫瑰蜜香茶那堤 Rose Fancy Tea Latte",
"size":"特大杯",
"price":"$170",
"calo":"344大卡" 
},

{
"name":"冰福吉茶那堤 Iced Hojicha Tea Latte",
"size":"中杯",
"price":"$140",
"calo":"257大卡" 
},

{
"name":"冰福吉茶那堤 Iced Hojicha Tea Latte",
"size":"大杯",
"price":"$155",
"calo":"358大卡" 
},

{
"name":"冰福吉茶那堤 Iced Hojicha Tea Latte",
"size":"特大杯",
"price":"$170",
"calo":"458大卡" 
},

{
"name":"冰醇濃抹茶那堤 Iced Pure Matcha Latte",
"size":"中杯",
"price":"$145",
"calo":"208大卡" 
},

{
"name":"冰醇濃抹茶那堤 Iced Pure Matcha Latte",
"size":"大杯",
"price":"$160",
"calo":"295大卡" 
},

{
"name":"冰醇濃抹茶那堤 Iced Pure Matcha Latte",
"size":"特大杯",
"price":"$175",
"calo":"362大卡" 
},

{
"name":"冰玫瑰蜜香茶那堤 Iced Rose Fancy Tea Latte",
"size":"中杯",
"price":"$140",
"calo":"169大卡" 
},

{
"name":"冰玫瑰蜜香茶那堤 Iced Rose Fancy Tea Latte",
"size":"大杯",
"price":"$155",
"calo":"216大卡" 
},

{
"name":"冰玫瑰蜜香茶那堤 Iced Rose Fancy Tea Latte",
"size":"特大杯",
"price":"$170",
"calo":"277大卡" 
},

{
"name":"冰經典紅茶那堤 Iced Black Tea Latte",
"size":"中杯",
"price":"$140",
"calo":"169大卡" 
},

{
"name":"冰經典紅茶那堤 Iced Black Tea Latte",
"size":"大杯",
"price":"$155",
"calo":"216大卡" 
},

{
"name":"冰經典紅茶那堤 Iced Black Tea Latte",
"size":"特大杯",
"price":"$170",
"calo":"277大卡" 
},

{
"name":"洋甘菊花草茶 Chamomile Herbal Blend",
"size":"中杯",
"price":"$120",
"calo":"2.8大卡" 
},

{
"name":"洋甘菊花草茶 Chamomile Herbal Blend",
"size":"特大杯",
"price":"$160",
"calo":"4.2大卡" 
},

{
"name":"英式紅茶 English Breakfast Black Tea",
"size":"中杯",
"price":"$120",
"calo":"5大卡" 
},

{
"name":"英式紅茶 English Breakfast Black Tea",
"size":"特大杯",
"price":"$160",
"calo":"10.1大卡" 
},

{
"name":"熱蜜柚紅茶 Black Tea with Ruby Grapefruit and Honey",
"size":"中杯",
"price":"$135",
"calo":"192大卡" 
},

{
"name":"熱蜜柚紅茶 Black Tea with Ruby Grapefruit and Honey",
"size":"大杯",
"price":"$150",
"calo":"281大卡" 
},

{
"name":"熱蜜柚紅茶 Black Tea with Ruby Grapefruit and Honey",
"size":"特大杯",
"price":"$165",
"calo":"370大卡" 
},

{
"name":"冰搖紅茶 Iced Shaken Black Tea",
"size":"中杯",
"price":"$105",
"calo":"55大卡" 
},

{
"name":"冰搖紅茶 Iced Shaken Black Tea",
"size":"大杯",
"price":"$115",
"calo":"83大卡" 
},

{
"name":"冰搖紅茶 Iced Shaken Black Tea",
"size":"特大杯",
"price":"$125",
"calo":"110大卡" 
},

{
"name":"冰搖檸檬果茶 Iced Shaken Lemon Passion Tea",
"size":"中杯",
"price":"$120",
"calo":"113大卡" 
},

{
"name":"冰搖檸檬果茶 Iced Shaken Lemon Passion Tea",
"size":"大杯",
"price":"$130",
"calo":"162大卡" 
},

{
"name":"冰搖檸檬果茶 Iced Shaken Lemon Passion Tea",
"size":"特大杯",
"price":"$140",
"calo":"209大卡" 
},

{
"name":"阿里山蜜柚烏龍青茶 Ruby Grapefruit Alishan Oolong Tea",
"size":"中杯",
"price":"$155",
"calo":"186大卡" 
},

{
"name":"阿里山蜜柚烏龍青茶 Ruby Grapefruit Alishan Oolong Tea",
"size":"大杯",
"price":"$170",
"calo":"319大卡" 
},

{
"name":"阿里山蜜柚烏龍青茶 Ruby Grapefruit Alishan Oolong Tea",
"size":"特大杯",
"price":"$185",
"calo":"335大卡" 
},

{
"name":"冰蜜柚紅茶 Iced Shaken Black Tea with Ruby Grapefruit and Honey",
"size":"中杯",
"price":"$135",
"calo":"178大卡" 
},

{
"name":"冰蜜柚紅茶 Iced Shaken Black Tea with Ruby Grapefruit and Honey",
"size":"大杯",
"price":"$150",
"calo":"266大卡" 
},

{
"name":"冰蜜柚紅茶 Iced Shaken Black Tea with Ruby Grapefruit and Honey",
"size":"特大杯",
"price":"$165",
"calo":"355大卡" 
},

{
"name":"冰搖檸檬紅茶 Iced Shaken Lemon Black Tea",
"size":"中杯",
"price":"$120",
"calo":"113大卡" 
},

{
"name":"冰搖檸檬紅茶 Iced Shaken Lemon Black Tea",
"size":"大杯",
"price":"$130",
"calo":"162大卡" 
},

{
"name":"冰搖檸檬紅茶 Iced Shaken Lemon Black Tea",
"size":"特大杯",
"price":"$140",
"calo":"209大卡" 
},

{
"name":"冰阿里山烏龍茶 Iced Alishan Oolong Tea",
"size":"中杯",
"price":"$150",
"calo":"3.5大卡" 
},

{
"name":"冰阿里山烏龍茶 Iced Alishan Oolong Tea",
"size":"特大杯",
"price":"$190",
"calo":"6大卡" 
}

]

collection_ref = db.collection("星巴克茶那堤菜單")
for doc in docs:
  collection_ref.add(doc)






