# Use_Api_Nozomi
Mediante un script en python lanzamos peticiones web a la api de las sondas de nozomi. 
Utilizando las siguientes querys:
- Nodos aprendidos -> query=nodes | group_by is_learned | sort is_learned | select is_learned count
- Nodos No complentamente aprendidos -> query=nodes | where is_learned == true and  is_fully_learned == false  | count
- Links No completamente aprendidos -> query=links | where is_learned == true  and is_fully_learned == false  | count
- Links aprendidos -> query=links | group_by is_learned | sort is_learned | select is_learned count
- Numero de alertas creadas  en las ultimas 24h -> query=alerts | where hours_ago(time) < 24 | sort time | select id type_id appliance_host time
- Numero de nodos creados -> query=nodes | where days_ago(created_at) < 1
