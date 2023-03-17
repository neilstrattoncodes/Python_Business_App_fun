# Neil Stratton
# February 6 - 2022

# Constants
EXTRA_MEM_COST = 5
EVEN_SITE = 80
ODD_SITE = 120
SITE_CLEANING_COST = 50
VIDEO_SURV_COST = 35
STANDARD_DUES = 75
EXECUTIVE_DUES = 150
PROCESSING_FEE = 59.99
CANCEL_FEE = .60
TAX = .15
YEAR_MONTHS = 12
HST_REG_NUM = "549-33-5849-4720-9885"
DATE = "2022-02-06"
BUSINESS_NAME = "St. John’s Marina & Yacht Club"
RECEIPT_TYPE = "Yearly Member Receipt"
CLIENT_TITLE = "Client Name and Address:"
DASHES = "-------------"

#Inputs
site_number = int(input("Enter site Number: "))
member_name = str(input("Enter member name: ")).upper()
street_address = str(input("Enter Street Address: ")).upper()
city_name = str(input(f"Enter city name: ")).upper()
province = str(input(f"Enter province (XX): ")).upper()
post_code = str(input(f"Enter Postal Code X1X-X1X: ")).upper()
home_phone = str(input(f"Enter Home phone #: "))
cell_phone = str(input(f"Enter Cell phone #: "))
membership_type = str(input(f"Enter membership type (S)tandard or (E)xecutive: ")).upper()
family_mem = int(input(f"Enter number of extra family and friends members: "))
site_cleaning = str(input(f"Do you want weekly site cleaning? Y or N: ")).upper()
video_surv = str(input(f"Do you want Video surveillance? Y or N: ")).upper()

# 1. Even Site, Standard membership, YES site cleaning, YES video surveillance #### FIRST SET START
if (site_number % 2) == 0 and membership_type == "S" and site_cleaning == "Y" and video_surv == "Y":
    subtotal = EVEN_SITE + SITE_CLEANING_COST + VIDEO_SURV_COST
    monthly_dues = STANDARD_DUES
    extra_charges = SITE_CLEANING_COST + VIDEO_SURV_COST
    site_type = EVEN_SITE

# 2. Odd Site, Standard membership, YES site cleaning, YES video surveillance
elif (site_number % 2) != 0 and membership_type == "S" and site_cleaning == "Y" and video_surv == "Y":
    subtotal = ODD_SITE + SITE_CLEANING_COST + VIDEO_SURV_COST
    monthly_dues = STANDARD_DUES
    extra_charges = SITE_CLEANING_COST + VIDEO_SURV_COST
    site_type = ODD_SITE

# 3. Even Site, Executive membership, YES site cleaning, YES video surveillance
elif (site_number % 2) == 0 and membership_type == "E" and site_cleaning == "Y" and video_surv == "Y":
    subtotal = EVEN_SITE + SITE_CLEANING_COST + VIDEO_SURV_COST
    monthly_dues = EXECUTIVE_DUES
    extra_charges = SITE_CLEANING_COST + VIDEO_SURV_COST
    site_type = EVEN_SITE

# 4.  Odd Site, Executive membership, YES site cleaning, YES video surveillance  #### FIRST SET END
elif (site_number % 2) != 0 and membership_type == "E" and site_cleaning == "Y" and video_surv == "Y":
    subtotal = ODD_SITE + SITE_CLEANING_COST + VIDEO_SURV_COST
    monthly_dues = EXECUTIVE_DUES
    extra_charges = SITE_CLEANING_COST + VIDEO_SURV_COST
    site_type = ODD_SITE

# 5.  Even Site, Standard membership, NO site cleaning,  YES video surveillance #### SECOND SET START
elif (site_number % 2) == 0 and membership_type == "S" and site_cleaning == "N" and video_surv == "Y":
    subtotal = EVEN_SITE + VIDEO_SURV_COST
    monthly_dues = STANDARD_DUES
    extra_charges = VIDEO_SURV_COST
    site_type = EVEN_SITE

