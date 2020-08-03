def read_input(file):
  file = open("dataset/" + file, "r")

  V, E, R, C, X = file.readline().split(" ")
  V = int(V)
  E = int(E)
  R = int(R)
  C = int(C)
  X = int(X)

  video_sizes = []
  video_sizes = file.readline().split(" ")
  for i, size in enumerate(video_sizes):
    video_sizes[i] = int(size)

  latencies_to_dc = []
  # 2D array
  latencies_to_cs = []
  # array of tuples 
  requests = []
  
  for e in range(E):
    L, num_cs = file.readline().split(" ")
    latencies_to_dc.append(int(L))

    latencies = []
    for cs in range(int(num_cs)):
      c_id, c_L = file.readline().split(" ")
      latencies.append((int(c_id), int(c_L)))

    latencies_to_cs.append(latencies)

  for r in range(R):
    v_id, e_id, num_req = file.readline().split(" ")
    requests.append((int(v_id), int(e_id), int(num_req)))
  
  file.close()
  return (video_sizes, latencies_to_dc, latencies_to_cs, requests, (V, E, R, C, X))
