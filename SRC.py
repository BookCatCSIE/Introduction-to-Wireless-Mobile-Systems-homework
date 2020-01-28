import matplotlib.pyplot as plt
import random
import math


time_num=0
time_list=[0]

handoff_num_Best=0
handoff_list_Best=[0]

handoff_num_Threshold=0
handoff_list_Threshold=[0]

handoff_num_Entrophy=0
handoff_list_Entrophy=[0]

handoff_num_My_principle=0
handoff_list_My_principle=[0]


car_num=0
car_pos_x=[]
car_pos_y=[]
car_direction=[]
car_remove_index=[]

car_now_BS_Best=[]
car_now_BS_Threshold=[]
car_now_BS_Entrophy=[]
car_now_BS_My_principle=[]

entry_x=[0,0,0,750,1500,2250,3000,3000,3000,2250,1500,750]
entry_y=[2250,1500,750,0,0,0,750,1500,2250,3000,3000,3000]

BS_x=[750,750,2250,2250]
BS_y=[2250,750,750,2250]

BS0_power_to_cars=[]
BS1_power_to_cars=[]
BS2_power_to_cars=[]
BS3_power_to_cars=[]


power_Bs = []


power_num_Best=0
power_list_Best=[0]

power_num_Threshold=0
power_list_Threshold=[0]

power_num_Entrophy=0
power_list_Entrophy=[0]

power_num_My_principle=0
power_list_My_principle=[0]


total_car_num=0


Pnt=(1/30)*math.exp(-1/30)
#print("Pnt : {}".format(Pnt))  # Pnt = 0.03224053668273353

# P min = -125 dBm

def calculate_BS_power(ii,xx,yy):
    distance=math.sqrt((xx-BS_x[ii])*(xx-BS_x[ii])+(yy-BS_y[ii])*(yy-BS_y[ii]))
    if distance>1:
        Pt=-60-20*math.log(distance,10)
        return Pt
    else:
        return -60

    
def Best(now_bs,bs0,bs1,bs2,bs3):
    if now_bs==0:
        next_bs=0
        max_bs_value=bs0
        if bs1>max_bs_value:
            max_bs_value=bs1
            next_bs=1
        if bs2>max_bs_value:
            max_bs_value=bs2
            next_bs=2
        if bs3>max_bs_value:
            max_bs_value=bs3
            next_bs=3 
    elif now_bs==1:
        next_bs=1
        max_bs_value=bs1
        if bs0>max_bs_value:
            max_bs_value=bs0
            next_bs=0
        if bs2>max_bs_value:
            max_bs_value=bs2
            next_bs=2
        if bs3>max_bs_value:
            max_bs_value=bs3
            next_bs=3 
    elif now_bs==2:
        next_bs=2
        max_bs_value=bs2
        if bs1>max_bs_value:
            max_bs_value=bs1
            next_bs=1
        if bs0>max_bs_value:
            max_bs_value=bs0
            next_bs=0
        if bs3>max_bs_value:
            max_bs_value=bs3
            next_bs=3
    else: # now_bs==3:
        next_bs=3
        max_bs_value=bs3
        if bs1>max_bs_value:
            max_bs_value=bs1
            next_bs=1
        if bs2>max_bs_value:
            max_bs_value=bs2
            next_bs=2
        if bs0>max_bs_value:
            max_bs_value=bs0
            next_bs=0
            
    return next_bs



