import xml.etree.ElementTree

def goodTime(creationDate):
    time = creationDate.split('T')[1][:8].split(':')
    return 0 <= int(time[0]) * 60 * 60 + int(time[1]) * 60 + int(time[0]) <= 6 * 60 * 60

def getQuestions(main_file, file):
    posts = {}
    correct_post = {}
    max_comments = 0
    tree = xml.etree.ElementTree.parse(main_file)
    help_tree = xml.etree.ElementTree.parse(file)
    help_root = help_tree.getroot()
    root = tree.getroot()
    for post in range(len(help_root)):
        correct_post[help_root[post].attrib['Id']] = int(help_root[post].attrib['PostTypeId'])
    for comment in range(len(root)):
        if correct_post[root[comment].attrib['PostId']] == 1 and goodTime(root[comment].attrib['CreationDate']):
            posts[root[comment].attrib['PostId']] = posts.get(root[comment].attrib['PostId'], 0) + 1
            max_comments = max(max_comments, posts[root[comment].attrib['PostId']])
    good_posts = []
    for question in posts:
        if posts[question] == max_comments:
            good_posts.append(question)
    return good_posts, max_comments