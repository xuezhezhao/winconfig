data={

   "error_code": 0,

   "stu_info": [

   {

     "id": 2059,

    "name": "小白",

     "sex": "男",

     "age": 28,

     "addr": "河南省济源市北海大道32号",

     "grade": "天蝎座",

     "phone": "18378309272",

     "gold": 10896,

      "info":{

          "card":434345432,

          "bank_name":'中国银行'

  }
},
{

                        "id": 2067,

                        "name": "小黑",

                        "sex": "男",

                        "age": 28,

                        "addr": "河南省济源市北海大道32号",

                        "grade": "天蝎座",

                        "phone": "12345678915",

                        "gold": 100

   }

  ]

    }
import pandas as pd
a=['1','5','9','65','2','6','5','65','e','e']
re=pd.value_counts(a)
print(re)

dict={}
print(list(dict))
for i in a:
    if i not in dict.keys():
        dict[i]=1
    else:
        dict[i]+=1
print(dict)
