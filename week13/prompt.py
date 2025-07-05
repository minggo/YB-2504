from together import Together

client = Together(api_key="a9e50c7d4d75cd6dbc4a71375ec02312810def94f45242f0dd1d65665ae237a4")

def get_user_input(prompt, default=None):
    user_input = input(f"{prompt}" + (f" (default: {default})" if default else "") + ": ").strip()
    return user_input if user_input else default

def get_list_input(prompt):
    raw = input(f"{prompt}(seperate with ,): ").strip()
    return [item.strip() for item in raw.split(",") if item.strip()]

def build_travel_request_from_cli():
    print("📍 Let's plan your New Zealand trip!\nPlease answer the following questions:\n")

    travel_request = {}

    travel_request["group_type"] = get_user_input("What is the group type? (e.g. family, couple, solo, friends)", "family")
    members = get_list_input("Enter group profile (e.g. 2 adults, 1 child)")
    travel_request["group_profile"] = members
    travel_request["has_kids"] = any("child" in member.lower() for member in members)

    travel_request["city"] = get_user_input("Which city are you visiting?", "Rotorua")
    travel_request["season"] = get_user_input("What season? (e.g. summer, winter)", "summer")
    travel_request["duration"] = int(get_user_input("How many days is your trip?", "3"))
    travel_request["budget"] = get_user_input("Budget level? (low, mid, high)", "mid")
    travel_request["interests"] = get_list_input("List your interests (e.g. nature, food, adventure)")
    travel_request["transport_mode"] = get_user_input("Mode of transport? (e.g. self-drive, public transport)", "self-drive")
    travel_request["language"] = get_user_input("Preferred language?", "English")

    return travel_request

def get_user_input(prompt, default=None):
    user_input = input(f"{prompt}" + (f" (default: {default})" if default else "") + ": ").strip()
    return user_input if user_input else default

def get_list_input(prompt):
    raw = input(f"{prompt}(separte with ,): ").strip()
    return [item.strip() for item in raw.split(",") if item.strip()]

def build_travel_request_from_cli():
    print("📍 Let's plan your New Zealand trip!\nPlease answer the following questions:\n")

    travel_request = {}

    travel_request["group_type"] = get_user_input("What is the group type? (e.g. family, couple, solo, friends)", "family")
    members = get_list_input("Enter group profile (e.g. 2 adults, 1 child)")
    travel_request["group_profile"] = members
    travel_request["has_kids"] = any("child" in member.lower() for member in members)

    travel_request["city"] = get_user_input("Which city are you visiting?", "Rotorua")
    travel_request["season"] = get_user_input("What season? (e.g. summer, winter)", "summer")
    travel_request["duration"] = int(get_user_input("How many days is your trip?", "3"))
    travel_request["budget"] = get_user_input("Budget level? (low, mid, high)", "mid")
    travel_request["interests"] = get_list_input("List your interests (e.g. nature, food, adventure)")
    travel_request["transport_mode"] = get_user_input("Mode of transport? (e.g. self-drive, public transport)", "self-drive")
    travel_request["language"] = get_user_input("Preferred language?", "English")

    return travel_request

def build_prompt(travel_request: dict) -> str:
    group_type = travel_request["group_type"]
    group_profile = ", ".join(travel_request["group_profile"])
    city = travel_request["city"]
    season = travel_request["season"]
    duration = travel_request["duration"]
    budget = travel_request["budget"]
    interests = ", ".join(travel_request["interests"])
    transport = travel_request.get("transport_mode", "not specified")
    language = travel_request.get("language", "English")

    prompt = f"""You are a local travel planner in New Zealand. Please create a travel itinerary based on the following information:

- Group type: {group_type}
- Group members: {group_profile}
- Destination: {city}
- Season: {season}
- Duration: {duration} days
- Budget: {budget}-range
- Travel interests: {interests}
- Transportation: {transport}
- Language: {language}

Please provide a day-by-day itinerary that includes activities suitable for the group, recommended attractions, dining suggestions, and practical tips related to the season and destination.
"""
    return prompt


def build_chat_bot(content):
    response = client.chat.completions.create(
        model="meta-llama/Llama-3.3-70B-Instruct-Turbo-Free",
        messages=[
        {
            "role": "user",
            "content": content
        }
        ],
        temperature=0.7,
        max_tokens=2000
    )
    print(response.choices[0].message.content)

if __name__ == "__main__":
    travel_request = build_travel_request_from_cli()
    prompt = build_prompt(travel_request)
    build_chat_bot(prompt)
