from json import dump, load


class SettingManager:
    def __init__(self):
        self.setting = Setting({})

        self.filename = "./sub/settings.json"
        self.file = None

        self.load()

    def load(self):
        self.file = open(self.filename, "r")
        self.setting = Setting(load(self.file))

    def save(self):
        dump(self.setting.dict, open(self.filename, "w"), indent=2)  # PyCharm Default: 2 indent


class Setting:
    def __repr__(self):
        return repr(self.dict)

    def __str__(self):
        return str(self.dict)

    def __init__(self, org):
        """
        :param org: Original Set of Dictionary
        """
        self.dict = org if org is not None else {}

    def get(self, key=""):
        if key:
            if not isinstance(key, dict): key = [key]

            _temp = []
            for k in key:
                if k in self.dict.keys():
                    data = self.dict[k]
                    if type(data) is type({}):
                        _temp.append(Setting(data))
                    else:
                        _temp.append(data)
                else:
                    _temp.append(None)

            return _temp[0] if len(_temp) == 1 else _temp
        else:
            return None

    def set(self, _set=''):
        if not isinstance(_set, dict):
            raise TypeError({"object":_set, "object_type":type(_set), "objective_type":dict})

        errors = []
        succs = []

        for k, v in _set.items():
            try:
                self.dict[k] = v
                succs.append(k)
            except Exception as ex:
                errors.append((k,ex))

        return {"error": True, "suc":succs, "skipped":errors} if len(errors) else {"error":False}

    def dictify(self):
        return self.dict