def Threshold(now_power,now_bs,bs0,bs1,bs2,bs3):
    next_bs=now_bs
    
    if now_power<-125:
        return Best(now_bs,bs0,bs1,bs2,bs3)
    elif now_bs==0 and bs0<-110:
        next_bs=0
        max_bs_value=bs0
        if bs1>max_bs_value:
            max_bs_value=bs1
            next_bs=1
        if bs2>max_bs_value:
            max_bs_value=bs2
            next_bs=2
        if bs3>max_bs_value:
            max_bs_value=bs3
            next_bs=3 
    elif now_bs==1 and bs1<-110:
        next_bs=1
        max_bs_value=bs1
        if bs0>max_bs_value:
            max_bs_value=bs0
            next_bs=0
        if bs2>max_bs_value:
            max_bs_value=bs2
            next_bs=2
        if bs3>max_bs_value:
            max_bs_value=bs3
            next_bs=3 
    elif now_bs==2 and bs2<-110:
        next_bs=2
        max_bs_value=bs2
        if bs1>max_bs_value:
            max_bs_value=bs1
            next_bs=1
        if bs0>max_bs_value:
            max_bs_value=bs0
            next_bs=0
        if bs3>max_bs_value:
            max_bs_value=bs3
            next_bs=3
    elif now_bs==3 and bs3<-110:
        next_bs=3
        max_bs_value=bs3
        if bs1>max_bs_value:
            max_bs_value=bs1
            next_bs=1
        if bs2>max_bs_value:
            max_bs_value=bs2
            next_bs=2
        if bs0>max_bs_value:
            max_bs_value=bs0
            next_bs=0
            
    return next_bs



def Entrophy(now_power,now_bs,bs0,bs1,bs2,bs3):
    if now_power<-125:
        return Best(now_bs,bs0,bs1,bs2,bs3)
    elif now_bs==0:
        next_bs=0
        max_bs_value=bs0+5
        if bs1>max_bs_value:
            max_bs_value=bs1
            next_bs=1
        if bs2>max_bs_value:
            max_bs_value=bs2
            next_bs=2
        if bs3>max_bs_value:
            max_bs_value=bs3
            next_bs=3 
    elif now_bs==1:
        next_bs=1
        max_bs_value=bs1+5
        if bs0>max_bs_value:
            max_bs_value=bs0
            next_bs=0
        if bs2>max_bs_value:
            max_bs_value=bs2
            next_bs=2
        if bs3>max_bs_value:
            max_bs_value=bs3
            next_bs=3 
    elif now_bs==2:
        next_bs=2
        max_bs_value=bs2+5
        if bs1>max_bs_value:
            max_bs_value=bs1
            next_bs=1
        if bs0>max_bs_value:
            max_bs_value=bs0
            next_bs=0
        if bs3>max_bs_value:
            max_bs_value=bs3
            next_bs=3
    else: # now_bs==3:
        next_bs=3
        max_bs_value=bs3+5
        if bs1>max_bs_value:
            max_bs_value=bs1
            next_bs=1
        if bs2>max_bs_value:
            max_bs_value=bs2
            next_bs=2
        if bs0>max_bs_value:
            max_bs_value=bs0
            next_bs=0
            
    return next_bs



def My_principle(now_power,now_bs,bs0,bs1,bs2,bs3):
    if now_power<-125:
        return Best(now_bs,bs0,bs1,bs2,bs3)
    elif now_bs==0:
        next_bs=0
        max_bs_value=bs0*(3/5)
        if bs1>max_bs_value:
            max_bs_value=bs1
            next_bs=1
        if bs2>max_bs_value:
            max_bs_value=bs2
            next_bs=2
        if bs3>max_bs_value:
            max_bs_value=bs3
            next_bs=3 
    elif now_bs==1:
        next_bs=1
        max_bs_value=bs1*(3/5)
        if bs0>max_bs_value:
            max_bs_value=bs0
            next_bs=0
        if bs2>max_bs_value:
            max_bs_value=bs2
            next_bs=2
        if bs3>max_bs_value:
            max_bs_value=bs3
            next_bs=3 
    elif now_bs==2:
        next_bs=2
        max_bs_value=bs2*(3/5)
        if bs1>max_bs_value:
            max_bs_value=bs1
            next_bs=1
        if bs0>max_bs_value:
            max_bs_value=bs0
            next_bs=0
        if bs3>max_bs_value:
            max_bs_value=bs3
            next_bs=3
    else: # now_bs==3:
        next_bs=3
        max_bs_value=bs3*(3/5)
        if bs1>max_bs_value:
            max_bs_value=bs1
            next_bs=1
        if bs2>max_bs_value:
            max_bs_value=bs2
            next_bs=2
        if bs0>max_bs_value:
            max_bs_value=bs0
            next_bs=0
            
    return next_bs





    
