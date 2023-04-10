'''
TODO
    -Improve image readability by direct download from phone, or image thresholding
    -Order images cronologically, and not randomly how it is now

NOTES:
-Works better the clearer the image is
-Approach is the only word consistently detected in each image
'''

# for going through files
import glob
# for reading images
import cv2
# for getting text from images
import pytesseract

# load settings
f = open("settings.csv", "r")
settings = f.read().split("\n")
f.close()
settingsComplete = []
for i in settings:
    current = i.split(",")
    if len(current) > 1:
        settingsComplete.append(current[0].strip())
        settingsComplete.append(current[1].strip())
print("settings set")

# add data from every image to single string
combined = ""
for i in glob.glob("Images/*"):
    image = cv2.imread(i)
    combined += pytesseract.image_to_string(image)
    combined += "THISISTHEENDOFANIMAGE"
    print("reading image {:s}".format(i))
print("finished reading images")
# process data
imageCount = 1
possibleApproaches = ["kosatka", "alkonost", "velum", "stealth", "annihilator", "patrol", "boat"]
possibleTargets = ["sinsimito", "tequilla", "ruby", "necklace", "bearer", "bonds", "pink", "diamond"]
times = []
approaches = []
targets = []
takes = []
data = combined.split("THISISTHEENDOFANIMAGE")
for i in data:
    current = i.split()
    #print(current)
    for j in current:
        # time
        lower = j.strip().lower()
        if "0:" in lower and len(times) < imageCount:
            times.append(lower)
        # approach
        if lower in possibleApproaches and len(approaches) < imageCount:
            if lower == "stealth" or lower == "annihilator":
                approaches.append("stealth annihilator")
            elif lower == "patrol" or lower == "boat":
                approaches.append("patrol boat")
            else:
                approaches.append(lower)
        # target
        if lower in possibleTargets and len(targets) < imageCount:
            if lower == "sinsimito" or lower == "tequilla":
                targets.append("sinsimito tequilla")
            elif lower == "ruby" or lower == "necklace":
                targets.append("ruby necklace")
            elif lower == "pink" or lower == "diamond":
                targets.append("pink diamond")
        # take
        if lower == "final" and len(takes) < imageCount:
            if "$" in current[current.index(j) + 2]:
                takes.append(current[current.index(j) + 2].replace(",",""))
    # lists only added to above if valid time found,
    # so if none found add here to make all parallel lists the same length
    if len(times) < imageCount:
        times.append("unknown")
    if len(approaches) < imageCount:
        approaches.append("unknown")
    if len(targets) < imageCount:
        # never detects bearer bonds
        targets.append("bearer bonds")
    if len(takes) < imageCount:
        takes.append("unknown")
    imageCount += 1

# parallel lists into string for writing to file
output = "Time, Approach, Target, Take\n"
for i in range(len(times)):
    if settingsComplete[settingsComplete.index("onlyCompletes") + 1] == "yes":
        if not("unknown" in "{:s}, {:s}, {:s}, {:s}\n".format(times[i], approaches[i], targets[i], takes[i])):
            output += "{:s}, {:s}, {:s}, {:s}\n".format(times[i], approaches[i], targets[i], takes[i])
    else:
        output += "{:s}, {:s}, {:s}, {:s}\n".format(times[i], approaches[i], targets[i], takes[i])

outFile = "finalOutput.csv"
if settingsComplete[settingsComplete.index("rewrite") + 1] == "yes":
    f = open(outFile, "w")
else:
    f = open(outFile, "a")
f.write(output)
f.close()
print("finished processing images")
