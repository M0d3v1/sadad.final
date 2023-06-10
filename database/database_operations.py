import sqlite3

def create_table():
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()

    query = '''
    CREATE TABLE IF NOT EXISTS news (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        content TEXT,
        category TEXT,
        created_at TEXT
    )
    '''
    cursor.execute(query)

    conn.commit()
    conn.close()

def insert_data(title, content, category, created_at):
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()

    query = "INSERT INTO news (title, content, category, created_at) VALUES (?, ?, ?, ?)"
    cursor.execute(query, (title, content, category, created_at))

    conn.commit()
    conn.close()

def main():
    create_table()

    insert_data('New Smartphone Launches', 'Tech company XYZ announces the launch of their latest smartphone with advanced features.', 'Tech', '2023-06-10 10:00:00')
    insert_data('Artificial Intelligence Breakthrough', 'Researchers develop a new AI algorithm that outperforms human experts in medical diagnosis.', 'Tech', '2023-06-09 14:30:00')
    insert_data('Tech Company Acquires Startup', 'Tech giant ABC acquires a promising startup specializing in virtual reality technology.', 'Tech', '2023-06-08 09:45:00')
    insert_data('New Operating System Release', 'Operating system XYZ releases its latest version, introducing improved security features and enhanced user experience.', 'Tech', '2023-06-07 16:20:00')
    insert_data('Robotics Advancements', 'Researchers make significant progress in robotics with the development of a humanoid robot capable of performing complex tasks.', 'Tech', '2023-06-06 11:15:00')
    insert_data('Cybersecurity Threats on the Rise', 'Experts warn about the increasing number of cybersecurity threats targeting individuals and organizations.', 'Tech', '2023-06-05 17:55:00')
    insert_data('New Breakthrough in Quantum Computing', 'Scientists achieve a major breakthrough in quantum computing, paving the way for faster and more powerful computers.', 'Tech', '2023-06-04 08:10:00')
    insert_data('Latest Gadgets Unveiled at Tech Expo', 'Tech enthusiasts gather at the annual Tech Expo to witness the unveiling of the latest gadgets and innovations.', 'Tech', '2023-06-03 13:40:00')
    insert_data('Social Media Platform Surpasses One Billion Users', 'Popular social media platform XYZ celebrates reaching one billion active users worldwide.', 'Tech', '2023-06-02 10:25:00')
    insert_data('Advancements in Renewable Energy', 'Scientists develop a breakthrough in renewable energy technology, making clean energy more accessible and efficient.', 'Tech', '2023-06-01 15:50:00')

if __name__ == '__main__':
    main()
