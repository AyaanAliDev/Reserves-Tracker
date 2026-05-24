import valkey

r = valkey.Valkey(host='localhost', port=6379, decode_responses=True)

# Data based on IMF COFER trends (1999-2021)
# Big Four: USD, EUR, JPY, GBP
# Nontraditional: AUD, CAD, RMB, CHF, etc.
data_big_four = {
    "1999": "98.5", "2001": "98.3", "2003": "98.0", "2005": "98.2", 
    "2007": "98.1", "2009": "97.0", "2011": "95.0", "2013": "93.5",
    "2015": "93.7", "2017": "93.0", "2019": "92.2", "2021": "90.5"
}

data_nontraditional = {
    "1999": "1.5", "2001": "1.7", "2003": "2.0", "2005": "1.8",
    "2007": "1.9", "2009": "3.0", "2011": "5.0", "2013": "6.5",
    "2015": "6.3", "2017": "7.0", "2019": "7.8", "2021": "9.5"
}

# Clear previous data and push new
r.flushall()
for year, val in data_big_four.items(): r.set(f"big4:{year}", val)
for year, val in data_nontraditional.items(): r.set(f"non:{year}", val)

print("--- Data ingestion complete: 1999-2021 series loaded ---")
