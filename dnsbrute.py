import dns.resolver

res = dns.resolver.Resolver()

response = res.resolve("bancocn.com", "A")

for info in response:
	print(info)
