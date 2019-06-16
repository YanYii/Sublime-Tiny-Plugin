import sublime
import sublime_plugin

PRE_HEADER = ['data:image/jpeg;base64', 'data:image/png;base64', 'data:image/bmp;base64', 'data:image/gif;base64', 'data:image/x-icon;base64']

class Yan1Base64PhotoCommand(sublime_plugin.TextCommand):
	def run(self, edit, action='remove', ext=''):
		if action == 'remove':
			region = sublime.Region(0, 30)
			header = self.view.substr(region).split(',')[0]
			if header in PRE_HEADER:
				self.view.replace(edit, sublime.Region(0, len(header) + 1), "")
		elif action == 'append' and ext != '':
			photo_type = ext
			if ext == 'ico':
				photo_type = 'x-icon'
			if ext == 'jpg':
				photo_type = 'jpeg'
			header = 'data:image/{};base64'.format(photo_type)
			self.view.insert(edit, 0, header + ",")
