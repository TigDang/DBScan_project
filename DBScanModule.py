from pointClass import Point


def RangeQuery(DB, Q, eps):
    Neighbors = set()
    for P in DB:
        if Point.getMetric(Q, P) <= eps:
            Neighbors.add(P)
    return Neighbors


def Scan(DB, eps, minPTS):
    C = 0
    N = set()
    for P in DB:
        if P.label == 'Undefined':
            N = RangeQuery(DB, P, eps)
            if len(N) < minPTS:
                P.setLabel('Noise')
            else:
                C = C + 1
                P.setLabel(str(C))
                S = N.difference(P)
                for Q in S:
                    if Q.label == 'Noise':
                        Q.setLabel(str(C))
                    if Q.label == 'Undefined':
                        Q.setLabel(str(C))
                        N = RangeQuery(DB, Q, eps)
                        if len(N) >= minPTS:
                            S = S | N

    print('Количество кластеров = ', C)