# 6.  Odd Site, Standard membership, NO site cleaning,  YES video surveillance
elif (site_number % 2) != 0 and membership_type == "S" and site_cleaning == "N" and video_surv == "Y":
    subtotal = ODD_SITE + VIDEO_SURV_COST
    monthly_dues = STANDARD_DUES
    extra_charges = VIDEO_SURV_COST
    site_type = ODD_SITE

# 7.  Even Site, Executive membership, NO site cleaning and YES video surveillance
elif (site_number % 2) == 0 and membership_type == "E" and site_cleaning == "N" and video_surv == "Y":
    subtotal = EVEN_SITE + VIDEO_SURV_COST
    monthly_dues = EXECUTIVE_DUES
    extra_charges = VIDEO_SURV_COST
    site_type = EVEN_SITE

# 8.  Odd Site, Executive membership, NO site cleaning, YES video surveillance #### SECOND SET END
elif (site_number % 2) != 0 and membership_type == "E" and site_cleaning == "N" and video_surv == "Y":
    subtotal = ODD_SITE + VIDEO_SURV_COST
    monthly_dues = EXECUTIVE_DUES
    extra_charges = VIDEO_SURV_COST
    site_type = ODD_SITE

# 9.  Even Site, Standard membership, YES site cleaning, NO video surveillance #### THIRD SET START
elif (site_number % 2) == 0 and membership_type == "S" and site_cleaning == "Y" and video_surv == "N":
    subtotal = EVEN_SITE + STANDARD_DUES + SITE_CLEANING_COST
    monthly_dues = STANDARD_DUES
    extra_charges = SITE_CLEANING_COST
    site_type = EVEN_SITE

# 10.  Odd Site, Standard membership, YES site cleaning, NO video surveillance
elif (site_number % 2) != 0 and membership_type == "S" and site_cleaning == "Y" and video_surv == "N":
    subtotal = ODD_SITE + SITE_CLEANING_COST
    monthly_dues = STANDARD_DUES
    extra_charges = SITE_CLEANING_COST
    site_type = ODD_SITE

# 11.  Even Site, Executive membership, YES site cleaning, NO video surveillance
elif (site_number % 2) == 0 and membership_type == "E" and site_cleaning == "Y" and video_surv == "N":
    subtotal = EVEN_SITE + SITE_CLEANING_COST
    monthly_dues = EXECUTIVE_DUES
    extra_charges = SITE_CLEANING_COST
    site_type = EVEN_SITE

# 12.  Odd Site, Executive membership, YES site cleaning, NO video surveillance ### THIRD SET END
elif (site_number % 2) != 0 and membership_type == "E" and site_cleaning == "Y" and video_surv == "N":
    subtotal = ODD_SITE + SITE_CLEANING_COST
    monthly_dues = EXECUTIVE_DUES
    extra_charges = SITE_CLEANING_COST
    site_type = ODD_SITE

# 13.  Even Site, Standard membership, NO site cleaning, NO video surveillance #### FOURTH SET START
elif (site_number % 2) == 0 and membership_type == "S" and site_cleaning == "N" and video_surv == "N":
    subtotal = EVEN_SITE
    monthly_dues = STANDARD_DUES
    extra_charges = 0
    site_type = EVEN_SITE

# 14. Odd Site, Standard membership with NO site cleaning, NO video surveillance
elif (site_number % 2) != 0 and membership_type == "S" and site_cleaning == "N" and video_surv == "N":
    subtotal = ODD_SITE
    monthly_dues = STANDARD_DUES
    extra_charges = 0
    site_type = ODD_SITE

# 15. Even Site, Executive membership, NO site cleaning, NO video surveillance
elif (site_number % 2) == 0 and membership_type == "E" and site_cleaning == "N" and video_surv == "N":
    subtotal = EVEN_SITE
    monthly_dues = EXECUTIVE_DUES
    extra_charges = 0
    site_type = EVEN_SITE

