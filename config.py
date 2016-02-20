import os
from pygithub3 import Github

GH_USERNAME = os.getenv("GH_USERNAME", None)
GH_TOKEN = os.getenv("GH_TOKEN", None)
GH_REPO = os.getenv("GH_REPO", "fifth-guy")
GH_SECRET_TOKEN = os.getenv("GH_SECRET_TOKEN", None)

assert GH_USERNAME is not None, "You must set the GH_USERNAME env var"
assert GH_TOKEN is not None, "You must set the GH_TOKEN env var"

github = Github(user=GH_USERNAME,
                token=GH_TOKEN,
                repo=GH_REPO)

def create_github_webhook(url):
    hook_data = {
        "name": "web",
        "active": True,
        "config": {
            "content_type": "json",
            "secret": GH_SECRET_TOKEN,
            "insecure_ssl": "1",
            "url": url
        },
        "events": ["pull_request_review_comment", ]
    }

    import pdb; pdb.set_trace()
    return github.repos.hooks.create(
        data=hook_data,
        user=GH_USERNAME,
        repo=GH_REPO)

#create_github_webhook("fifth-guy.herokuapp.com/comment-webhook")