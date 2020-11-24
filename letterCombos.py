def letterCombinations(digits: str):
  mapping = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }

  res = []
  dfs(digits, mapping, "", res)
  return res

def dfs(digits: str, mapping, currString: str, res: [str]):
  
  # O(3 ^ n), n := #digits

  # base case
  if digits == "":
    res.append(currString)
    return

  # recursive case
  for letter in mapping[digits[0]]:
    dfs(digits[1:], mapping, currString + letter, res)

  