from locust import HttpUser, task, between

class PhotoAlbumUser(HttpUser):
    wait_time = between(1, 2) # 1-2 másodperces szünet a kérések között

    @task(3)
    def view_home(self):
        self.client.get("/")

    @task(2)
    def view_photolist(self):
        self.client.get("/")

    @task(1)
    def check_login_page(self):
        self.client.get("/users/login/")