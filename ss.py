import json

list1 = []
list2 = []
list3 = []
list4 = []
list5 = []
list6 = []
book_list = []
book_dict = {'name':'','author':'','book_info':'','grade':'','quote':'','img_url':''}




   

with open("F:\json\\test.json") as load_f:
    load_dict = json.load(load_f)
    for i in load_dict:
        authors = i.get('author')
        names = i.get('title')
        book_infos = i.get('book_info')
        grades = i.get('grade')
        quotes = i.get('quote')
        img_urls = i.get('img_url')
        for name in names:
            list1.append(name)
        for author in authors:
            list2.append(author)
        for book_info in book_infos:
            list3.append(book_info)
        for grade in grades:
            list4.append(grade)
        for quote in quotes:
            list5.append(quote)
        for img_url in img_urls:
            list6.append(img_url)
       
            

    print(len(list1))
    print(len(list2))
    print(len(list3))
    print(len(list4))
    print(len(list5))
    for i in range(0,len(list5)):
        book_dict['name'] = list1[i]
        book_dict['author'] = list2[i]
        book_dict['book_info'] = list3[i]
        book_dict["grade"] = list4[i]
        book_dict["quote"] = list5[i]
        book_dict['img_url'] = list6[i]
        book_list.append(book_dict)
        book_dict = {'name':'','author':'','book_info':'','grade':'','quote':'','img_url':''}


        
        
        
    book_list = json.dumps(book_list)
    fo = open("test6.json","w")
    fo.write(book_list)
    fo.close()




    

    
   
      
       
        
       



