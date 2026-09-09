SELECT
    research_status,
    COUNT(*) AS assumption_count
FROM bladepulse.assumption_registry
GROUP BY research_status
ORDER BY research_status;