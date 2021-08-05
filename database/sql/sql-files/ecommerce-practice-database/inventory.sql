create table if not exists item (
    created_at      timestamp           default current_timestamp,
    updated_at      timestamp           default current_timestamp,
	item_id		    uuid primary key default uuid_generate_v4(),
	inventory_id   	uuid,
	item_name		varchar(25)			not null unique,
	item_description varchar(255)		not null unique,
	price 			double precision	not null,
	image			bytea
);

create table if not exists inventory (
	created_at      timestamp       default current_timestamp,
	updated_at      timestamp       default current_timestamp,
	inventory_id	uuid primary key default uuid_generate_v4(),
	item_id			uuid,
	item_name       varchar(25),
	quantity		smallint		not null
);

alter table inventory
    add foreign key (item_id) references item(item_id);

alter table inventory
    add foreign key (item_name) references item(item_name);

alter table item
    add foreign key (inventory_id) references inventory(inventory_id);

do $$
declare
    ret_item_id uuid;
    ret_inventory_id uuid;
	ret_item_name varchar(25);
begin
    insert into item (item_name, item_description, price)
    values ('iPad', '2023 Model', 399.99)
    returning item_id, item_name into ret_item_id, ret_item_name;

    insert into inventory (item_id, item_name, quantity)
    values (ret_item_id, ret_item_name, 39)
    returning inventory_id into ret_inventory_id;
    
    update item set inventory_id = ret_inventory_id where item_id = ret_item_id;
end $$;