import opendht
node = opendht.DhtRunner()
node.run()
node.bootstrap("bootstrap.ring.cx", "4222")
node.put(opendht.InfoHash.get("aaa"), opendht.Value(b'bbb'))
result = node.get(opendht.InfoHash.get("aaa"))
for r in result:
    print(r)

