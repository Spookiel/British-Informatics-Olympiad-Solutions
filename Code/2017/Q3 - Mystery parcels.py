from functools import lru_cache

@lru_cache(maxsize=None)
def item_ways(parcel_weight,num_item,max_weight):
  if parcel_weight == 0 and num_item == 0:
    return 1
  elif parcel_weight <= 0 or num_item <= 0:
    return 0
  return sum([
      item_ways(parcel_weight-i, num_item-1, i)
      for i in range(1,max_weight+1)
      ])

@lru_cache(maxsize=None)
def parcel_ways(num_parcel,max_weight,num_item,parcel_weight):
  if num_parcel == 0 and num_item == 0:
    return 1
  elif num_parcel <= 0 or num_item <= 0:
    return 0
  return sum([
      parcel_ways(num_parcel-1, max_weight, num_item-i, parcel_weight) * item_ways(parcel_weight, i, max_weight)
      for i in range(1,num_item+1)
      ])

p,i,n,w = [int(i) for i in input().split()]

print(parcel_ways(p, i, n, w))