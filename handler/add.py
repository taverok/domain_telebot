from telegram import Bot, Update
from helper import *
from model.domain import sanitize, Domain


def add_command(bot: Bot, update: Update, args):
    subcommand, *args = args

    if subcommand not in add_subcommands.keys():
        text = "subcommand {} not recognized, available are {}".format(subcommand, add_subcommands.keys)
        bot.send_message(chat_id=get_chat_id(update), text=text)
        return

    add_subcommands.get(subcommand)(bot, update, args)


def add_domain(bot: Bot, update: Update, args):
    project, *domains = args
    new_domains = [sanitize(d) for d in domains]
    all_domains[project].extend(new_domains)

    text = "domains added:\n {}".format("\n".join(new_domains))
    bot.send_message(chat_id=get_chat_id(update), text=text)


def add_project(bot: Bot, update: Update, args):
    project, *_ = args
    all_projects.append(project)

    text = "project {} added".format(project)
    bot.send_message(chat_id=get_chat_id(update), text=text)


add_subcommands = {
    'domain': add_domain,
    'project': add_project
}


def check_command(bot: Bot, update: Update, args):
    project, *_ = args

    text = ""
    for d in all_domains.get(project):
        domain = Domain(d)
        if domain.needs_prolongation():
            text += "{} ends in {} days\n".format(d, domain.days_left())

    if text:
        bot.send_message(chat_id=get_chat_id(update), text=text)