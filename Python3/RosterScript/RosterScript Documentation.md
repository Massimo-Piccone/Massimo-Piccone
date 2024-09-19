# Roster PDF to iCalendar Script (Python3)
> This script works out-of-the-box for Emirates Roster. <br>
> You can find the complete script [here.](rosterScript.py) <br>
> [Here is a quick Tutorial](https://youtu.be/3E1GoA7wCEk) on how to use it - make sure you turn on *captions*.
## Objective
The purpose of this script is to make an easy and reliable way to convert a PDF schedule into iCalendar events.
I aim to make this as 'open source' and reusable as possible. There are some subscription-based services that can do this for you, but why pay when you can do it yourself?

To make this easier to work with, I emphasize regulating and defining the PDF output in **Step 1.** By doing this you can "easily" configure your pattern and ensure **Step 2** will function properly with minimal alterations.

## Strategy  
This script works by identifying the departure airport and setting this as the time-zone to base the event. To calculate the duration of the event we take the provided duration value (departure to arrival). The only issue is that I want the event to start the event at report time, so we find the difference between report time and departure and add this with the duration to get the full event time. 

My vision for this project comprised of 3 distinct components.
1. The script needed to scrape the PDF and process it to identify necessary information.
2. Use this regulated information to create iCalendar events accurately in every necessary time-zone.
3. (Optional) Add reminders for preparation.

## Prerequisites:

**PDF**
- Needs to be consistently structured and contain the following:
- Report time,
- Departure time,
- Departure Station, and
- Duration of flight.

**Python3**
- You will need a way of running a python3 script. <br> To do this I suggest [Jupyter Notebook](https://jupyter.org) or better yet, [Python](https://www.python.org) itself. Follow the provided instructions to install either.

## Step 1. Scrape the PDF for necessary information.
> This is an example of the PDF format all information presented is purely fictional for educational purposes.

<img width="502" alt="Screenshot 2024-09-18 at 17 30 24" src="https://github.com/user-attachments/assets/ddc2e112-f80c-4e94-8282-dacaba12f2f1">


### 1a. Extract and standardize the information.
I used PyPDF2 to extract and regulate the information on the PDF. I recommend following these steps to ensure the extraction is working properly on your PDF. Simply replace the complete path to your PDF file to begin.
```python
import PyPDF2

# Function to extract and clean up text from PDF
def extract_PDF_text(PDF_path):
    with open(PDF_path, 'rb') as file:
        reader = PyPDF2.PDFReader(file)
        text_data = []
        
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text = page.extract_text()
            if text:  # Ensure text is not None
                text = text.strip()  # Remove leading and trailing whitespace
                text = ' '.join(line.strip() for line in text.split('\n'))  # Remove line breaks and extra spaces
                text_data.append(text)  # Append cleaned text

    return text_data

# Function to compact text into a single string
def compact_text(text_data):
    compacted_text = ''.join(text_data)  # Join all text data
    compacted_text = ''.join(compacted_text.split())  # Remove all spaces
    return compacted_text

# Specify the PDF and extract
PDF_path = "/Users/massimopiccone/Desktop/Roster.pdf"  # Replace with the path to your PDF
PDF_text_content = extract_PDF_text(PDF_path)
compacted_text = compact_text(PDF_text_content)

# Print the compacted content
print(compacted_text)
```
> Output:
```
DutyDepartureArrivalDateTypeRep.timeFlightNo.StationTimeStationTimeDur.End01Sun02Mon03Tue20:25500DXB21:55BOM02:3603:1104Wed20:25501BOM04:35DXB05:5602:5105Thu06Fri07Sat05:25805DXB06:56JED08:3902:4305:25806JED10:38DXB14:2702:4908Sun14:15095DXB15:48FCO19:5206:0409Mon21:10096FCO22:22DXB06:1705:5510Tue11Wed12Thu13Fri14Sat15Sun16Mon08:35703DXB10:24MRU16:5606:3217Tue20:50704MRU21:50DXB04:2506:3518Wed19Thu07:40398DXB09:10DPS22:2009:1020Fri21Sat23:35399DPS00:35DXB05:3509:0022Sun23Mon24Tue08:25229DXB09:55SEA13:2514:3025Wed26Thu16:00230SEA17:15DXB18:3014:1527Fri28Sat29Sun01
```
Removing spaces and line breaks will help regulate the format and should make processing more reliable across multiple PDF files.

### 1b. Format and Filter the information. 
Now that I had this long string, I had to capture and identify the information that I needed. To do this I used regular expressions, which allowed me to capture the information in the horizontal rows. I started with the date and matched each value with its meaning. Anything that doesn't match is ignored.

To use this, paste the string you got from the previous function `compacted_text = """YOUR:COMPACT:STRING"""`
If your PDF is different, you will likely need to update the regular expression to identify the `pattern`.

<img width="520" alt="Screenshot 2024-09-18 at 19 26 37" src="https://github.com/user-attachments/assets/69121e2b-5b8b-4e22-904d-b37f93b94b95">

The pattern I am trying to identify is: **`03Tue20:25500DXB21:55BOM02:3603:11`** 

Heres a breakdown:

- `pattern = r'` to begin the regular expression.
- `(\d{2})` looks for 2 digits, representing the day of the month = `03`
- `(?:\w{3})?` skips 3 letters (Capital or lowercase), representing the day = `Tue`
- `(\d{2}:\d{2})` looks for 4 digits separated by a colon, representing the Rep.time = `20:25`
- `(\d{3})` looks for 3 digits, representing the Flight number =`500`
- `([A-Z]{3})` looks for 3 Capital letters, representing the Departure station = `DXB`
- `(\d{2}:\d{2})` looks for 4 digits separated by a colon, representing the Departure time = `21:55`
- `([A-Z]{3})` looks for 3 Capital letters, representing the Arrival station = `BOM`
- `(\d{2}:\d{2})` looks for 4 digits separated by a colon, representing the Arrival time = `02:36`
- `(\d{2}:\d{2})` looks for 4 digits separated by a colon, representing the Duration = `03:11`

`pattern = r'(\d{2})(?:\w{3})?(\d{2}:\d{2})(\d{3})([A-Z]{3})(\d{2}:\d{2})([A-Z]{3})(\d{2}:\d{2})(\d{2}:\d{2})'`

If your pattern is different, don't forget to configure this to match your pattern with the definitions.
```python
for match in matches:
    day, rep_time, flight_no, dep_station, dep_time, arr_station, arr_time, duration = match
```
---
```python
import re

# Original text
compacted_text = """DutyDepartureArrivalDateTypeRep.timeFlightNo.StationTimeStationTimeDur.End01Sun02Mon*03Tue20:25500DXB21:55BOM02:3603:11*04Wed20:25501BOM04:35DXB05:5602:5105Thu06Fri07Sat05:25805DXB06:56JED08:3902:4305:25806JED10:38DXB14:2702:4908Sun14:15095DXB15:48FCO19:5206:0409Mon21:10096FCO22:22DXB06:1705:5510Tue11Wed12Thu13Fri14Sat15Sun16Mon08:35703DXB10:24MRU16:5606:3217Tue20:50704MRU21:50DXB04:2506:3518Wed19Thu07:40398DXB09:10DPS22:2009:1020Fri21Sat23:35399DPS00:35DXB05:3509:0022Sun23Mon24Tue08:25229DXB09:55SEA13:2514:3025Wed26Thu16:00230SEA17:15DXB18:3014:1527Fri28Sat29Sun01"""

# Regular expression to match valid entries with flight data (time, flight number, etc.)
pattern = r'(\d{2})(?:\w{3})?(\d{2}:\d{2})(\d{3})([A-Z]{3})(\d{2}:\d{2})([A-Z]{3})(\d{2}:\d{2})(\d{2}:\d{2})'

matches = re.findall(pattern, compacted_text)

# Reformatting and printing the output
for match in matches:
    day, rep_time, flight_no, dep_station, dep_time, arr_station, arr_time, duration = match
    print(f"{day}, {rep_time}, {dep_station}, {dep_time}, {arr_station}, {arr_time}, {duration}, {flight_no}")

# Check if matches are found
if not matches:
    print("No matches found! Please check the regular expression or the input format.")
else:
    print(f"Found {len(matches)} matches")
```
> Output:
> day, rep_time, flight_no, dep_station, dep_time, arr_station, arr_time, duration
```
03, 20:25, DXB, 21:55, BOM, 02:36, 03:11, 500
04, 20:25, BOM, 04:35, DXB, 05:56, 02:51, 501
07, 05:25, DXB, 06:56, JED, 08:39, 02:43, 805
08, 14:15, DXB, 15:48, FCO, 19:52, 06:04, 095
09, 21:10, FCO, 22:22, DXB, 06:17, 05:55, 096
16, 08:35, DXB, 10:24, MRU, 16:56, 06:32, 703
17, 20:50, MRU, 21:50, DXB, 04:25, 06:35, 704
19, 07:40, DXB, 09:10, DPS, 22:20, 09:10, 398
21, 23:35, DPS, 00:35, DXB, 05:35, 09:00, 399
24, 08:25, DXB, 09:55, SEA, 13:25, 14:30, 229
26, 16:00, SEA, 17:15, DXB, 18:30, 14:15, 230
Found 12 matches
```
## Step 2. Use this information to make a time-zone-sensitive iCalendar file.

#### 2a) Specify the libraries I need to make this.
- `PyPDF2`: for manipulating and extracting data from PDF files.
- `re`: regular expressions, enabling pattern matching, searching, splitting, and replacing text within strings.
- `pytz`: accurate and cross-platform time-zone calculations
- `datetime`: for manipulating dates and times, allowing for operations like formatting, arithmetic, and time-zone handling.
- `icalendar`: used to create, parse, and manipulate iCalendar files in a standardized format.
```python
import PyPDF2
import re
import pytz
from datetime import datetime, timedelta
from icalendar import Event, Calendar
```
This is the function I made in step 1a.
```python
# Function to extract and clean up text from PDF
def extract_PDF_text(PDF_path):
    with open(PDF_path, 'rb') as file:
        reader = PyPDF2.PDFReader(file)
        text_data = []
        
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text = page.extract_text()
            if text:
                text = text.strip()
                text = ' '.join(line.strip() for line in text.split('\n'))
                text_data.append(text)
                
    return text_data

# Function to compact text into a single string
def compact_text(text_data):
    compacted_text = ''.join(text_data)
    compacted_text = ''.join(compacted_text.split())
    return compacted_text
```
I added many time-zones to lighten any future workload. It is important to ensure the necessary time-zones are mapped before each use.
```python
  # Define time-zone mapping
station_time-zones = {
    'AUH': 'Asia/Muscat',
    'AMS': 'Europe/Amsterdam',
    'ATH': 'Europe/Athens',
    'BKK': 'Asia/Bangkok',
    'BCN': 'Europe/Madrid',
    'PEK': 'Asia/Shanghai',
    'BER': 'Europe/Berlin',
    'BOS': 'America/New_York',
    'BRU': 'Europe/Brussels',
    'CAI': 'Africa/Cairo',
    'ORD': 'America/Chicago',
    'CMB': 'Asia/Colombo',
    'DFW': 'America/Chicago',
    'DEL': 'Asia/Kolkata',
    'DXB': 'Asia/Dubai',
    'GVA': 'Europe/Zurich',
    'HKG': 'Asia/Hong_Kong',
    'IST': 'Europe/Istanbul',
    'CGK': 'Asia/Jakarta', 
    'JNB': 'Africa/Johannesburg',
    'KUL': 'Asia/Kuala_Lumpur',
    'LHR': 'Europe/London',
    'LAX': 'America/Los_Angeles',
    'MAD': 'Europe/Madrid',
    'MAN': 'Europe/Manchester',
    'MEL': 'Australia/Melbourne',
    'MIA': 'America/New_York',
    'SVO': 'Europe/Moscow',
    'BOM': 'Asia/Kolkata',
    'JFK': 'America/New_York',
    'CDG': 'Europe/Paris',
    'FCO': 'Europe/Rome',
    'GRU': 'America/Sao_Paulo',
    'ICN': 'Asia/Seoul',
    'PVG': 'Asia/Shanghai',
    'SIN': 'Asia/Singapore',
    'SYD': 'Australia/Sydney',
    'NRT': 'Asia/Tokyo',
    'ZRH': 'Europe/Zurich',
    'MRU': 'Indian/Mauritius',
    'DPS': 'Asia/Jakarta', 
    'BOM': 'Asia/Kolkata',
    'JED': 'Asia/Riyadh',
    'FCO': 'Europe/Rome',
    'MRU': 'Indian/Mauritius',
    'DPS': 'Asia/Jakarta', 
    'SEA': 'America/Los_Angeles',
    'MCT': 'Asia/Muscat'
    # ADD MORE AS NEEDED
}
```
This segment calculates event duration while handling time-zone localization. The result is a localized event start time and the total duration, including pre-event time.
```python
def convert_to_local(date_str, time_str, time-zone):
    local_tz = pytz.time-zone(time-zone)
    local_time_str = f"{date_str} {time_str}"
    try:
        local_time = local_tz.localize(datetime.strptime(local_time_str, '%Y-%m-%d %H:%M'))
    except ValueError:
        print(f"Error parsing date/time: {local_time_str}")
        raise
    return local_time

def calculate_event_duration(rep_date, rep_time, dep_time, duration, time-zone):
    # Combine date and time strings
    rep_datetime_str = f"{rep_date} {rep_time}"
    dep_datetime_str = f"{rep_date} {dep_time}"
    
    # Convert to local time
    rep_datetime = convert_to_local(rep_date, rep_time, time-zone)
    dep_datetime = convert_to_local(rep_date, dep_time, time-zone)
    
    # Handle crossing midnight
    if dep_datetime < rep_datetime:
        dep_datetime += timedelta(days=1)
    
    # Calculate the duration between rep_time and dep_time
    pre_event_duration = (dep_datetime - rep_datetime).total_seconds()
    event_duration = timedelta(hours=int(duration.split(':')[0]), minutes=int(duration.split(':')[1]))
    
    total_event_duration = event_duration + timedelta(seconds=pre_event_duration)
    return rep_datetime, total_event_duration
```
This is the initiation of the PDF extraction and filtration from 1a and 1b. 
```python
# Extract and compact text from PDF
PDF_path = "WHERE/YOUR/PDF/FILE-IS.PDF"  # Replace with your PDF path
PDF_text_content = extract_PDF_text(PDF_path)
compacted_text = compact_text(PDF_text_content)

# Regular expression to match valid entries with flight data
pattern = r'(\d{2})(?:\w{3})?(\d{2}:\d{2})(\d{3})([A-Z]{3})(\d{2}:\d{2})([A-Z]{3})(\d{2}:\d{2})(\d{2}:\d{2})' # Replace with your own if you need.
matches = re.findall(pattern, compacted_text)

# Check if matches are found
if not matches:
    print("No matches found! Please check the regular expression or the input format.")
else:
    print(f"Found {len(matches)} Flights")
```
This is the segment that is responsible or creating the actual calendar events.
```python
# Create a calendar object
cal = Calendar()

# Process each flight
for match in matches:
    day, rep_time, flight_no, dep_station, dep_time, arr_station, arr_time, duration = match
    
    # Use the current year and month
    current_year = datetime.now().year
    current_month = datetime.now().month
    rep_date = f"{current_year}-{current_month:02d}-{day}"
    
    # Calculate event start time and duration
    try:
        rep_datetime, total_event_duration = calculate_event_duration(
            rep_date, rep_time, dep_time, duration, station_time-zones[dep_station]
        )
    except ValueError:
        print(f"Skipping event due to parsing error for flight {flight_no}")
        continue
    
    # Create a flight event
    flight_event = Event()
    flight_event.add('summary', f"Flight {flight_no} from {dep_station} to {arr_station}")
    flight_event.add('dtstart', rep_datetime)
    flight_event.add('dtend', rep_datetime + total_event_duration)
    flight_event.add('location', f"{dep_station} to {arr_station}")
    
    # Add the flight event to the calendar
    cal.add_component(flight_event)

# Write the calendar to a file
with open('/Users/massimopiccone/Desktop/Flights.ics', 'wb') as f:  # Replace with desired path
    f.write(cal.to_ical())

print("iCal file has been created.")
```
```
Found 12 Flights
iCal file has been created.
```
<img width="1440" alt="Screenshot 2024-09-18 at 17 22 09" src="https://github.com/user-attachments/assets/6fd552e0-4276-4dc4-82b2-303fd23943ed">
<img width="1536" alt="Screenshot 2024-09-18 at 16 27 41" src="https://github.com/user-attachments/assets/7468058b-7cd1-4f0d-8c76-8c34a8b9cd3c">
<img width="1536" alt="Screenshot 2024-09-18 at 16 26 58" src="https://github.com/user-attachments/assets/be6a4013-adba-40b6-939d-cb533a71df26">

## Step 3. Add rest and recovery events.
#### I added this code directly after the flight creation within the calendar creation process.
As you can see, I created a 9-hour event before every flight. This is to ensure she has enough time to sleep, pack and get ready. <br>
I also added a 2-hour recovery period where she is finishing post-flight duties and travelling to her accommodation. This is mainly to show that she is still busy.
```python
    # Create a "Rest" event 9 hours before the flight
    rest_event = Event()
    rest_start = rep_datetime - timedelta(hours=9)
    rest_end = rep_datetime
    rest_event.add('summary', f"Rest before flight {flight_no}")
    rest_event.add('dtstart', rest_start)
    rest_event.add('dtend', rest_end)
    rest_event.add('location', dep_station)
    cal.add_component(rest_event)

     # Create a "Recover" event starting immediately after the flight and lasting 2 hours
    recover_event = Event()
    recover_start = rep_datetime + total_event_duration
    recover_end = recover_start + timedelta(hours=2)
    recover_event.add('summary', f"Recover after flight {flight_no}")
    recover_event.add('dtstart', recover_start)
    recover_event.add('dtend', recover_end)
    recover_event.add('location', arr_station)
    cal.add_component(recover_event)

# Write the calendar to a file
with open('/Users/massimopiccone/Desktop/Flights.ics', 'wb') as f:  # Replace with desired path
    f.write(cal.to_ical())
# Print confirmation
print("iCal file has been created.")
```
```
Found 12 Flights
iCal file has been created.
```
<img width="1536" alt="Screenshot 2024-09-18 at 16 37 05" src="https://github.com/user-attachments/assets/f254e106-e170-4fbb-8e2d-7b4470579278">
<img width="1536" alt="Screenshot 2024-09-18 at 16 34 50" src="https://github.com/user-attachments/assets/15c5f295-e3cd-462d-9d8d-1d94786fd4b9">

### Notes:
- If your roster lists flights into the next month, it will be processed as if it were in your current month.
- This script only creates events for the current month, anything outside of that needs to be manually moved.
- Be sure to map all necessary airport codes before use, I will update this to my own needs and you should do the same.

## Summary
I used Python to effectively read a monthly roster PDF file and turn it into an iCalendar file with time-zone support. 
The code has built-in redundancy such as normalizing all information, and it also includes confirmation and troubleshooting snippets to help identify potential issues. As final touches, I included preparation and recovery events to help plan a more structured life for my friend.

# What's next?
I still have a few ideas that I want to include but it gets exponentially more complicated and tedious so I'm leaving it here for now.

- Scraping and formatting (or simply listing) bus times. I want it to specify the bus that she needs to catch to get her to the airport before her report time.
- I would also look into making this more acceptable through some sort of GUI application, or website. For now, a quick tutorial will be all.

You can find the complete script [here.](rosterScript.py) <br> I will keep this project up-to-date with my own progress. Feel free to use and change this project to fit your needs.
