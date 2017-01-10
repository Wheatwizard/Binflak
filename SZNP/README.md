#About

SZNP, like Bin-Flak, is an attempt to compress all valid Brain-Flak programs into as few bytes as
possible.  Unlike Bin-Flak SZNP trades what little readabilty and writabilty Bin-Flak might have 
for more compression and overall shorter programs.

#How does it work

SZNP works on a grammar defined in rules.py known as the SZNP grammar.  This grammar describes a 
subset of Brain-Flak programs.  This subset is defined such that any program not spanned by the
grammar is equivalent to some program of equal or shorter Brain-Flak length than some program
that is spanned by the grammar.

The SZNP grammar is defined in rules.py and can be redefined at any time.  We hope to make
improvements to this grammar in the future and will update the file accordingly.  However it
should be noted that even the slightest change to the grammar will nullify the vast majority of
programs written in SZNP.

The compiler of SZNP takes a number and translates that into a path along the grammar and then
traverses that path to get the appropriate program.

#Writing in SZNP

To write in SZNP one must first create a valid Brain-Flak program that is spanned by the SZNP
grammar.  Once a program has been found one must find the path that creates the program in the
SZNP grammar.  

Now you must set up an accumulator.  At the end of the process this will be your source code.
For each step in the traversal you must multiply your accumulator by the number of possible 
transformations at that step and add the index of the transformation that you chose.

Someday a compiler may exist that does this on its own.
