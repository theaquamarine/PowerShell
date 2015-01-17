import unittest

import sublime


class ViewTest(unittest.TestCase):
    def setUp(self):
        self.view = sublime.active_window().new_file()

    def append(self, text):
        self.view.run_command('append', {'characters': text})

    def tearDown(self):
        self.view.set_scratch(True)
        self.view.close()


class SyntaxTest(ViewTest):
    def _setSyntax(self, rel_path):
        self.view.set_syntax_file(rel_path)

    def getScopeNameAt(self, pt):
        return self.view.scope_name(pt)

    def getFinestScopeNameAt(self, pt):
        return self.getScopeNameAt(pt).split()[-1]

    def getScopeNameAtRowCol(self, row, col):
        text_pt = self.view.text_point(row, col)
        return self.getScopeNameAt(text_pt)

    def getFinestScopeNameAtRowCol(self, row, col):
        return self.getScopeNameAtRowCol(row, col).split()[-1]

class PowerShellSyntaxTest(SyntaxTest):
    def setUp(self):
        super().setUp()
        self._setSyntax('Packages/PowerShell/Support/PowershellSyntax.tmLanguage')

class PowerShellSyntaxTokenTest(PowerShellSyntaxTest):

    def getTokenHeader(self):
        return ['scope_name', 'str', 'start', 'end']

    def getTokens(self):
        selectors = [
            "comment.block",
            "comment.documentation.embedded",
            "comment.line.number-sign",
            "constant.character.escape",
            "constant.language",
            "constant.numeric.hexadecimal",
            "constant.numeric.scientific",
            "constant.string.documentation",
            "entity.name",
            "entity.name.function.invocation",
            "entity.other",
            "entity.other.attribute-name",
            "entity.other.attribute.parameter",
            "interpolated.complex.source",
            "interpolated.simple.source",
            "keyword.control",
            "keyword.operator.assignment",
            "keyword.operator.bitwise",
            "keyword.operator.comparison",
            "keyword.operator.documentation",
            "keyword.operator.logical",
            "keyword.operator.math",
            "keyword.operator.other",
            "keyword.operator.range",
            "keyword.operator.redirection",
            "keyword.operator.string-format",
            "keyword.operator.unary",
            "keyword.other",
            "keyword.other.statement-separator",
            "meta",
            "meta.group.array-expression",
            "meta.group.complex.subexpression",
            "meta.scriptblock",
            "punctuation.end.definition.comment.block",
            "punctuation.start.definition.comment.block",
            "source",
            "storage",
            "storage.modifier.scope",
            "string.quoted.double",
            "string.quoted.double.heredoc",
            "string.quoted.single",
            "string.quoted.single.heredoc",
            "support.constant",
            "support.constant.variable",
            "support.function",
            "support.variable.automatic",
            "support.variable.drive",
            "variable.language",
            "variable.other",
            "variable.other.normal",
            "variable.other.readwrite",
        ]
        tokens = []
        for selector in selectors:
            regions = self.view.find_by_selector(selector)
            for region in regions:
                tokens += [{ 'scope_name': selector, 'str': self.view.substr(region), 'start': region.a, 'end': region.b }]
        return tokens
