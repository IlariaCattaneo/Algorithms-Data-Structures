def largest_cluster(A, D=10):
    cluster = []
    for a in A:
        clu = []
        for b in A:
            if b <= a and b - a <= D:
                clu.append(b)
        if len(clu) > len(cluster):
            cluster = clu
    print(cluster)

largest_cluster([12,2,34,7,21,24,50,45,-9,7,45])