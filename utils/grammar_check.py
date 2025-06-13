# utils/grammar_check.py

import language_tool_python

def check_grammar(text):
    tool = language_tool_python.LanguageTool('en-US')
    matches = tool.check(text)

    suggestions = []
    for match in matches:
        suggestions.append({
            "error": match.message,
            "suggestions": match.replacements,
            "sentence": match.context,
            "offset": match.offset,
            "length": match.errorLength
        })

    return suggestions
