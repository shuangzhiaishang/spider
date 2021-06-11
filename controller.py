from model import Model

class Controller():
    def __init__(self, view, db):
        self._view = view
        self._model = Model(self._view, db)
        self._connectSignals()
        
    def _connectSignals(self):
        self._view.pushButtonBegin.clicked.connect(self._model.begin)
        self._view.pushButtonClear.clicked.connect(self._model.clear)
        self._view.pushButtonQuit.clicked.connect(quit)
        self._view.pushButtonSave.clicked.connect(self._model.save)