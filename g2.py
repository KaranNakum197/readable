import google.generativeai as genai

class HealthAssistant:
    def __init__(self, api_key):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("gemini-1.5-flash")

    def get_patient_data(self, patient_id):
        """Demo method – replace with your DB lookup"""
        demo_db = {
            1: {
                "risk_score": 78,
                "risk_level": "High",
                "contributing_factors": ["High cholesterol", "Diabetes", "Smoking"],
                "complications": ["Hypertension"],
                "age": 55,
                "gender": "Male"
            }
        }
        return demo_db.get(patient_id, None)

    def generate_prevention_advice(self, patient_id):
        """Generate personalized prevention advice using Gemini"""
        patient_data = self.get_patient_data(patient_id)
        
        if not patient_data:
            return "Patient not found in database."
        
        # Create prompt for Gemini
        prompt = f"""
        You are a helpful medical assistant providing lifestyle guidance.

        Patient details:
        - Risk of heart disease: {patient_data['risk_score']}/100 ({patient_data['risk_level']} risk)
        - Contributing factors: {', '.join(patient_data['contributing_factors'])}
        - Complications: {', '.join(patient_data['complications']) if patient_data['complications'] else 'None currently'}
        - Demographics: Age = {patient_data['age']}, Gender = {patient_data['gender']}

        Task:
        Create a personalized prevention plan for this patient. 
        The advice must be clear, practical, and safe for a general audience. 
        Focus on the main causes of risk first, then general heart health.

        Include:
        1. **Foods to Avoid** (specific to risk factors, e.g., cholesterol → fatty foods, diabetes → sugary foods)
        2. **Foods to Include** (give examples of everyday healthy options)
        3. **Exercise Recommendations** (consider age, fitness level, obesity if present)
        4. **Lifestyle Changes** (stress reduction, sleep, smoking/alcohol, monitoring)

        Format the response as a clean, patient-friendly guide with clear sections.
        """

        # Call Gemini
        response = self.model.generate_content(prompt)
        return response.text.strip()


# ---------------- DEMO ----------------
if __name__ == "__main__":
    assistant = HealthAssistant(api_key="AIzaSyAJQ9sxky15sn_ETAI3tV-oyH1hFrT9bVw")
    advice = assistant.generate_prevention_advice(1)
    print(advice)
