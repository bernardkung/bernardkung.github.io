import datetime
import os

def  create_blog_post():
    '''Automate creating a post markdown file.'''

    title = input("Enter blog title: ")

    today = datetime.datetime.today().date()
    underscore_title = title.replace(" ", "-").lower()
    full_title = "{today}-{title}.md".format(today=today, title=underscore_title)
    
    script_path = os.path.dirname(__file__)
    rel_path = "_posts/" + full_title
    abs_path = os.path.join(script_path, rel_path)
    
    post_content = "---\nlayout: post\ntitle: {}\ndate: {}\n---\n\n".format(title, today)

    with open(abs_path, "x") as new_post_file:
        new_post_file.write(post_content)

create_blog_post()


