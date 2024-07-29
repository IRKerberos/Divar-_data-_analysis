import sqlite3

def create_database(db_name, table_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    create_table_query = f'''
    CREATE TABLE IF NOT EXISTS {table_name} (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        brand_type TEXT,
        fuel_type TEXT,
        engine_status TEXT,
        front_chassis TEXT,
        rear_chassis TEXT,
        body_status TEXT,
        insurance_deadline INTEGER,
        gearbox TEXT,
        base_price INTEGER,
        mileage INTEGER,
        model_year INTEGER,
        color TEXT,
        location TEXT,
        url TEXT UNIQUE
    );
    '''

    cursor.execute(create_table_query)
    conn.commit()
    conn.close()

def add_record(db_name, table_name, brand_type, fuel_type, engine_status, front_chassis, rear_chassis, body_status,
               insurance_deadline, gearbox, base_price, mileage, model_year, color, location, url):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    check_query = f"SELECT COUNT(*) FROM {table_name} WHERE url = ?"
    cursor.execute(check_query, (url,))
    result = cursor.fetchone()

    if result[0] > 0:
        pass
    else:
        insert_query = f'''
        INSERT INTO {table_name} (brand_type, fuel_type, engine_status, front_chassis, rear_chassis, body_status, insurance_deadline, gearbox, base_price, mileage, model_year, color, location, url)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
        '''

        cursor.execute(insert_query, (
            brand_type, fuel_type, engine_status, front_chassis, rear_chassis, body_status, insurance_deadline, gearbox,
            base_price, mileage, model_year, color, location, url))

        conn.commit()

    conn.close()
