def calculate_project_emissions(N_k0, n_ky, FC_PJkj, NCV_j, EF_FFj):
    """
    Calculate the project emissions for solar cooker projects.

    Parameters:
    - N_k0: Dictionary mapping each household type or cluster (k) to the number of households provided with solar cookers.
    - n_ky: Dictionary mapping each household type or cluster (k) to the proportion of households where solar cookers are operational.
    - FC_PJkj: Nested dictionary mapping each household type or cluster (k) to each type of project fuel (j) and its annual consumption.
    - NCV_j: Dictionary mapping each type of project fuel (j) to its net calorific value (GJ/mass or volume unit).
    - EF_FFj: Dictionary mapping each type of project fuel (j) to its CO2 emission factor (tCO2/GJ).

    Returns:
    - Total project emissions in tCO2 for the year.
    """
    total_project_emissions = 0
    for k, households in N_k0.items():
        operational_households = households * n_ky.get(k, 1) # Default to 1 if not specified
        for j, consumption in FC_PJkj.get(k, {}).items():
            emissions = operational_households * consumption * NCV_j[j] * EF_FFj[j]
            total_project_emissions += emissions
    return total_project_emissions

# Example usage
N_k0 = {'type1': 100}  # Example: 100 households of type1
n_ky = {'type1': 0.95}  # Example: 95% of type1 households use the solar cooker
FC_PJkj = {'type1': {'LPG': 2}}  # Example: 2 units of LPG consumed annually per household in project scenario
NCV_j = {'LPG': 0.025}  # Example: Net calorific value of LPG
EF_FFj = {'LPG': 0.056}  # Example: Emission factor of LPG

# Calculate project emissions
project_emissions = calculate_project_emissions(N_k0, n_ky, FC_PJkj, NCV_j, EF_FFj)
print(f"Project Emissions: {project_emissions} tCO2/year")
