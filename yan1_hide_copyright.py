import sublime
import sublime_plugin


class Yan1HideCopyrightCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		# check last 5 line
		regions = self.view.lines(sublime.Region(0, self.view.size()))

		# check csdn, jianshu
		# print(last_regions)
		last_regions = regions[-5:]
		flag = self.check_csdn(last_regions)
		if not flag:
			flag = self.check_jianshu(last_regions)
		
		if flag:
			self.erase_content(edit, last_regions[0].begin()-1, last_regions[-1].end())

		# check zhihu
		if not flag:
			first_region = regions[:5]
			flag = self.check_zhihu(first_region)
			if flag:
				self.erase_content(edit, first_region[0].begin(), first_region[-1].end() + 1)

	def erase_content(self, edit, begin, end):
		region = sublime.Region(begin, end)
		self.view.erase(edit, region)

	def check_csdn(self, regions):
		line_idx = -2
		content = self.view.substr(regions[line_idx])
		flag = content.startswith('https://blog.csdn.net', 3)
		return flag

	def check_jianshu(self, regions):
		line_idx = -3
		content = self.view.substr(regions[line_idx])
		flag = content.startswith('https://www.jianshu.com', 3)
		return flag

	def check_zhihu(self, regions):
		line_idx = 1
		content = self.view.substr(regions[line_idx])
		flag = content.startswith('https://www.zhihu.com', 3)
		return flag

