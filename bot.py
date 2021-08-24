import config
import praw
import sys

class bot():
    def __init__(self):
        self.reddit = praw.Reddit("flairbot")
        self.subr = self.reddit.subreddit(str(config.subreddit))

    def change_flair(self):
        search_string = "flair:" + config.flair_text_to_change
        submissions = self.subr.search(search_string)
        count_of_subs = len(list(submissions))

        for submission in submissions:
            choices = submission.flair.choices()
            template_id = next(flair for flair in choices if flair["flair_text"] == config.flair_to_set)["flair_template_id"]
            submission.flair.select(template_id)


        return count_of_subs

if __name__ == '__main__':
    while True:
        result = bot().change_flair()
        print(result)
        if result < 1:
            break