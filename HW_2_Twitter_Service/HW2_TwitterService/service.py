# Author: Pooja Sindham and Aarsh Seth
# Team Puma

from mastodon import Mastodon

class MastodonService:
    def __init__(self, access_token):
        """Initialize Mastodon API client."""
        self.mastodon = Mastodon(access_token=access_token, api_base_url='https://mastodon.social')

    def create_post(self, post_text):
        """Create a post on Mastodon."""
        if not post_text.strip():
            raise Exception("Invalid post content")
        if len(post_text) > 500:
            raise Exception("Invalid post content")
        return self.mastodon.status_post(post_text)

    def retrieve_post(self, post_id):
        """Retrieve a post by ID."""
        return self.mastodon.status(post_id)

    def delete_post(self, post_id):
        """Delete a post by ID."""
        return self.mastodon.status_delete(post_id)
