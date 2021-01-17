from konlpy.tag import Komoran
import numpy as np

komoran = Komoran()

query = "가락지빵 할게요"
pos = komoran.pos(query)
print("; " + query + "\n")
for a in pos:
    i = 1
    print(str(i) + "\t" + a[0] + "\t" + a[1])
    int(i)
print(pos)
pred_index = np.argmax(query)
print(pred_index)
