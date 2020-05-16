from django.shortcuts import render

vegies_dict1={"name":"potato","price/kg":"20 rs"}
vegies_dict2={"name":"tomato","price/kg":"12 rs"}
vegies_dict3={"name":"brinjal","price/kg":"25 rs"}
vegies_dict4={"name":"carrot","price/kg":"30 rs"}
list_vegies=[vegies_dict1,vegies_dict2,vegies_dict3,vegies_dict4]
context={'store_vegies':list_vegies}

def greet(request):
    context={"greet":"Welcome to Kushwaha grocery store"}
    return render(request,"template_inheritance_app/welcome.html",context)

def items_here(request):
    
    return render(request,"template_inheritance_app/shop.html",context)


