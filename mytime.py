from datetime import datetime, timedelta

class Time(object):

    def __init__(self):
        self.hours = int(datetime.now().strftime("%H"))
        self.minutes = int(datetime.now().strftime("%M"))
        self.year = int(datetime.now().strftime("%Y"))
        self.month = datetime.now().strftime("%B")
        self.imonth = int(datetime.now().strftime("%m"))
        self.day = datetime.now().strftime("%A")
        self.date = datetime.now().strftime("%d")

    def update_hours(self, hrs):
        self.hours += hrs
        if(self.hours >= 24):
            self.hours -= 24
        time_temp = datetime.now() + timedelta(days=1)
        self.set_date(time_temp.strftime("%d"))
        self.update_day(time_temp)

    def inc_date(self):
        self.date = int(self.date) + 1
        new_time = datetime(self.get_iyear(), self.get_imonth(), self.get_date() + 1)
        self.update_day(new_time)

    def update_min(self, min):
        self.minutes += min
        if(self.minutes >= 60):
            self.minutes -= 60
            self.update_hours(1)
    
    def update_day(self, time):
        self.day = time.strftime("%A")

    def set_hours(self, inp):
        self.hours = inp
    def set_min(self, inp):
        self.minutes = inp
    def set_year(self, inp):
        self.year = inp
    def set_month(self, inp):
        self.month = inp
    def set_day(self, inp):
        self.day = inp
    def set_date(self, inp):
        self.date = inp

    def get_hours(self):
        if(self.hours >= 0 and self.hours <= 9):
            return '0' + str(self.hours)
        else:
            return str(self.hours)
    def get_ihours(self):
        return self.hours
    def get_min(self):
        if(self.minutes >= 0 and self.minutes <=9):
            return '0' + str(self.minutes)
        return str(self.minutes)
    def get_imin(self):
        return self.minutes
    def get_imonth(self):
        return self.imonth
    def get_year(self):
        return str(self.year)
    def get_iyear(self):
        return self.year
    def get_month(self):
        return self.month
    def get_day(self):
        return self.day
    def get_date(self):
        return self.date
    def get_sdate(self):
        return str(self.date)
    def get_human(self):
        return self.get_hours() +  self.get_min() + " hours, " +  str(self.get_day()) + ", " +  str(self.get_date()) + " " +  str(self.get_month()) + ", " +  str(self.get_year())
