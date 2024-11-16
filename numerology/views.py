from django.shortcuts import render
from .forms import NameForm


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
            name = form.cleaned_data['name']
            numerology_number, life_path_description = calculate_numerology(name)
            return render(request, 'numerology/numerology_result.html', {'numerology_number': numerology_number, 'life_path': life_path_description})
    else:
        form = NameForm()
    return render(request, 'numerology/name_input.html', {'form': form})

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