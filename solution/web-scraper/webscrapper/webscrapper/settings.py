# Scrapy settings for scrapy_files project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "webscrapper"

SPIDER_MODULES = ["webscrapper.spiders"]
NEWSPIDER_MODULE = "webscrapper.spiders"

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = "scrapy_files (+http://www.yourdomain.com)"
# USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html


DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'scrapy.downloadermiddlewares.retry.RetryMiddleware': None,
    'scrapy_fake_useragent.middleware.RandomUserAgentMiddleware': 400,
    'scrapy_fake_useragent.middleware.RetryUserAgentMiddleware': 401,
#    'rotating_proxies.middlewares.RotatingProxyMiddleware': 610,
#    'rotating_proxies.middlewares.BanDetectionMiddleware': 620,
}
FAKEUSERAGENT_PROVIDERS = [
    'scrapy_fake_useragent.providers.FakeUserAgentProvider',  # this is the first provider we'll try
    'scrapy_fake_useragent.providers.FakerProvider',
    # if FakeUserAgentProvider fails, we'll use faker to generate a user-agent string for us
    'scrapy_fake_useragent.providers.FixedUserAgentProvider',  # fall back to USER_AGENT value
]
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0;'
# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3
RANDOMIZE_DOWNLOAD_DELAY = True
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en",
    "Accept-Encoding": "gzip, deflate, br",
    "Referer": "https://www.google.pl/?hl=pl"
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    "scrapy_files.middlewares.ScrapyFilesSpiderMiddleware": 543,
# }


# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'scrapy_files.pipelines.JsonSavePipeline': 300,
 }

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
AUTOTHROTTLE_ENABLED = True
# The initial download delay
AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = "httpcache"
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
#FEED_FORMAT = "json"
#FEED_URI = "output.json"

