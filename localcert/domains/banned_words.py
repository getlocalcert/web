# A list of the ~1000 most popular websites
# I split out the labels so TLDs, domain names, and subdomains are present
# These are banned to prevent lookalike domains
banned_words = set(
    [
        "0byv9mgbn0",
        "11st",
        "1337x",
        "17ok",
        "17track",
        "2movierulz",
        "360doc",
        "3c",
        "3dmgame",
        "4chan",
        "4pda",
        "51cto",
        "51sole",
        "52pojie",
        "5ch",
        "65vk1fba34",
        "91jm",
        "9gag",
        "aa",
        "abola",
        "abs-cbn",
        "ac",
        "academia",
        "accuweather",
        "adaranth",
        "adobe",
        "adp",
        "afreecatv",
        "agoda",
        "airbnb",
        "akoam",
        "aksam",
        "albawabhnews",
        "alibaba",
        "alicdn",
        "aliexpress",
        "alipay",
        "aliyun",
        "allegro",
        "allocine",
        "alnigeringcer",
        "alodokter",
        "alwafd",
        "amazon",
        "amazonaws",
        "ameblo",
        "americanas",
        "americanexpress",
        "andhrajyothy",
        "animeflv",
        "anjuke",
        "ao",
        "aol",
        "aparat",
        "apkpure",
        "apple",
        "appledaily",
        "ar",
        "archive",
        "archiveofourown",
        "arpa",
        "artstation",
        "arxiv",
        "as",
        "asahi",
        "asana",
        "ask",
        "asos",
        "asus",
        "at",
        "atlassian",
        "att",
        "au",
        "auction",
        "audible",
        "autodesk",
        "avgle",
        "avito",
        "axisbank",
        "az",
        "azure",
        "b3z29k1uxb",
        "ba",
        "babytree",
        "baidu",
        "baike",
        "bancodevenezuela",
        "bandcamp",
        "banesconline",
        "banggood",
        "bankmellat",
        "bankofamerica",
        "basecamp",
        "battle",
        "bbc",
        "be",
        "beeg",
        "behance",
        "bellesa",
        "best2019-games-web1",
        "bestbuy",
        "bet365",
        "bet9ja",
        "beytoote",
        "bhphotovideo",
        "biblegateway",
        "bicentenariobu",
        "bild",
        "bilibili",
        "billdesk",
        "binance",
        "bing",
        "biobiochile",
        "bitbucket",
        "bitly",
        "biz",
        "blackboard",
        "bleacherreport",
        "blibli",
        "blizzard",
        "blog",
        "blogger",
        "blogspot",
        "bloomberg",
        "bnsjb1ab1e",
        "bol",
        "bolasport",
        "bongacams",
        "booking",
        "bookmyshow",
        "box",
        "bp",
        "br",
        "breitbart",
        "brilio",
        "bukalapak",
        "businessinsider",
        "butheptesitrew",
        "buzzfeed",
        "bzw315",
        "ca",
        "caijing",
        "caixa",
        "caliente",
        "cam4",
        "cambridge",
        "canada",
        "canalrcn",
        "canva",
        "capitalone",
        "cbbp1",
        "cbsnews",
        "cbssports",
        "cc",
        "ccleaner",
        "ccm",
        "cctv",
        "cdiscount",
        "cdninstagram",
        "cdstm",
        "ch",
        "chase",
        "chaturbate",
        "chatwork",
        "chegg",
        "chess",
        "china",
        "chinaz",
        "chip",
        "chiphell",
        "chouftv",
        "chron",
        "cima4u",
        "cimaclub",
        "cinecalidad",
        "cisco",
        "citi",
        "cjl58f3agc",
        "cl",
        "clarin",
        "cloudflare",
        "cloudfront",
        "cn",
        "cnbc",
        "cnbeta",
        "cnblogs",
        "cnet",
        "cnn",
        "cnnindonesia",
        "cnzz",
        "co",
        "codecanyon",
        "codepen",
        "coinbase",
        "coinmarketcap",
        "com",
        "concursolutions",
        "constantcontact",
        "corriere",
        "costco",
        "coupang",
        "coursera",
        "craigslist",
        "creditkarma",
        "creditonebank",
        "cricbuzz",
        "crptgate",
        "crunchbase",
        "crunchyroll",
        "cryptobrowser",
        "csdn",
        "ctfile",
        "ctrip",
        "curseforge",
        "cz",
        "dafont",
        "dailymail",
        "dailymotion",
        "dailypost",
        "daum",
        "dawmal",
        "dawn",
        "dcard",
        "dcinside",
        "de",
        "dell",
        "deloplen",
        "delta",
        "depositphotos",
        "detail",
        "detik",
        "deviantart",
        "dhl",
        "dianping",
        "dictionary",
        "digikala",
        "discogs",
        "discordapp",
        "discover",
        "discuss",
        "divar",
        "dkn",
        "dmm",
        "doc88",
        "docusign",
        "donga",
        "doorblog",
        "douban",
        "doubleclick",
        "douyu",
        "downdetector",
        "dribbble",
        "drive2",
        "drom",
        "dropbox",
        "drudgereport",
        "dspmulti",
        "duba",
        "duckduckgo",
        "duolingo",
        "dw",
        "dytt8",
        "dz",
        "ea",
        "eastday",
        "ebay",
        "ebay-kleinanzeigen",
        "ebc",
        "ecleneue",
        "ecosia",
        "edu",
        "eg",
        "e-hentai",
        "eksisozluk",
        "elbalad",
        "elmogaz",
        "elmundo",
        "elpais",
        "elsevier",
        "elwatannews",
        "emol",
        "engadget",
        "ensonhaber",
        "envato",
        "epfindia",
        "epicgames",
        "err",
        "es",
        "eshkol",
        "espn",
        "espncricinfo",
        "etsy",
        "ettoday",
        "eu",
        "europa",
        "eventbrite",
        "evernote",
        "exhentai",
        "exoclick",
        "expedia",
        "express",
        "expressvpn",
        "eyny",
        "facebook",
        "fandom",
        "fanfiction",
        "farfetch",
        "fast",
        "fazenda",
        "fbsbx",
        "fc2",
        "fedex",
        "feedly",
        "feng",
        "fidelity",
        "filehippo",
        "files",
        "fiverr",
        "flaticon",
        "flickr",
        "flipkart",
        "flvto",
        "fmovies",
        "food",
        "forbes",
        "force",
        "foxnews",
        "fr",
        "free",
        "freejobalert",
        "freepik",
        "friv",
        "fullhdfilmizlesene",
        "gamepedia",
        "gamer",
        "gamersky",
        "gamespot",
        "gamib",
        "gazeta",
        "gearbest",
        "geeksforgeeks",
        "genius",
        "getawesome2",
        "getbootstrap",
        "getpocket",
        "gfycat",
        "gg",
        "giphy",
        "gismeteo",
        "github",
        "gitlab",
        "gizmodo",
        "glassdoor",
        "globo",
        "gloyah",
        "gmanetwork",
        "gmarket",
        "gmw",
        "gmx",
        "go",
        "goal",
        "godaddy",
        "gogoanime",
        "gome",
        "goo",
        "goodreads",
        "google",
        "googlevideo",
        "gosuslugi",
        "gov",
        "gr",
        "grammarly",
        "grid",
        "groupon",
        "gsmarena",
        "gstatic",
        "gtarcade",
        "gyazo",
        "hamariweb",
        "hao123",
        "harvard",
        "hatena",
        "hatenablog",
        "hdfcbank",
        "healthline",
        "heavy",
        "hepsiburada",
        "heroesofrpg",
        "hesport",
        "hespress",
        "hh",
        "hk",
        "hm",
        "homedepot",
        "hootsuite",
        "hotels",
        "hotnewhiphop",
        "hotstar",
        "howtogeek",
        "hp",
        "huanqiu",
        "huawei",
        "hubspot",
        "huffpost",
        "hulu",
        "hupu",
        "hurriyet",
        "huya",
        "ibm",
        "ibps",
        "icicibank",
        "icloud",
        "id",
        "idntimes",
        "ieee",
        "ifeng",
        "ign",
        "ikea",
        "ilovepdf",
        "im",
        "imdb",
        "imgur",
        "impress",
        "in",
        "incometaxindiaefiling",
        "indeed",
        "independent",
        "indiamart",
        "indiatimes",
        "indiatoday",
        "indosport",
        "indoxxi",
        "info",
        "infobae",
        "inquirer",
        "instagram",
        "instructure",
        "int",
        "intel",
        "intentmedia",
        "interia",
        "internetdownloadmanager",
        "intoday",
        "intuit",
        "inven",
        "investing",
        "investopedia",
        "io",
        "iqiyi",
        "iqoption",
        "ir",
        "irctc",
        "issuu",
        "istockphoto",
        "it",
        "ithome",
        "itmedia",
        "ivi",
        "japanpost",
        "jb51",
        "jd",
        "jf71qh5v14",
        "jiameng",
        "jianshu",
        "jma",
        "joins",
        "jooble",
        "jp",
        "jrj",
        "jugantor",
        "jumia",
        "justdial",
        "jw",
        "kakaku",
        "kakao",
        "kapanlagi",
        "kaskus",
        "kayak",
        "kerumal",
        "khanacademy",
        "kickstarter",
        "kijiji",
        "kinopoisk",
        "kissanime",
        "kizlarsoruyor",
        "kknews",
        "klix",
        "kompas",
        "kompasiana",
        "kooora",
        "kotaku",
        "kp",
        "kr",
        "kumparan",
        "kz",
        "l6b587txj1",
        "labanquepostale",
        "ladbible",
        "lazada",
        "leagueoflegends",
        "leboncoin",
        "lefigaro",
        "legit",
        "lemonde",
        "lenovo",
        "lenta",
        "libero",
        "lifewire",
        "lifo",
        "line",
        "linkedin",
        "liputan6",
        "list",
        "list-manage",
        "live",
        "livedoor",
        "livejasmin",
        "livejournal",
        "livescore",
        "login",
        "lordsfilm",
        "lowes",
        "lt",
        "ltn",
        "lun",
        "ma",
        "macys",
        "mail",
        "mailchimp",
        "makeuseof",
        "mama",
        "manoramaonline",
        "marca",
        "marketwatch",
        "marriott",
        "mathrubhumi",
        "mawdoo3",
        "mayoclinic",
        "me",
        "media",
        "mediafire",
        "medium",
        "meetup",
        "mega",
        "memurlar",
        "mercadolibre",
        "mercadolivre",
        "mercari",
        "merdeka",
        "merriam-webster",
        "messenger",
        "metropoles",
        "mg",
        "mgid",
        "mi",
        "microsoft",
        "microsoftonline",
        "mil",
        "mileroticos",
        "milliyet",
        "minecraft",
        "mit",
        "mlb",
        "mobile",
        "momoshop",
        "moneycontrol",
        "moocauby",
        "motor1",
        "motorsport",
        "mozilla",
        "mptentry",
        "msn",
        "mx",
        "myanimelist",
        "myanmarload",
        "myfreecams",
        "mynet",
        "myntra",
        "myornamenti",
        "myshopify",
        "myway",
        "myworkday",
        "n11",
        "namasha",
        "namnak",
        "namu",
        "narcity",
        "nate",
        "nature",
        "naukri",
        "naver",
        "nba",
        "nbcnews",
        "ndtv",
        "ne",
        "neobux",
        "net",
        "netflix",
        "newegg",
        "news",
        "news18",
        "nexon",
        "nextdoor",
        "nexusmods",
        "ng",
        "nga",
        "nhentai",
        "nhk",
        "nianhuo",
        "nicovideo",
        "nih",
        "nike",
        "nikkei",
        "ninisite",
        "nl",
        "norton",
        "notifications",
        "nownews",
        "npr",
        "ntdtv",
        "ntralpenedhy",
        "nur",
        "nvidia",
        "nvzhuang",
        "nyaa",
        "nypost",
        "nytimes",
        "nz",
        "office",
        "office365",
        "ok",
        "okezone",
        "okta",
        "olx",
        "onet",
        "onlinesbi",
        "onlinevideoconverter",
        "op",
        "openload",
        "or",
        "oracle",
        "orange",
        "org",
        "oschina",
        "otvfoco",
        "ouedkniss",
        "ouo",
        "outbrain",
        "ozon",
        "pages",
        "panda",
        "pandora",
        "pantip",
        "patch",
        "patreon",
        "patria",
        "paypal",
        "paytm",
        "payu",
        "pcgamer",
        "pchome",
        "pe",
        "pelisplus",
        "pexels",
        "phengung",
        "pikabu",
        "pinimg",
        "pinterest",
        "pixabay",
        "pixiv",
        "pixnet",
        "pk",
        "pl",
        "playstation",
        "pngtree",
        "pole-emploi",
        "politico",
        "polygon",
        "popads",
        "popcash",
        "poste",
        "primevideo",
        "prnt",
        "pro",
        "prom",
        "propdfconverter",
        "prothomalo",
        "provincial",
        "pt",
        "ptt",
        "pulzo",
        "punchng",
        "python",
        "qj",
        "qq",
        "qualtrics",
        "quintag",
        "quizlet",
        "quora",
        "rakuten",
        "rambler",
        "rapidgator",
        "rarbg",
        "rarbgprx",
        "rbc",
        "reallifecam",
        "realtor",
        "reclameaqui",
        "redd",
        "reddit",
        "redfin",
        "rediff",
        "rednet",
        "redtube",
        "repubblica",
        "researchgate",
        "reuters",
        "reverso",
        "ria",
        "ro",
        "roblox",
        "rottentomatoes",
        "royalbank",
        "rt",
        "ru",
        "ruliweb",
        "runoob",
        "ruten",
        "rutor",
        "rutracker",
        "sa",
        "sahibinden",
        "sakshi",
        "salesforce",
        "samsung",
        "sarkariresult",
        "savefrom",
        "sberbank",
        "sc",
        "sciencedirect",
        "sci-hub",
        "scol",
        "scribd",
        "sdpnoticias",
        "searchdimension",
        "seasonvar",
        "secureserver",
        "segmentfault",
        "semanticscholar",
        "service-now",
        "setare",
        "setn",
        "seznam",
        "sg",
        "shaparak",
        "shein",
        "shimo",
        "shopee",
        "shopify",
        "show",
        "shutterstock",
        "si",
        "sina",
        "sindonews",
        "site",
        "siteadvisor",
        "sk",
        "skype",
        "slack",
        "slickdeals",
        "slideshare",
        "smallpdf",
        "smzdm",
        "so",
        "socialblade",
        "softonic",
        "sogou",
        "sohu",
        "sonyliv",
        "soso",
        "soundcloud",
        "souq",
        "sourceforge",
        "southwest",
        "sozcu",
        "spankbang",
        "spectrum",
        "speedtest",
        "spiegel",
        "spotify",
        "springer",
        "sputniknews",
        "square-enix",
        "squarespace",
        "stackexchange",
        "stackoverflow",
        "state",
        "steamcommunity",
        "steampowered",
        "storiespace",
        "storm",
        "strava",
        "stremanp",
        "studio",
        "suara",
        "subito",
        "subject",
        "subscene",
        "superuser",
        "surveymonkey",
        "susm0q6jys",
        "sxyprn",
        "t",
        "t66y",
        "tabelog",
        "taboola",
        "taleo",
        "tandfonline",
        "taobao",
        "target",
        "td",
        "teamviewer",
        "tebyan",
        "techradar",
        "techtudo",
        "telegram",
        "telegraph",
        "telewebion",
        "tencent",
        "tenki",
        "th",
        "theepochtimes",
        "thefreedictionary",
        "theguardian",
        "thehindu",
        "themeforest",
        "thepiratebay",
        "thesaurus",
        "thestartmagazine",
        "thesun",
        "theverge",
        "thewhizmarketing",
        "thingiverse",
        "tianya",
        "timeanddate",
        "tistory",
        "tmall",
        "to",
        "tokopedia",
        "t-online",
        "toutiao",
        "tr",
        "tradingview",
        "trello",
        "trendingnow",
        "tribunnews",
        "tripadvisor",
        "trustpilot",
        "tsinghua",
        "tumblr",
        "turkiye",
        "tutorialspoint",
        "tv",
        "tw",
        "twimg",
        "twitch",
        "twitter",
        "ua",
        "uber",
        "udemy",
        "udn",
        "uidai",
        "uk",
        "ukr",
        "ultimate-guitar",
        "uniqlo",
        "unsplash",
        "uol",
        "ups",
        "uptobox",
        "uptodown",
        "upwork",
        "urbandictionary",
        "urdupoint",
        "us",
        "usaa",
        "usatoday",
        "usbank",
        "userapi",
        "usps",
        "utorrent",
        "uzone",
        "v2ex",
        "varzesh3",
        "ve",
        "verizonwireless",
        "verystream",
        "vice",
        "video",
        "vidio",
        "vimeo",
        "visualstudio",
        "viva",
        "vk",
        "vn",
        "vnexpress",
        "vtv",
        "w3schools",
        "walmart",
        "washingtonpost",
        "wattpad",
        "wayfair",
        "weather",
        "web",
        "webex",
        "weblio",
        "webmd",
        "website",
        "weebly",
        "weibo",
        "wellsfargo",
        "westernjournal",
        "wetransfer",
        "whatsapp",
        "wiki",
        "wikihow",
        "wikimedia",
        "wikipedia",
        "wiktionary",
        "wildberries",
        "wiley",
        "wish",
        "wix",
        "wixsite",
        "wondershare",
        "wordpress",
        "wordreference",
        "wowhead",
        "wp",
        "wsj",
        "wunderground",
        "www",
        "wysasys",
        "xbombo",
        "xda-developers",
        "xe",
        "xfinity",
        "xhamster",
        "xinhuanet",
        "y2mate",
        "yadi",
        "yahoo",
        "yallakora",
        "yandex",
        "yao",
        "yaplakal",
        "yelp",
        "youdao",
        "youjizz",
        "youku",
        "youm7",
        "youth",
        "youtube",
        "yr9n47004g",
        "ytimg",
        "ytmp3",
        "yts",
        "yy",
        "za",
        "zara",
        "zendesk",
        "zhanqi",
        "zhaopin",
        "zhiding",
        "zhihu",
        "zillow",
        "zippyshare",
        "zoho",
        "zol",
        "zoom",
    ]
)
