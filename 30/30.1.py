def BlobFibonacciego(rounds):
  if rounds in (1, 2): return 1
  return BlobFibonacciego(rounds - 1) + BlobFibonacciego(rounds - 2)

rounds = 13
print(f'Mass after {rounds} rounds :', BlobFibonacciego(rounds))