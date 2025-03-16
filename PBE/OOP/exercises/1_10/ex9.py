class Patient():
    def __init__(self, patient_name, patient_age, consultation_history : list):
        self.name = patient_name
        self.age = patient_age
        self.consult_hist = consultation_history

    def new_consultation(self, consult_date : str, consult_doctor : str):
        self.consult_hist.append(
            {
                'date': consult_date,
                'doctor': consult_doctor
            })

    def __str__(self):
        consultations = "\n".join(
            [f"Date: {consult['date']}, Doctor: {consult['doctor']}" for consult in self.consult_hist]
        )
        print(self.consult_hist)
        return f"{self.name} patient attended the following consultations:\n{consultations}"

        
patient1 = Patient('Rafael', 17, [
    {
    'date': '01/01/25',
    'doctor': 'Leafar'

    },
    {
    'date': '02/02/25',
    'doctor': 'Godofredo'
    }
])

patient1.new_consultation('03/03/25', 'Alfredo')
print(patient1)
