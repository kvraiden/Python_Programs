filename = input("Enter file name: ")
fhand = open(filename, "r")
total_confidence = 0
count = 0

for line in fhand:
    if line.startswith("X-DSPAM-Confidence:"):
        space_index = line.find(" ")
        my_num = float(line[space_index + 1:])
        total_confidence += my_num
        count += 1
print("Average spam confidence:", total_confidence / count)
