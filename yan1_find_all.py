import sublime
import sublime_plugin


class Yan1FindAllCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		sels = self.view.sel()
		if len(sels) == 1:
			sel = sels[0]
			content = self.view.substr(sel)
			# print('select content:' + content)
			if content != '':
				regions = self.view.find_all(content)
				# print(regions)
				sels.clear()
				sels.add_all(regions)
