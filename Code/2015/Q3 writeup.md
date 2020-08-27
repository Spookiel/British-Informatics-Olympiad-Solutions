## Q3 - Modern Art

In this problem, we need to work out the **nth** term in the sequence.

##### The example sequence is

```
1 ->  ABBC
2 ->  ABCB
3 ->  ACBB
4 ->  BABC
5 ->  BACB
6 ->  BBAC
7 ->  BBCA
8 ->  BCAB
9 ->  BCBA
10 -> CABB
11 -> CBAB
12 -> CBBA
```

#### How to approach problems like this?

The main way to approach a problem like this is to find some way to reduce the number of terms we need to check before finding the answer. 

Let's first find a way to work out the total number of terms for a given input.
For the input `1 2 1 0 8`, we interpret that as 1 A, 2 Bs and 1 C.

###The maths 

To help gain an understanding of the maths that can be used to work out the total number of terms, let's first look at what is the case if we have one of each letter.

```
1 letter -> A -> 1 term
2 letters -> AB, BA -> 2 terms
3 letters -> ABC, ACB, BAC, BCA, CAB, CBA -> 6 terms
```

It becomes clear that when you only have one of each letter, you can work out the number of terms by just taking `factorial(number of letters)`.

####Why is this the case?

Think of the term as *n* blank spaces - *n* being the total number of letters.

**(e.g 4 letters,    _ _ _ _ )**

Let's start by thinking about how many choices of letter we have for each blank space.

The first gap is easy, we have `4` letters, and any one of them can go there.

Now we have three letters left, and there are `3` choices left for that one

Then `2` choices left for the second last gap

Finally there is `1` choice left for the last gap.

#####Putting it together

This means there are `4*3*2*1 = 24` total terms.

[Here](https://www.mathplanet.com/education/algebra-2/discrete-mathematics-and-probability/permutations-and-combinations) is a link explaining permutations and combinations in more detail.

Our algorithm will work like this

1. For each gap, work out how many terms start with an A,B,C,D
2. If we find more terms start with an A than the current index we are looking for, then we know our answer must be A _ _ _
3. If there are less terms starting with an A than the current index then we try B, then C, and finally D
4. We repeat this process for each gap, which builds up the answer step by step

#####Here's an example:

Let's say we have 1 A, 1 B, 1 C, 1 D and our target is 10

Our current answer is `""` - empty

We first check how many terms match A _ _ _. In this case it's `3*2*1 = 6`.

`6 is less than 10`, so we know if there are only 6 terms that start with an `A`, then the 10th term can't start with an `A`.

Now we can rule out the first 6 terms, so effectively we are searching for the 4th term now.

Here's an easy way to visualise this:

```
1 ->  ABCD
2 ->  ABDC
3 ->  ACBD
4 ->  ACDB
5 ->  ADBC
6 ->  ADCB
```
We cut out the first 6 terms, so the 7th-12th terms effectively become
```
1 ->  BACD
2 ->  BADC
3 ->  BCAD
4 ->  BCDA
5 ->  BDAC
6 ->  BDCA
```

Next we check how many terms start with a `B`. It's 6 (`3*2*1`)

This is greater than 4 (the 4th term in the new list is what we're searching for), so we know our answer starts with B _ _ _ .

Now we check how many terms start with BA _ _. The answer is `2`.

This is less than 4, so we subtract.

We are now searching for the *2nd* term. 

Now we check how many terms start with BC _ _. The answer is `2`

This is equal to the term we are searching for so we don't subtract. Instead we restart from `A`.

Now we search for the number of terms starting with BCA _. The answer is just `1`.

This is less than `2`, so we subtract.

We are now searching for how many terms start with BCD _. Again, just `1`.

We now only have one letter left to choose from, so we know that the final letter must be  `A`.

Therefore the 10th term is `BCDA`.







