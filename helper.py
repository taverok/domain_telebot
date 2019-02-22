from collections import defaultdict
from telegram import Update


WARN_DAY_REMAINS = 60
all_domains = defaultdict(list)
all_projects = []
current_projects = []


def get_chat_id(update: Update):
    return update.message.chat_id
