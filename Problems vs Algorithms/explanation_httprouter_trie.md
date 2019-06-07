### Code Design

I implemented a class called `RouteTrieNode` whose `children` value is a _defaultdict_ of the same class, simplifying the insert operation on `RouteTrie`. For the lookup operation, I hardcoded a check for the root route ("/") since it would get skipped in `split_path()` hence never added by its value to the trie. The `RouteTrie.root` node comes to rescue in resolving to the "root handler".

### Efficiency

##### Time complexity

- It takes linear time to insert routes; O(n)
- It takes linear time to find routes; O(n)

##### Space Complexity

- The space taken by my solution increases proportionally to the number of routes; O(n)
