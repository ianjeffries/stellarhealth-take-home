# stellarhealth-take-home
Repo showing Ian Jeffries' work for the stellar health coding exercise. Can find the final masked log in 
stellarhealth-take-home/dob_masking/masked_logs.txt

# Questionaire

1. I had observed through visual scanning of the text file that the date of births had a few different formats, the important ones being 
some were formatted with a / between dates, while others were formatted with a -, and finally some were in varchar form
rather than numeric. I built my code assuming that I had found every scenario and built it in a way to preserve the formatting. 

2. One major limitation of my code is that I assume I found all date formatting scenarios. I think it's relatively dynamic,
as it takes spacing into account, but if a new format were to show up my solution wouldn't catch it. To solve this, I would
probably think up a series of tests that see if there are any DOB records that are un-documented, and raise this as an error
before loading the log. Human intervention would be required to identify the new formatting. 

3. I would write the original log and the masked log to my desktop, then compare them side by side in my editor using 
Pycharm's compare file functionality to ensure the X replacement was populating correctly. I also searched "DOB" and scanned
through all the highlighted lines to identify any formatting scenarios I missed, along with variations of date formatting that I could think
of. 

4. On a systems level, I would probably first use a lambda to identify the keys within the s3 bucket along with their line length. 
I would store the keys in a dynamoDB along with how I would like to batch them. These records would have a set TTL that sends an 
SNS to lambda to process them in batches concurrently. 

5. My testing would be a lot more comprehensive, basically searching out anything that could be a DOB and making sure we
have a pattern to mask it. This would require alerts and human intervention at the beginning, but hopefully the frequency would
go down as we found more examples.

