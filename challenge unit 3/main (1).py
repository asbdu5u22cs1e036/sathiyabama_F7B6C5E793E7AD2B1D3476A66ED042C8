def linearsearchproduct(productlist, targetproduct):
  indices = []

  for index, product in enumerate(productlist):
    if product == targetproduct:
     indices.append(index)

  return indices


#Example usage:
product = ['Shoes', 'Boots', 'Loafer', 'Shoes', 'Sandal', 'Shoes']
target = 'Shoes'
result = linearsearchproduct(product,target)
print(result)
