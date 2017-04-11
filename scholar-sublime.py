import sublime, sublime_plugin
import webbrowser

class ScholarsublimeSearchPaperCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for selection in self.view.sel():
            # if the user didn't select anything, search the currently highlighted word
            region = None
            if selection.empty():
                region = self.view.word(selection)
            else:
                region = selection
            text = self.view.substr(region)
            url = "http://scholar.google.com/scholar?hl=en&q=" + text
            webbrowser.open_new(url)




class ScholarsublimeSearchAuthorCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for selection in self.view.sel():
            # if the user didn't select anything, search the currently highlighted word
            region = None
            if selection.empty():
                region = self.view.word(selection)
            else:
                region = selection
            text = self.view.substr(region)
            url = "http://scholar.google.com/citations?hl=en&view_op=search_authors&mauthors=" + text
            webbrowser.open_new(url)
