import os
import pandas as pd
from datetime import datetime
from ics import Calendar, Event
from zoneinfo import ZoneInfo



def df_import():
    """
    Function to import the lab calendar dataframe and return it
    """
    df = pd.read_excel("lab_meeting_calendar.xlsx", sheet_name="2025")
    #df = df[df["Cancelled"]==False]  #filtering for lab meetings that are not cancelled
    df = df.fillna("")
    return(df)



def cal_csv():
    """
    Function to make a csv and outlook ics calendar file
    """
    # Making an event log dictionary to add events to
    event_log = {
        "Subject": [],
        "Start Date": [],
        "Start Time": [],
        "End Date": [],
        "End Time": [],
        "Location": [],
        "Description": [],
        "All Day Event": [],
        "Private": []
    }

    # Looping over all entries in the excel doc
    for index, row in df.iterrows():
        # Event descriptions
        lab_meeting = row["Lab Meeting"]
        jc = row["Journal Club"]
        totw = row["Technique of the Week"]
        food = row["Food (no nuts)"]
        notes = row["Notes"]
        desc = f"Lab Meeting: {lab_meeting}\nJournal Club: {jc}\nTechnique of the Week: {totw}\nFood (no nuts): {food}\n\nNotes: {notes}"
        #print(desc)
        
        # Adding items to the dictionary
        event_log["Subject"].append("Frankfort Lab Meeting")
        event_log["Start Date"].append(row["Date"])
        event_log["Start Time"].append(datetime.strptime('10am', '%I%p').time())
        event_log["End Date"].append(row["Date"])
        event_log["End Time"].append(datetime.strptime('12pm', '%I%p').time())
        event_log["Location"].append("4th floor conference room")
        event_log["Description"].append(desc)
        event_log["All Day Event"].append(False)
        event_log["Private"].append(False)
        
    # Turning dictionary into dataframe
    df_csv = pd.DataFrame.from_dict(event_log)
    
    # Create calendar
    calendar = Calendar()

    # Setting the time zone to central time
    tz = ZoneInfo("America/Chicago")

    # Loop over DataFrame rows
    for index, row in df_csv.iterrows():
        event = Event()
        event.name = row["Subject"]
        
        # Combine date and time
        start_dt = datetime.combine(pd.to_datetime(row["Start Date"]).date(), row["Start Time"]).replace(tzinfo=tz)
        end_dt = datetime.combine(pd.to_datetime(row["End Date"]).date(), row["End Time"]).replace(tzinfo=tz)
        
        #print(start_dt)
        #print(end_dt)
        
        event.begin = start_dt
        event.end = end_dt
        event.location = row["Location"]
        event.description = row["Description"]
        
        calendar.events.add(event)
    
    # Returning
    return(df_csv, calendar)



def web_df():
    """
    make a df to display on the website
    """
    df_web = df[["Date", "Lab Meeting", "Journal Club", "Food (no nuts)", "Notes"]]
    df_web.columns = ["Date", "Lab Meeting", "Journal Club", "Food", "Notes"]
    df_web = df_web[["Date", "Lab Meeting", "Journal Club", "Food", "Notes"]]
    return(df_web)




def df_exporter():
    """
    Export csv, calendar, and web dataframe
    """
    # Write to .ics file for Outlook calendar
    with open("frankfort_lab_meetings.ics", "w") as f:
        f.writelines(calendar)
    
    # Exporting to csv for importing into outlook
    df_csv.to_csv("lab_meeting_calendar.csv", index=False)

    # Exporting to html for use on the lab website
    df_web.to_html("lab_meeting_calendar.html", index=False, justify="left", border=0)



# Executing
if __name__ == "__main__":
    print(os.getcwd())
    df = df_import()
    df_csv, calendar = cal_csv()
    df_web = web_df()
    df_exporter()
    print("Done with script!")