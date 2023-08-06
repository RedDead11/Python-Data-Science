filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]

newfilenames = []

for filename in filenames:
    
    if filename.endswith("hpp"):
        new_filename = filename.replace("hpp", "h")
        newfilenames.append(new_filename)
        #print(filename)
    
    else:
        newfilenames.append(filename)



print(newfilenames) 
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]