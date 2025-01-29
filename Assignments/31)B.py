'''B) Create the following lists using a for loop:
The list [&#39;a&#39;,&#39;bb&#39;,&#39;ccc&#39;,&#39;dddd&#39;, . . . ] that ends with 26 copies of the letter z.'''
def letter_printer():
    letter_list = []
    for i in range(26):
        letter_list.append(chr(97+i)*(i+1))
    print(letter_list)

letter_printer()