ROTATING_PROXY_LIST = [
    '34.23.45.223:80',
    '20.6.0.172:80',
    '72.10.160.170:5385',
    '114.156.77.107:8080',
    '139.162.78.109:3128',
    '8.219.97.248:80',
    '47.88.3.19:8080',
    '20.219.182.59:3129',
    '133.242.229.79:33333',
    '20.204.212.45:3129',
    '146.59.202.70:80',
    '138.91.159.185:80',
    '20.205.61.143:80',
    '195.181.172.211:8081',
    '185.217.143.96:80',
    '89.185.29.2:80',
    '45.140.189.95:29003',
    '159.65.77.168:8585',
    '45.87.68.7:15321',
    '20.204.212.76:3129',
    '79.137.199.255:8888',
    '159.138.255.141:8080',
    '142.93.72.28:10006',
    '47.243.177.210:8088',
    '8.212.23.2:80',
    '20.219.177.85:3129',
    '162.223.94.164:80',
    '49.228.131.169:5000',
    '103.235.153.81:8080',
    '13.244.87.238:4145',
    '20.219.183.188:3129',
    '142.171.194.101:80',
    '181.49.243.14:44443',
    '198.49.68.80:80',
    '50.171.32.225:80',
    '50.228.141.97:80',
    '50.173.140.145:80',
    '50.204.219.225:80',
    '50.235.240.86:80',
    '50.169.23.170:80',
    '50.207.199.86:80',
    '50.202.75.26:80',
    '50.231.172.74:80',
    '107.1.93.217:80',
    '50.217.226.46:80',
    '50.168.210.232:80',
    '162.248.225.230:80',
    '50.173.140.138:80',
    '50.169.135.10:80',
    '50.204.219.226:80',
    '50.172.75.122:80',
    '50.218.57.70:80',
    '50.223.38.6:80',
    '50.174.145.14:80',
    '50.204.190.234:80',
    '50.218.57.74:80',
    '50.217.226.40:80',
    '50.170.90.30:80',
    '50.204.219.228:80',
    '50.169.37.50:80',
    '50.222.245.42:80',
    '50.217.226.41:80',
    '50.218.57.67:80',
    '50.174.7.158:80',
    '50.168.210.234:80',
    '50.168.72.113:80',
    '50.207.199.83:80',
    '50.230.222.202:80',
    '96.113.158.126:80',
    '50.171.32.224:80',
    '50.228.141.101:80',
    '24.205.201.186:80',
    '50.174.145.12:80',
    '50.168.72.117:80',
    '50.174.145.11:80',
    '50.217.226.44:80',
    '107.1.93.222:80',
    '50.204.219.224:80',
    '107.1.93.208:80',
    '107.1.93.223:80',
    '50.170.90.34:80',
    '50.173.140.147:80',
    '50.217.226.42:80',
    '50.222.245.44:80',
    '50.168.163.179:80',
    '50.218.57.66:80',
    '50.168.210.238:80',
    '50.168.163.180:80',
    '50.204.219.227:80',
    '50.228.141.99:80',
    '50.218.57.64:80',
    '50.168.72.116:80',
    '107.1.93.220:80',
    '50.172.75.124:80',
    '32.223.6.94:80',
    '107.1.93.212:80',
    '50.170.90.31:80',
    '50.200.12.82:80',
    '50.228.141.98:80',
    '50.174.145.10:80',
    '78.38.8.35:8080',
    '175.106.11.172:8080',
    '157.230.248.158:3128',
    '181.174.115.9:1994',
    '200.60.4.238:999',
    '20.204.214.79:3129',
    '85.95.167.124:11110',
    '104.236.195.60:10002',
    '50.168.72.112:80',
    '50.173.140.150:80',
    '50.231.104.58:80',
    '50.200.12.80:80',
    '50.207.199.87:80',
    '107.1.93.209:80',
    '172.108.208.74:80',
    '159.203.61.169:8080',
    '162.223.89.84:80',
    '50.174.145.9:80',
    '50.171.32.229:80',
    '50.237.207.186:80',
    '107.1.93.218:80',
    '50.171.32.230:80',
    '50.200.12.87:80',
    '50.207.199.81:80',
    '50.168.72.119:80',
    '50.200.12.84:80',
    '50.168.163.166:80',
    '80.150.50.226:80',
    '50.173.140.149:80',
    '50.222.245.50:80',
    '50.168.163.182:80',
    '50.221.74.130:80',
    '50.239.72.16:80',
    '50.168.72.122:80',
    '50.168.72.114:80',
    '189.202.188.149:80',
    '50.168.210.235:80',
    '50.168.163.183:80',
    '50.207.199.85:80',
    '50.172.75.123:80',
    '50.171.32.222:80',
    '50.174.145.15:80',
    '50.172.23.10:80',
    '50.206.111.91:80',
    '107.1.93.219:80',
    '50.175.212.74:80',
    '50.218.57.71:80',
    '50.168.163.177:80',
    '50.168.210.236:80',
    '107.1.93.215:80',
    '50.168.72.115:80',
    '50.228.141.96:80',
    '50.228.141.102:80',
    '50.172.75.126:80',
    '50.207.199.84:80',
    '50.168.210.226:80',
    '46.149.77.234:80',
    '50.221.230.186:80',
    '50.223.38.2:80',
    '50.217.226.45:80',
    '50.174.7.159:80',
    '85.8.68.2:80',
    '50.174.7.152:80',
    '50.171.152.30:80',
    '50.222.245.46:80',
    '50.122.86.118:80',
    '107.1.93.211:80',
    '50.168.163.178:80',
    '50.174.7.153:80',
    '162.248.224.103:80',
    '139.59.1.14:8080',
    '107.1.93.216:80',
    '213.33.2.28:80',
    '50.239.72.17:80',
    '50.174.7.156:80',
    '50.217.29.198:80',
    '80.120.130.231:80',
    '50.168.163.181:80',
    '50.170.90.28:80',
    '80.228.235.6:80',
    '213.33.126.130:80',
    '50.171.32.227:80',
    '50.239.72.19:80',
    '103.127.1.130:80',
    '127.0.0.7:80',
    '50.207.199.80:80',
    '50.171.32.226:80',
    '50.174.7.157:80',
    '50.171.32.228:80',
    '50.218.57.65:80',
    '20.198.96.26:80',
    '47.254.88.205:2011',
    '181.65.180.188:999',
    '122.3.176.110:8080',
    '24.192.227.234:8080',
    '47.88.29.108:3001',
    '189.240.60.169:9090',
    '130.162.224.168:1080',
    '67.43.228.250:18003',
    '20.219.178.121:3129',
    '67.43.227.226:25639',
    '67.43.227.228:9039',
    '178.128.113.118:23128',
    '50.206.111.89:80',
    '50.174.41.66:80',
    '41.77.188.131:80',
    '178.73.192.17:3128',
    '50.174.7.162:80',
    '50.239.72.18:80',
    '20.24.43.214:80',
    '50.218.57.68:80',
    '62.99.138.162:80',
    '93.20.25.100:80',
    '0.0.0.0:80',
    '50.228.141.103:80',
    '20.111.54.16:8123',
    '50.174.7.155:80',
    '85.26.146.169:80',
    '20.219.177.38:3129',
    '134.209.29.120:8080',
    '20.219.177.73:3129',
    '50.168.163.176:80',
    '190.58.248.86:80',
    '20.210.113.32:80',
    '20.206.106.192:80',
    '50.220.168.134:80',
    '20.219.235.172:3129',
    '213.143.113.82:80',
    '190.97.236.40:2023',
    '128.199.244.96:1234',
    '186.96.95.205:999',
    '139.144.71.214:80',
    '197.243.20.186:80',
    '154.65.39.7:80',
    '190.103.177.131:80',
    '162.223.116.54:80',
    '67.43.228.253:14869',
    '72.10.160.171:5369',
    '165.227.120.250:10006',
    '20.204.214.23:3129',
    '68.188.59.198:80',
    '50.173.140.146:80',
    '50.231.110.26:80',
    '50.170.90.24:80',
    '50.173.140.148:80',
    '50.228.83.226:80',
    '50.174.7.154:80',
    '50.222.245.41:80',
    '50.206.111.88:80',
    '68.185.57.66:80',
    '50.174.145.8:80',
    '50.200.12.86:80',
    '50.222.245.45:80',
    '50.171.68.130:80',
    '50.221.166.2:80',
    '104.148.86.252:3129',
    '134.19.254.2:21231',
    '213.170.117.150:8080',
    '64.225.8.132:10000',
    '12.186.205.121:80',
    '107.1.93.213:80',
    '50.170.90.27:80',
    '50.173.140.144:80',
    '50.170.90.26:80',
    '216.137.184.253:80',
    '50.204.219.231:80',
    '50.171.32.231:80',
    '123.30.154.171:7777',
    '50.217.226.43:80',
    '58.234.116.197:80',
    '41.230.216.70:80',
    '107.1.93.210:80',
    '96.113.159.162:80',
    '41.207.187.178:80',
    '107.1.93.214:80',
    '50.204.219.229:80',
    '107.1.93.221:80',
    '50.174.145.13:80',
    '20.169.221.14:3128',
    '190.97.252.18:999',
    '51.255.208.33:1991',
    '108.177.248.79:8118',
    '172.241.137.152:8118',
    '43.130.35.101:10684',
    '172.241.137.83:8118',
    '23.105.86.110:8118',
    '23.81.127.36:8118',
    '23.108.42.115:8118',
    '172.241.137.110:8118',
    '172.241.137.157:8118',
    '23.81.127.78:8118',
    '23.108.42.80:8118',
    '23.81.127.180:8118',
    '23.108.64.117:8118',
    '23.105.78.202:8118',
    '23.108.78.165:8118',
    '23.81.127.199:8118',
    '108.177.248.46:8118',
    '23.108.42.168:8118',
    '23.105.86.40:8118',
]
