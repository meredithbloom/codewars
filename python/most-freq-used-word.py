
# Most frequently used words in a text - 4kyu
'''
Write a function that, given a string of text (possibly with punctuation and line-breaks), returns an array of the top-3 most occurring words, in descending order of the number of occurrences.

Assumptions:
A word is a string of letters (A to Z) optionally containing one or more apostrophes (') in ASCII.
Apostrophes can appear at the start, middle or end of a word ('abc, abc', 'abc', ab'c are all valid)
Any other characters (e.g. #, \, / , . ...) are not part of a word and should be treated as whitespace.
Matches should be case-insensitive, and the words in the result should be lowercased.
Ties may be broken arbitrarily.
If a text contains fewer than three unique words, then either the top-2 or top-1 words should be returned, or an empty array if a text contains no words.

'''

string1 = "In a village of La Mancha, the name of which I have no desire to call to mind, there lived not long since one of those gentlemen that keep a lance in the lance-rack, an old buckler, a lean hack, and a greyhound for coursing. An olla of rather more beef than mutton, a salad on most nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra on Sundays, made away with three-quarters of his income."


valid = (r'[a-zA-Z\']')


def check_char(char):
    if char.isalpha() or char == "'":
        return True
    else:
        return False



def top_3_words(text):
    c = Counter(re.findall(r"[a-z']+", re.sub(r" '+ ", " ", text.lower())))
    #print(list(c))
    common = c.most_common(3)
    words = []
    for word in common:
        words.append(word[0])
    print(words)




# top_3_words(string1)

#top_3_words("a a a  b  c c  d d d d  e e e e e")
#top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e")
# top_3_words("  //wont won't won't ")
# top_3_words("  '  ")
# top_3_words("  '''  ")
# top_3_words("LNHjcei-nBiKKCMgv -  LNHjcei-kepvNClzV!/;:_kDupSNELy?,: _QcibmQkHy,;_,,DARKdSL/. .!nBiKKCMgv//!!!DARKdSL!/LNHjcei//dLOFmmu'//_.yltqos .?;-kDupSNELy. ./nBiKKCMgv- ,_yltqos//._LNHjcei:_/dLOFmmu'__QcibmQkHy ?! LNHjcei!._QcibmQkHy,LNHjcei/.;LNHjcei_.;?yltqos:nBiKKCMgv:_ ./yltqos_ !LNHjcei-yltqos:!-?.yltqos :/nBiKKCMgv _!?QcibmQkHy-,:DARKdSL,!!;kDupSNELy,/ !!yltqos, :-kDupSNELy?-; _kDupSNELy/!kDupSNELy,_dLOFmmu'/--yltqos?yltqos-yltqos!-!yltqos!_?/_kDupSNELy_-!?kDupSNELy_!kDupSNELy?yltqos:LNHjcei yltqos/_ !kDupSNELy!!?kDupSNELy--.;-kDupSNELy?-kDupSNELy/!?;nBiKKCMgv./yltqos!/dLOFmmu'-,!:/kepvNClzV:dLOFmmu'.,??yltqos?_kDupSNELy?nBiKKCMgv./:-;LNHjcei ,.:kDupSNELy-kDupSNELy,yltqos!QcibmQkHy!kDupSNELy.nBiKKCMgv:..:kDupSNELy/yltqos,/.,LNHjcei/:!DARKdSL! ::?kepvNClzV_QcibmQkHy_/?/_kDupSNELy,_-nBiKKCMgv!///.kDupSNELy .yltqos:/;LNHjcei-:,?QcibmQkHy.!?.QcibmQkHy.LNHjcei  /yltqos._yltqos.?__LNHjcei/.?.kDupSNELy.!nBiKKCMgv!_: yltqos-dLOFmmu' kepvNClzV//_.?yltqos:nBiKKCMgv?;LNHjcei/nBiKKCMgv: ,kDupSNELy!;!:yltqos. .,:yltqos . ;yltqos/?,;;dLOFmmu'..:!nBiKKCMgv//DARKdSL.QcibmQkHy_:,./dLOFmmu'!dLOFmmu'_yltqos/.; nBiKKCMgv,-/_dLOFmmu'? dLOFmmu'._:..LNHjcei;/_dLOFmmu'!kDupSNELy -;;-kDupSNELy:.;?nBiKKCMgv,,yltqos,? ::dLOFmmu';-?;-LNHjcei/; ;_DARKdSL/? ??kDupSNELy:?QcibmQkHy, /nBiKKCMgv ?LNHjcei_- ::yltqos?_:;?kDupSNELy:!LNHjcei_,_?;")