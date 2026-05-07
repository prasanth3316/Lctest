# 3986. Maximum Path Score in a Grid

🔗 [Open on LeetCode](https://leetcode.com/problems/maximum-path-score-in-a-grid/) | **Medium** | `Array` `Dynamic Programming` `Matrix`

---

## 📝 Problem Description

You are given an `m x n` grid where each cell contains one of the values 0, 1, or 2. You are also given an integer `k`.

You start from the top-left corner `(0, 0)` and want to reach the bottom-right corner `(m - 1, n - 1)` by moving only **right** or **down**.

Each cell contributes a specific score and incurs an associated cost, according to their cell values:

	
- 0: adds 0 to your score and costs 0.
	
- 1: adds 1 to your score and costs 1.
	
- 2: adds 2 to your score and costs 1. ​​​​​​​

Return the **maximum** score achievable without exceeding a total cost of `k`, or -1 if no valid path exists.

**Note:** If you reach the last cell but the total cost exceeds `k`, the path is invalid.

 

Example 1:

**Input:** grid = [[0, 1],[2, 0]], k = 1

**Output:** 2

**Explanation:**​​​​​​​

The optimal path is:

	
		
			Cell
			grid[i][j]
			Score
			Total

			Score
			Cost
			Total

			Cost
		
	
	
		
			(0, 0)
			0
			0
			0
			0
			0
		
		
			(1, 0)
			2
			2
			2
			1
			1
		
		
			(1, 1)
			0
			0
			2
			0
			1
		
	

Thus, the maximum possible score is 2.

Example 2:

**Input:** grid = [[0, 1],[1, 2]], k = 1

**Output:** -1

**Explanation:**

There is no path that reaches cell `(1, 1)`​​​​​​​ without exceeding cost k. Thus, the answer is -1.

 

**Constraints:**

	
- `1 <= m, n <= 200`
	
- `0 <= k <= 10^3​​​​​​​`
	
- `^​​​​​​​grid[0][0] == 0`
	
- `0 <= grid[i][j] <= 2`

## 💡 Hints

<details>
<summary>Show hints</summary>

1. Use dynamic programming.
2. Let <code>dp[i][j][c]</code> = max score at cell <code>(i,j)</code> with total cost exactly <code>c</code> (0 <= <code>c</code> <= <code>k</code>).
3. Update <code>dp[i][j][c]</code> from <code>(i-1,j)</code> and <code>(i,j-1)</code> using <code>cost = (grid[i][j] == 0 ? 0 : 1)</code> and <code>score = grid[i][j]</code>.
4. Answer = <code>max(dp[m-1][n-1][c])</code> for <code>c=0..k</code>, or <code>-1</code> if none.

</details>