for i in range(86400):  # 86400 times
    #print("")
    time_num=time_num+1
    time_list.append(time_num)
    print("time_num : {}".format(time_num)) 
    
    # 12 entries generate car or not
    for j0 in range(12):
        generate_car=False
        generate_car_value=random.random()
        #print("generate_car_value : {}".format(generate_car_value))
        if generate_car_value <= Pnt:
            generate_car=True
            car_num=car_num+1
            total_car_num=total_car_num+1
        #print("car_num : {}".format(car_num))
        
        if generate_car == True:
            car_pos_x.append(entry_x[j0])
            car_pos_y.append(entry_y[j0])
            if j0<3:
                car_direction.append(2)
            elif j0<6:
                car_direction.append(3)
            elif j0<9:
                car_direction.append(0)
            else:
                car_direction.append(1)
            
            if j0==0 or j0==11 or j0==10:
                car_now_BS_Best.append(0)
                car_now_BS_Threshold.append(0)
                car_now_BS_Entrophy.append(0)
                car_now_BS_My_principle.append(0)
            elif j0==1 or j0==2 or j0==3:
                car_now_BS_Best.append(1)
                car_now_BS_Threshold.append(1)
                car_now_BS_Entrophy.append(1)
                car_now_BS_My_principle.append(1)
            elif j0==4 or j0==5 or j0==6:
                car_now_BS_Best.append(2)
                car_now_BS_Threshold.append(2)
                car_now_BS_Entrophy.append(2)
                car_now_BS_My_principle.append(2)
            else:
                car_now_BS_Best.append(3)
                car_now_BS_Threshold.append(3)
                car_now_BS_Entrophy.append(3)
                car_now_BS_My_principle.append(3)
            

    #----------------------------------------------------------------
