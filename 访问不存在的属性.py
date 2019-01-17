class Test:
    def __getattr__(self, name):
        return 'This attribute isn\'t exsit.'
        
            
