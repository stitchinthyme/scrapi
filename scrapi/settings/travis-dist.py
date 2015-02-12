DEBUG = False

BROKER_URL = 'amqp://guest@localhost'

STORAGE_METHOD = 'disk'
ARCHIVE_DIRECTORY = 'archive/'
RECORD_DIRECTORY = 'records'

CELERY_EAGER_PROPAGATES_EXCEPTIONS = True

STORE_HTTP_TRANSACTIONS = False

NORMALIZED_PROCESSING = ['storage', 'elasticsearch']
RAW_PROCESSING = ['storage', 'elasticsearch']

SENTRY_DNS = None

USE_FLUENTD = False
FLUENTD_ARGS = ('scrapi',)

# OUTPUT SETTINGS
OSF_ENABLED = False

VERIFY_SSL = True
OSF_PREFIX = 'http://localhost:5000'

APP_ID = 'some id'

API_KEY_LABEL = 'some label'
API_KEY = 'some api key'

ELASTIC_URI = 'localhost:9200'
ELASTIC_TIMEOUT = 10
ELASTIC_INDEX = 'share'

FRONTEND_KEYS = [
    u'description',
    u'contributors',
    u'tags',
    u'raw',
    u'title',
    u'id',
    u'source',
    u'dateUpdated'
]