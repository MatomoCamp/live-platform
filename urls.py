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
    "PBWV7L": "https://bbb-mtmc-2021.cloud-ed.fr/b/adm-4x6-d69-3j3",
    "GR9YQZ": "https://bbb-mtmc-2021.cloud-ed.fr/b/adm-utm-dis-kbn",
    "ZBWZHJ": "https://bbb-mtmc-2021.cloud-ed.fr/b/adm-y8m-nzp-x8r",
    "Y9AAMG": "https://bbb-mtmc-2021.cloud-ed.fr/b/adm-s3t-fj8-yt3",
}

recording_ids = {
    "G8K8AV": "hvT8uffTv5VUHuTBmKpTSw",
    "M9XPRG": "diyX79F4BuZK8211mw2fDK",
    "XTF7GX": "pzcpV32ibe7ersq663xHWu",
    "FDEE9Z": "dM3Rr4VNd2wvrA1EqyFc9T",
    "PBWV7L": "oiMkGGpP3mDNsJNL9d835B",
    "LKVJQ8": "8jEpE55dohwRHsQwPr5p6b",
    "DM8S7W": "oHbeE3zkk625HUvDVDtiVN",
    "LZ8NYG": "mmcu1wTvNLThuLti46Awza",
    "WGWW8R": "7jLhv438Q5vynKVMZ8ZqNb",
    "GDGZXF": "aeDEypqe36V3rit3zZ87k9",
    "9JHC8H": "nFQJq2ebTNQjeDCUTtEJo5",
    "GR9YQZ": "gqEzAyzDJz4KLR9gwygVK2",
    "GF7XD9": "dYuZAcGqWQYjtGPTSvacWY",
    "G98E3P": "34s6TgxQTWwsAQaqwHBv3U",
    "QRSQ8D": "bSaUBU9X5nBeMp7pWdNAGW",
    "3TTRKG": "wkefNPHyR4V115D8jvMNDC",
    "QQJ3ZS": "vQAunDod7FvMSD348rtxrv",
    "N3U3BT": "1JY5GBWLpe12bs1fGXMLgp",
    "PX7EHX": "kxzaXbKKtnRNH23XvpAZSN",
    "MKKVHX": "hyidpah6wPo91gz4tQW8YZ",
    "7AJEKD": "6QcpPoV5toTVi9dtHzR2TT",
    "HU8NSN": "qKNiW52zgX9tXGBFrBUwK8",
    "Y9AAMG": "xyiEgWGSUZVERTDcg2HqbB",
    "URWXGR": "9cExMatGbi3xH4hjJgndvt",
    "ENHZCR": "dEYt3WxM5V4jBk6BhT5oab",
    "GMUXZZ": "7N9bhdSHYq6zvfrt5E8mwN",
    "8HSWJD": "cBxLoU5N9g23C7QbBFsAf6"

}

for name in chat_rooms.values():
    for letter in name:
        assert letter in set(ascii_lowercase).union(set(digits)).union({"-"})
