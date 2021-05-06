class ConvertTime:
    def __init__(self, clean: bool = False):
        """IF CLEAN = TRUE, THEN ConvertTime.format() WONT SHOW TIMES THAT ARE 0"""
        self.convertedTime = {"days": 0, "hours": 0, "minutes": 0, "seconds": 0}
        self.clean = clean

    @staticmethod
    def days(time: int):
        if time >= 86400:
            if time % 86400 == 0:
                return {"total": int(time / 86400), "remainder": 0}
            else:
                return {"total": int(time / 86400), "remainder": time % 86400}
        else:
            return {"total": 0, "remainder": time}

    @staticmethod
    def hours(time: int):
        if time >= 3600:
            if time % 3600 == 0:
                return {"total": int(time / 3600), "remainder": 0}
            else:
                return {"total": int(time / 3600), "remainder": time % 3600}
        else:
            return {"total": 0, "remainder": time}

    @staticmethod
    def minutes(time: int):
        if time >= 60:
            if time % 60 == 0:
                return {"total": int(time / 60), "remainder": 0}
            else:
                return {"total": int(time / 60), "remainder": time % 60}
        else:
            return {"total": 0, "remainder": time}

    def convert(self, time: int):
        days = self.days(time)
        self.convertedTime["days"] = days["total"]
        hours = self.hours(days["remainder"])
        self.convertedTime["hours"] = hours["total"]
        minutes = self.minutes(hours["remainder"])
        self.convertedTime["minutes"] = minutes["total"]
        self.convertedTime["seconds"] = minutes["remainder"]

    def map_items(self, key: str):
        """USED TO CONVERT ITEMS IN DICT TO STRING
        THIS FUNCTION IS CALLED EXCLUSIVELY BY ConvertTime.format()"""
        if int(self.convertedTime[key]) == 1:
            return f"{self.convertedTime[key]} {key[:-1]}"
        elif int(self.convertedTime[key]) == 0:
            if not self.clean:
                return f"{self.convertedTime[key]} {key}"
            else:
                return None
        else:
            return f"{self.convertedTime[key]} {key}"

    def format(self, separator: str = ","):
        """FORMATS JSON INTO HUMAN READABLE STR
        :separator = str: the separator between each time type ex:  (1 day, 4 hours) or  (1 day and 4 hours)"""
        holding_list = map(self.map_items, self.convertedTime.keys())

        return f"{separator} ".join(filter(lambda x: x is not None, holding_list))

    def convert_and_format(self, time: int, separator: str = ","):
        """JUST convert() + format()"""
        self.convert(time)
        return self.format(separator)


if __name__ == '__main__':
    t = 62
    conv = ConvertTime(clean=True)
    print(conv.convert_and_format(t, separator=" and"))
