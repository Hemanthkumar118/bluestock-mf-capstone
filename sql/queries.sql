-- Top 5 funds by AUM
SELECT scheme_name, aum_crore
FROM 07_scheme_performance_clean
ORDER BY aum_crore DESC
LIMIT 5;

-- Average NAV
SELECT AVG(nav)
FROM 02_nav_history_clean;

-- Top SIP inflow categories
SELECT category, SUM(monthly_sip_amount)
FROM 04_monthly_sip_inflows_clean
GROUP BY category;

-- Expense ratio below 1%
SELECT scheme_name, expense_ratio_pct
FROM 07_scheme_performance_clean
WHERE expense_ratio_pct < 1;

-- Highest Sharpe Ratio
SELECT scheme_name, sharpe_ratio
FROM 07_scheme_performance_clean
ORDER BY sharpe_ratio DESC
LIMIT 10;