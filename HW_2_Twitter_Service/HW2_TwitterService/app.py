
# Author: Pooja Sindham and Aarsh Seth
# Team Puma

from flask import Flask, render_template, request, jsonify
from mastodon import Mastodon, MastodonAPIError, MastodonNetworkError, MastodonUnauthorizedError
import os
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

# Initialize Mastodon API
mastodon = Mastodon(
    access_token=os.getenv('ACCESS_TOKEN'),
    api_base_url="https://mastodon.social"
)

#Function for error handling
def handle_error(error_message, status_code=500):
    return jsonify({"error": error_message}), status_code

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/post", methods=["POST"])
def create_post():
    try:
        content = request.json.get("content", "")
        if not content.strip():
            return handle_error("Post content cannot be empty", 400)
        post = mastodon.status_post(content)
        return jsonify({"message": "Post created", "id": post["id"]})
    except MastodonUnauthorizedError:
        return handle_error("Invalid API credentials. Please check your access token.", 401)
    except MastodonAPIError as e:
        return handle_error(f"Mastodon API error: {str(e)}")
    except MastodonNetworkError:
        return handle_error("Network error. Please check your connection.", 503)
    except Exception as e:
        return handle_error(f"Unexpected error: {str(e)}")

@app.route("/get/<post_id>", methods=["GET"])
def get_post(post_id):
    try:
        post = mastodon.status(post_id)
        return jsonify({"content": post["content"], "created_at": post["created_at"]})
    except MastodonAPIError as e:
        return handle_error(f"Failed to retrieve post: {str(e)}", status_code=404)
    except Exception as e:
        return handle_error(f"Unexpected error: {str(e)}")

@app.route("/delete/<post_id>", methods=["DELETE"])
def delete_post(post_id):
    try:
        mastodon.status_delete(post_id)
        return jsonify({"message": "Post deleted successfully"})
    except MastodonAPIError as e:
        return handle_error(f"Failed to delete post: {str(e)}")
    except Exception as e:
        return handle_error(f"Unexpected error: {str(e)}")

@app.route("/user", methods=["GET"])
def get_user_details():
    try:
        account = mastodon.account_verify_credentials()
        return jsonify({
            "username": account["username"],
            "followers": account["followers_count"],
            "following": account["following_count"],
            "statuses": account["statuses_count"]
        })
    except MastodonAPIError as e:
        return handle_error(f"Failed to fetch user details: {str(e)}")
    except Exception as e:
        return handle_error(f"Unexpected error: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)
