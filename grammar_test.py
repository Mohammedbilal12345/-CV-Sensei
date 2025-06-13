# grammar_test.py

import language_tool_python

tool = language_tool_python.LanguageTool('en-US')
text = "He go to school every days."

matches = tool.check(text)

for match in matches:
    print(f"Issue: {match.message}")
    print(f"Suggestion: {match.replacements}")
    print(f"Sentence: {match.context}")
    print("---")
