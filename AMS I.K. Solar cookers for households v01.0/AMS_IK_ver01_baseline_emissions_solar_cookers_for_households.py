def calculate_emission_reductions(BE, PE):
    """
    Calculate the emission reductions from a solar cooker project.

    Parameters:
    - BE: Baseline emissions in tCO2 for the year.
    - PE: Project emissions in tCO2 for the year.

    Returns:
    - Emission reductions in tCO2 for the year.
    """
    return BE - PE

# Example usage
BE = 100  # Baseline emissions in tCO2/year from previous calculation
PE = 5    # Project emissions in tCO2/year, assuming minimal operational emissions

# Calculate emission reductions
emission_reductions = calculate_emission_reductions(BE, PE)
print(f"Emission Reductions: {emission_reductions} tCO2/year")

