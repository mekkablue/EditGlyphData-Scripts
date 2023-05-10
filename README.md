# EditGlyphData-Scripts

These are mekkablue scripts for [EditGlyphData.app](https://glyphsapp.com/tools/editglyphdata).

## Installation

Copy and paste this into Terminal.app, and press the Return key:

```
git clone https://github.com/mekkablue/EditGlyphData-Scripts ~/Library/Application\ Support/EditGlyphData/Scripts/mekkablue/
```

Then, in EditGlyphData.app, hold down the Opt key, and pick *Script > Reload Scripts* (Cmd-Opt-Shift-Y), or restart the app.

## Updating to the Latest Version

Copy and paste this into Terminal.app, and press the Return key:

```
cd ~/Library/Application\ Support/EditGlyphData/Scripts/mekkablue/; git checkout
```

Then, in EditGlyphData.app, hold down the Opt key, and pick *Script > Reload Scripts* (Cmd-Opt-Shift-Y), or restart the app.


## Scripts

* **Recount Unicodes from First Encoded Glyph:** Will reset Unicode values for each selected glyph, starting with the value of the first encoded glyph. Will add 1 for each subsequent glyph.
	* Option: `App.defaults["com.mekkablue.RecountUnicodes.skipUnencoded"] = False`: set to `False` if entries without a Unicode value should receive a Unicode value; set to `True` if unencoded entries should remain without a Unicode value


## License

Copyright 2023 Rainer Erich Scheichelbauer (@mekkablue)

Licensed under the Apache License, Version 2.0 (the "License"); you may not use the software provided here except in compliance with the License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

See the License file included in this repository for further details.
