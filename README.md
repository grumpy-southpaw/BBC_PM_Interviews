# BBC_PM_Interviews

This is a list of interviews on the BBC PM programme (https://www.bbc.co.uk/programmes/b006qskw), starting with the 25/03/2019 edition, and a simple python script to produce some plots.

The data are stored as a simple csv file (bbc_pm.csv). 

Inclusion: 
* Any live or pre-recorded interview or statement with a sitting member of parliament.

Exclusion:
* Any clip of an MP speaking during a summary of the news headlines.
* Any clip of an MP speaking in the house of commons.

The data are pretty simply structured:


Date - the date the programme was first broadcast

Interviewee	- Name of the person being interviewed

Party	- The political party they belong to (or independent)

Senior - Whether the MP is a senior member of their party. This means a minister for the governing party, shadow minister for the official opposition and spokesperson for other parties. Independent MPs cannot be senior.

min_start	- The minute the clip started (using the online player's time index)

sec_start	- The second the clip started

min_stop - The minute the clip ended

sec_stop - the second the clip ended 

Elapsed	- Decimal minutes the clip lasted: min_start + sec_start / 60 - (min_stop + sec_stop / 60)

Notes - Any other notes of interest


Questions / Comments can be sent to my email address (southpawgrumpy@gmail.com) or twitter (@grumpy_southpaw)
