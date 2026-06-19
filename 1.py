# str = """g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."""

# K -> M : K + 2
# O -> Q : O + 2
# E -> G : E + 2
str = "map"

parsed_str = """"""

for ch in str:
    if ch in {" "}:
        parsed_str += " "
        continue
    parsed_str += chr(97 + (ord(ch)- 95)%26)

"""i hope you didnt translate it by handd thats what computers are ford doing it in by hand is inefficient and thatws why this text is so longd using stringdmaketransxy is recommendedd now apply on the urld"""
print(parsed_str)
# Next One ->ocr