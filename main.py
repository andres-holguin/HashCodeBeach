from input import read_input

def main():
  video_sizes, latencies_to_dc, latencies_to_cs, requests, (V, E, R, C, X) = read_input("example.in")
  print(video_sizes)
  print(latencies_to_dc)
  print(latencies_to_cs)
  print(requests)

if __name__ == '__main__':
  main()
