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
    # "KDBDPX": "translating-matomo",
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
    # "XAAHDQ": "open-source-data-visualization",
    "XTF7GX": "tips-and-tricks",
    "Y9AAMG": "host-own-instance",
    "ZBWZHJ": "cleaninsights-workshop",
    "QQJ3ZS": "privacy-in-web-analytics",

    # 2022

    "H7YHTG": "event-introduction-2022",  # Event introduction by the MatomoCamp organizers
    # "JSPF8U": "",  # Yet to be named support talk
    # "PYQY3A": "",  # Monter une infrastructure Matomo qui gère des millions de hits par mois n’est pas si simple
    # "3DBQCM": "",  # How to create your own Matomo plugin? A technical introduction to developing for Matomo.
    "3LRN3P": "ideal-matomo",  # Imagine Ideal Matomo !
    # "EMG79M": "",  # Réussir l'implémentationde Matomo - SOS Villages d'enfants x Elevate
    # "MWQUT7": "",  # An Inside Look at the Future of Matomo: User Experience + User Connection
    # "S37GBU": "",  # Gestion de projet Web Analytics avec Matomo
    "PU7SJR": "contributing-back",  # Contribute back
    # "33QBWR": "",  # Is Matomo only for European companies and authorities?
    # "AXGTWL": "",  # Analysez vos performances digitales avec Matomo
    # "SXLAJL": "",  # Integrating Matomo in a data stack
    # "R393MD": "",  # Matomo: External Dashboards & Data Visualization
    # "SNEUXP": "",  # Migration de vos datas Google Analytics UA vers Matomo
    # "QCGUJB": "",  # Linux security hardening on a Matomo installation
    # "ADJLAW": "",  # Open source dashboards ontop of Matomo with Apache Superset
    # "PYT37H": "",  # Matomo et WordPress comment les connecter ?
    # "QB8VY8": "",  # Running Matomo with open source technologies such as Kubernetes and docker
    # "XGPBTU": "",  # Why Wholesale Distributors in the US should be using Matomo
    # "XMGR83": "",  # Les traductions dans Matomo, comment ça marche?
    # "UKTQD8": "",
    # # Server installation, typical implementation, and Italian GDPR compliance with Matomo (Italian language)
    # "EDHADW": "",  # Tag Manager/Consent solutions
    # "CQ3TRP": "",  # Matomo & Vanilla Analytics
    # "U9GDMC": "",  # Building Matomo plugins with VueJS.
    # "TPFDWN": "",  # Get a kick ass dashboard in Matomo
    "SRDLAJ": "das-problem-zu-viel",  # Das Problem "zu viel" - Mehr Insights in Matomo
    # "KDWXFH": "",  # Get started with intranet analytics in Matomo
    "XRVPDS": "das-problem-zu-wenig",  # Das Problem "zu wenig" - Mehr Insights in Matomo
    # "ZXGJYA": "",  # Improve your SEO with Matomo
    # "7YDHL7": "",  # Tracking SPA applications with Matomo
    # "97RZGZ": "",  # Standortermittlung mit Matomo
    # "FXLH93": "",  # Data Creation and Snowplow Open Source
    # "FUD7JR": "",  # How to use Matomo Log Analysis to retrieve audience data
    # "BRH8SH": "",  # Datenschutzkonformes Performance Marketing mit Matomo
    # "N3WJCA": "",  # How to create a plugin for Matomo when you are not a developer?
    # "YE9MYB": "",  # Plausible Analytics: Simple, lightweight, open source and privacy-first analytics
    # "389UYH": "",  # Utilisez Matomo avec Joomla
    "E893JM": "web-analytics-book",  # The big book about web analytics
    # "WXXXXE": "",  # The ultimate guide to migrate to Matomo: 7 best practices
    "ST38HK": "closing-event-2022",  # MatomoCamp closing
}

archive_names = {
    "3TTRKG": "trackingSPA",
    "7AJEKD": "Background Tracking",
    "8HSWJD": "Q&A",
    "9JHC8H": "Closing",
    "DM8S7W": "SAAS",
    "ENHZCR": "GDPR Masses",
    "FDEE9Z": "Wrapped",
    "G8K8AV": "incidences côté infra",
    "G98E3P": "User Feedback",
    "GDGZXF": "Opening",
    "GF7XD9": "Tag Manager Basics",
    "GMUXZZ": "Conversion rate",
    "GR9YQZ": "Matomo Kompakt",
    "HU8NSN": "DPO",
    # "KDBDPX": "translating-matomo",
    "LKVJQ8": "Public Sector",
    "LZ8NYG": "Stay Compliant",
    "M9XPRG": "Cleaninsights",
    "MKKVHX": "Business",
    "N3U3BT": "Metabase",
    "PBWV7L": "SEO",
    "PX7EHX": "configurer RGPD",
    "QRSQ8D": "Break Matomo",
    "URWXGR": "Million Pageviews",
    "WGWW8R": "Surveillance Societies",
    # "XAAHDQ": "open-source-data-visualization",
    "XTF7GX": "Tips and Tricks",
    "Y9AAMG": "Host your own Instance",
    # "ZBWZHJ": "cleaninsights-workshop",
    "QQJ3ZS": "PII"

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
