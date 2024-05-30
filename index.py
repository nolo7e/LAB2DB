#! C:/Users/ivano/AppData/Local/Programs/Python/Python38-32/python.exe
import mysql.connector
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs

class RequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        post_params = parse_qs(post_data)

        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='Observatory'
        )

        cursor = connection.cursor()
        sql_insert = "INSERT INTO Sector (coordinates, light_intensity, foreign_objects, star_objects_count, unknown_objects_count, defined_objects_count, notes) VALUES (%s, 3.4, 5, 30, 2, 28, %s)"
        insert_data = (post_params[b'col1'][0].decode('utf-8'), 'Новый сектор')
        cursor.execute(sql_insert, insert_data)
        connection.commit()

        print('Done. Hint: ' + sql_insert)

    def do_GET(self):
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='Observatory'
        )

        cursor = connection.cursor()
        sql_select = 'EXEC JoinTables \'Sector\', \'NaturalObjects\''
        cursor.execute(sql_select)
        results = cursor.fetchall()

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        self.wfile.write('<tr>'.encode())
        for key in cursor.column_names:
            self.wfile.write(('<th>' + key + '</th>').encode())
        self.wfile.write('</tr>'.encode())

        for row in results:
            self.wfile.write('<tr>'.encode())
            for value in row:
                self.wfile.write(('<td>' + str(value) + '</td>').encode())
            self.wfile.write('</tr>'.encode())

        cursor.close()
        connection.close()

server = HTTPServer(('127.0.0.1', 80), RequestHandler)
print('Server running at http://127.0.0.1:80/')
server.serve_forever()