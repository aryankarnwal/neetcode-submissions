class Singleton:
    __instance = None
   
    # In python consider this method as the 'getInstance'
    def __new__(cls):

        if not cls.__instance:
            cls.__instance = super().__new__(cls)
        return cls.__instance
        


    def getValue(self) -> str:
        return self.value
    def setValue(self, value: str):
        self.value = value
