# Team Members: [Adam Guerrero]
# Course: CS151, Prof. Mehri
# Date: [Sep 27, 2021]
# Programming Assignment: 1

# Program Inputs: [length, width, and height of a room in feet]
# Program Outputs: [total area to be painted in Square feet and amount of paint needed in gallons]
# Input - Ask for Length,Width,Height of the Room Via Feet
# calculate Lth(Length)
# calculate Wth(Width)
# calculate Hght(Height)

# Length(sq ft) * Width(sq ft) * Height(ft) = Volume of figure

# Volume of wall (sq ft) = Length(Sq ft) * Height(Sq ft)
# Volume of wall (sq ft) = Length(Sq ft) * Height(Sq ft)
# Volume of wall (sq ft) = Width(Sq ft) * Height(Sq ft)
# Volume of wall (sq ft) = Width(Sq ft) * Height(Sq ft)

# 15 - 18 Add all together = Area of all 4 walls

# Length(Sq Ft) * Width(Sq Ft) = Area of Ceiling

# Area of Ceiling(Sq Ft) + Area of all 4 walls(Sq Ft) = Total Area that needs to be Paint/Primed

# Find How much primer is needed
# 1 Gallon of Primer = 200 Sq ft

# Find How much paint is needed
# 1 Gallon of Paint = 350 Sq Ft

user_input = input("Enter the number of Width of Figure in Sq ft to find Wall Areas and Ceiling Area: ")
user_input = input("Enter the number of Height of Figure in Sq ft to find Wall Areas and Ceiling Area: ")
user_input = input("Enter the number of Length of Figure in Sq ft to find Wall Areas and Ceiling Area: ")
Width = float(user_input)
Height = float(user_input)
Length = float(user_input)

# calculate 2 sides of wall  (Sq Ft)

Area_of_Wall = (Length * Height) * 2

# Calculate 2 sides of the wall (Sq ft)
Area_of_Wall = (Width * Height) * 2

# Calculate ceiling Area (Sq ft)
Area_of_Ceiling = (Length * Width)

# Calculate Area to paint
Area_To_Paint = (Area_of_Ceiling + Area_of_Wall)

print("Area to be painted ", Area_To_Paint, "Sq ft")
# Calculate Area to paint in primer
Primer_Needed = (Area_To_Paint / 200)
print("Primer needed to paint ", Primer_Needed, "Gal")
Paint_Needed = (Area_To_Paint / 350)
print("Paint needed to paint", Paint_Needed, "Gal")