import re

# Sample text to test the regex patterns
sample_text = """
Here are some sample data:
- Email: j.anyar@alustudent.com, test.user+regex@example.com
- URL: https://github.com/Jongkuch1/alu_regex-data-extraction
- Phone numbers: +250 (0) 794411361, +211 (0) 929621876, + 254 (0) 711225041
- Time: 14:30, 2:30 PM
"""

# Regex patterns
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
url_pattern = r'https?://(?:www\.)?\S+\.\S+'
phone_pattern = r'\+\d{1,3}\s?\(?\d{1,4}\)?\s?\d{6,10}'
time_pattern = r'\b(?:[01]?\d|2[0-3]):[0-5]\d\b|\b(?:1[0-2]|0?[1-9]):[0-5]\d\s?(?:AM|PM)\b'


# Extract data using regex
emails = re.findall(email_pattern, sample_text)
urls = re.findall(url_pattern, sample_text)
phones = re.findall(phone_pattern, sample_text)
times = re.findall(time_pattern, sample_text)

# Print results
print("Extracted Emails:", emails)
print("Extracted URLs:", urls)
print("Extracted Phone Numbers:", phones)
print("Extracted Times:", times)
