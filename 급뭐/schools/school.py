from datetime import datetime

KINT = 1
ELEM = 2
MIDDLE = 3
HIGH = 4


class School:
    def __init__(self, region, type, code):
        self.region = region
        self.type = type
        self.code = code

        self.url = "http://stu.{region}.go.kr/sts_sci_md00_001.do?schulCode=" \
                   "{code}&schulCrseScCode={type}&schulKndScCode=0{type}&schMmealScCode=1" \
            .format(region=self.region, code=self.code, type=self.type)

    def get(self, date=None):
        if date is None:
            date = datetime.now()

        if date:
            if isinstance(date, datetime):
                y, m, d = list(map(int, date.strftime("%Y|%m|%d").split("|")))

                link = self.url + "&ay={year}&mm={month}".format(year=y, month=m)

            else:
                raise TypeError("[{}] `Date` has not supported type (expected datetime.datetime)".format(__name__))

        else:
            raise ValueError("[{}] `Date` has not supported value".format(__name__))
