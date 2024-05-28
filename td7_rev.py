# -*- coding: utf-8 -*-
"""
Created on Tue May 28 10:41:53 2024

@author: ye

"""
#IMPORT
import re
import numpy as np
import string#?



#FONCTIONS
def supprimer_ponctuation(texte_brut):
    ponc=r'[^\w\s]|[\t\d]'
    texte=re.sub(ponc, ' ',texte_brut)
    return texte


def lire_texte(chemin):
    with open (chemin,'r',encoding='utf-8')as f:
        lignes=[]
        ligne=f.readline()
        
        while ligne:
            ligne=supprimer_ponctuation(ligne)
            ligne=ligne.lower().rstrip()
            lignes.append (ligne)
            
            #next:
            ligne=f.readline()
            
    return lignes
       

def add2dic(l,initial,first_order,second_order):
    toks=l.split(' ')
    toks =[t for t in toks if t!='']#sinon, bcp de ''#pq?
    
    for i, tok in enumerate(toks):
        if i==0:#premier mot
            if tok not in initial:
                initial[tok]=1
            else :
                initial[tok]+=1


        elif i==1:#seconde mot
            premier=toks[0]
            if premier not in first_order:
                first_order[premier]=[]
            
            first_order[premier].append(tok)
        
        elif i==len(toks)-1:#dernier mot
            k=toks[i-2]+' '+toks[i-1]
            if k not in second_order:
                second_order[k]=[]
            second_order[k].append(tok)
            
            k_=toks[i-1]+' '+tok
            if k_ not in second_order:
                second_order[k_]=[]
            second_order[k_].append ('END')
            
        else :
            k=toks[i-2]+' '+toks[i-1]
            if k not in second_order:
                second_order[k]=[]
            second_order[k].append(tok)
            
    return initial,first_order,second_order

            
def list2pdic(mots):#liste de mots à dic de pb
    #compter freq    
    dic_pb={}
    for m in mots:
        if m not in dic_pb:
            dic_pb[m]=1
        else :
            dic_pb[m]+=1
    som=sum(dic_pb.values())
    
    #calculer pourcentage de chaque clé
    for k, val in dic_pb.items():
        dic_pb[k]=val/som

    return dic_pb

def sample_word(dic):
    #np.random.seed(1234)#fixer la val de p0, sinon, p0 est aléatoire
    p0=np.random.random()
    p=0
    for m,pb in dic.items():
        #print(m,pb)
        p+=pb
        if p>p0:
            break 
        
    return m

def generate(n,initial,first_order,second_order):
    for i in range(n):
        
        first_m=sample_word(initial)
        #print ('1er mot:',first_m)
        
        second_m=sample_word(first_order[first_m])
        #print('2e mot:',second_m)
        
        phz=first_m+' '+second_m
        #print(phz)
    
        while phz:
           
            toks=phz.split(' ')
            bigram=' '.join(toks[-2:])
            #print("bigram:", bigram)
            #print(second_order[bigram])
            next_m=sample_word(second_order[bigram])
            #print(next_m)
            if next_m !='END':
                phz+=' '+next_m
            else :
                break 
            
        print(f'phz{i+1}: {phz}','\n')

#CODE
# chemin='robert_frost.txt'
# lignes=lire_texte(chemin)

# #DIC DE CORPUS
# initial={}
# first_order={}
# second_order={}

# for l in lignes:
#     initial,first_order,second_order=add2dic(l, initial, first_order, second_order) 
# # print('initial:',initial)
# # print('first_order:',first_order)
# # print ('second_order:',second_order)



#NORMALISER 
#initial:
# som=sum(initial.values())
# #print (som)
# for m, freq in initial.items():
#     initial[m]=freq/som

# #first+second order
# for k, mots in first_order.items(): 
#     dic_pb=list2pdic(mots)
#     first_order[k]=dic_pb
    

# for k, mots in second_order.items(): 
#     dic_pb=list2pdic(mots)
#     second_order[k]=dic_pb
        

#GENERATION    
n=3   
generate(n,initial,first_order,second_order)
        
        
                       
    












