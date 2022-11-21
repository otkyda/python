#!/usr/bin/env python
# coding: utf-8

# ### Тема “Вычисления с помощью Numpy”

# In[1]:


import numpy as np


# ### Задание массива

# In[5]:


a = np.array([[1, 6],
              [2, 8],
              [3, 11],
              [3, 10],
              [1, 7]])


# ### Задание 1. Поиск средних значений

# In[8]:


mean_a = np.mean(a, axis = 0)
mean_a


# ### Задание 2. Вычисление массива a_centered

# In[9]:


a_centered = a - mean_a
a_centered


# In[12]:


a_centered_sp = np.dot(a_centered.T[0], a_centered.T[1])
a_centered_sp


# ### Задание 3. Вычисление скалярного произведения столбцов массива

# In[14]:


a_cov = a_centered_sp / (a.shape[0] - 1)
a_cov


# ### Задание 4. Вычисление ковариации с помощью функции np.cov

# In[16]:


a_cov = np.cov(a.T)[0, 1]
a_cov


# ### Тема “Работа с данными в Pandas”

# In[1]:


import pandas as pd


# ### Задание 1. Создание датафреймов authors и book

# In[12]:


authors = pd.DataFrame({'author_id':[1, 2, 3], 
                        'author_name':['Тургенев', 'Чехов', 'Островский']}, columns=['author_id', 'author_name'])
authors


# In[9]:


book = pd.DataFrame({'author_id':[1, 1, 1, 2, 2, 3, 3],
                     'book_title':['Отцы и дети', 'Рудин', 'Дворянское гнездо', 'Толстый и тонкий', 
                                    'Дама с собачкой', 'Гроза', 'Таланты и поклонники'], 
                     'price':[450, 300, 350, 500, 450, 370, 290]}, columns=['author_id', 'book_title', 'price'])
book


# ### Задание 2. Получить датафрейм authors_price, соединив датафреймы authors и books по полю author_id

# In[17]:


authors_price = pd.merge(authors, book, on = 'author_id', how = 'right')
authors_price


# ### Задание 3. Создание датафрейма top5, в котором содержатся строки из authors_price с пятью самыми дорогими книгами

# In[19]:


top5 = authors_price.sort_values(by='price', ascending=False).head(5)
   top5


# ### Задание 4. Создание датафрейма authors_stat на основе информации из authors_price

# In[28]:


authors_stat = authors_price.groupby('author_name').agg({'price':['min', 'max', 'mean']})
authors_stat = authors_stat.rename(columns={'min':'min_price', 'max':'max_price', 'mean':'mean_price'})
authors_stat


# In[ ]:




