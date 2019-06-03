from faker import Faker
import pandas

fake = Faker()
fakeRU = Faker('ru_RU')
fakeGR = Faker('el_GR')
fakeCN = Faker('zh_CN')

data_dict = {
                "name_EN": [],
                "name_RU": [],
                "name_GR": [],
                "name_CN": [],
                "iban": [],
                "ssn": [],\
                "binary": [],
                "password": []
            }

for x in range(5):
    data_dict["name_EN"].append(fake.first_name())
    data_dict["name_RU"].append(fakeRU.first_name())
    data_dict["name_GR"].append(fakeGR.first_name())
    data_dict["name_CN"].append(fakeCN.first_name())
    data_dict["iban"].append(fake.iban())
    data_dict["ssn"].append(fake.ssn(taxpayer_identification_number_type="SSN"))
    data_dict["binary"].append(fake.binary(length=4))
    data_dict["password"].append(fake.password(length=10,
                                                special_chars=True,
                                                digits=True,
                                                upper_case=True,
                                                lower_case=True))

output = pandas.DataFrame(data_dict)
# file = open("test_data.txt","w")
# file.write(output)
# file.close()
#output.to_csv("output.csv", index=False, header=True)

print(output)
