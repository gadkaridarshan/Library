def bmi_formula(mass: float, height: float):
    """
    Calculate BMI based on the formula BMI(kg/m2) = mass(kg) / height(m)2
    :param mass: mass for BMI calculation
    ":param height: height for BMI calculation
    :return:
    """

    if height is None or height == 0:
        return None
    else:
        return mass / ((height/100) ** 2)