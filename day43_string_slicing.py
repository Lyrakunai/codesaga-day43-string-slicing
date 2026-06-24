# =====================================
# Day 43 - String Slicing
# =====================================


# Basic Slicing
word = "Python"
print(word[1:4])      # yth
print(word[:3])       # Pyt
print(word[2:])       # thon


# Full Slice
print(word[:])        # Python


# Length Formula
# end - start
employee_id = "EMP45821HR"
print(employee_id[3:8])   # 45821
# 8 - 3 = 5 characters


# Empty Slice Cases
print(word[3:3])      # ''
print(word[5:2])      # ''


# Out-of-Range Slicing
print(word[0:100])    # Python
print(word[4:100])    # on
print(word[-100:100]) # Python


# Indexing vs Slicing
print(word[2])        # t
print(word[2:3])      # t



# Negative Slicing
print(word[-3:])      # hon
print(word[:-2])      # Pyth
print(word[-4:-1])    # tho


# Positive + Negative Mix
print(word[1:-1])     # ytho


# Empty Slice With
# Positive + Negative Mix
print(word[3:-3])     # ''


# Real World Examples

# Username
username = "naina_2026"
print(username[:5])   # naina


# Email
email = "naina@gmail.com"
print(email[:5])      # naina
print(email[6:])      # gmail.com


# Employee ID
employee = "EMP45821HR"
print(employee[3:8])  # 45821


# Bank Account
account = "ACC9988776655"
print(account[-4:])   # 6655


# Website Preview
text = "ArtificialIntelligence"
print(text[:10])      # Artificial


# Chocolate Practice
choco = "Chocolate"
print(choco[3:7])     # cola
print(choco[5:9])     # late