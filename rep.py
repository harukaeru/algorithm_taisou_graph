x = open('x.txt').read()

conv = {
  'いっぽ': 'a',
  'すすんで': 'b',
  'まえならえ': 'c',
  'えらいひと': 'd',
  'ひっくりかえって': 'e',
  'ぺこりんこ': 'f',
  'よこにあるいて': 'g',
  'きょろ': 'h',
  'ちょっと': 'i',
  'ここらで': 'j',
  'ひらおよぎ': 'k',
  'しゃがんで': 'l',
  'くりひろい': 'm',
  'くうき': 'n',
  'いれましょ': 'o',
  'シュウ': 'p',
  'ッ': 'q',
  'がはいって': 'r',
  'ピュウ': 's',
  'そろそろ': 't',
  'おわり': 'u',
  'かな': 'v',
}

rev_conv = {}
for k, v in conv.items():
    rev_conv[v] = k

y = (
    x
    .replace('いっぽ', 'a')
    .replace('すすんで', 'b')
    .replace('まえならえ', 'c')
    .replace('えらいひと', 'd')
    .replace('ひっくりかえって', 'e')
    .replace('ぺこりんこ', 'f')
    .replace('よこにあるいて', 'g')
    .replace('きょろ', 'h')
    .replace('ちょっと', 'i')
    .replace('ここらで', 'j')
    .replace('ひらおよぎ', 'k')
    .replace('しゃがんで', 'l')
    .replace('くりひろい', 'm')
    .replace('くうき', 'n')
    .replace('いれましょ', 'o')
    .replace('シュウ', 'p')
    .replace('ッ', 'q')
    .replace('がはいって', 'r')
    .replace('ピュウ', 's')
    .replace('そろそろ', 't')
    .replace('おわり', 'u')
    .replace('かな', 'v')
    .replace(' ', '')
    .replace('\n', '')
)
print(y)
