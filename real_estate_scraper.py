import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView

def render(source_url):
    """Fully render HTML, JavaScript and all."""
    class Render(QWebEngineView):
        def __init__(self, url):
            self.html = None
            self.app = QApplication(sys.argv)
            QWebEngineView.__init__(self)
            self.loadFinished.connect(self._loadFinished)
            self.load(QUrl(url))
            self.app.exec_()

        def _loadFinished(self, result):
            # This is an async call, you need to wait for this
            # to be called before closing the app
            self.page().toHtml(self._callable)

        def _callable(self, data):
            self.html = data
            # Data has been stored, it's safe to quit the app
            self.app.quit()

    return Render(source_url).html

url = "https://www.point2homes.com/CA/Real-Estate-Listings/MB/Winnipeg.html?location=Winnipeg%2C+MB&search_mode=location&PropertyType=Homes&page=1"
print(render(url))