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
"name":"特選雲朵泡泡美式咖啡 Starbucks Aerocano",
"size":"中杯",
"price":"$115",
"calo":"12大卡" 
},

{
"name":"特選雲朵泡泡美式咖啡 Starbucks Aerocano",
"size":"大杯",
"price":"$130",
"calo":"18大卡" 
},

{
"name":"特選雲朵泡泡美式咖啡 Starbucks Aerocano",
"size":"特大杯",
"price":"$145",
"calo":"24大卡" 
},

{
"name":"特選蜜柚雲朵泡泡美式咖啡 Starbucks Honey Ruby Grapefruit Aerocano",
"size":"中杯",
"price":"$140",
"calo":"118大卡" 
},

{
"name":"特選雲朵泡泡美式咖啡 Starbucks Aerocano",
"size":"大杯",
"price":"$155",
"calo":"176大卡" 
},

{
"name":"特選雲朵泡泡美式咖啡 Starbucks Aerocano",
"size":"特大杯",
"price":"$170",
"calo":"235大卡" 
},

{
"name":"雲朵泡泡美式咖啡 Classic Starbucks® Aerocano",
"size":"中杯",
"price":"$140",
"calo":"118大卡" 
},

{
"name":"雲朵泡泡美式咖啡 Classic Starbucks® Aerocano",
"size":"大杯",
"price":"$155",
"calo":"176大卡" 
},

{
"name":"雲朵泡泡美式咖啡 Classic Starbucks® Aerocano",
"size":"特大杯",
"price":"$170",
"calo":"235大卡" 
},

{
"name":"蜂蜜荔枝洋甘菊茶 Honey Lychee Chamomile Herbal Blend",
"size":"中杯",
"price":"$145",
"calo":"155大卡" 
},

{
"name":"蜂蜜荔枝洋甘菊茶 Honey Lychee Chamomile Herbal Blend",
"size":"大杯",
"price":"$160",
"calo":"231大卡" 
},

{
"name":"蜂蜜荔枝洋甘菊茶 Honey Lychee Chamomile Herbal Blend",
"size":"特大杯",
"price":"$175",
"calo":"309大卡" 
},

{
"name":"冰黑糖風味奶香咖啡 Iced Brown Sugar Creamy Coffee",
"size":"中杯",
"price":"$145",
"calo":"286大卡" 
},

{
"name":"冰黑糖風味奶香咖啡 Iced Brown Sugar Creamy Coffee",
"size":"大杯",
"price":"$160",
"calo":"306大卡" 
},

{
"name":"冰黑糖風味奶香咖啡 Iced Brown Sugar Creamy Coffee",
"size":"特大杯",
"price":"$175",
"calo":"327大卡" 
},

{
"name":"鹹焦糖奶油爆米花風味那堤 Salted Caramel Popcorn Creamy Latte",
"size":"大杯",
"price":"$185",
"calo":"659大卡" 
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
"name":"冰焦糖奶香星享那堤 Iced Creamy Caramel Latte",
"size":"大杯",
"price":"$165",
"calo":"672大卡" 
},

{
"name":"冰焦糖奶香星享那堤 Iced Creamy Caramel Latte",
"size":"特大杯",
"price":"$180",
"calo":"855大卡" 
},

{
"name":"焦糖奶香星享那堤 Creamy Caramel Latte",
"size":"大杯",
"price":"$165",
"calo":"651大卡" 
},

{
"name":"焦糖奶香星享那堤 Creamy Caramel Latte",
"size":"特大杯",
"price":"$180",
"calo":"790大卡" 
},

{
"name":"冰焦糖奶香紅茶那堤 Iced Creamy Caramel Black Tea Latte",
"size":"大杯",
"price":"$170",
"calo":"709大卡" 
},

{
"name":"冰焦糖奶香紅茶那堤 Iced Creamy Caramel Black Tea Latte",
"size":"特大杯",
"price":"$180",
"calo":"770大卡" 
}

]

collection_ref = db.collection("星巴克星推薦飲品")
for doc in docs:
  collection_ref.add(doc)






