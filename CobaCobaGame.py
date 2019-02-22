import sys, math, random

Zona_Platinum=[]
Total_Platinum=0
Range={}

playerCount, my_id, zone_count, link_count = [int(i) for i in input().split()]
#Read Platinum in Zone
for i in range(zone_count):
   zone_id, platinum_source = [int(i) for i in input().split()]
   Zona_Platinum.append(platinum_source)
   
for i in range(link_count):
   zone1, zone2 = [int(i) for i in input().split()]
   if zone1 not in Range:
       Range[zone1]=[]
   if zone2 not in Range:
       Range[zone2]=[]
   if zone2 not in Range[zone1]:
       Range[zone1].append(zone2)
   if zone1 not in Range[zone2]:
       Range[zone2].append(zone1)

# game loop
while True:
   Zones=[]
   zones_own=[]
   My_Zones=[]
   spawn=""
   Perpindahan=""
   
   platinum = int(input()) # my available Platinum
   #Read My Places
   for i in range(zone_count):
       z_id, owner_id, pods_P0, pods_P1, podsP2, podsP3 = [int(i) for i in input().split()]
       exec("count=podsP"+str(my_id))
       Zones.append(owner_id)
       if count:
           zones_own.append([z_id,owner_id,count])
   
   #moving
   for zone in zones_own:
       if zone[1]==my_id:
           pilihan=random.randint(0,len(Range[zone[0]])-1)
           Perpindahan+=str(zone[2])+" "+str(zone[0])+" "+str((Range[zone[0]])[pilihan])+" "
   
   for zone in range(len(Zones)-1):
       if Zones[zone]==my_id:
           Total_Platinum+=Zona_Platinum[zone]
           My_Zones.append(zone)
   while Total_Platinum>=20:
       pilihan=random.randint(0,len(My_Zones)-1)
       spawn+="1 "+str(My_Zones[pilihan])+" "
       Total_Platinum-=20
   
   #Instructions
   print(Perpindahan) 
   print(spawn)