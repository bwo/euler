module Primes(primes, nonprimes) where
data People a = VIP a (People a) | Crowd [a]
 
mergeP :: Ord a => People a -> People a -> People a
mergeP (VIP x xt) ys                    = VIP x $ mergeP xt ys
mergeP (Crowd xs) (Crowd ys)            = Crowd $ merge  xs ys
mergeP xs@(Crowd ~(x:xt)) ys@(VIP y yt) = case compare x y of
    LT -> VIP x $ mergeP (Crowd xt) ys
    EQ -> VIP x $ mergeP (Crowd xt) yt
    GT -> VIP y $ mergeP xs yt
 
 
merge :: Ord a => [a] -> [a] -> [a]
merge xs@(x:xt) ys@(y:yt) = case compare x y of
    LT -> x : merge xt ys
    EQ -> x : merge xt yt
    GT -> y : merge xs yt
 
diff xs@(x:xt) ys@(y:yt) = case compare x y of
    LT -> x : diff xt ys
    EQ ->     diff xt yt
    GT ->     diff xs yt
 
foldTree :: (a -> a -> a) -> [a] -> a
foldTree f ~(x:xs) = f x . foldTree f . pairs $ xs
    where pairs ~(x: ~(y:ys)) = f x y : pairs ys
 
primes, nonprimes :: [Integer]
primes    = 2:3:diff [5,7..] nonprimes
nonprimes = serve . foldTree mergeP . map multiples $ tail primes
    where
    multiples p = vip [p*k | k <- [p,p+2..]]
 
    vip (x:xs)       = VIP x $ Crowd xs
    serve (VIP x xs) = x:serve xs
    serve (Crowd xs) = xs
-- From haskell wiki. Given the number of exercises that basically come down to "can you generate primes efficiently?" this is arguably cheating, but also those problems are arguably duplicates of each other.
