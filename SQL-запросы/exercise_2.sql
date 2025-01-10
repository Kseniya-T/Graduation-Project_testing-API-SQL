SELECT track,
	CASE
		WHEN "cancelled"=true THEN '-1'
		WHEN "finished"=true THEN '2'
		WHEN "inDelivery"=true THEN '1'
		ELSE '0'
	END as status
FROM "Orders";