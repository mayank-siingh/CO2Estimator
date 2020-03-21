import typing

# The data gives the value for co2 emitted in case of petrol and diesel in gm/litre
co2_gasoline = 2347.698
co2_diesel = 2689.273

# defining the function for evaluating the co2 emitted
def co2Emitted(carType : str,mileage : float,distance : float) -> float:
    # Here the code 
    # goes which 
    # evaluates the co2 emitted
    # taking 3 parameters i.e 
    # 1. carType : 'petrol' or 'diesel'
    # 2. mileage : of car/vehicle(in km/litres)
    # 3. distance : to be travelled during the journey(in kms.)
