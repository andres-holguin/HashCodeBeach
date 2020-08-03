def greedy(input_data):
  video_sizes, latencies_to_dc, latencies_to_cs, requests, (V, E, R, C, X) = input_data
  c_e_L = {}
  for e in range(E):
    for (c, L) in latencies_to_cs[e]:
      c_e_L[c, e] = L
  video_requests = {}
  for (v_id, e_id, num_req) in requests:
    video_requests[v_id, e_id] = num_req
  


