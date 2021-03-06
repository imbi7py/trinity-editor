from PyQt5.QtWidgets import QSplitter, QFrame, QVBoxLayout, QPlainTextEdit, QLabel
from PyQt5.QtCore import *
from PyQt5.QtGui import QFont, QColor, QFontMetrics
from PyQt5.Qsci import QsciScintilla, QsciLexerHTML

def ui_add_splitter_and_textedit(self):
	""""Set splitter, andthen create textEdits. Finally, append textEdits to the splitter."""
	# make a splitter
	splitter = QSplitter(Qt.Horizontal,self.centralwidget)	
	
	#set the default dont for the textEdits
	default_font = QFont()
	default_font_family = "Mono" #"Mono"
	default_font_size = 10
	default_font.setFamily(default_font_family)
	default_font.setPointSize(default_font_size)

	#set html column
	self.html_verticalFrame = QFrame()
	self.html_verticalFrame.setObjectName("html_verticalFrame")
	self.html_verticalLayout = QVBoxLayout(self.html_verticalFrame)
	self.html_verticalLayout.setContentsMargins(8, 9, 9, 3)
	self.html_verticalLayout.setObjectName("css_verticalLayout")
	self.label_html = QLabel(self.html_verticalFrame)
	self.label_html.setObjectName("label_html")
	self.html_verticalLayout.addWidget(self.label_html)

	self.html_textedit = QsciScintilla(self.html_verticalFrame)
	self.html_textedit.setFont(default_font)

	html_lexer = QsciLexerHTML()
	html_lexer.setDefaultFont(default_font)
	html_lexer.setFont(default_font, QsciLexerHTML.Default)
	html_lexer.setFont(default_font, QsciLexerHTML.HTMLComment)
	self.html_textedit.setLexer(html_lexer)
	# WrapCharacter Lines are wrapped at character boundaries = 2
	# See: http://pyqt.sourceforge.net/Docs/QScintilla2/classQsciScintilla.html#a7081c7ff25b5f6bd5b3a6cbd478a9f42
	self.html_textedit.setWrapMode(2)

	self.html_textedit.setMarginsFont(default_font)
	fontmetrics = QFontMetrics(default_font)
	self.html_textedit.setMarginWidth(0, fontmetrics.width("000") + 2)

	# NumberMargin The margin contains line numbers = 3 
	# See: http://pyqt.sourceforge.net/Docs/QScintilla2/classQsciScintilla.html#aedab060e87e0533083ea8f1398302090
	self.html_textedit.setMarginLineNumbers(0, True)

	self.html_textedit.setCaretLineVisible(True)
	self.html_textedit.setCaretLineBackgroundColor(QColor("#FAEF8E"))




	self.html_textedit.setObjectName("html_textedit")
	self.html_verticalLayout.addWidget(self.html_textedit)

	#set css column
	self.css_verticalFrame = QFrame()
	self.css_verticalFrame.setObjectName("css_verticalFrame")
	self.css_verticalLayout = QVBoxLayout(self.css_verticalFrame)
	self.css_verticalLayout.setContentsMargins(8, 9, 9, 3)
	self.css_verticalLayout.setObjectName("css_verticalLayout")
	self.label_css = QLabel(self.css_verticalFrame)
	self.label_css.setObjectName("label_css")
	self.css_verticalLayout.addWidget(self.label_css)
	self.css_textedit = QPlainTextEdit(self.css_verticalFrame)
	self.css_textedit.setObjectName("css_textedit")
	self.css_verticalLayout.addWidget(self.css_textedit)

	#set js column
	self.js_verticalFrame = QFrame()
	self.js_verticalFrame.setObjectName("js_verticalFrame")
	self.js_verticalLayout = QVBoxLayout(self.js_verticalFrame)
	self.js_verticalLayout.setContentsMargins(8, 9, 9, 3)
	self.js_verticalLayout.setObjectName("js_verticalLayout")
	self.label_js = QLabel(self.js_verticalFrame)
	self.label_js.setObjectName("label_js")
	self.js_verticalLayout.addWidget(self.label_js)
	self.js_textedit = QPlainTextEdit(self.js_verticalFrame)
	self.js_textedit.setObjectName("js_textedit")
	self.js_verticalLayout.addWidget(self.js_textedit)

	#set default font
	self.html_textedit.setFont(default_font)
	self.css_textedit.setFont(default_font)
	self.js_textedit.setFont(default_font)
	
	#add the widgets to the splitter
	splitter.addWidget(self.html_verticalFrame)
	splitter.addWidget(self.css_verticalFrame)
	splitter.addWidget(self.js_verticalFrame)

	#add the splitter to the horizonal layout.
	self.horizontalLayout.addWidget(splitter)
