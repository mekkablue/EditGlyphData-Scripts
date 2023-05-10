#MenuTitle: Recount Unicodes from First Encoded Glyph
__doc__="""
Will reset Unicode values for each selected glyph, starting with the value of the first encoded glyph. Will add 1 for each subsequent glyph.
"""

skipUnencoded = bool(App.defaults["com.mekkablue.RecountUnicodes.skipUnencoded"])
# set to False if entries without a Unicode should receive a Unicode
# set to True if unencoded entries should remain without a Unicode

print("\n\n\n📜 Recount Unicodes from First Encoded Glyph")
doc = App.orderedDocuments()[0]
docURL = doc.fileURL()
if docURL:
	print(f"📄 {docURL.path()}")

print(f"\n👩🏽‍🍳 Recounting Unicode values in {len(doc.selectedInfos)} selected entries...")
unicodeValue = None
for info in doc.selectedInfos:
	if unicodeValue == None and info.unicode:
		unicodeValue = int(info.unicode, 16)
	
	if unicodeValue != None and (not skipUnencoded or info.unicode):
		info.unicode = f"{unicodeValue:04X}"
		print(f"\t🔢 New code {info.unicode} for: {info.name}")
		unicodeValue += 1

print(f"\n🕵🏽 Verifying if there are double encodings...")
codeDict = {}
for info in doc.infos:
	code = info.unicode
	if code != None and code in codeDict.keys():
		codeDict[code].append(info.name)
	else:
		codeDict[code] = [info.name]
for code in sorted(codeDict.keys()):
	infos = codeDict[code]
	if len(infos) > 1:
		print(f"\t⚠️ {code} in {len(infos)} entries: {', '.join(infos)}")
print("\nDone.")