class TestScope():
    b = None 
    def test_local(self):
        a = "test"
        self.b = "test hello world"

ts = TestScope()
ts.test_local()
print(ts.b)

