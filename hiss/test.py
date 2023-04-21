import yaml

with open("../dataset/example/metadata/0001TP_006690.yml", "r") as f:
    data= yaml.safe_load(f)
print(data)
medical_history = data["patient_information"]["medical_history"]

print(medical_history, medical_history)
for m in medical_history:
    print(m)