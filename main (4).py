# 3.1 Write a function called near search product that takes the list of products and a target product name as input. The function should perform a linear search to find the target product in the list and return a list of indices of all occurrences of the product if found, or an empty list if the product is not found
def linearSearchProduct(productList, targetProduct):
  indices=[]
  for index, product in enumerate(productList):
    if product == targetProduct:
      indices.append(index)
  return indices

products = ["shoes","boat","loafer","shoes","sandal","shoes"]
target = "shoes"
result = linearSearchProduct(products, target)
print(result)
