def read_csv(filename):
    data = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        lines = in_file.readlines()
        for line in lines:
            columns = line.strip().split(',')
            data.append(columns)
    return data


def get_champions(data):
    champions = {}
    for row in data[1:]:
        name = row[1]
        if name in champions:
            champions[name] += 1
        else:
            champions[name] = 1
    return champions


def get_countries(data):
    countries = set()
    for row in data[1:]:
        country = row[2]
        countries.add(country)
    return countries


def main():
    filename = "wimbledon.csv"
    data = read_csv(filename)

    champions = get_champions(data)
    countries = get_countries(data)

    print("Wimbledon Champions:")
    for champion, wins in champions.items():
        print(f"{champion} {wins}")

    sorted_countries = sorted(countries)
    countries_str = ", ".join(sorted_countries)
    print("\nThese", len(countries), "countries have won Wimbledon:")
    print(countries_str)


if __name__ == "__main__":
    main()
