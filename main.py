import json
import os
class Healthcare:
    def __init__(self,organization,phone_number,email, employess_cnt_all, employess_cnt_rightnow):
        self._organization = organization
        self.__phone_number = phone_number
        self.__email = email
        self.__employess_cnt_all = employess_cnt_all
        self.__employess_cnt_rightnow = employess_cnt_rightnow
        if self.__employess_cnt_all <= 0:
            raise ValueError ("Не может быть количество всех сотрудников в организации быть меньше или равно 0!")
    def communication_with_organization(self):
        print(f"Телефон: {self.phone_number}  Почта для связи {self.email}")
    def absent_employees(self):
        print(f"Сегодня отсутсвует {self.__employess_cnt_all - self.__employess_cnt_rightnow} сотрудников")
def SetHealhtcare():
    organization = input("Введите название организации: ")
    phone_number = input("Введите номер телефона: ")
    email = input("Введите почту: ")
    employess_cnt_all = input("Введите общее количество сотрудников: ")
    employess_cnt_rightnow = input("Введите количество сотрудников на данным момент: ")
    all_health = Healthcare(organization, phone_number, email, int(employess_cnt_all), int(employess_cnt_rightnow))
    return all_health
class Doctor(Healthcare):
    def __init__(self, experience, educations, speciality,availability):
        self.__experience = experience
        self.__educations = educations
        self.__speciality = speciality
        self.__availability = availability
    def check_availability(self):
        if self.__availability == "Yes":
            print("The doctor is free!")
def SetDoctor():
    experience = input("Введите опыт врача(в годах): ")
    educations = input("Введите образование(я) врача: ")
    speciality = input("Введите специальность врача: ")
    availability = input("Врач свободен? Введите Да или нет: ")
    all_doctor = Doctor(experience, educations, speciality, availability)
    return all_doctor
class Patient(Healthcare):
    def __init__(self, age, height, weight, temperature):
        self.__age = age
        self.__height = height
        self.__weight = weight
        self.__temperature = temperature
    def high_temperature(self):
        if self.__temperature > 36.6:
            print(f" У пациента повышенная температура! А именно: {self.__temperature}")
def SetPatient():
    age = input("Введите опыт врача(в годах): ")
    height = input("Введите образование(я) врача: ")
    weight = input("Введите специальность врача: ")
    temperature = input("Врач свободен? Введите Да или нет: ")
    all_patient = Patient(age, height, weight, temperature)
    return all_patient
def readAnyFiles(filePath):
    fileName, fileExtension = os.path.splitext(filePath)
    #json
    if fileExtension == ".json":
        try:
            with open(filePath, 'r') as f:
                lines = f.readlines()
                for fileLine in lines:
                    dict_obj = json.loads(fileLine)
                    print(dict_obj)
        except FileNotFoundError:
            print("Wrong file path while reading file:", filePath)
# если расширение файла не поддерживается
    else:
        print("Unsupported file extension:", fileExtension)
def write_to_json(obj, filePath):
    # проверка на правильность пути файла
    try:
        with open(filePath, "a") as file_stream:
            json.dump(obj.__dict__, file_stream)
            #добавляем разделение для красивой записи в файл
            file_stream.write('\n')
    except FileNotFoundError:
        print("Wrong file path while writing json:", filePath)

Patient1 = Patient(18, 177, 65, 37.2)
Doctor1 = Doctor(22, 'MGU', 'Surgeon', 'Yes')
Patient2 = Patient(65, 165, 74, 36.6)
write_to_json(Patient1, "laba1test.json")
write_to_json(Doctor1, "laba1test.json")
write_to_json(Patient2, "laba1test.json")
readAnyFiles("laba1test.json")
