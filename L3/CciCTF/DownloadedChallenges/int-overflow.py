import numpy as np

int64_tab = np.array([0], dtype=np.int64)
val = int(input("A vous de tester !\n"))
if val == -1:
        exit()

int64_tab[0] = val
int64_tab[0] = (int64_tab[0] * 7) + 1
print(int64_tab[0])
if int64_tab[0] == -1:
        print("Vous avez trouvé le flag!")