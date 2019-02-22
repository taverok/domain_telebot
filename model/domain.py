import os
import string
from datetime import datetime

from whois import whois


class Domain:
    ENV_KEY_DAYS_LEFT = "DAYS_LEFT_LIMIT"
    DEFAULT_DAYS_LEFT_LIMIT = 10

    def __init__(self, domain: str):
        self.domain = domain.strip().strip("/")
        self.whois_info = whois(domain)
        self.expiration_date = get_expiration_date(self.whois_info)

    def needs_prolongation(self, warn_days=None):
        if not warn_days:
            warn_days = os.getenv(self.ENV_KEY_DAYS_LEFT, default=self.DEFAULT_DAYS_LEFT_LIMIT)

        return (self.expiration_date - datetime.now()).days < warn_days

    def days_left(self):
        return (self.expiration_date - datetime.now()).days


def get_expiration_date(whois_info) -> datetime:
    expiration_date = whois_info.get("expiration_date")

    return expiration_date[0] if isinstance(expiration_date, list) else expiration_date


def sanitize(domain: str):
    return domain.strip(string.punctuation+string.whitespace)
