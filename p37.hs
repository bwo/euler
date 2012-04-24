import Control.Monad
import Data.List
import Primes

firstdig :: Integer -> Integer
firstdig = read . head . drop 1 . inits . show

maybeTruncatable :: Integer -> Bool
maybeTruncatable p
    | p >= 11 = (p `rem` 10) `elem` [3,5,7] && firstdig p `elem` [2,3,5,7]
    | otherwise = (p `rem` 10) `elem` [2,3,5,7] && firstdig p `elem` [2,3,5,7]

inits2 = reverse . drop 1 . reverse . drop 2 . inits
tails2 = drop 2 . reverse . drop 1 . tails

isTruncatable :: Integer -> Bool
isTruncatable p 
    | not $ maybeTruncatable p = False 
    | p < 100 = True
    | otherwise = let ins = inits2 $ show p
                      tls = tails2 $ show p
                  in and [isprime $ read x | x <- ins++tls]

isprime 1 = False
isprime n = isp n primes
    where
      isp n (p:pt) 
          | n < 0 = False
          | n < p*p = True
          | n `rem` p == 0 = False
          | otherwise = isp n pt

main = print $ sum $ drop 4 $ take 15 $ filter isTruncatable primes
