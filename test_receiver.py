from receiver import app


class TestClass:

    def test_health(self):
        self.app = app.test_client()
        response = self.app.get('/api/v1/info')
        assert response.status_code == 200
