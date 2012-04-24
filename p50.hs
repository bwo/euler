module Main(main) where
import Primes 

belowmillion = takeWhile (< 1000000) primes

longestpossible = growchain belowmillion 0 0
    where
      growchain (p:ps) count sum 
          | sum >= 1000000 = count
          | otherwise = growchain ps (count+1) (sum+p)
      growchain [] _ _ = 0 --will never happen

-- we don't want the longest *chain* but the prime summed by the longest chain.
longest = countdown $ longestpossible 
    where 
      countdown chainlength 
          | success = sum chain
          | otherwise = countdown $ chainlength - 1
          where 
            (success, chain) = existschain chainlength
      existschain chainlength = findsum chain rest
          where
            (chain, rest) = startchain chainlength belowmillion
      findsum chain [] = (sum chain `elem` belowmillion,chain)
      findsum chain@(c:ct) (r:rt) 
          | sum chain > 1000000 = (False, [])
          | sum chain `elem` belowmillion = (True, chain)
          | otherwise = findsum (ct++[r]) rt
      startchain n lst =  (take n lst, drop n lst)
            
main = do
  print longest
