import sys, math, random

Zones_Platinum=[]
total_Platinum=0
chance={}

player_count, my_id, zone_count, link_count = [int(i) for i in input().split()]
#Read Platinum in Zone
for i in range(zone_count):
   zone_id, platinum_source = [int(i) for i in input().split()]
   Zones_Platinum.append(platinum_source)
   
for i in range(link_count):
   zone1, zone2 = [int(i) for i in input().split()]
   if zone1 not in chance:
       chance[zone1]=[]
   if zone2 not in chance:
       chance[zone2]=[]
   if zone2 not in chance[zone1]:
       chance[zone1].append(zone2)
   if zone1 not in chance[zone2]:
       chance[zone2].append(zone1)

# game loop
while True:
   Zones=[]
   zone_present=[]
   my_zones=[]
   spawn=""
   perpindahan=""
   
   platinum = int(input()) # my available Platinum
   #Read My Places
   for i in range(zone_count):
       zId, ownerId, podsP0, pods_P1, podsP2, podsP3 = [int(i) for i in input().split()]
       exec("count=podsP"+str(my_id))
       Zones.append(ownerId)
       if count:
           zone_present.append([zId,ownerId,count]) 
   
   #moving
   for zone in zone_present:
       if zone[1]==my_id:
           probability=random.randint(0,len(chance[zone[0]])-1)
           perpindahan+=str(zone[2])+" "+str(zone[0])+" "+str((chance[zone[0]])[probability])+" "
   
   for zone in range(len(Zones)-1):
       if Zones[zone]==my_id:
           total_Platinum+=Zones_Platinum[zone]
           my_zones.append(zone)
   while total_Platinum>=20:
       probability=random.randint(0,len(my_zones)-1)
       spawn+="1 "+str(my_zones[probability])+" "
       total_Platinum-=20
   
   #Instructions
   print(perpindahan) 
   print(spawn)
