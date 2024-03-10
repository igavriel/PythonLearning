import psycopg2

class UrlService:
    def __init__(self):
        self.connection = psycopg2.connect(
            host="localhost",
            database="tinyurl",
            user="postgres",
            password="password"
        )
        self.cursor = self.connection.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS urls (
                id SERIAL PRIMARY KEY,
                original_url TEXT NOT NULL,
                short_url TEXT NOT NULL UNIQUE
            )
        """)
        self.connection.commit()

    def create_url(self, original_url):
        short_url = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        self.cursor.execute("INSERT INTO urls (original_url, short_url) VALUES (%s, %s)", (original_url, short_url))
        self.connection.commit()
        return Url(original_url, short_url)

    def get_url_by_short_url(self, short_url):
        self.cursor.execute("SELECT original_url FROM urls WHERE short_url = %s", (short_url,))
        row = self.cursor.fetchone()
        if row is not None:
            return Url(row[0], short_url)
        else:
            return None
