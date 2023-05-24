#MenuTitle: Regenerate Production Name for All Glyphs
__doc__="""
Resets all production names to the structure: uniXXXX or uXXXXX, or to whatever GlyphData stipulates, e.g., ‘uni1E91’ for zcircumflex.
"""

print("Resetting all production names of frontmost document:")

for info in Doc.infos:
	info.generateUniName()
	print(f"{info.productionName} ← {info.name} ({info.unicode})")

print("✅ Done.")