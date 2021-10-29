from string import ascii_lowercase, digits

chat_rooms = {
    "3TTRKG": "spa-applications",
    "7AJEKD": "background-tracking",
    "8HSWJD": "q-a",
    "9JHC8H": "closing-event",
    "DM8S7W": "matomo-for-a-saas",
    "ENHZCR": "gdpr-compliance",
    "FDEE9Z": "research-trial",
    "G8K8AV": "incidences-cote-infra",
    "G98E3P": "user-feedback-plugin",
    "GDGZXF": "event-introduction",
    "GF7XD9": "tagmanager-basics",
    "GMUXZZ": "conversion-rate-optimization",
    "GR9YQZ": "matomo-kompakt",
    "HU8NSN": "risk-for-a-dpo",
    "KDBDPX": "translating-matomo",
    "LKVJQ8": "public-sector",
    "LZ8NYG": "compliant-with-privacy-regulations",
    "M9XPRG": "cleaninsights-talk",
    "MKKVHX": "building-own-business",
    "N3U3BT": "metabase",
    "PBWV7L": "seo",
    "PX7EHX": "configurer-matomo-dans-le-respect-du-rgpd",
    "QRSQ8D": "break-and-fix",
    "URWXGR": "millions-of-pageviews",
    "WGWW8R": "surveillance-societies",
    "XAAHDQ": "open-source-data-visualization",
    "XTF7GX": "tips-and-tricks",
    "Y9AAMG": "host-own-instance",
    "ZBWZHJ": "cleaninsights-workshop",
    "QQJ3ZS": "privacy-in-web-analytics"
}

workshop_urls = {
    "PBWV7L": "https://example.com",
    "GR9YQZ": "https://example.com",
    "ZBWZHJ": "https://example.com",
    "Y9AAMG": "https://example.com",
}

for name in chat_rooms.values():
    for letter in name:
        assert letter in set(ascii_lowercase).union(set(digits)).union({"-"})
