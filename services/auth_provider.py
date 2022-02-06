def authenticate(email, password):
    if email == 'admin@admin.com' and password == 'bad_password':
        return {
            'username': 'admin',
            'email': 'admin@admin.com',
            'roles': ['admin', 'user']
        }
    else:
        return False