#MenuTitle: Set All Sort Names to ‘scriptName.unicodePoint’
__doc__="""
Sets all sort names to the structure: [NAME OF SCRIPT].[UTF16 UNICODE CODEPOINT], e.g., Adieresis would have ‘latin.00C4’ as new sort name.
"""

print("Resetting all sort names of frontmost ")

for info in Doc.infos:
	info.sortName = f"{info.script}.{info.unicode}"
	print(f"ℹ️ {info.name}: {info.sortName}")

print("✅ Done.")