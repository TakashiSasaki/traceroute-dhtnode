import pings

p = pings.Ping(quiet=False) # Pingオブジェクト作成
res = p.ping("google.com")  # googleを監視

