# Weighted Random Numbers

Some time last year, I was asked the following question in a technical interview.

> Suppose you want create a utility that would help you decide on which restaurant you wanted to go to for lunch. You want you and your friends to be able to input some rankings for each restaurant, and then you want your system to spit out some random restaurant when queried, such that restaurants with higher ratings are more likely to be returned (proportional to their rating).

Given this problem statement, I assumed that they wanted me to design a data structure that supported the following operations:

```
insert(restaurant, rating)
query() -> returns random restaurant with likelihoods proportional to rating
```

This problem is very similar to another fairly common interview question (something like http://blog.gainlo.co/index.php/2016/11/11/uber-interview-question-weighted-random-numbers/), **except I was told that my ```add(restaurant, rating)``` operation should be able to support reassigning ratings to restaurants.**

During the interview, the solution I gave had either O(n) inserts and O(log n) queries, or O(1) inserts and O(n) queries. The 2 solutions above are really the same, and are very similar to the binary search on prefix array idea in the above link. The reason for O(n) insert time and O(log n) query time is that, if we support reassigning previously inserted restaurants, we need to recalculate prefix array, with the binary search query operation being unchaged. Alternatively, we can defer the calculation of the prefix array computation until we need it durng the query, making insertions O(1), but increasing query time to O(n).

Sadly, this solution of mine did not get me the job. I had searched the internet for a better solution to this problem, but oculdn't find one that had this extra constraint of being able to reassign ratings/weights.

However, after recently reattempting this problem, I think I have found a way to do this problem such that both inserts and queries are O(log n), while also needing no more than O(n) space.

The code in this repo is an implementation of the solution I came up with. The main idea of the solution is as follows. This code is neither the cleanest code, nor most well tested, and I *highly* doubly I'd be able to come up with this, or even recreate this code, in an interview setting.

Nonetheless, here is the basic idea of the data structure.

***

In order to solve this problem ,we could imagine assigning each restaurant a segment of the real number line of length proportional to its rating. Inserting would just be adding another segment at the end of where the current segments end. To query, we would generate a random number between 0 and total length of all the intervals, and see which interval it fell in, and return the restaurant that owned that interval.

The problem is that, wed have to either move around adjacent intervals, or having a gap in the number line/probabilty space( this solution would work, ie when we just try again with a diff random number if the removed segment was the one that was chosen. However, some pathological examples quickly show why this would be a bad idea.) whenever we reassigned a restaurant a new rating. This is the soruce of the problme of having to 'recompute' the prefix arrays in the above solutions.

A different approach is to consider a binary tree with the following structure.

- Leaf ndoes of the tree contain the (restaurant, rating) pairs, which we can think of as the intervals on the real numberline/probability space.
- Each non-leaf node contains the sum of the ratings in its sub tree.

Note that, the root would contain the sum total of all the ratings/intervals inserted.


If we had such a tree, querying would simply be generating a random number, and traversing down the tree until we reached a leaf node. Note that, in this representation, the interval in root.left contains the sum of all the intervals upto some number, and the intervals in root.right has the rest of the intervals. To see which interval corresponded to the generated random number, we would either traverse left or right, depending on whether the random number was less than the sum of the intervals in the left sub tree. We would recrusively traverse the tree til we hit a leaf node.

This would take O(log n), since a tree that has n leaf nodes has at most total ~2n total nodes (I think), so the depth of the tree would be O(log n).


Generating such a tree is simply adding leaf nodes to the tree such that we maintain the invariant that all the intermeidary nodes have the sum of intervals in its sub tree. Adding an interval/updating an existing one amounts to traversing to a leaf node, changing its value, and traversing back up to change any necessary intermeidary ndoes. Again, O(log n).

Instead of writing a lengthier bad explanation, Ill just refer you to the code. Hopefully that makes more sense.



