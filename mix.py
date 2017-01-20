def mix_string(a, b):
  a1 = ''
  a2 = ''
  b1 = ''
  b2 = ''
  count = 1
  for c in a:
    if count <= 2:
	  a1 += c 
    elif count > 2:
	  a2 += c 
    count += 1
  count1 = 1
  for c in b:
    if count1 <= 2:
	  b1 += c
    elif count1 > 2:
	  b2 += c 
    count1 += 1
  return (b1+a2) + ' ' + (a1+b2)
  
print mix_string('dog', 'dinner')