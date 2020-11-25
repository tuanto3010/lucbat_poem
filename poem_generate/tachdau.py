# -*- coding: utf-8 -*-
import re
import sys
import os
import subprocess

patterns = {
    '[àáảãạăắằẵặẳâầấậẫẩ]': 'a',
    '[đ]': 'd',
    '[èéẻẽẹêềếểễệ]': 'e',
    '[ìíỉĩị]': 'i',
    '[òóỏõọôồốổỗộơờớởỡợ]': 'o',
    '[ùúủũụưừứửữự]': 'u',
    '[ỳýỷỹỵ]': 'y'
}

daucau = {
    '[àằầèềìòồờùừỳ]' : 'huyen',
    '[áắấéếíóốớúứý]' : 'sac',
    '[ảẳẩẻểỉỏổởủửỷ]' : 'hoi',
    '[ãẵẫẽễĩõỗỡũữỹ]' : 'nga',
    '[ạặậẹệịọộợụựỵ]' : 'nang'
    # '[aăâeêioôơuưyđd]' : 'nang'
}

def convert(text):
    """
    Convert from 'Tieng Viet co dau' thanh 'Tieng Viet khong dau'
    text: input string to be converted
    Return: string converted
    """
    output = text
    for regex, replace in patterns.items():
        output = re.sub(regex, replace, output)
        # deal with upper case
        output = re.sub(regex.upper(), replace.upper(), output)
    return output
# a,e,u,i,o
def validate_daucau(string):
    '''
    input: string ex: tô huỳnh tuấn
    output string has been change to daucau ex: ngang huyen sac

    '''
    if not isinstance(string,str):
        print("Currently, this function just support string input")
        return 0
    # if string is None:
    #     pass

    list_word=string.split()
    list_output=[]
    for word in list_word:
        dau=''
        for regex_daucau, daucau_name in daucau.items():
            if re.search(regex_daucau,word):
                dau=daucau_name
        if(dau=="" or dau=="huyen"): # "" as ngang
            list_output.append("bang")
        else:
            list_output.append("trac")
    string_output=' '.join(list_output)
    return string_output
def exe_bash():
    pass

def re_first_chacracter(word):
    '''
        this function design for removing the first character from string
        for examples: tuan -- > uan, phong --> ong
        my idea: VN word must be have a specific format
        so we just need to remove from the first char to a,o,i,e ^^^
    '''
    if len(word.split()) > 1:
        print("This function just support for word not string contains multi words")
        return

    m = re.search(r'(?=[ioaeu])\w+', word)
    result=m.group(0)
    return result
print(re_first_chacracter('tuan'))
