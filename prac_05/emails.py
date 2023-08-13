def extract_name(email):
    parts = email.split('@')
    name_parts = parts[0].split('.')
    name = ' '.join(name_parts).title()
    return name



