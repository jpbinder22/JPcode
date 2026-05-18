 #!/usr/bin/env python3

 # Define the string
quote = "Live Long And Prosper"

 # Chain methods to lower the string, split it, and join with "-"
result = "-".join(quote.lower().split())
print(result)


