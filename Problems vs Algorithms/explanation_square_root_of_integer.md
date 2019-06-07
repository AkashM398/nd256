### Code Design

I implemented my solution using iterative binary search algorithm. I am setting the `end_number` to be half the input number to reduce the search space for the algorithm. The square root of a number is lesser than half the number. If the input number is 0 or 1, the algorithm terminates early by returning the number.

### Efficiency

##### Time complexity

- It takes logarithmic time to get the result; O(log n)

##### Space Complexity

- The space taken by my solution is not affected by the input; O(1)
