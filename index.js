/*
                                                                             .:://++++++//:-.
                                                                           .++/::++++++++++++/`
                                                                           :++   /+++++++++++/:
                                                                           :++/:/++++++++++////
  __  __ _                _____       _   _                                .---------+++//////:
 |  \/  (_)              |  __ \     | | | |                        -:///////////////++///////: ddddhs:
 | \  / |_  ___ _ __ ___ | |__) |   _| |_| |__   ___  _ __        -++++++++++++++++++/////////: ddddddds`
 | |\/| | |/ __| '__/ _ \|  ___/ | | | __| '_ \ / _ \| '_ \      .+++++++++++++++++///////////: ddddddddo
 | |  | | | (__| | | (_) | |   | |_| | |_| | | | (_) | | | |     /+++++++++++++++/////////////`/ddddddddd
 |_|  |_|_|\___|_|  \___/|_|    \__, |\__|_| |_|\___/|_| |_|     ++++++++++++/::::::::::::--..+dddddddddd
                                 __/ |                           ++++++++++:`-+syyyyyyyysssyhdddddddddddd
                                |___/                            /++++++++-.hmmdddddddddddddddddddddddddh
                                                                 -+++++++/`omddddddddddddddddddddddddddd+
                                                                  :++++///`sddddddddddddddddddddddddddd+
                                                                   .://///`sdddddddddhyyyyyyyyyyyyyys/`
                                                                           sdddddddddo++++++++/
                                                                           sdddddddddddddhshddy
                                                                           oddddddddddddd`  hdy
                                                                           .yddddddddddddyoydd/
                                                                             ./oyhhdddddhys+:`
WELL DONE!

You've found the source! :-)

If you want to see how the editor works you should check out the python-main.js file - it has all sorts of
helpful comments for you so you'll be able to work it all out.

If you're wondering what the long string of random looking characters is at the end of this file, well, it's
a copy of the MicroPython runtime that we copy onto the micro:bit. When you click download, the code you've
written in the editor is similarly encoded and then inserted at the end where you see a line of ::::::::::::
characters.

If you want to know more about Python visit:

http://python.org/

If you want to know more about MicroPython (the version of Python we're using here), then visit:

http://micropython.org/

Finally, remember the Zen of MicroPython:

Code,
Hack it,
Less is more,
Keep it simple,
Small is beautiful,

Be brave! Break things! Learn and have fun!
Express yourself with MicroPython.

:-)

Happy hacking,

Nicholas and Damien.
*/
function entry() {
	const fs = require("fs");
	const upyhex = require("./lib/hexlify");
	const firmware = require("./lib/firmware");

	var fileName = process.argv[2];
	if (!fileName) {
		console.log("Usage: p2h <filename>");
		process.exit();
	}
	var file = fs.readFileSync(fileName);
	var input = file.toString();
	var output = upyhex.injectPyStrIntoIntelHex(firmware, input);
	fs.writeFileSync("microbit.hex", output);
}
module.exports = entry;
