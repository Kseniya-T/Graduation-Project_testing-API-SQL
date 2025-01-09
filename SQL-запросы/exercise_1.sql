SELECT login, count("inDelivery")
FROM "Orders" AS o
JOIN "Couriers" AS c ON o."courierId"=c.id
WHERE "inDelivery"=true
GROUP BY login;