
# coding: utf-8

# In[3]:


import bs4


# In[4]:


from urllib.request import urlopen as uReq


# In[5]:


from bs4 import BeautifulSoup as soup


# In[6]:


my_url='https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38'


# In[7]:


uClient=uReq(my_url)


# In[8]:


page_html=uClient.read()


# In[9]:


uClient.close()


# In[10]:


page_soup=soup(page_html,"html.parser")


# In[11]:


page_soup.h1


# In[12]:


page_soup.p


# In[13]:


page_soup.body.span


# In[14]:


containers=page_soup.findAll("div",{"class":"item-container"})


# In[15]:


len(containers)


# In[16]:


containers[0]


# In[17]:


contain=containers[0]
container=containers[0]


# In[18]:


container.div


# In[19]:


container.div.div.a


# In[20]:


container.div.div.a.img


# In[21]:


container.div.div.a.img["title"]


# In[22]:


title_container=container.findAll("a",{"class":"item-title"})


# In[23]:


title_container[0]


# In[24]:


title_container[0].text


# In[25]:


shipping_container=container.findAll("li",{"class":"price-ship"})


# In[26]:


shipping_container[0]


# In[27]:


shipping_container[0].text


# In[28]:


shipping_container[0].text.strip()


# In[29]:




for container in containers:
	brand=container.div.div.a.img["title"]

	title_container=container.findAll("a",{"class":"item-title"})
	product_name=title_container[0].text

	shipping_container=container.findAll("li",{"class":"price-ship"})
	shipping=shipping_container[0].text.strip() 


	print("brand:" + brand)
	print("product_name:" + product_name)
	print("shipping:" + shipping)



# In[38]:


filename="croducts.csv"
f=open(filename,"w")
headers="brand,product_name,shipping\n"
f.write(headers)
f.write(brand + "," + product_name.replace(",","|") + "," + shipping)
f.close()

