import statistics
 
data = [220, 100, 190, 180, 250, 190, 240, 180, 140, 180, 190]
 
# Finding Mean
print("\nMean: ", statistics.mean(data))
 
# Finding Median
print("Median: ", statistics.median(data))
 
# Finding Single Mode
print("Single Mode: ", statistics.mode(data))
 
# Finding Multiple Modes
print("Mode: ", statistics.multimode(data))
