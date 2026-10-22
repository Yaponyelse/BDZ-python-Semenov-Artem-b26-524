import re
text = "Это   строка    с     большим    количеством   пробелов."
print(re.sub(r" +", " ", text))
text2 = "   Текст   с   пробелами   "
print(re.sub(r" +", " ", text2).strip())