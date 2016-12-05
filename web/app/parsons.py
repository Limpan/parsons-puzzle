from pygments.formatters import HtmlFormatter


class CustomHtmlFormatter(HtmlFormatter):

    def wrap(self, source, outfile):
        return self._wrap_code(source)

    def _wrap_code(self, source):
        for i, t in source:
            if i == 1:
                n = len(t) - len(t.lstrip())
                t = '{1}##{0}'.format(t, n)
            yield i, t
