import sublime
import sublime_plugin

# generate order, order by select
class Yan1GenerateOrderCommand(sublime_plugin.TextCommand):
	def run(self, edit, symbol):
		sels = self.view.sel()
		# print(symbol)
		count = len(sels)
		for sel in reversed(sels):
			self.view.insert(edit, sel.a, str(count) + symbol)
			count -= 1
