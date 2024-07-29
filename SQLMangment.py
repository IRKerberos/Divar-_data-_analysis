import mysql.connector


def create_database(db_name, table_name):
    conn = mysql.connector.connect(user='root', password='',
                                  host='127.0.0.1',
                                  database=db_name)

    cursor = conn.cursor()

    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")

    conn.close()

    conn = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='',
        database=db_name
    )

    cursor = conn.cursor()

    create_table_query = f'''
    CREATE TABLE IF NOT EXISTS {table_name} (
        id INT AUTO_INCREMENT PRIMARY KEY,
        brand_type VARCHAR(255),
        fuel_type VARCHAR(255),
        engine_status VARCHAR(255),
        front_chassis VARCHAR(255),
        rear_chassis VARCHAR(255),
        body_status VARCHAR(255),
        insurance_deadline INT,
        gearbox VARCHAR(255),
        base_price INT,
        mileage INT,
        model_year INT,
        color VARCHAR(255),
        location VARCHAR(255),
        url VARCHAR(255) UNIQUE
    );
    '''

    cursor.execute(create_table_query)

    conn.commit()
    conn.close()


def add_record(db_name, table_name, brand_type, fuel_type, engine_status, front_chassis, rear_chassis, body_status,
               insurance_deadline, gearbox, base_price, mileage, model_year, color, location, url):
    conn = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='',
        database=db_name
    )

    cursor = conn.cursor()

    check_query = f"SELECT COUNT(*) FROM {table_name} WHERE url = %s"
    cursor.execute(check_query, (url,))
    result = cursor.fetchone()

    if result[0] > 0:
        pass
    else:
        insert_query = f'''
        INSERT INTO {table_name} (brand_type, fuel_type, engine_status, front_chassis, rear_chassis, body_status, insurance_deadline, gearbox, base_price, mileage, model_year, color, location, url)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
        '''

        cursor.execute(insert_query, (
            brand_type, fuel_type, engine_status, front_chassis, rear_chassis, body_status, insurance_deadline, gearbox,
            base_price, mileage, model_year, color, location, url))

        conn.commit()

    conn.close()