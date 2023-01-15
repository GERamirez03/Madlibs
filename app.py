from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from static.stories import Story, story

app = Flask(__name__)
app.config['SECRET_KEY'] = "my-secret"

debug = DebugToolbarExtension(app)

prompts = story.prompts

@app.route('/')
def show_homepage():
    return render_template('homepage.html', prompts = prompts)

@app.route('/story')
def show_story():
    story_dict = {}
    for prompt in prompts:
        story_dict[prompt] = request.args[prompt]
    story_text = story.generate(story_dict)
    return render_template('story.html', story_text = story_text)