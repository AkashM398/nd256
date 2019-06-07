### Code Design

I implemented my solution to get the suffixed words by iterating through the trie getting characters in the suffix. Then recursing over children nodes to get the rest of the characters in possible words.

### Efficiency

##### Time complexity

- It takes quadratic time to reach the last character in suffix; O(n²)
- It takes linear time to recurse through each child to get the remaining characters; O(n)

##### Space Complexity

- The space taken by my solution increases proportionally to the input; O(n)
