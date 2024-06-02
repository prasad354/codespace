def calculate_energy(mass):
    # Energy (Joules) = mass (kg) * speed of light squared (m^2/s^2)
    speed_of_light_squared = (299792458) ** 2
    energy = mass * speed_of_light_squared
    return energy

def main():
    # Prompt the user for mass in kilograms
    mass_kg = int(input("Enter mass in kilograms: "))
    
    # Calculate the energy in Joules
    energy_joules = calculate_energy(mass_kg)
    
    # Output the result
    print("Equivalent energy in Joules:", energy_joules)

# Call the main function to execute the program
if __name__ == "__main__":
    main()
