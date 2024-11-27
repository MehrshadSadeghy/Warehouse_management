# project name: Warehouse management
In this project, django forms are used to receive information from the user and django rest framework is used to send information in the form of API.

urls:
# 1. phone/add/phones
for adding phone in database.

# 2. brand/add/country
for adding country in database.

# 3. brand/add/brand
for adding brand in database.

# 4. brand/redirect/brand/country/
it returns the information of brands whose nationality is equal to the input country

# 5. phone/ui/v1/search_by_brand/
for getting the brand name from the user and sending it to the URL(phone/search/brand/<str:brand>/api/v1/)

# 6. phone/search/brand/<brand_name>/api/v1/
searching for phones whose brand is the same as the incoming brand.

# 7. phone/api/v1/reports/same_brand_country_and_country_search/
searching for phones whose country of manufacture is equal to its nationality.
