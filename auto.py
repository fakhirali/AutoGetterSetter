filename = "code.cpp"

# Open the file as f.
# The function readlines() reads the file.
with open(filename) as f:
	 content = f.readlines()

# Show the file contents line by line.
# We added the comma to print single newlines and not double newlines.
# This is because the lines contain the newline character '\n'.
inclass = False
data = []
for line in content:
	words = line.split()
	#print(word)

	if(inclass and len(words) > 0):
		if words[0] != 'private:':
			if words[0] == "public:":
				inclass = False
				#break
			else:
				words[-1] = words[-1][:-1]
				data.append(words)		
	if(len(words) > 0 and words[0] == "class"):
		inclass = True
	
for i in range(len(data)):
	#print(data[i])
	print(f"// setter for {data[i][1]}")
	print(f"void set{data[i][1]}({data[i][0]} {data[i][1][0]})" + "{")
	print(f"	{data[i][1]} = {data[i][1][0]};")
	print("}")

	print(f"// getter for {data[i][1]}")
	print(f"{data[i][0]} get{data[i][1]}()" + "{")
	print(f"	return {data[i][1]};")
	print("}")

