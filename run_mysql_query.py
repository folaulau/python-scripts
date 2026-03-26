import mysql.connector
from sshtunnel import SSHTunnelForwarder

# SSH and MySQL Configuration
SSH_HOST = "ops-nvirginia.datappraise.com"  # SSH bastion host (jump server)
SSH_PORT = 22  # Default SSH port
SSH_USER = "dbuser"  # SSH user
SSH_KEY_FILE = "/Users/folaukaveinga/Datappraise/server_ssh_key"  # Private key file for authentication

RDS_HOST = "vbdb-ro.datappraise.com"  # Your AWS RDS MySQL endpoint
RDS_PORT = 3306  # Default MySQL port
DB_USER = "fkaveinga"
DB_PASSWORD = "y5t5LhAM22&4K*g"
DB_NAME = "VPANational"

# Establish SSH Tunnel
try:
    with SSHTunnelForwarder(
        (SSH_HOST, SSH_PORT),
        ssh_username=SSH_USER,
        ssh_pkey=SSH_KEY_FILE,
        remote_bind_address=(RDS_HOST, RDS_PORT),
        local_bind_address=('127.0.0.1', 3307)  # Local port to bind the tunnel
    ) as tunnel:

        print("SSH Tunnel established.")

        # Connect to MySQL through the tunnel
        connection = mysql.connector.connect(
            host="127.0.0.1",
            port=3307,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )

        print("Connected to MySQL.")

        # Execute Query
        cursor = connection.cursor()
        cursor.execute("SELECT NOW();")  # Example query to check the current time
        result = cursor.fetchone()
        print("Current time from DB:", result[0])

        # Close connection
        cursor.close()
        connection.close()
        print("Connection closed.")

except Exception as e:
    print("Error:", str(e))
