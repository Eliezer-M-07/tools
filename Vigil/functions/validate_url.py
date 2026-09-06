from urllib.parse import urlparse

def validate_url(url):
    
    result = urlparse(url)
    
    if result.scheme in ('http', 'https') and result.netloc:
        return True
    else:
        return False
