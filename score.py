from input import read_input
from functools import reduce

def score(file):
  score = 0;
  video_sizes, latencies_to_dc, latencies_to_cs, requests, (V, E, R, C, X) = read_input("example.in")
  file = open("output/" + file, "r")
  num_cs = int(file.readline())
  
  for i in range(num_cs):
    cs_id, v_ids = file.readline().split(" ")

# Score, independently each endpoint
e_score = lambda CS_ID, E_ID, V_ID: (Ld(E_ID) - L(CS_ID, E_ID))*R(V_ID, E_ID)

# Score how much is saved
score_saved = lambda CS_ID, V_ID:
  score = 0
  for e in range(E):
    score_saved += e_score(CS_ID, e, V_ID)
  return score