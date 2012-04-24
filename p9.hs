module Main(main) where

pyts = [(a*b*(1000-a-b)) | a <- [1..998], b <- [a..998], (a*a)+(b*b) == (1000-a-b)*(1000-a-b)]

main = do
    print (head pyts)
