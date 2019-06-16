import sublime
import sublime_plugin


class Yan1SummaryCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		# sum all selected
		sels = self.view.sel()
		result = 0
		for sel in sels:
			content = self.view.substr(sel)
			try:
				result += int(content)
			except Exception as e:
				print('The select content {} can not parse to int'.format(content))
		self.view.window().status_message('The sum result : {}'.format(result))