#    print("before")
#    print("car_pos_x : {}".format(car_pos_x))
#    print("car_pos_y : {}".format(car_pos_y))
#    print("car_direction : {}".format(car_direction))
#    print("car_now_BS_Best : {}".format(car_now_BS_Best))
#    print("car_now_BS_Threshold : {}".format(car_now_BS_Threshold))
#    print("car_now_BS_Entrophy : {}".format(car_now_BS_Entrophy))
#    print("car_now_BS_My_principle : {}".format(car_now_BS_My_principle))
    #------------------------------------------------------------------------
    
    
    # deal with movement of each car
    for j in range(car_num):
        car_at_intersection_x=False
        car_at_intersection_y=False
        for k1 in range(3):
            if car_pos_x[j]==750*(k1+1):
                car_at_intersection_x=True
        for k2 in range(3):
            if car_pos_y[j]==750*(k2+1):
                car_at_intersection_y=True
            
        if car_at_intersection_x == True and car_at_intersection_y == True:
            car_movement=random.randint(0,5)  #0,1,2 straight , 3,4 right , 5 left
            
            if car_direction[j]==0:
                if car_movement==0 or car_movement==1 or car_movement==2:
                    car_direction[j]=0
                    car_pos_x[j]=car_pos_x[j]-10
                elif car_movement==3 or car_movement==4:
                    car_direction[j]=3
                    car_pos_y[j]=car_pos_y[j]+10
                else:
                    car_direction[j]=1
                    car_pos_y[j]=car_pos_y[j]-10
            elif car_direction[j]==1:
                if car_movement==0 or car_movement==1 or car_movement==2:
                    car_direction[j]=1
                    car_pos_y[j]=car_pos_y[j]-10
                elif car_movement==3 or car_movement==4:
                    car_direction[j]=0
                    car_pos_x[j]=car_pos_x[j]-10
                else:
                    car_direction[j]=2
                    car_pos_x[j]=car_pos_x[j]+10
            elif car_direction[j]==2:
                if car_movement==0 or car_movement==1 or car_movement==2:
                    car_direction[j]=2
                    car_pos_x[j]=car_pos_x[j]+10
                elif car_movement==3 or car_movement==4:
                    car_direction[j]=1
                    car_pos_y[j]=car_pos_y[j]-10
                else:
                    car_direction[j]=3
                    car_pos_y[j]=car_pos_y[j]+10
            else:
                if car_movement==0 or car_movement==1 or car_movement==2:
                    car_direction[j]=3
                    car_pos_y[j]=car_pos_y[j]+10
                elif car_movement==3 or car_movement==4:
                    car_direction[j]=2
                    car_pos_x[j]=car_pos_x[j]+10
                else:
                    car_direction[j]=0
                    car_pos_x[j]=car_pos_x[j]-10        
        elif (car_pos_x[j]==0 and car_at_intersection_y == True):
            car_movement=random.randint(0,5)  #0,1,2 straight , 3,4 right , 5 left
            
            if car_direction[j]==0:
                if car_movement==0 or car_movement==1 or car_movement==2:
                    car_direction[j]=0
                    car_pos_x[j]=car_pos_x[j]-10
                elif car_movement==3 or car_movement==4:
                    car_direction[j]=3
                    car_pos_y[j]=car_pos_y[j]+10
                else:
                    car_direction[j]=1
                    car_pos_y[j]=car_pos_y[j]-10
            elif car_direction[j]==1:
                if car_movement==0 or car_movement==1 or car_movement==2:
                    car_direction[j]=1
                    car_pos_y[j]=car_pos_y[j]-10
                elif car_movement==3 or car_movement==4:
                    car_direction[j]=0
                    car_pos_x[j]=car_pos_x[j]-10
                else:
                    car_direction[j]=2
                    car_pos_x[j]=car_pos_x[j]+10
            elif car_direction[j]==2:
                if car_movement==0 or car_movement==1 or car_movement==2:
                    car_direction[j]=2
                    car_pos_x[j]=car_pos_x[j]+10
                elif car_movement==3 or car_movement==4:
                    car_direction[j]=1
                    car_pos_y[j]=car_pos_y[j]-10
                else:
                    car_direction[j]=3
                    car_pos_y[j]=car_pos_y[j]+10
            else:
                if car_movement==0 or car_movement==1 or car_movement==2:
                    car_direction[j]=3
                    car_pos_y[j]=car_pos_y[j]+10
                elif car_movement==3 or car_movement==4:
                    car_direction[j]=2
                    car_pos_x[j]=car_pos_x[j]+10
                else:
                    car_direction[j]=0
                    car_pos_x[j]=car_pos_x[j]-10  
        elif (car_pos_x[j]==3000 and car_at_intersection_y == True):
            car_movement=random.randint(0,5)  #0,1,2 straight , 3,4 right , 5 left
            
            if car_direction[j]==0:
                if car_movement==0 or car_movement==1 or car_movement==2:
                    car_direction[j]=0
                    car_pos_x[j]=car_pos_x[j]-10
                elif car_movement==3 or car_movement==4:
                    car_direction[j]=3
                    car_pos_y[j]=car_pos_y[j]+10
                else:
                    car_direction[j]=1
                    car_pos_y[j]=car_pos_y[j]-10
            elif car_direction[j]==1:
                if car_movement==0 or car_movement==1 or car_movement==2:
                    car_direction[j]=1
                    car_pos_y[j]=car_pos_y[j]-10
                elif car_movement==3 or car_movement==4:
                    car_direction[j]=0
                    car_pos_x[j]=car_pos_x[j]-10
                else:
                    car_direction[j]=2
                    car_pos_x[j]=car_pos_x[j]+10
            elif car_direction[j]==2:
                if car_movement==0 or car_movement==1 or car_movement==2:
                    car_direction[j]=2
                    car_pos_x[j]=car_pos_x[j]+10
                elif car_movement==3 or car_movement==4:
                    car_direction[j]=1
                    car_pos_y[j]=car_pos_y[j]-10
                else:
                    car_direction[j]=3
                    car_pos_y[j]=car_pos_y[j]+10
            else:
                if car_movement==0 or car_movement==1 or car_movement==2:
                    car_direction[j]=3
                    car_pos_y[j]=car_pos_y[j]+10
                elif car_movement==3 or car_movement==4:
                    car_direction[j]=2
                    car_pos_x[j]=car_pos_x[j]+10
                else:
                    car_direction[j]=0
                    car_pos_x[j]=car_pos_x[j]-10  
        elif (car_at_intersection_x == True and car_pos_y[j]==0):
            car_movement=random.randint(0,5)  #0,1,2 straight , 3,4 right , 5 left
            
            if car_direction[j]==0:
                if car_movement==0 or car_movement==1 or car_movement==2:
                    car_direction[j]=0
                    car_pos_x[j]=car_pos_x[j]-10
                elif car_movement==3 or car_movement==4:
                    car_direction[j]=3
                    car_pos_y[j]=car_pos_y[j]+10
                else:
                    car_direction[j]=1
                    car_pos_y[j]=car_pos_y[j]-10
            elif car_direction[j]==1:
                if car_movement==0 or car_movement==1 or car_movement==2:
                    car_direction[j]=1
                    car_pos_y[j]=car_pos_y[j]-10
                elif car_movement==3 or car_movement==4:
                    car_direction[j]=0
                    car_pos_x[j]=car_pos_x[j]-10
                else:
                    car_direction[j]=2
                    car_pos_x[j]=car_pos_x[j]+10
            elif car_direction[j]==2:
                if car_movement==0 or car_movement==1 or car_movement==2:
                    car_direction[j]=2
                    car_pos_x[j]=car_pos_x[j]+10
                elif car_movement==3 or car_movement==4:
                    car_direction[j]=1
                    car_pos_y[j]=car_pos_y[j]-10
                else:
                    car_direction[j]=3
                    car_pos_y[j]=car_pos_y[j]+10
            else:
                if car_movement==0 or car_movement==1 or car_movement==2:
                    car_direction[j]=3
                    car_pos_y[j]=car_pos_y[j]+10
                elif car_movement==3 or car_movement==4:
                    car_direction[j]=2
                    car_pos_x[j]=car_pos_x[j]+10
                else:
                    car_direction[j]=0
                    car_pos_x[j]=car_pos_x[j]-10  
        elif (car_at_intersection_x == True and car_pos_y[j]==3000):
            car_movement=random.randint(0,5)  #0,1,2 straight , 3,4 right , 5 left
            
            if car_direction[j]==0:
                if car_movement==0 or car_movement==1 or car_movement==2:
                    car_direction[j]=0
                    car_pos_x[j]=car_pos_x[j]-10
                elif car_movement==3 or car_movement==4:
                    car_direction[j]=3
                    car_pos_y[j]=car_pos_y[j]+10
                else:
                    car_direction[j]=1
                    car_pos_y[j]=car_pos_y[j]-10
            elif car_direction[j]==1:
                if car_movement==0 or car_movement==1 or car_movement==2:
                    car_direction[j]=1
                    car_pos_y[j]=car_pos_y[j]-10
                elif car_movement==3 or car_movement==4:
                    car_direction[j]=0
                    car_pos_x[j]=car_pos_x[j]-10
                else:
                    car_direction[j]=2
                    car_pos_x[j]=car_pos_x[j]+10
            elif car_direction[j]==2:
                if car_movement==0 or car_movement==1 or car_movement==2:
                    car_direction[j]=2
                    car_pos_x[j]=car_pos_x[j]+10
                elif car_movement==3 or car_movement==4:
                    car_direction[j]=1
                    car_pos_y[j]=car_pos_y[j]-10
                else:
                    car_direction[j]=3
                    car_pos_y[j]=car_pos_y[j]+10
            else:
                if car_movement==0 or car_movement==1 or car_movement==2:
                    car_direction[j]=3
                    car_pos_y[j]=car_pos_y[j]+10
                elif car_movement==3 or car_movement==4:
                    car_direction[j]=2
                    car_pos_x[j]=car_pos_x[j]+10
                else:
                    car_direction[j]=0
                    car_pos_x[j]=car_pos_x[j]-10  
        elif car_pos_x[j]==0 and car_pos_y[j]==0:
            if car_direction[j]==0:
                car_direction[j]=3
                car_pos_y[j]=car_pos_y[j]+10
            elif car_direction[j]==1:
                car_direction[j]=2
                car_pos_x[j]=car_pos_x[j]+10
            elif car_direction[j]==2:
                car_direction[j]=2
                car_pos_x[j]=car_pos_x[j]+10
            else:
                car_direction[j]=3
                car_pos_y[j]=car_pos_y[j]+10
        elif car_pos_x[j]==3000 and car_pos_y[j]==0:
            if car_direction[j]==2:
                car_direction[j]=3
                car_pos_y[j]=car_pos_y[j]+10
            elif car_direction[j]==1:
                car_direction[j]=0
                car_pos_x[j]=car_pos_x[j]-10 
            elif car_direction[j]==0:
                car_direction[j]=0
                car_pos_x[j]=car_pos_x[j]-10 
            else:
                car_direction[j]=3
                car_pos_y[j]=car_pos_y[j]+10
        elif car_pos_x[j]==3000 and car_pos_y[j]==3000:
            if car_direction[j]==2:
                car_direction[j]=1
                car_pos_y[j]=car_pos_y[j]-10
            elif car_direction[j]==3:
                car_direction[j]=0
                car_pos_x[j]=car_pos_x[j]-10
            elif car_direction[j]==0:
                car_direction[j]=0
                car_pos_x[j]=car_pos_x[j]-10
            else:
                car_direction[j]=1
                car_pos_y[j]=car_pos_y[j]-10
        elif car_pos_x[j]==0 and car_pos_y[j]==3000:
            if car_direction[j]==0:
                car_direction[j]=1
                car_pos_y[j]=car_pos_y[j]-10
            elif car_direction[j]==3:
                car_direction[j]=2
                car_pos_x[j]=car_pos_x[j]+10
            elif car_direction[j]==2:
                car_direction[j]=2
                car_pos_x[j]=car_pos_x[j]+10
            else:
                car_direction[j]=1
                car_pos_y[j]=car_pos_y[j]-10
        else:
            if car_direction[j]==0:
                car_pos_x[j]=car_pos_x[j]-10
            elif car_direction[j]==1:
                car_pos_y[j]=car_pos_y[j]-10
            elif car_direction[j]==2:
                car_pos_x[j]=car_pos_x[j]+10
            else:
                car_pos_y[j]=car_pos_y[j]+10
    
    # cars go out or not
    car_remove_index.clear()
    for j2 in range(car_num):
        if car_pos_x[j2]<0 or car_pos_x[j2]>3000 or car_pos_y[j2]<0 or car_pos_y[j2]>3000:
            car_remove_index.append(j2)
    
    #print("car_remove_index : {}".format(car_remove_index))
            
    for j3 in range(len(car_remove_index)):
        car_num=car_num-1
        car_pos_x.pop(car_remove_index[j3])
        car_pos_y.pop(car_remove_index[j3])
        car_direction.pop(car_remove_index[j3])
        car_now_BS_Best.pop(car_remove_index[j3])
        car_now_BS_Threshold.pop(car_remove_index[j3])
        car_now_BS_Entrophy.pop(car_remove_index[j3])
        car_now_BS_My_principle.pop(car_remove_index[j3])
        for j5 in range(len(car_remove_index)):
            car_remove_index[j5] = car_remove_index[j5]-1
    
    

    BS0_power_to_cars.clear()
    BS1_power_to_cars.clear()
    BS2_power_to_cars.clear()
    BS3_power_to_cars.clear()
    for kk in range(car_num):
        BS0_power_to_cars.append(calculate_BS_power(0,car_pos_x[kk],car_pos_y[kk]))
        BS1_power_to_cars.append(calculate_BS_power(1,car_pos_x[kk],car_pos_y[kk]))
        BS2_power_to_cars.append(calculate_BS_power(2,car_pos_x[kk],car_pos_y[kk]))
        BS3_power_to_cars.append(calculate_BS_power(3,car_pos_x[kk],car_pos_y[kk]))
    
