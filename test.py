import opendht as dht

node = dht.DhtRunner()
node.run()

node.bootstrap("bootstrap.ring.cx", "4222")

node.put(dht.InfoHash.get("aaa"), dht.Value(b'bbb'))

results = node.get(dht.InfoHash.get("aaa"))
for r in results:
    print(r)
