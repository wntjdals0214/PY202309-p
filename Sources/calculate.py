#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#function 3-1 1차 감염에 대한 확률계산
def calculate_1st_percentage(infection, disease_list):
    conflict_hour = 0 # 겹치는 시간
    infection_percentage = 0 # 감염확률
    for infecter in disease_list:
        for j in range(14):
            if infection[j] == infecter[j]: # 이용자와 각 감염자의 같은 시간의 이동경로를 비교
                conflict_hour += 1
    infection_percentage += conflict_hour * 0.3 #확률계산
    print(infection_percentage)
    return infection_percentage
#function 3-2 2차 감염에 대한 확률계산
def calculate_2nd_percentage(infect_percent, main_disease, compare_disease1, compare_disease2):
    disease1_conflict_hour = 0 # main 질병 감염자와 disease1 감염자가 겹치는 시간
    disease2_conflict_hour = 0 # main 질병 감염자와 disease2 감염자가 겹치는 시간
    infection_percentage1 = 0 # disease1 감염자가 main 질병의 감염 되었을 확률
    infection_percentage2 = 0 # disease2 감염자가 main 질병의 감염 되었을 확률
    for infect in main_disease:
        for suspected_infect in compare_disease1:
            for i in range(14):
                # main 질병 감염자와 disease1 감염자의 같은 시간의 이동경로를 비교
                if infect[i]==suspected_infect[i]: 
                    disease1_conflict_hour += 1
        # disease1 감염자의 main 질병 감염확률과 이용자의 main 잘병확률을 곱하여 이용자의 diseease1 감염자를 통한 main 질병의 2차 감염확률을 계산
        infection_percentage1 += infect_percent * 0.01 * disease1_conflict_hour * 0.2 # 2차감염 확률계산
        print(infection_percentage1)
        for suspected_infect in compare_disease2:
            for i in range(14):
                if infect[i]==suspected_infect[i]:
                    disease2_conflict_hour += 1
        # disease2 감염자의 main 질병 감염확률과 이용자의 main 잘병확률을 곱하여 이용자의 diseease2 감염자를 통한 main 질병의 2차 감염확률을 계산
        infection_percentage2 += infect_percent * 0.01 * disease2_conflict_hour * 0.2 # 2차감염 확률계산
        print(infection_percentage2)
    return infection_percentage1 + infection_percentage2 # 두 확률을 더하여 최종 2차 감염 확률을 계산한다.
    
    

