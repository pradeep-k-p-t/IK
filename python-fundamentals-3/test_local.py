class TestScope():
    b = None 
    def test_local(self):
        a = "test"
        self.b = "test hello world"

    def test_global(self):
        #global s
        s = "gloabal s"


ts = TestScope()
ts.test_local()
print(ts.b)

s = "local s"
ts.test_global()
print(s)
