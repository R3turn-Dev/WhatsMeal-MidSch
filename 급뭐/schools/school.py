from datetime import datetime


class School:
    def __init__(self, region, code):
        self.region = region
        self.code = code

        self.url = None

    def get(self, date=None):
        if date is None:
            date = datetime.now()

        if date:
            if isinstance(date, datetime):
                y, m, d = list(map(int, date.strftime("%Y|%m|%d").split("|")))

                # TODO: Parse homepage with School Code

            else:
                raise TypeError("[{}] `Date` has not supported type (expected datetime.datetime)".format(__name__))

        else:
            raise ValueError("[{}] `Date` has not supported value".format(__name__))