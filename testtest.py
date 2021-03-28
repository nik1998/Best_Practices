
if __name__ == "__main__":
    flag = "VrnCTF{Ge1ald_gr5at_adv5n1ur2r0}".encode()
    bbb = int.from_bytes(flag, "little")
    cdd = 276794517999693338085844729161533548917
    print(cdd^bbb)
    st = (cdd^bbb).to_bytes(32, byteorder='little')
    print(st)

