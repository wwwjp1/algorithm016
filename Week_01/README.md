学习笔记
1.两数之和
    方法1：暴力遍历，两层循环，找到nums[i]+nums[j]==target，返回[i,j]。时间复杂度O(n**2)
    方法2：hashset，遍历一次，如果{}中有key target- nums[i],则返回对应value,否则nums[i]:i存入hashset中。O（n)
    方法3：双端指针，sorted list的夹逼遍历，因为要返回indices，所以需要一个新数组。在通过python的index方法或者自己遍历，找到原nums中对应的index，假设为first和second，得到first之后需要将其在原nums中pop，以防止重复值出现无法index到正确second，之后若second>first, second++得到正确index。

21.合并两个有序链表
    方法1：递归，将头指针指向的结点的较小值与剩余的部分相连，头指针后移，继续递归。
    方法2：遍历，通过遍历完成上面的递归过程，需要preHead作为头节点，指向第一个结点作为记录，用于最后返回头结点。previous用于将每次的较小值结点与剩余部分链接，previous需要每次后移。

26.删除排序数组中的重复项
    双指针，快慢指针，慢指针i init=0,快指针j init=1，比较nums[i]和nums[j]，若不相等，则nums[++i] = nums[j]。

66.加一
    略

88.合并两个有序数组
    从尾部开始遍历，将较小值放在m+n-1 index中，由于nums1空间足够。m--或n--，同时m+n-1 --

189.旋转数组
    1.暴力法，每次前移一个数字，O（n**k），注意前移一次的写法。
        previous = nums[-1]
        for i in range(len(nums)):
            previous, nums[i] = nums[i], previous
    2.new array, loop nums i --> (i+k) % len(nums)
    3.3 times reverse
        first, reverse全部
        second，reverse前k个
        third，reverse后n-k个
        reverse是O(logn)的，可以双端指针,交换位置，指针--

283.move zero
    1.双指针，慢指针记录0位置
    2.count+loop，count 0的数量，非零数前移count位

641.设计循环双端队列
    pass
    看代码，注意是循环的。
    需要两个指针记录头部插入位置和尾部插入位置，front和rear
    attention:  1. 这里 init front=k-1， rear=0 # 反过来了
                2. 循环的front和rear更新：
                    头插入,删除：front=(front-1)%k，front=(front+1)%k
                    尾插入,删除：rear=(rear+1)%k，rear=(rear-1)%k
