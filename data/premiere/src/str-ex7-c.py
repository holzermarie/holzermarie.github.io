# FONCTIONS
def est_numerique(car):
    pt_code = ord(car)
    if pt_code >= 48 and pt_code <= 57:
        return True
    return False

def est_numerique(car):
    return ord(car) >= 48 and ord(car) <=57

# SCRIPT
# TESTS
assert not est_numerique("k")
assert est_numerique("4")

# res1 = est_numerique("k")
# print(res1)
# res2 = est_numerique("4")
# print(res2)