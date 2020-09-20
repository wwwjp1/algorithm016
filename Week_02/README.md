### 第二周作业题
##### 有效的字母异位词
- 1.数组模拟hashmap，将ASCII码作为index，count作为value存入数组中。

```py
    # hashmap
    slist, tlist = [0] *26, [0]* 26
    for i in s:
        slist[ord(i) - ord("a")] += 1
    for j in t:
        tlist[ord(j) - ord("a")] += 1
    return slist == tlist
```
- 2.dict, 思路一样, 也可以只用一个dict，遍历s时++，t时--
```py
    #dict
    dic_s, dict_t = {}, {}
    for i in s: dic_s[i] = dic_s.get(i, 0) + 1
    for i in s: dic_t[i] = dic_t.get(i, 0) + 1
    return dic_s == dict_t
```

##### 两数之和
- 1.暴力遍历 O(n**2)
```py
    for i in range(len(nums)-1):
        for j in range(len(nums)):
            if nums[i]+nums[j]==target:
                return [i, j]
```
- 2.hashset,存放nums[i]，如果target-nums[i]在hashset中，则返回[i, target-nums[i]]
```py
    hashset = {}
    for i in range(len(nums)):
        if hashset.get(target-nums[i]) is not None: return [i, target-nums[i]]
        hashset[nums[i]] = i
```
- 3.sorted array，双端指针，夹逼遍历，因为返回index，所以需要新数组
```py
        temp = nums.copy()
        temp.sort()
        l = 0
        r = len(nums) - 1
        while l < r:
            res = temp[l] + temp[r]
            if  res < target:
                l += 1
            elif res > target:
                r -= 1
            else:
                break
        fir = nums.index(temp[l])
        nums.pop(fir)
        sec = nums.index(temp[r])
        if fir <= sec:
            sec += 1
        return [fir, sec]
```

##### N叉树的前序遍历
```py
        # 1.recursion
        res = []
        def helper(root):
            if root:
                res.append(root.val)
                for i in root.children:
                    helper(i)
        helper(root)
        return res

        # 2.stack
        res = []
        stack = [root]
        while stack:
            cur = stack.pop()
            if cur:
                res.append(cur.val)
                stack.extend(cur.children[::-1])
        return res
```

##### 字母异位词分组
- 1.hashtable, 将sorted的str作为key，将str加入其value 列表中。
- 2.tuple的写法。
```py
        # 1.
        hashtable = {}
        for item in sorted(strs):
            sortedStr = "".join(sorted(item))
            hashtable[sortedStr] = hashtable.get(sortedStr, []) + [item]
        return [*hashtable.values()]
        
        # 2.
        ht = {}
        for item in sorted(strs):
            key = tuple(sorted(item))
            ht[key] = ht.get(key, []) + [item]
        return [*ht.values()]
```

##### 二叉树的中序遍历
```py
        # 1.recursion
        res = []
        def helper(root):
            if root:
                if root.left:
                    helper(root.left)
                res.append(root.val)
                if root.right:
                    helper(root.right)
        helper(root)
        return res

        # 2.stack
        stack, res = [], []
        curr = root
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right
        return res
```

##### 二叉树的前序遍历
```py
        # 1. recursion
        ans = []
        def helper(curr):
            if curr:
                ans.append(curr.val)
                if curr.left: helper(curr.left)
                if curr.right: helper(curr.right)
        helper(root)
        return ans

        # 2.stack 
        stack = []
        ans = []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                ans.append(curr.val)
                curr = curr.left
            curr = stack.pop()
            curr = curr.right
        return ans
```

##### N叉树的层序遍历
- 1.bfs,用queue实现，模板。循环遍历当前queue，循环结束后level中是每一层的结点值。
```py
# bfs
        queue = collections.deque([root])
        res = []
        while queue:
            level = []
            size = len(queue)
            for _ in range(size):
                curr = queue.popleft()
                if curr:
                    level.append(curr.val)
                    queue.extend(curr.children)
            if level: res.append(level)
        return res
```

- 2.dfs，level作为参数传递，控制结点值加入对应的res的level list中就行。
```py
        # dfs
        def helper(root, level):
            if not root: return []
            if len(res) == level: res.append([])
            res[level].append(root.val)
            for child in root.children: helper(child, level + 1)
        res = []
        helper(root, level=0)
        return res
```

##### 前K个高频元素
- 1.dict + sort
```py
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # dic = Counter(nums)
        dic = {}
        for item in nums:
            dic[item] = dic.get(item, 0) + 1
        res = sorted(dic.items(), key=lambda item:item[1], reverse=True)
        return list(map(lambda item: item[0], res))[:k]
```
- 2.利用大顶堆,这里使用python的heapq
```py
        dic = Counter(nums)
        queue, res = [], []
        for key in dic:
            heapq.heappush(queue, (-dic[key], key))
        for i in range(k):
            res.append(heapq.heapqpop()[1])
        return res
```

##### 丑数 不会做, 抄题解
- 动态规划。主要是：丑数=较小丑数*因子(2,3,5),且是离下一个丑数最近的丑数。
```py
    dp, a, b, c = [1] * n, 0, 0, 0
    for i in range(1, n):
        n2, n3, n5 = dp[a]*2, dp[b]*3, dp[c]*5
        dp[i] = min(n2, n3, n5)
        if dp[i] == n2: a += 1
        if dp[i] == n3: b += 1
        if dp[i] == n5: c += 1
    return dp[-1]
```