def calculate_emission_reductions(BE_y, PE_y, LE_y):
    """
    Calculate the emission reductions for a solar cooker project.

    Parameters:
    - BE_y: Baseline emissions in year y (tCO2).
    - PE_y: Project emissions in year y (tCO2).
    - LE_y: Leakage in year y (tCO2).

    Returns:
    - Emission reductions in year y (tCO2).
    """
    ER_y = BE_y - PE_y - LE_y
    return ER_y

# Example usage
BE_y = 100  # Example baseline emissions in tCO2 for the year
PE_y = 5    # Example project emissions in tCO2 for the year
LE_y = 1    # Example leakage in tCO2 for the year

# Calculate emission reductions
emission_reductions = calculate_emission_reductions(BE_y, PE_y, LE_y)
print(f"Emission Reductions: {emission_reductions} tCO2/year")
