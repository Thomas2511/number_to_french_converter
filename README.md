# number to french converter

This is a simple number to french converter taking integer values from 0 to 999999.

## data

The values from 0 to 99 being 'mostly' unique values I asked ChatGPT to list them for me, and saved them as a data file.
Prompt to list and format the values:
"Liste moi les chiffres en français de zéro à quatre vingt dix neuf avec un seul chiffre par ligne avec les chiffres écrits en toutes lettres. Ecris moi le résultat avec chaque chiffre entouré de guillemets et chaque ligne se finissant par une virgule."

## algorithm

- Split the number into two sections: thousands and the rest.
- Check for French rules concerning the thousands.
- Created a function to convert a number of 3 digits, checking the French rules applying to the hundreds.
- Applied the function to the 3 digits corresponding to the thousands, then to the 3 digits corresponding to the rest.
