CREATE OR REPLACE FUNCTION NthHighestSalary (n INT)
RETURNS TABLE (salary INT)
AS $$
BEGIN
    IF n < 1 THEN
        RETURN;
    END IF;

    RETURN QUERY
        SELECT DISTINCT e.salary
        FROM   Employee AS e
        ORDER  BY e.salary DESC
        LIMIT  1
        OFFSET n - 1;
END;
$$ LANGUAGE plpgsql;