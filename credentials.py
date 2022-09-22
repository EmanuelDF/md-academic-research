# TWITTER API CREDENTIALS
BEARER_TOKEN = "<YOUR_BEARER_TOKEN>" # Your Twitter Bearer Token Credential string

# DATABASE LOCATION AND CREDENTIALS
db_user = "root"  # Caution: same user can't write in multiple DB, use an exclusive user
db_password = "mysql"
host = "localhost:3306"  # Localhost if local DB, or ip to external. Can use Amazon RDS.
db_name = "twitter"
db_table = "nome_social"  # If table doesn't exists, will create. If Exist, will append