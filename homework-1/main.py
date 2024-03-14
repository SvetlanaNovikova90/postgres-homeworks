"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv

import psycopg2


def get_customers_data():
    with psycopg2.connect(host='localhost',
                          database='north',
                          user='postgres',
                          password='1101') as conn:
        with conn.cursor() as cur:
            with open('./north_data/customers_data.csv', encoding='utf-8') as file_customers:
                reader = csv.DictReader(file_customers)
                for row in reader:
                    cur.execute('INSERT INTO customers VALUES (%s, %s, %s)',
                                (row['customer_id'], row['company_name'], row['contact_name']))
    conn.close()


def get_employees_data():
    with psycopg2.connect(host='localhost',
                          database='north',
                          user='postgres',
                          password='1101') as conn:
        with conn.cursor() as cur:
            with open('./north_data/employees_data.csv', encoding='utf-8') as file_employees:
                reader = csv.DictReader(file_employees)
                for row in reader:
                    cur.execute('INSERT INTO employers VALUES (%s, %s, %s, %s, %s, %s)',
                                (row['employee_id'],
                                 row['first_name'],
                                 row['last_name'],
                                 row['title'],
                                 row['birth_date'],
                                 row['notes'],
                                 ))
    conn.close()


def get_orders_data():
    with psycopg2.connect(host='localhost',
                          database='north',
                          user='postgres',
                          password='1101') as conn:
        with conn.cursor() as cur:
            with open('./north_data/orders_data.csv', encoding='utf-8') as file_orders:
                reader = csv.DictReader(file_orders)
                for row in reader:
                    cur.execute('INSERT INTO orders VALUES (%s, %s, %s, %s, %s)',
                                (row['order_id'],
                                 row['customer_id'],
                                 row['employee_id'],
                                 row['order_date'],
                                 row['ship_city']
                                 ))
    conn.close()


if __name__ == '__main__':
    get_employees_data()
    get_customers_data()
    get_orders_data()
