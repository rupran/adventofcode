import md5

counter = 0
start = 'bgvyzdsv'
while True:
    m = md5.new()
    m.update(start)
    m.update(str(counter))
    d = m.hexdigest()
    
    if str(d).startswith("000000"):
        break

    counter += 1

print counter
