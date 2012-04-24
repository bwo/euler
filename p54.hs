module Main(main) where
import Control.Monad
import Data.Monoid
import List
import IO
data Cval = One | Two | Three | Four | Five | Six | Seven | Eight | Nine | Ten | Jack | Queen | King | Ace deriving (Show, Eq, Enum, Ord)
readsCval "" = []
readsCval (c:cs) = case c of 
                     '1' -> [(One,cs)]
                     '2' -> [(Two,cs)]
                     '3' -> [(Three,cs)]
                     '4' -> [(Four, cs)]
                     '5' -> [(Five,cs)]
                     '6' -> [(Six,cs)]
                     '7' -> [(Seven,cs)]
                     '8' -> [(Eight,cs)]
                     '9' -> [(Nine,cs)]
                     'T' -> [(Ten,cs)]
                     'J' -> [(Jack,cs)]
                     'Q' -> [(Queen,cs)]
                     'K' -> [(King,cs)]
                     'A' -> [(Ace,cs)]
                     otherwise -> []
instance Read Cval where
    readsPrec _ s = readsCval s

data Suit = Spades | Hearts | Diamonds | Clubs deriving (Show, Eq, Enum, Ord)
readsSuit "" = []
readsSuit (c:cs) = case c of 
                     'S' -> [(Spades,cs)]
                     'C' -> [(Clubs,cs)]
                     'D' -> [(Diamonds,cs)]
                     'H' -> [(Hearts,cs)]
                     otherwise -> []
instance Read Suit where
    readsPrec _ s = readsSuit s
data Card = Card {value :: Cval, suit :: Suit} deriving (Show, Eq)
instance Ord Card where
    compare c1 c2 = compare (value c1) (value c2)
readsCard "" = []
readsCard cs = [(Card val st, rest) | (val, r) <- reads cs, (st, rest) <- reads r]

instance Read Card where
    readsPrec _ = readsCard 
data Hand = Highcard Card | Pair Card | TwoPair Card Card | ThreeKind Card | Straight Card | Flush Card | Fullhouse Card Card | FourKind Card | SFlush Card | RFlush deriving (Show, Eq, Ord)

both (Just x) (Just y) = (Just x)
both _ _ = Nothing

isflush ((Card _ st):rest) 
    | all (\card -> (suit card) == st) rest = Just $ Flush $ head $ reverse rest
    | otherwise = Nothing

isstraight hand@((Card val _):rest) 
    | all (\(v, c) -> v == value c) $ zip [val .. ] hand = Just $ Straight $ head hand
    | otherwise = Nothing

isstraightflush hand = (both (isflush hand) (isstraight hand)) >>= (\(Flush c) -> Just $ SFlush c)

isroyalflush hand@((Card v _):rst) = maybe Nothing (\_ -> if v == Ten then Just RFlush else Nothing) (isstraightflush hand)

isfourkind ((Card v1 _):(c@(Card v2 _)):rest)
    | v2 == (value $ head $ tail $ tail rest) = Just $ FourKind c
    | v1 == v2 && v1 == (value $ head $ tail rest) = Just $ FourKind c
    | otherwise = Nothing 

isfullhouse [(Card v1 _), (c2@(Card v2 _)), (c3@(Card v3 _)), (c4@(Card v4 _)), (Card v5 _)] 
    | v1 == v2 && v3 == v5 = Just $ Fullhouse c3 c2
    | v1 == v3 && v4 == v5 = Just $ Fullhouse c4 c3
    | otherwise = Nothing

isthreekind [(Card v1 _), (Card v2 _), (c@(Card v3 _)), (Card v4 _), (Card v5 _)] 
    | v5 == v3 = Just $ ThreeKind c
    | v2 == v4 = Just $ ThreeKind c
    | v1 == v3 = Just $ ThreeKind c
    | otherwise = Nothing

istwopair [(Card v1 _), (c2@(Card v2 _)), (Card v3 _), (c4@(Card v4 _)), (Card v5 _)] 
    | v1v2 && v3 == v4 = Just $ TwoPair c4 c2
    | v1v2 && v4v5 = Just $ TwoPair c4 c2
    | v2 == v3 && v4v5 = Just $ TwoPair c4 c2
    | otherwise = Nothing
    where
      v1v2 = v1 == v2
      v4v5 = v4 == v5

ispair [(Card v1 _), (c2@(Card v2 _)), (Card v3 _), (c4@(Card v4 _)), (Card v5 _)] 
    | v1 == v2 = Just $ Pair c2
    | v2 == v3 = Just $ Pair c2
    | v3 == v4 = Just $ Pair c4
    | v4 == v5 = Just $ Pair c4
    | otherwise = Nothing

highcard hs = Just $ Highcard $ head $ reverse hs

best hnd = h where
    hand = List.sort hnd
    -- highcard always returns Just something, so this pattern never fails.
    (Just h) = msum $ map ($ hand) [isroyalflush, isstraightflush, isfourkind, isfullhouse, isflush, isstraight, isthreekind, istwopair, ispair, highcard]

readhandline :: String -> (Hand, Hand)
readhandline s = (best p1, best p2)
  where
    (p1,p2) = splitAt 5 $ rhl s [] 
    rhl "" a = reverse a
    rhl "\r" a = reverse a -- dos file.
    rhl s a = rhl s'' (c:a)
        where
          [(c,s')] = reads s
          s'' = case s' of
                  [] -> s'
                  (' ':st) -> st
                  otherwise -> s'

main = do
  hndl <- openFile "poker.txt" ReadMode
  handpairs <- (liftM $ map readhandline . lines) $ hGetContents hndl
  print $ foldl (\a (p1,p2) -> if (compare p1 p2) == GT then a+1 else a) 0 handpairs

