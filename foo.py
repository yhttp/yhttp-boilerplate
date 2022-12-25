from yhttp import Application


__version__ = '0.1.0'


app = Application()


# Add builtin settings here
app.settings.merge('''
''')


# http handlers
import handlers
