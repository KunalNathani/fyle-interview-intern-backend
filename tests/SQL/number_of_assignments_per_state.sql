-- Write query to get number of assignments for each state
SELECT state, count(state) FROM assignments GROUP BY state;