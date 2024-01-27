def calculate_fuel_efficiency(distance, fuel_consumed):
    distance = float(distance)
    fuel_consumed = float(fuel_consumed)

    if distance <= 0 or fuel_consumed <= 0:
        return "Distance and fuel consumed must be positive numbers."

    fuel_efficiency = distance / fuel_consumed
    return fuel_efficiency

def main():
    print("Fuel Efficiency Calculator")

    # Get user input for distance and fuel consumption
    distance = input("Enter the distance traveled (in miles): ")
    fuel_consumed = input("Enter the amount of fuel consumed (in gallons): ")

    # Calculate fuel efficiency
    result = calculate_fuel_efficiency(distance, fuel_consumed)

    # Display the result
    if isinstance(result, float):
        print(f"Fuel efficiency: {result:.2f} miles per gallon (MPG)")
    else:
        print(f"Error: {result}")

if __name__ == "__main__":
    main()