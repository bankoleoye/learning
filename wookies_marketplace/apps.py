from django.apps import AppConfig


class WookiesMarketplaceConfig(AppConfig):
    name = 'wookies_marketplace'
    
    def ready(self):
        print("import signals")
        try:
            print("importing signals")
            import wookies_marketplace.signals  # noqa F401
        except ImportError:
            print("problem importing signals")
            pass
