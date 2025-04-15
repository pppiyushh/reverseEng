
This is a very goo problem for someone who is just starting with RE.
While analysing the code in the decompiler (I am using Ghidra), we observe this line here:

if  (string_innput[i] - string_input[i +1] != -1)

To our input t opass, we should not enter this if. So any combo will work (with length 16, because of previous if) as long as this is satisfied.
ex: abababababababab 
  : abcdefghijklmnop

