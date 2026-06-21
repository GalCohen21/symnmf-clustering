import sys

points = []
centroids = []
clusters = []
d = 0

def dist(point1, point2):
    return sum((float(point1[i]) - float(point2[i]))**2 for i in range(d)) ** 0.5

def point_to_cluster():
    for i in range(len(clusters)):
        clusters[i] = []

    for point in points:
        nearest = float('inf')
        idx = 0
        c_idx = 0
        for centroid in centroids:
            dis = dist(point, centroid)
            if dis < nearest:
                nearest = dis
                c_idx = idx
            idx += 1
        clusters[c_idx].append(point)

def cluster_avg(eps):
    global centroids
    flag = 0
    new_centroids = []
    for idx, cluster in enumerate(clusters):
        if len(cluster) == 0:
            new_centroids.append(centroids[idx])
            continue
        tmp = []
        for j in range(d):
            s = sum(float(p[j]) for p in cluster)
            tmp.append(s / len(cluster))
        if dist(centroids[idx], tmp) > eps:
            flag = 1
        new_centroids.append(tmp)
    centroids = new_centroids
    return flag

def kmeans(input_points, k, max_iter=300, eps=0.001):
    global points, centroids, clusters, d
    points = [list(map(float, p)) for p in input_points]
    d = len(points[0])
    centroids = points[:k]
    clusters = [[] for _ in range(k)]
    
    for _ in range(max_iter):
        point_to_cluster()
        if cluster_avg(eps) == 0:
            break
    
    labels = []
    for point in points:
        nearest = float('inf')
        idx = 0
        c_idx = 0
        for centroid in centroids:
            dis = dist(point, centroid)
            if dis < nearest:
                nearest = dis
                c_idx = idx
            idx += 1
        labels.append(c_idx)
    return labels

if __name__ == "__main__":
    if len(sys.argv) not in [3, 4]:
        print("An Error Has Occurred")
        sys.exit()

    if len(sys.argv) == 3:
        iter = 200
        f = sys.argv[2]
    else:
        iter = sys.argv[2]
        f = sys.argv[3]
        if not iter.isdigit() or not (1 < int(iter) < 1000) or iter[0] == "0":
            print("Invalid maximum iteration!")
            sys.exit()

    if not f.endswith(".txt"):
        print("NA")
        sys.exit()

    f1 = open(f)

    N = 0
    for line in f1:
        N += 1

    f1 = open(f)
    d = len(f1.readline().split(","))
    
    f1 = open(f)
    points = []
    for line in f1:
        points.append(line.split(","))

    k = sys.argv[1]
    if not k.isdigit() or not (1 < int(k) < N) or k[0] == "0":
        print("Invalid number of clusters!")
        sys.exit()
    
    k = int(k)
    iter = int(iter)
    centroids = points[:k]
    clusters = [[] for _ in range(k)]

    for _ in range(iter):
        try:
            point_to_cluster()
            if cluster_avg(0.001) == 0:
                break
        except:
            print("An Error Has Occurred")
            sys.exit()

    for centroid in centroids:
        print(",".join(f"{float(x):.4f}" for x in centroid))
