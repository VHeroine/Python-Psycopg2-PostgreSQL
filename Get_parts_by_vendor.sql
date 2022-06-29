create or replace function get_parts_by_vendor(id integer)
returns table(part_id integer, part_name varchar) as
$$
begin

return query

select parts.part_id,
       parts.part_name
  from parts

  join vendor_parts
    on vendor_parts.part_id = parts.part_id

 where vendor_id = id;

end;
$$

language plpgsql;