# 16. Odd Site, Executive membership, NO site cleaning,  NO video surveillance #### FOURTH SET END
elif (site_number % 2) != 0 and membership_type == "E" and site_cleaning == "N" and video_surv == "N":
    subtotal = ODD_SITE
    monthly_dues = EXECUTIVE_DUES
    extra_charges = 0
    site_type = ODD_SITE

# Site cleaning input change output
if site_cleaning == "Y":
    site_cleaning ="YES"
else:
    site_cleaning = "NO"

# Video Surveillance input change output
if video_surv == "Y":
    video_surv = "YES"
else:
    video_surv = "NO"

# Membership type input change output
if membership_type == "E":
    membership_type = "EXECUTIVE"
else:
    membership_type = "STANDARD"

# Calculations
final_total_wtax = subtotal + (family_mem * EXTRA_MEM_COST)
extra_members = family_mem * EXTRA_MEM_COST
site_charges = site_type + extra_members   # EVEN OR ODD SITE
subtotal_cost = extra_charges + site_charges
sales_tax = subtotal_cost * TAX
yearly_total = subtotal + sales_tax + (PROCESSING_FEE / YEAR_MONTHS) * YEAR_MONTHS
total_monthly_charge = sales_tax + subtotal_cost # FIX HERE
total_monthly_fees = total_monthly_charge + monthly_dues
total_yearly_fees = total_monthly_fees * YEAR_MONTHS
monthly_payment = (total_yearly_fees + PROCESSING_FEE) / YEAR_MONTHS
cancellation_fee = (site_type + extra_members) * YEAR_MONTHS * CANCEL_FEE

# Dollar formatting
sales_tax_out = f"${sales_tax:,.2f}"
yearly_total_out = f"${yearly_total:,.2f}"
site_charges_out = f"${site_charges:,.2f}"
cancellation_fee_out = f"${cancellation_fee:,.2f}"
extra_charges_out = f"${extra_charges:,.2f}"
subtotal_out = f"${subtotal_cost:,.2f}"
total_monthly_charge_out = f"${total_monthly_charge:,.2f}"
subtotal_out = f"${subtotal_cost:,.2f}"
monthly_dues_out = f"${monthly_dues:,.2f}"
total_monthly_fees_out = f"${total_monthly_fees:,.2f}"
total_yearly_fees_out = f"${total_yearly_fees:,.2f}"
monthly_payment_out = f"${monthly_payment:,.2f}"


# Print outputs
print("")
print("")
print(f"       {BUSINESS_NAME:^24}")
print(f"       {RECEIPT_TYPE:^27}")
print(f"-"*45)
print("")
print(f"{CLIENT_TITLE:<25}")
print("")
print(f"{member_name:^24} ")
print(f"{street_address:^24} ")
print(f"{city_name}, {province} {post_code}")
print("")
print(f"Phone: {home_phone:>5}(H)")
print(f"       {cell_phone:>5}(C)")
print("")
print(f"Site #: {site_number}           Member Type: {membership_type:>10}")
print(f"Alternate Members:                  {family_mem:>7}")
print(f"Weekly site cleaning:               {site_cleaning:>7}")
print(f"Video surveillance:                 {video_surv:>7}")
print(f"")
print(f"Site Charges:                       {site_charges_out:>7}")
print(f"Extra charges:                      {extra_charges_out:>7}")
print(f"                              {DASHES:>7}")
print(f"Subtotal:                           {subtotal_out:>7}")
print(f"Sales tax (HST):                    {sales_tax_out:>7}")
print(f"                              {DASHES:>7}")
print(f"Total monthly charges:              {total_monthly_charge_out:>7}")
print(f"Monthly dues:                       {monthly_dues_out:>7}")
print(f"                              {DASHES:>7}")
print(f"Total monthly fees:                 {total_monthly_fees_out:>7}")
print(f"Total yearly fees:                {total_yearly_fees_out:>7}")
print("")
print(f"Monthly payment:                    {monthly_payment_out:>7}")
print("")
print(f"-"*45)
print("")
print(f"Issued: {DATE}")
print(f"HST Reg No: {HST_REG_NUM}")
print(f"Cancellation fee:                   {cancellation_fee_out:>7}")







