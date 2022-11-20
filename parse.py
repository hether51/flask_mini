# import csv

# with open('names.csv','r') as cvs_file:
#     csv_reader = csv.DictReader(cvs_file)

#     with open('new_names.csv','w') as new_file:
#         fieldnames = ['first_name','second_name']

#         csv_writer = csv.DictWriter(new_file,fieldnames=fieldnames,delimiter='\t')
#         csv_writer.writeheader()
#         for line in csv_reader:
#             del line['email']
#             csv_writer(line)
    

import jwt
import datetime,time

token = jwt.encode({"email":"woojamwtj@163.com",\
        "exp":datetime.datetime.now(tz=datetime.timezone.utc)+datetime.timedelta(seconds=3)},\
        "fake_sec",algorithm="HS256")

print(type(token),token)

de_token = jwt.decode(token,"fake_sec",algorithms=["HS256"])

print(de_token)

time.sleep(4)

try:
    de_token = None
    de_token = jwt.decode(token,"fake_sec",algorithms=["HS256"])
except jwt.ExpiredSignatureError:
    pass


if de_token:
    print(de_token)
else:
    print("out of time")



