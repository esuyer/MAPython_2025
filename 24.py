poll = {
  'cat': 100,
  'dog': 150,
  'rabbit': 15,
  'fish': 20,
  'pig': 5
}

poll['hampster'] = 30
print(poll)

poll['hampster'] = 35
print(poll)

Pig = input('how many new votes did the pig get?')
poll['pig'] += int(Pig)
print(poll)
