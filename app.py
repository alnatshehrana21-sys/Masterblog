import json
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


# --- Helper Functions ---

def fetch_posts():
    """Reads the blog posts from the JSON file."""
    try:
        with open('posts.json', 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_posts(posts):
    """Writes the list of blog posts back to the JSON file."""
    with open('posts.json', 'w') as file:
        json.dump(posts, file, indent=4)


# --- Routes ---

@app.route('/')
def index():
    blog_posts = fetch_posts()
    return render_template('index.html', posts=blog_posts)


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        posts = fetch_posts()

        author = request.form.get('author')
        title = request.form.get('title')
        content = request.form.get('content')

        # 1. VALIDATION: Ensure no fields are empty
        if not author or not title or not content:
            return "Error: All fields are required!", 400

        # 2. ID MAX LOGIC: Find the highest ID and add 1
        if posts:
            new_id = max(post['id'] for post in posts) + 1
        else:
            new_id = 1

        new_post = {
            "id": new_id,
            "author": author,
            "title": title,
            "content": content
        }

        posts.append(new_post)
        save_posts(posts)
        return redirect(url_for('index'))

    return render_template('add.html')


@app.route('/delete/<int:post_id>', methods=['POST'])
def delete(post_id):
    posts = fetch_posts()
    # Filter the list to exclude the post with the matching ID
    updated_posts = [p for p in posts if p['id'] != post_id]

    save_posts(updated_posts)
    return redirect(url_for('index'))


@app.route('/update/<int:post_id>', methods=['GET', 'POST'])
def update(post_id):
    posts = fetch_posts()
    # Using 'next' is a clean way to find the dictionary we want
    post_to_update = next((p for p in posts if p['id'] == post_id), None)

    if not post_to_update:
        return "Post not found", 404

    if request.method == 'POST':
        # Capture updated data
        post_to_update['author'] = request.form.get('author')
        post_to_update['title'] = request.form.get('title')
        post_to_update['content'] = request.form.get('content')

        save_posts(posts)
        return redirect(url_for('index'))

    return render_template('update.html', post=post_to_update)


if __name__ == '__main__':
    # Using 5001 if your Port 5000 is still blocked by AirPlay
    app.run(host="127.0.0.1", port=5000, debug=True)