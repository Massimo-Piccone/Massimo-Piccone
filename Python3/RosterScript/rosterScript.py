# -----!-!-!-!- BEFORE USE -!-!-!-!----- 
# 1. ADD NECESSARY TIMEZONE MAPPING (pytz) (LINE 85)
# 2. DEFINE FULL PATH TO YOUR ROSTER PDF /FILE.pdf (LINE 119)
# 3. DEFINE FULL PATH TO CALENDAR OUTPUT FOLDER AND /FILE-NAME.ics (LINE 185)

import PyPDF2
import re
import pytz
from datetime import datetime, timedelta
from icalendar import Event, Calendar

# Function to extract and clean up text from PDF
def extract_pdf_text(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
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


  # Define timezone mapping
station_timezones = {
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

def convert_to_local(date_str, time_str, timezone):
    local_tz = pytz.timezone(timezone)
    local_time_str = f"{date_str} {time_str}"
    try:
        local_time = local_tz.localize(datetime.strptime(local_time_str, '%Y-%m-%d %H:%M'))
    except ValueError:
        print(f"Error parsing date/time: {local_time_str}")
        raise
    return local_time

def calculate_event_duration(rep_date, rep_time, dep_time, duration, timezone):
    # Combine date and time strings
    rep_datetime_str = f"{rep_date} {rep_time}"
    dep_datetime_str = f"{rep_date} {dep_time}"
    
    # Convert to local time
    rep_datetime = convert_to_local(rep_date, rep_time, timezone)
    dep_datetime = convert_to_local(rep_date, dep_time, timezone)
    
    # Handle crossing midnight
    if dep_datetime < rep_datetime:
        dep_datetime += timedelta(days=1)
    
    # Calculate the duration between rep_time and dep_time
    pre_event_duration = (dep_datetime - rep_datetime).total_seconds()
    event_duration = timedelta(hours=int(duration.split(':')[0]), minutes=int(duration.split(':')[1]))
    
    total_event_duration = event_duration + timedelta(seconds=pre_event_duration)
    return rep_datetime, total_event_duration

# Extract and compact text from PDF
pdf_path = "/FULL/PATH/TO/YOUR/PDF-FILE.pdf"  # REPLACE WITH PATH TO YOUR PDF
pdf_text_content = extract_pdf_text(pdf_path)
compacted_text = compact_text(pdf_text_content)

# Regular expression to match valid entries with flight data
pattern = r'(\d{2})(?:\w{3})?(\d{2}:\d{2})(\d{3})([A-Z]{3})(\d{2}:\d{2})([A-Z]{3})(\d{2}:\d{2})(\d{2}:\d{2})'
matches = re.findall(pattern, compacted_text)

# Check if matches are found
if not matches:
    print("No matches found! Please check the regular expression or the input format.")
else:
    print(f"Found {len(matches)} Flights")

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
            rep_date, rep_time, dep_time, duration, station_timezones[dep_station]
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
with open('TELL/IT/WHERE/TO/MAKE/THE/CALENDAR-FILE.ics', 'wb') as f:  # REPLACE WITH PATH TO DESIRED OUTPUT FOLDER AND /FILE NAME.ICS
    f.write(cal.to_ical())

print("iCal file 'flight_schedule.ics' has been created.")
