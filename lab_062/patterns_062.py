import re

date = r"\b\d{1,2}[/-]\d{1,2}[/-]\d{2}"
phone = r'\b(?:01)[-\s]\d{7}\b'
email = r'\b(?:\w+\.)*\w+\@\w+\.\w+(?:\.\w+)*\b'
ldate = r'\b\d{1,2}\s(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s\d{2}'
