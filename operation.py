from datetime import datetime
from json import JSONDecodeError


def Create_Event(org,events_json_file,Event_ID,Event_Name,Start_Date,Start_Time,End_Date,End_Time,Users_Registered,Capacity,Availability):
    
    d={
        "org":org,
        "Event_Id":Event_ID,
        "Event_Name":Event_Name,
        "Start Date":Start_Date,
        "Start Date":Start_Time,
        "End Date":End_Date,
        "End Time":End_Time,
        "user":Users_Registered,
        "capacity":Capacity,
        "availability":Availability
        }
    f=open(events_json_file,'r')
    try:
        content=json.load(f)
        if d not in content:
            content.append(d)
            f.seek(0)
            f.truncate()
            json.dump(content,f)
    except JSONDecodeError:
        l=[]
        l.append(d)
        json.dump(l,f)
    f.close()
    
def View_Events(org,events_json_file,):
    Details=[]
    f=open(events_json_file,'r+')
    content=json.load(f)
    for i in range(len(content)):
        if content[i]["Organizer"]==org:
            Details.append(content[i])
    f.close()
    return Details
def View_Event_ByID(events_json_file,Event_ID):
    Details=[]
    f=open(events_json_file,'r+')
    content=json.load(f)
    for i in range(len(content)):
        if content[i]["ID"]==Event_ID:
            Details.append(content[i])
    f.close()
    return Details
def Update_Event(org,events_json_file,event_id,detail_to_be_updated,updated_details):
    f=open(events_json_file,'r+')
    content=json.load(f)
    for i in range(len(content)):
        if content[i]["ID"]==event_id:
            
            try:
                a=content[i][detail_to_be_updated]
            except KeyError:
                return False
            content[i][detail_to_be_updated]==updated_details
            f.seek(0)
            f.truncate()
            json.dump(content,f)
            f.close()
            return True
    f.close()
    return False

def Delete_Event(org,events_json_file,event_ID):
    
    f=open(events_json_file,'r+')
    content=json.load(f)
    for i in range(len(content)):
        if content[i]["Organizer"]==org and content[i]["ID"]==event_ID:
            del content[i]
            f.seek(0)
            f.truncate()
            json.dump(content,f)
            f.close()
            return True
    f.close()
    return False

def Register_for_Events(events_json_file,event_id,Full_Name):
    date_today=str(date.today())
    now=datetime.now()
    current_time=now.strftime("%H:%M:%S")
    f=open(events_json_file,'w')
    try:
         content=json.load(f)
    except JSONDecodeError:
        f.close()
        return False
    for i in range(len(content)):
        if content[i]["ID"]==event_id and content[i]["Seats Available"]>0:
            if content[i]["End Date"]>=date_today and content[i]["End Time"]>=current_time:
                content[i]["User Registered"].apppend (Full_Name)
                content[i]["Seats Available"]-=1
            f.seek(0)
            f.truncate()
            json.dump(content,f)
            f.close()
            return True
    f.close()
    return False

def fetch_all_Events(events_json_file,Full_Name,event_details,upcoming_ongoing):
    date_today=str(date.today())
    now=datetime.now()
    current_time=now.strftime("%H:%M:%S")
    f=open(events_json_file,'w')
    try:
         content=json.load(f)
    except JSONDecodeError:
        f.close()
        return upcoming_ongoing
    for i in range(len(content)):
        if Full_Name in content[i]["Users Registered"]:
            if content[i]["End Date"]>=date_today and content[i]["End Time"]>=current_time:
                upcoming_ongoing.apppend(content[i])
                
            
    f.close()
    return upcoming_ongoing




def View_all_events(events_json_file):
    details=[]
    f=open(events_json_file,'r+')
    try:
        content=json.load(f)
        f.close()
    except JSONDecodeError:
        f.close()
        return details
    for i in range(len(content)):
        details.append(content[i])
    return details


def Delete_Event(members_json_file,Full_Name,new_password,):
    
    f=open(members_json_file,'r+')
    content=json.load(f)
    c=0
    
    for i in range(len(content)):
        if content[i]["Full Name"]==Full_Name:
            content[i]["Password"]==new_password
            c=1
            break
    f.seek(0)
    f.truncate()
    json.dump(content,f)
    f.close()
    if c==1:
        return True
    else:
        return False
  
           
           

