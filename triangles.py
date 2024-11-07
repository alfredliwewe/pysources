def calculate_area_of_triangle(base, height):
    result = 1/2 * base * height
    return result # float


def calculate_area_of_rectangle(length, width):
    result = length * width
    return result

def calculate_area_of_trapezium(length,height):
    trapz_area = (length + height) / 2
    return trapz_area


area_trapz = calculate_area_of_trapezium(16,20)
print("Area of trapezium: ")
print(area_trapz)


area_triangle_n12 = calculate_area_of_triangle(40,24)
print("We are now calculating area of triangle at point n12")
print(area_triangle_n12)

sum_of_areas = area_trapz + area_triangle_n12
print("Apapa taphatikiza ma areas ")
print(sum_of_areas)