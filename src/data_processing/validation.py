"""
Data validation functions.
"""


# Example function to implement:
def validate_isbn(isbn):
    """Validate ISBN-13 format."""
    isbn = str(isbn)
    isbn = isbn.replace("-","")
#    isbntxt = isbntxt.replace("-","")
#    try:
#        int(isbn)
#        print("pass: " + isbntxt)
#        if len(a) == 13
#        return True
#        else
#            return False
#    except:
#        print("fail: " + str(isbn))      
#        return False
    if len(isbn) == 13:
        return True
    else:
        print("Fail: " + isbn)
        return False


#    return True
