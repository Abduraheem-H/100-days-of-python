import requests


class Post:
    def __init__(self, post_id):
        self.post_id = post_id

    def get_post_by_id(self):
        response = requests.get(url=f"https://api.npoint.io/c790b4d5cab58020d391")
        post_data = response.json()
        for post in post_data:
            if post["id"] == self.post_id:
                return post
        return None
