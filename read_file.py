def load_medicines(filename):
    medicines = []
    try:
        with open(filename, 'r') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                parts = [p.strip() for p in line.split(',')]
                if len(parts) != 6:
                    print(f"Warning: Invalid line format (skipped): {line}")
                    continue
                try:
                    med = {
                        'name': parts[0],
                        'brand': parts[1],
                        'stock': int(parts[2]),
                        'rate_tablet': float(parts[3]),
                        'rate_strip': float(parts[4]),
                        'tablets_per_strip': int(parts[5])
                    }
                    medicines.append(med)
                except ValueError:
                    print(f"Warning: Invalid numerical data (skipped): {line}")
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        from write_file import create_sample_file
        create_sample_file(filename)
        return load_medicines(filename)
    return medicines
