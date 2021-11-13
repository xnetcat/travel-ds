from travelds.scrapers import (
    Hotels, Expedia
)

from travelds.proxies import SpysMe


SCRAPERS = {
    "hotels.com": Hotels,
    "expedia": Expedia
}

PROXIES = {
    "spys.me": SpysMe
}

CITIES = [
    "New York",
    "Barcelona",
    "Moscow",
    "Tokyo",
    "Seoul",
    "Berlin",
    "Amsterdam",
    "Buenos Aires",
    "Rio de Janeiro",
    "Warsaw",
    "London",
    "Rome",
    "Chennai",
    "Shanghai",
    "Guangzhou",
    "Beijing",
    "Paris",
    "Dhaka",
    "Melbourne",
    "Madrid",
    "Kiev",
    "Istanbul",
    "Cairo",
    "Lagos",
    "Karachi",
    "Delhi",
    "Sao Paulo",
    "Mexico City",
    "Los Angeles",
    "Manila",
    "Kinshasa",
    "Bogotá",
    "Jakarta",
    "Lima",
    "Bangkok",
    "Ho Chi Minh City",
    "Kuala Lumpur",
    "Hong Kong",
    "Riyadh",
]

COUNTRIES = ['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antarctica', 'Antigua And Barbuda', 'Argentina', 'Armenia', 'Aruba', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bermuda', 'Bhutan', 'Bolivia', 'Bosnia', 'Botswana', 'Brazil', 'Brunei Darussalam', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Cayman Islands', 'Central African Republic', 'Chad', 'Chile', 'China', 'Colombia', 'Comoros', 'Costa Rica', "Cote D'Ivoire", 'Croatia', 'Cuba', 'Curacao', 'Cyprus', 'Czechia', 'Czechoslovakia', 'Democratic Republic Of Congo', 'Denmark', 'Djibouti', 'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia', 'Faroe Islands', 'Fiji', 'Finland', 'France', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Gibraltar', 'Greece', 'Guadeloupe', 'Guam', 'Guatemala', 'Guernsey', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Vatican', 'Honduras', 'Hong Kong', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Isle Of Man', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jersey', 'Jordan', 'Kazakhstan', 'Kenya', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macao', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Malta', 'Mexico', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Caledonia', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'North Macedonia', 'Norway', 'Oman', 'Pakistan', 'Palestinian Territory', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Puerto Rico', 'Qatar', 'Republic Of Congo', 'Reunion', 'Romania', 'Russian Federation', 'Rwanda', 'San Marino', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia']

REGIONS = ['Catalonia', 'Andalucia', 'Basque Country', 'Comunidad de Madrid']