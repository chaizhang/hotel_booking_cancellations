# information from iso.org

iso_to_country_dict = {
    'PRT': 'Portugal', 
    'GBR': 'United Kingdom', 
    'USA': 'United States of America', 
    'ESP': 'Spain', 
    'IRL': 'Ireland', 
    'FRA': 'France',
    'ROU': 'Romania', 
    'NOR': 'Norway', 
    'OMN': 'Oman', 
    'ARG': 'Argentina', 
    'POL': 'Poland', 
    'DEU': 'Germany', 
    'BEL': 'Belgium', 
    'CHE': 'Switzerland', 
    'CN': 'China', # we believe that here "CN" refers to the alpha-2 ISO country code for China
    'GRC': 'Greece', 
    'ITA': 'Italy', 
    'NLD': 'Netherlands', 
    'DNK': 'Denmark', 
    'RUS': 'Russian Federation', 
    'SWE': 'Sweden', 
    'AUS': 'Australia', 
    'EST': 'Estonia', 
    'CZE': 'Czechia', 
    'BRA': 'Brazil', 
    'FIN': 'Finland', 
    'MOZ': 'Mozambique', 
    'BWA': 'Botswana', 
    'LUX': 'Luxembourg', 
    'SVN': 'Slovenia', 
    'ALB': 'Albania', 
    'IND': 'India', 
    'CHN': 'China', # alpha-3 ISO country code for China
    'MEX': 'Mexico', 
    'MAR': 'Morocco', 
    'UKR': 'Ukraine', 
    'SMR': 'San Marino', 
    'LVA': 'Latvia', 
    'PRI': 'Puerto Rico', 
    'SRB': 'Serbia', 
    'CHL': 'Chile', 
    'AUT': 'Austria', 
    'BLR': 'Belarus', 
    'LTU': 'Lithuania', 
    'TUR': 'Türkiye', 
    'ZAF': 'South Africa', 
    'AGO': 'Angola', 
    'ISR': 'Israel', 
    'CYM': 'Cayman Islands', 
    'ZMB': 'Zambia', 
    'CPV': 'Cabo Verde', 
    'ZWE': 'Zimbabwe', 
    'DZA': 'Algeria', 
    'KOR': 'Korea', 
    'CRI': 'Costa Rica', 
    'HUN': 'Hungary', 
    'ARE': 'United Arab Emirates', 
    'TUN': 'Tunisia', 
    'JAM': 'Jamaica', 
    'HRV': 'Croatia', 
    'HKG': 'Hong Kong', 
    'IRN': 'Iran', 
    'GEO': 'Georgia', 
    'AND': 'Andorra', 
    'GIB': 'Gibraltar', 
    'URY': 'Uruguay', 
    'JEY': 'Jersey', 
    'CAF': 'Central African Republic', 
    'CYP': 'Cyprus', 
    'COL': 'Colombia', 
    'GGY': 'Guernsey', 
    'KWT': 'Kuwait', 
    'NGA': 'Nigeria', 
    'MDV': 'Maldives', 
    'VEN': 'Venezuela', 
    'SVK': 'Slovakia', 
    'FJI': 'Fiji', 
    'KAZ': 'Kazakhstan', 
    'PAK': 'Pakistan', 
    'IDN': 'Indonesia', 
    'LBN': 'Lebanon', 
    'PHL': 'Philippines', 
    'SEN': 'Senegal', 
    'SYC': 'Seychelles', 
    'AZE': 'Azerbaijan', 
    'BHR': 'Bahrain', 
    'NZL': 'New Zealand', 
    'THA': 'Thailand', 
    'DOM': 'Dominican Republic', 
    'MKD': 'North Macedonia', 
    'MYS': 'Malaysia', 
    'ARM': 'Armenia', 
    'JPN': 'Japan', 
    'LKA': 'Sri Lanka', 
    'CUB': 'Cuba', 
    'CMR': 'Cameroon', 
    'BIH': 'Bosnia and Herzegovina', 
    'MUS': 'Mauritius', 
    'COM': 'Comoros', 
    'SUR': 'Suriname', 
    'UGA': 'Uganda', 
    'BGR': 'Bulgaria', 
    'CIV': "Côte d'Ivoire", 
    'JOR': 'Jordan', 
    'SYR': 'Syrian Arab Republic', 
    'SGP': 'Singapore', 
    'BDI': 'Burundi', 
    'SAU': 'Saudi Arabia', 
    'VNM': 'Viet Nam', 
    'PLW': 'Palau', 
    'QAT': 'Qatar', 
    'EGY': 'Egypt', 
    'PER': 'Peru', 
    'MLT': 'Malta', 
    'MWI': 'Malawi', 
    'ECU': 'Ecuador', 
    'MDG': 'Madagascar', 
    'ISL': 'Iceland', 
    'UZB': 'Uzbekistan', 
    'NPL': 'Nepal', 
    'BHS': 'Bahamas', 
    'MAC': 'Macao', 
    'TGO': 'Togo', 
    'TWN': 'Taiwan', 
    'DJI': 'Djibouti', 
    'STP': 'Sao Tome and Principe', 
    'KNA': 'Saint Kitts and Nevis', 
    'ETH': 'Ethiopia', 
    'IRQ': 'Iraq', 
    'HND': 'Honduras', 
    'RWA': 'Rwanda', 
    'KHM': 'Cambodia', 
    'MCO': 'Monaco', 
    'BGD': 'Bangladesh', 
    'IMN': 'Isle of Man', 
    'TJK': 'Tajikistan', 
    'NIC': 'Nicaragua', 
    'BEN': 'Benin', 
    'VGB': 'Virgin Islands', 
    'TZA': 'Tanzania', 
    'GAB': 'Gabon', 
    'GHA': 'Ghana', 
    'TMP': 'Timor-Leste', 
    'GLP': 'Guadeloupe', 
    'KEN': 'Kenya', 
    'LIE': 'Liechtenstein', 
    'GNB': 'Guinea-Bissau', 
    'MNE': 'Montenegro', 
    'UMI': 'United States Minor Outlying Islands', 
    'MYT': 'Mayotte', 
    'FRO': 'Faroe Islands', 
    'MMR': 'Myanmar', 
    'PAN': 'Panama', 
    'BFA': 'Burkina Faso', 
    'LBY': 'Libya', 
    'MLI': 'Mali', 
    'NAM': 'Namibia', 
    'BOL': 'Bolivia', 
    'PRY': 'Paraguay', 
    'BRB': 'Barbados', 
    'ABW': 'Aruba', 
    'AIA': 'Anguilla', 
    'SLV': 'El Salvador', 
    'DMA': 'Dominica', 
    'PYF': 'French Polynesia', 
    'GUY': 'Guyana', 
    'LCA': 'Saint Lucia', 
    'ATA': 'Antarctica', 
    'GTM': 'Guatemala', 
    'ASM': 'American Samoa', 
    'MRT': 'Mauritania', 
    'NCL': 'New Caledonia', 
    'KIR': 'Kiribati', 
    'SDN': 'Sudan', 
    'ATF': 'French Southern Territories', 
    'SLE': 'Sierra Leone', 
    'LAO': 'Lao',
}