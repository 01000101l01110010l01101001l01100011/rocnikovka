import control_algorithm
import algorithm_new

cont = control_algorithm.control(50)
sus = algorithm_new.sus(50)


print("All:", cont)
print("My:", sus)
print("My was faster by", cont - sus, "seconds and by", (cont - sus)/cont*100, "%")