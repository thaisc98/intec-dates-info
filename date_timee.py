from datetime import datetime

class DateTimee:
    def dateTimeDO(self):
        date = datetime.now().strftime("%d %B, %Y %H:%M:%S");
        if date is None:
            return "Invalid"
        return date;