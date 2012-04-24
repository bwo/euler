module Main(main) where
import Monad
import List
data Chain = Octagon Integer | Hexagon Integer | Heptagon Integer | Pentagon Integer | Square Integer | Triangle Integer deriving Show
instance (Eq Chain)
    where
      (==) a b = (toint a) == (toint b)
toint (Octagon a) = a
toint (Heptagon a) = a
toint (Hexagon a) = a
toint (Pentagon a) = a
toint (Triangle a) = a
toint (Square a) = a

polygonal n = 1 : zipWith (+) (polygonal n) (map (\x -> 1 + n*x) [1..])
tris = polygonal 1
squares = polygonal 2
pents = polygonal 3
hexes = polygonal 4
hepts = polygonal 5
octs = polygonal 6
fourdigs = takeWhile (<10000) . dropWhile (<1000)
fdocts = map Octagon $ fourdigs octs
fdhepts = map Heptagon $ fourdigs hepts
fdhexes = map Hexagon $ fourdigs hexes
fdpents = map Pentagon $ fourdigs pents
fdsqs = map Square $ fourdigs squares
fdtris = map Triangle $ fourdigs tris
mostshapes = [fdhepts, fdhexes, fdpents, fdsqs, fdtris]

shlink a b = (drop 2 $ show $ toint a) == (take 2 $ show $ toint b) && a /= b
link a sofar c@(Octagon b)
    | shlink a c = return ((c,delete fdocts sofar))
    | otherwise = mzero
link a sofar c@(Heptagon b)
    | shlink a c = return ((c,delete fdhepts sofar))
    | otherwise = mzero
link a sofar c@(Hexagon b)
    | shlink a c = return ((c,delete fdhexes sofar))
    | otherwise = mzero
link a sofar c@(Pentagon b)
    | shlink a c = return ((c,delete fdpents sofar))
    | otherwise = mzero
link a sofar c@(Square b)
    | shlink a c = return ((c,delete fdsqs sofar))
    | otherwise = mzero
link a sofar c@(Triangle b)
    | shlink a c = return ((c,delete fdtris sofar))
    | otherwise = mzero

flatten :: [[a]] -> [a]
flatten = foldl1 (++)

cands = [[l1,l2,l3,l4,l5,l6] | l1 <- fdocts,
         (l2, nxt) <-  concatMap (link l1 mostshapes) (flatten mostshapes),
         (l3, nxt') <- concatMap (link l2 nxt) (flatten nxt),
         l1 /= l3, 
         (l4, nxt'') <- concatMap (link l3 nxt') (flatten nxt'),
         l1 /= l4, l2 /= l4,
         (l5, nxt''') <- concatMap (link l4 nxt'') (flatten nxt''),
         l1 /= l5, l2 /= l5, l3 /= l5,
         (l6, lst) <- concatMap (link l5 nxt''') (flatten nxt'''),
         l2 /= l6, l3 /= l6, l4 /= l6,
         shlink l6 l1]
main = do
  print . sum . map toint $ head cands