#    print("BS0_power_to_cars : {}".format(BS0_power_to_cars))
#    print("BS1_power_to_cars : {}".format(BS1_power_to_cars))
#    print("BS2_power_to_cars : {}".format(BS2_power_to_cars))
#    print("BS3_power_to_cars : {}".format(BS3_power_to_cars))
    
    
    
    total_power_Best = 0
    total_power_Threshold = 0
    total_power_Entrophy = 0
    total_power_My_principle = 0
    
    for kk2 in range(car_num): 
        power_Bs.clear()
        power_Bs = [BS0_power_to_cars[kk2],BS1_power_to_cars[kk2],BS2_power_to_cars[kk2],BS3_power_to_cars[kk2]]
        
        
        car_before_BS_Best = car_now_BS_Best[kk2]
        car_now_BS_Best[kk2] = Best(car_now_BS_Best[kk2],BS0_power_to_cars[kk2],BS1_power_to_cars[kk2],BS2_power_to_cars[kk2],BS3_power_to_cars[kk2])
        if car_now_BS_Best[kk2] != car_before_BS_Best:
            handoff_num_Best=handoff_num_Best+1
            
        car_before_BS_Threshold = car_now_BS_Threshold[kk2]
        car_now_BS_Threshold[kk2] = Threshold(power_Bs[car_now_BS_Threshold[kk2]],car_now_BS_Threshold[kk2],BS0_power_to_cars[kk2],BS1_power_to_cars[kk2],BS2_power_to_cars[kk2],BS3_power_to_cars[kk2])
        if car_now_BS_Threshold[kk2] != car_before_BS_Threshold:
            handoff_num_Threshold=handoff_num_Threshold+1
            
        car_before_BS_Entrophy = car_now_BS_Entrophy[kk2]
        car_now_BS_Entrophy[kk2] = Entrophy(power_Bs[car_now_BS_Entrophy[kk2]],car_now_BS_Entrophy[kk2],BS0_power_to_cars[kk2],BS1_power_to_cars[kk2],BS2_power_to_cars[kk2],BS3_power_to_cars[kk2])
        if car_now_BS_Entrophy[kk2] != car_before_BS_Entrophy:
            handoff_num_Entrophy=handoff_num_Entrophy+1
        
        car_before_BS_My_principle = car_now_BS_My_principle[kk2]
        car_now_BS_My_principle[kk2] = My_principle(power_Bs[car_now_BS_My_principle[kk2]],car_now_BS_My_principle[kk2],BS0_power_to_cars[kk2],BS1_power_to_cars[kk2],BS2_power_to_cars[kk2],BS3_power_to_cars[kk2])
        if car_now_BS_My_principle[kk2] != car_before_BS_My_principle:
            handoff_num_My_principle=handoff_num_My_principle+1
            
        
            
        total_power_Best = total_power_Best + power_Bs[car_now_BS_Best[kk2]]
        total_power_Threshold = total_power_Threshold + power_Bs[car_now_BS_Threshold[kk2]]
        total_power_Entrophy = total_power_Entrophy + power_Bs[car_now_BS_Entrophy[kk2]]
        total_power_My_principle = total_power_My_principle + power_Bs[car_now_BS_My_principle[kk2]]
        
            
    #----------------------------------------------------------------
