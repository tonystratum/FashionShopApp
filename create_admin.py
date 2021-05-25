from fashionshop import bcrypt, db
from fashionshop.models import User
from utils import query_to_dict

# Enter the admin credentials below.
# This user will be able to access the admin panel.

USERNAME = "admin"
EMAIL = "admin@shop.com"
PASSWORD = "QRvZPBN99yEs4Ci"

admin_query = f"""select id from "user" where username = '{USERNAME}' fetch first row only;"""
if not any(query_to_dict(db, admin_query)):
    db.session.add(
        User(
            username=USERNAME,
            email=EMAIL,
            password=bcrypt.generate_password_hash(PASSWORD).decode('utf-8'),
            admin=True
        )
    )
    db.session.commit()
    print("Admin user created successfully!")
else:
    print("Admin user is already present.")
