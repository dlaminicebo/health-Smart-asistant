import streamlit as st

# ---- AGENTS ----

# Step 1: User Proxy Agent
def user_proxy_agent():
    st.header("👤 User Proxy Agent")
    st.write("Please enter your health information:")

    weight = st.number_input("Weight (kg)", min_value=30.0, max_value=200.0)
    height = st.number_input("Height (cm)", min_value=100.0, max_value=250.0)
    age = st.number_input("Age", min_value=10, max_value=100)
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    dietary_pref = st.selectbox("Dietary Preference", ["Veg", "Non Veg", "Vegan"])

    if st.button("Submit"):
        user_data = {
            "weight": weight,
            "height": height,
            "age": age,
            "gender": gender,
            "dietary_pref": dietary_pref,
        }
        st.session_state["user_data"] = user_data
        st.success("User data collected! Proceeding to BMI Agent...")

# Step 2: BMI Tool + BMI Agent
def bmi_agent(user_data):
    st.header("📏 BMI Agent")
    height_m = user_data["height"] / 100
    bmi = user_data["weight"] / (height_m ** 2)
    bmi = round(bmi, 2)

    if bmi < 18.5:
        category = "Underweight"
        recommendation = "Increase calorie intake. Consider strength training."
    elif 18.5 <= bmi < 24.9:
        category = "Normal"
        recommendation = "Maintain your current lifestyle and diet."
    elif 25 <= bmi < 29.9:
        category = "Overweight"
        recommendation = "Incorporate more physical activity and a balanced diet."
    else:
        category = "Obese"
        recommendation = "Consult a doctor. Follow a strict diet and exercise plan."

    st.write(f"**Your BMI:** {bmi} ({category})")
    st.write(f"**Health Recommendation:** {recommendation}")

    return {"bmi": bmi, "category": category, "recommendation": recommendation}

# Step 3: Diet Planner Agent
def diet_planner_agent(user_data, bmi_data):
    st.header("🥗 Diet Planner Agent")
    preference = user_data["dietary_pref"]

    st.write(f"Diet Preference: {preference}")
    st.write("Here is a suggested meal plan:")

    if preference == "Veg":
        meal_plan = ["Breakfast: Oats with fruits", "Lunch: Dal, roti, sabzi", "Dinner: Paneer curry with rice"]
    elif preference == "Non Veg":
        meal_plan = ["Breakfast: Eggs and toast", "Lunch: Grilled chicken and salad", "Dinner: Fish curry and rice"]
    else:
        meal_plan = ["Breakfast: Almond milk smoothie", "Lunch: Vegan bowl with quinoa", "Dinner: Tofu stir-fry"]

    for meal in meal_plan:
        st.markdown(f"- {meal}")

# Step 4: Workout Scheduler Agent
def workout_scheduler_agent(user_data, bmi_data):
    st.header("🏋️ Workout Scheduler Agent")
    age = user_data["age"]
    gender = user_data["gender"]
    category = bmi_data["category"]

    st.write("Here is your weekly workout plan:")

    if category == "Underweight":
        plan = ["Day 1: Strength Training", "Day 2: Yoga", "Day 3: Rest", "Day 4: Core Exercises", "Day 5: Strength Training"]
    elif category == "Normal":
        plan = ["Day 1: Cardio + Strength", "Day 2: Yoga", "Day 3: Rest", "Day 4: Full Body Workout", "Day 5: Walking + Core"]
    elif category == "Overweight":
        plan = ["Day 1: Walking + Light Cardio", "Day 2: Yoga", "Day 3: Walking", "Day 4: Strength (low impact)", "Day 5: Swimming or Cycling"]
    else:
        plan = ["Day 1: Walking", "Day 2: Chair Exercises", "Day 3: Rest", "Day 4: Stretching", "Day 5: Light Yoga"]

    for day in plan:
        st.markdown(f"- {day}")

# ---- STREAMLIT APP LOGIC ----

st.set_page_config(page_title="Smart Health Assistant", layout="centered")

st.title("🤖 Smart Health Assistant")

if "user_data" not in st.session_state:
    user_proxy_agent()
else:
    user_data = st.session_state["user_data"]
    bmi_data = bmi_agent(user_data)
    diet_planner_agent(user_data, bmi_data)
    workout_scheduler_agent(user_data, bmi_data)