#    print("after")
#    print("car_pos_x : {}".format(car_pos_x))
#    print("car_pos_y : {}".format(car_pos_y))
#    print("car_direction : {}".format(car_direction))
#    print("car_now_BS_Best : {}".format(car_now_BS_Best))
#    print("car_now_BS_Threshold : {}".format(car_now_BS_Threshold))
#    print("car_now_BS_Entrophy : {}".format(car_now_BS_Entrophy))
#    print("car_now_BS_My_principle : {}".format(car_now_BS_My_principle))
    #------------------------------------------------------------------------
    
#    print("handoff_num_Best : {}".format(handoff_num_Best))
#    print("handoff_num_Threshold : {}".format(handoff_num_Threshold))
#    print("handoff_num_Entrophy : {}".format(handoff_num_Entrophy))
#    print("handoff_num_My_principle : {}".format(handoff_num_My_principle))
    
    handoff_list_Best.append(handoff_num_Best)
    handoff_list_Threshold.append(handoff_num_Threshold)
    handoff_list_Entrophy.append(handoff_num_Entrophy)
    handoff_list_My_principle.append(handoff_num_My_principle)
    
    if car_num != 0:
        power_list_Best.append(total_power_Best/car_num)
        power_list_Threshold.append(total_power_Threshold/car_num)
        power_list_Entrophy.append(total_power_Entrophy/car_num)
        power_list_My_principle.append(total_power_My_principle/car_num)
    else:
        power_list_Best.append(0)
        power_list_Threshold.append(0)
        power_list_Entrophy.append(0)
        power_list_My_principle.append(0)
    
    
