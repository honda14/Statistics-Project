def mean(data):
    return sum(data) / len(data)

def median(data):
    data = sorted(data)
    n = len(data)
    if n % 2 == 1:
        return data[n // 2]
    else:
        return (data[n // 2 - 1] + data[n // 2]) / 2

def mode(data):
    freq = {}
    for num in data:
        freq[num] = freq.get(num, 0) + 1
    max_count = max(freq.values())
    modes = [k for k, v in freq.items() if v == max_count]
    if len(modes) == len(freq):
        return "No mode"
    return modes

def data_range(data):
    return max(data) - min(data)

def mid_range(data):
    return (max(data) + min(data)) / 2

def mean_absolute_deviation(data):
    m = mean(data)
    return sum(abs(x - m) for x in data) / len(data)

def variance_population(data):
    m = mean(data)
    return sum((x - m) ** 2 for x in data) / len(data)

def variance_sample(data):
    m = mean(data)
    return sum((x - m) ** 2 for x in data) / (len(data) - 1)

def std_dev_population(data):
    return variance_population(data) ** 0.5

def std_dev_sample(data):
    return variance_sample(data) ** 0.5

def coef_variance_population(data):
    return (std_dev_population(data) / mean(data)) * 100

def coef_variance_sample(data):
    return (std_dev_sample(data) / mean(data)) * 100

def get_data():
    raw = input("Enter numbers separated by space: ")
    return [float(x) for x in raw.strip().split()]

options = {
    "1": ("Mean", mean),
    "2": ("Median", median),
    "3": ("Mode", mode),
    "4": ("Range", data_range),
    "5": ("Mid-Range", mid_range),
    "6": ("Mean Absolute Deviation", mean_absolute_deviation),
    "7": ("Population Variance", variance_population),
    "8": ("Sample Variance", variance_sample),
    "9": ("Population Standard Deviation", std_dev_population),
    "10": ("Sample Standard Deviation", std_dev_sample),
    "11": ("Coefficient of Variation (Population)", coef_variance_population),
    "12": ("Coefficient of Variation (Sample)", coef_variance_sample)
}

while True:
    print("\nSelect an operation:")
    for k, v in options.items():
        print(f"{k}. {v[0]}")

    while True:

        choice = input("Enter operation number: ").strip().capitalize()
    
        if choice in options:
            data = get_data()
            result = options[choice][1](data)
            print("Result:", result)
            break
        else:
            print("Invalid choice, try again.")
    
    again = input("\nDo you want to perform another operation? (y/n): ").strip().capitalize()
    if again == 'No' or again == 'N':
        break