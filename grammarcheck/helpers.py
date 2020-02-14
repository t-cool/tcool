import language_check

tool = language_check.LanguageTool('en-US')


def check_grammar(text):
    suggestions = tool.check(text)
    return suggestions