#print("handoff_list_Best : {}".format(handoff_list_Best))
#print("handoff_list_Threshold : {}".format(handoff_list_Threshold))
#print("handoff_list_Entrophy : {}".format(handoff_list_Entrophy))
#print("handoff_list_My_principle : {}".format(handoff_list_My_principle))    
            
print("handoff_list_Best : {}".format(handoff_list_Best[-1]))
print("handoff_list_Threshold : {}".format(handoff_list_Threshold[-1]))
print("handoff_list_Entrophy : {}".format(handoff_list_Entrophy[-1]))
print("handoff_list_My_principle : {}".format(handoff_list_My_principle[-1]))   

for pp in range(len(power_list_Best)):
    power_num_Best = power_num_Best + power_list_Best[pp]
    power_num_Threshold = power_num_Threshold + power_list_Threshold[pp]
    power_num_Entrophy = power_num_Entrophy + power_list_Entrophy[pp]
    power_num_My_principle = power_num_My_principle + power_list_My_principle[pp]


power_num_Best = power_num_Best/86400
power_num_Threshold = power_num_Threshold/86400
power_num_Entrophy = power_num_Entrophy/86400
power_num_My_principle = power_num_My_principle/86400

print("power_num_Best : {}".format(power_num_Best))
print("power_num_Threshol : {}".format(power_num_Threshold))         
print("power_num_Entrophy : {}".format(power_num_Entrophy))         
print("power_num_My_principle : {}".format(power_num_My_principle))         

print("total_car_num : {}".format(total_car_num))  
        
    
plt.style.use('bmh')
fig0=plt.figure()
ax=plt.axes()
plt.plot(time_list,handoff_list_Best,'-')
plt.title("Best")
plt.xlabel("time")
plt.ylabel("total number of handoffs")
#fig0.savefig('Best.png')


plt.style.use('bmh')
fig1=plt.figure()
ax=plt.axes()
plt.plot(time_list,handoff_list_Threshold,'-')
plt.title("Threshold")
plt.xlabel("time")
plt.ylabel("total number of handoffs")
#fig0.savefig('Threshold.png')



plt.style.use('bmh')
fig2=plt.figure()
ax=plt.axes()
plt.plot(time_list,handoff_list_Entrophy,'-')
plt.title("Entrophy")
plt.xlabel("time")
plt.ylabel("total number of handoffs")
#fig0.savefig('Entrophy.png')


plt.style.use('bmh')
fig3=plt.figure()
ax=plt.axes()
plt.plot(time_list,handoff_list_My_principle,'-')
plt.title("My_principle")
plt.xlabel("time")
plt.ylabel("total number of handoffs")
#fig0.savefig('My_principle.png')



