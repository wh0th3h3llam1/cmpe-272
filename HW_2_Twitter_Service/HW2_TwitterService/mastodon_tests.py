# Author: Pooja Sindham and Aarsh Sheth
# Team Puma

import unittest
from unittest.mock import patch, Mock
from app import app


class TestMastodonAPI(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.valid_post_id = "98765"

    @patch("app.mastodon.status_post")
    @patch("app.mastodon.status")
    @patch("app.mastodon.status_delete")
    @patch("app.mastodon.account_verify_credentials")
    def test_mastodon_api(self, mock_account, mock_delete, mock_get, mock_post):

        # Create a Post
        with self.subTest("Create Post"):
            mock_post.return_value = {"id": self.valid_post_id}
            response = self.client.post("/post", json={"content": "Hello Mastodon!"})
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json["id"], self.valid_post_id)

        # Retrieve the Created Post
        with self.subTest("Retrieve Post"):
            mock_get.return_value = {
                "id": self.valid_post_id,
                "content": "Hello Mastodon!",
                "created_at": "2025-02-28T10:00:00Z",
            }
            response = self.client.get(f"/get/{self.valid_post_id}")
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json["content"], "Hello Mastodon!")

        # Delete the Post
        with self.subTest("Delete Post"):
            mock_delete.return_value = {}
            response = self.client.delete(f"/delete/{self.valid_post_id}")
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json["message"], "Post deleted successfully")

        # Retrieve Deleted Post (Should Fail)
        with self.subTest("Retrieve Deleted Post"):
            mock_get.side_effect = Exception("Post not found")
            response = self.client.get(f"/get/{self.valid_post_id}")
            self.assertEqual(response.status_code, 500)
            self.assertIn("error", response.json)

        # Get User Details
        with self.subTest("Get User Details"):
            mock_account.return_value = {
                "username": "testuser",
                "followers_count": 100,
                "following_count": 50,
                "statuses_count": 200,
            }
            response = self.client.get("/user")
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json["username"], "testuser")


if __name__ == "__main__":
    unittest.main()
