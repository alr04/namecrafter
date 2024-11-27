from django.shortcuts import render
from .forms import NameForm


# Top 100 baby boy names in the US for 2022
boy_names = [
    "Liam", "Noah", "Oliver", "James", "Elijah", "William", "Henry", "Lucas", "Benjamin", "Theodore",
    "Mateo", "Levi", "Sebastian", "Daniel", "Jack", "Michael", "Alexander", "Owen", "Asher", "Samuel",
    "Ethan", "Leo", "Jackson", "Mason", "Ezra", "John", "Hudson", "Luca", "Aiden", "Joseph",
    "David", "Jacob", "Logan", "Luke", "Julian", "Gabriel", "Grayson", "Wyatt", "Matthew", "Maverick",
    "Dylan", "Isaac", "Elias", "Anthony", "Thomas", "Jayden", "Carter", "Santiago", "Ezekiel", "Charles",
    "Josiah", "Caleb", "Cooper", "Lincoln", "Miles", "Christopher", "Nathan", "Isaiah", "Kai", "Joshua",
    "Andrew", "Angel", "Adrian", "Cameron", "Nolan", "Waylon", "Jaxon", "Roman", "Eli", "Wesley",
    "Aaron", "Ian", "Christian", "Ryan", "Leonardo", "Brooks", "Axel", "Walker", "Jonathan", "Easton",
    "Everett", "Weston", "Bennett", "Robert", "Jameson", "Landon", "Silas", "Jose", "Beau", "Micah",
    "Colton", "Jordan", "Jeremiah", "Parker", "Greyson", "Rowan", "Adam", "Nicholas", "Theo", "Xavier"
]

# Top 100 baby girl names in the US for 2022
girl_names = [
    "Olivia", "Emma", "Charlotte", "Amelia", "Sophia", "Isabella", "Ava", "Mia", "Evelyn", "Luna",
    "Harper", "Camila", "Sofia", "Scarlett", "Elizabeth", "Eleanor", "Emily", "Chloe", "Mila", "Violet",
    "Penelope", "Gianna", "Aria", "Abigail", "Ella", "Avery", "Hazel", "Nora", "Layla", "Lily",
    "Aurora", "Nova", "Ellie", "Madison", "Grace", "Isla", "Willow", "Zoe", "Riley", "Stella",
    "Eliana", "Ivy", "Victoria", "Emilia", "Zoey", "Naomi", "Hannah", "Lucy", "Elena", "Lillian",
    "Maya", "Leah", "Paisley", "Addison", "Natalie", "Valentina", "Everly", "Delilah", "Leilani", "Madelyn",
    "Kinsley", "Ruby", "Sophie", "Alice", "Genesis", "Claire", "Audrey", "Sadie", "Aaliyah", "Josephine",
    "Autumn", "Brooklyn", "Quinn", "Kennedy", "Cora", "Savannah", "Caroline", "Athena", "Natalia", "Hailey",
    "Aubrey", "Emery", "Anna", "Iris", "Bella", "Eloise", "Skylar", "Jade", "Gabriella", "Ariana",
    "Maria", "Adeline", "Lydia", "Sarah", "Nevaeh", "Serenity", "Liliana", "Ayla", "Everleigh", "Raelynn"
]



def calculate_all_combinations(last_name):
    results = []
    for first_name in boy_names:
        full_name = f"{first_name} {last_name}"
        numerology_number, life_path_description = calculate_numerology(full_name)
        results.append({
            "full_name": full_name,
            "numerology_number": numerology_number,
            "life_path": life_path_description
        })


    for first_name in girl_names:
        full_name = f"{first_name} {last_name}"
        numerology_number, life_path_description = calculate_numerology(full_name)
        results.append({
            "full_name": full_name,
            "numerology_number": numerology_number,
            "life_path": life_path_description
        })
    return results




##____________________________________________________________________________________________________


def calculate_numerology(name):
    """Calculates the numerology number and life path based on the name."""

    def name_to_number(name):
        """Converts a name to its numerology number."""
        numerology_map = {
            'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9,
            'J': 1, 'K': 2, 'L': 3, 'M': 4, 'N': 5, 'O': 6, 'P': 7, 'Q': 8, 'R': 9,
            'S': 1, 'T': 2, 'U': 3, 'V': 4, 'W': 5, 'X': 6, 'Y': 7, 'Z': 8
        }

        name = name.strip().upper()
        num_sum = sum(numerology_map[char] for char in name if char in numerology_map)

        while num_sum > 9 and num_sum not in [11, 22, 33]:
            num_sum = sum(int(digit) for digit in str(num_sum))

        return num_sum

    def get_life_path(num_sum):
        """Retrieves the life path description based on the numerology number."""
        life_paths = {
            1: "Leadership, independence, and a pioneering spirit.",
            2: "Diplomacy, peace, and partnerships are key.",
            3: "Creativity, self-expression, and joy in life.",
            4: "Stability, hard work, and strong foundations.",
            5: "Adventure, freedom, and adaptability.",
            6: "Responsibility, nurturing, and family-oriented.",
            7: "Spirituality, introspection, and a love for knowledge.",
            8: "Ambition, power, and financial success.",
            9: "Humanitarianism, compassion, and a focus on the greater good.",
            11: "Vision, inspiration, and enlightenment as a master number.",
            22: "Master builder, achieving large-scale dreams and ideas.",
            33: "Master teacher, devotion, and a focus on selfless service."
        }
        return life_paths.get(num_sum, "Unknown life path number")

    # Call the functions to calculate numerology and life path
    numerology_number = name_to_number(name)
    life_path_description = get_life_path(numerology_number)

    return numerology_number, life_path_description









def name_input(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            name = full_name = f"{first_name} {last_name}"
            #name = form.cleaned_data['name']
            numerology_number, life_path_description = calculate_numerology(name)
            return render(request, 'numerology/numerology_result.html', {
                'numerology_number': numerology_number,
                'life_path': life_path_description,
                'first_name': first_name,
                'last_name': last_name
            })
    else:
        form = NameForm()
    return render(request, 'numerology/name_input.html', {
        'form': form,
        'boy_names': boy_names,
        'girl_names': girl_names,})
    










def numerology_result(request):
    # Retrieve results from the session
    numerology_number = request.session.get('numerology_number', None)
    life_path_description = request.session.get('life_path_description', None)

    if not numerology_number or not life_path_description:
        return render(request, 'numerology/numerology_error.html', {'error': 'No results found. Please calculate your numerology first.'})

    return render(request, 'numerology/numerology_result.html', {
        'numerology_number': numerology_number,
        'life_path': life_path_description
    })

##___________________________________________________________________________________________


    