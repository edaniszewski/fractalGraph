###################################################
#
#	Author	:	Erick Daniszewski
#	Date	:	15 May 2014
#	Name	:	fractalGraph.py
#	Summary	:	computes and plots a fractal graph
#	as described by Mandelbrot in "a fractal walk 
#	down wall street"
#
###################################################


from __future__ import division 	# This will allow us to do floating point division (// is integer division now)
import matplotlib.pyplot as plt 	# Import pyplot so we can make cool graphs


#######################################
##		Variable Definitions
#######################################

# set the number of fractal iterations ( when n > 3, things slow down A LOT.)
n = 3

# an array of color options for the different lines (letter corresponds to color, - corresponds to line type)
colors = ['g-', 'r-', 'y-', 'm-', 'c-', 'k-', 'w-']

# Initial x-coordinates -- these need to be in increasing order to plot correctly
initx = [0, 1, 2, 3, 4, 5]
# Initial y-coordinates
inity = [0, 3, 2, 4, 3, 5]

# Sort the y values in increasing order so you can find the range
sortedY = sorted(inity)

# The domain should be the distance between the largest and smallest x
initDomain = initx[-1] - initx[0]
# The range should be the distance between the largest and smallest y
initRange = sortedY[-1] - sortedY[0]


#######################################
##		Fractal Logic
#######################################




# Handle the case where the coordinate arrays are of different size
if len(initx) != len(inity):
	print "The two coordinate arrays are of different size"
	exit(0)

# Plot the initial graph -- this shape will be our fractal template
plt.plot(initx, inity, 'b-')


# Iterate the fractal by the number n, specified earlier
for j in range(n):

	# Initialize arrays to hold the x and y coordinates of the current iteration
	newx = []
	newy = []

	# Go iterate through every element of the initial array
	for i in range(len(initx)-1):
		# Get the domain between the current element and the next element
		currentDomain = initx[i+1] - initx[i]
		# Get the range between the current element and the next element
		currentRange = inity[i+1] - inity[i]

		# Since we want a scalar multiplier to apply to our points, make it
		# the ratio between the domain/range just found and the domain/range
		# of our initial graph (since that is essentially our fractal template)
		domainScale = currentDomain / initDomain
		rangeScale = currentRange / initRange

		# Apply the scaling factor to each x coordinate in the initial array in order 
		# to create a new set of points between the current and next element of the initial array
		for val in initx:
			# Scale, and add the amount of the current element in the initial array so it
			# is offset to the proper location
			x = (val*domainScale) + initx[i]
			newx.append(x)

		# Apply the scaling factor to each y coordinate in the initial array in order 
		# to create a new set of points between the current and next element of the initial array
		for val in inity:
			# Scale, and add the amount of the current element in the initial array so it
			# is offset to the proper location
			y = (val*rangeScale) + inity[i]
			newy.append(y)

	# Set the init arrays to be equal to the arrays we just built, so on the next pass
	# though the loop, we are advancing the level of the fractal.
	initx = newx
	inity = newy

	# Plot the current line
	plt.plot(newx, newy, colors[j])




#######################################
##		Plotting
#######################################

# The plotting for the graphs occurred within the logic so multiple plots could be overlayed.
# This section is to format the graph and show it.


# Label the y-axis
plt.ylabel('output')
# Label the x-axis
plt.xlabel('input')
# display the graph
plt.show()


