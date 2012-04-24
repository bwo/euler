module Main(main) where
import Char
eterms = 1 : 2 : 1 : map (\a -> if a == 1 then 1 else a+2) eterms
process (num, denom) addend = (denom,denom*addend+num)
finalize (num, denom) = (2*denom+num,denom)
digitalsum = sum . (map Char.digitToInt) . show
main = do
  (f:fs) <- return (reverse $ take 99 eterms)
  print $ digitalsum $ fst $ finalize (foldl process (1,f) fs)
