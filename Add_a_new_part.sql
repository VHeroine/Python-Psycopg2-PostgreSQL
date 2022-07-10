create or replace procedure add_new_part(new_part_name   varchar,
	                                     new_vendor_name varchar
                                         ) 
as $$
declare
    v_part_id     int;
    v_vendor_id   int;
begin

	-- Inserting data into the parts table.
	insert
	  into parts(part_name) 
	values(new_part_name) 
	returning part_id into v_part_id;
	
	-- Inserting a new vendor.
	insert
	  into vendors(vendor_name)
	values(new_vendor_name)
	returning vendor_id into v_vendor_id;
	
	-- Inserting data into vendor_parts.
	insert
	  into vendor_parts(part_id, vendor_id)
	values(v_part_id,v_vendor_id);

end;
$$
language plpgsql;