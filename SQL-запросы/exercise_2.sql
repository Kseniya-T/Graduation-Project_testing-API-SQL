SELECT cancelled, finished, "inDelivery",
	CASE
		WHEN "cancelled"=true THEN '-1'
		WHEN "finished"=true THEN '2'
		WHEN "inDelivery"=true THEN '1'
		ELSE '0'
	END
FROM "Orders";