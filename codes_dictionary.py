# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 15:39:32 2019
@author: Timofey Eltsov
"""

dict = {"Afghanistan" : {'Alpha-2': 'AF', 'Alpha-3': 'AFG', 'Numeric code': '004', 'Link to ISO 3166-2': 'ISO 3166-2:AF', 'Independent': 'Yes'},
"Åland Islands" : {'Alpha-2': 'AX', 'Alpha-3': 'ALA', 'Numeric code': '248', 'Link to ISO 3166-2': 'ISO 3166-2:AX', 'Independent': 'No'},
"Albania" : {'Alpha-2': 'AL', 'Alpha-3': 'ALB', 'Numeric code': '008', 'Link to ISO 3166-2': 'ISO 3166-2:AL', 'Independent': 'Yes'},
"Algeria" : {'Alpha-2': 'DZ', 'Alpha-3': 'DZA', 'Numeric code': '012', 'Link to ISO 3166-2': 'ISO 3166-2:DZ', 'Independent': 'Yes'},
"American Samoa" : {'Alpha-2': 'AS', 'Alpha-3': 'ASM', 'Numeric code': '016', 'Link to ISO 3166-2': 'ISO 3166-2:AS', 'Independent': 'No'},
"Andorra" : {'Alpha-2': 'AD', 'Alpha-3': 'AND', 'Numeric code': '020', 'Link to ISO 3166-2': 'ISO 3166-2:AD', 'Independent': 'Yes'},
"Angola" : {'Alpha-2': 'AO', 'Alpha-3': 'AGO', 'Numeric code': '024', 'Link to ISO 3166-2': 'ISO 3166-2:AO', 'Independent': 'Yes'},
"Anguilla" : {'Alpha-2': 'AI', 'Alpha-3': 'AIA', 'Numeric code': '660', 'Link to ISO 3166-2': 'ISO 3166-2:AI', 'Independent': 'No'},
"Antarctica" : {'Alpha-2': 'AQ', 'Alpha-3': 'ATA', 'Numeric code': '010', 'Link to ISO 3166-2': 'ISO 3166-2:AQ', 'Independent': 'No'},
"Antigua and Barbuda" : {'Alpha-2': 'AG', 'Alpha-3': 'ATG', 'Numeric code': '028', 'Link to ISO 3166-2': 'ISO 3166-2:AG', 'Independent': 'Yes'},
"Argentina" : {'Alpha-2': 'AR', 'Alpha-3': 'ARG', 'Numeric code': '032', 'Link to ISO 3166-2': 'ISO 3166-2:AR', 'Independent': 'Yes'},
"Armenia" : {'Alpha-2': 'AM', 'Alpha-3': 'ARM', 'Numeric code': '051', 'Link to ISO 3166-2': 'ISO 3166-2:AM', 'Independent': 'Yes'},
"Aruba" : {'Alpha-2': 'AW', 'Alpha-3': 'ABW', 'Numeric code': '533', 'Link to ISO 3166-2': 'ISO 3166-2:AW', 'Independent': 'No'},
"Australia" : {'Alpha-2': 'AU', 'Alpha-3': 'AUS', 'Numeric code': '036', 'Link to ISO 3166-2': 'ISO 3166-2:AU', 'Independent': 'Yes'},
"Austria" : {'Alpha-2': 'AT', 'Alpha-3': 'AUT', 'Numeric code': '040', 'Link to ISO 3166-2': 'ISO 3166-2:AT', 'Independent': 'Yes'},
"Azerbaijan" : {'Alpha-2': 'AZ', 'Alpha-3': 'AZE', 'Numeric code': '031', 'Link to ISO 3166-2': 'ISO 3166-2:AZ', 'Independent': 'Yes'},
"Bahamas" : {'Alpha-2': 'BS', 'Alpha-3': 'BHS', 'Numeric code': '044', 'Link to ISO 3166-2': 'ISO 3166-2:BS', 'Independent': 'Yes'},
"Bahrain" : {'Alpha-2': 'BH', 'Alpha-3': 'BHR', 'Numeric code': '048', 'Link to ISO 3166-2': 'ISO 3166-2:BH', 'Independent': 'Yes'},
"Bangladesh" : {'Alpha-2': 'BD', 'Alpha-3': 'BGD', 'Numeric code': '050', 'Link to ISO 3166-2': 'ISO 3166-2:BD', 'Independent': 'Yes'},
"Barbados" : {'Alpha-2': 'BB', 'Alpha-3': 'BRB', 'Numeric code': '052', 'Link to ISO 3166-2': 'ISO 3166-2:BB', 'Independent': 'Yes'},
"Belarus" : {'Alpha-2': 'BY', 'Alpha-3': 'BLR', 'Numeric code': '112', 'Link to ISO 3166-2': 'ISO 3166-2:BY', 'Independent': 'Yes'},
"Belgium" : {'Alpha-2': 'BE', 'Alpha-3': 'BEL', 'Numeric code': '056', 'Link to ISO 3166-2': 'ISO 3166-2:BE', 'Independent': 'Yes'},
"Belize" : {'Alpha-2': 'BZ', 'Alpha-3': 'BLZ', 'Numeric code': '084', 'Link to ISO 3166-2': 'ISO 3166-2:BZ', 'Independent': 'Yes'},
"Benin" : {'Alpha-2': 'BJ', 'Alpha-3': 'BEN', 'Numeric code': '204', 'Link to ISO 3166-2': 'ISO 3166-2:BJ', 'Independent': 'Yes'},
"Bermuda" : {'Alpha-2': 'BM', 'Alpha-3': 'BMU', 'Numeric code': '060', 'Link to ISO 3166-2': 'ISO 3166-2:BM', 'Independent': 'No'},
"Bhutan" : {'Alpha-2': 'BT', 'Alpha-3': 'BTN', 'Numeric code': '064', 'Link to ISO 3166-2': 'ISO 3166-2:BT', 'Independent': 'Yes'},
"Bolivia (Plurinational State of)" : {'Alpha-2': 'BO', 'Alpha-3': 'BOL', 'Numeric code': '068', 'Link to ISO 3166-2': 'ISO 3166-2:BO', 'Independent': 'Yes'},
"Bonaire, Sint Eustatius and Saba" : {'Alpha-2': 'BQ', 'Alpha-3': 'BES', 'Numeric code': '535', 'Link to ISO 3166-2': 'ISO 3166-2:BQ', 'Independent': 'No'},
"Bosnia and Herzegovina" : {'Alpha-2': 'BA', 'Alpha-3': 'BIH', 'Numeric code': '070', 'Link to ISO 3166-2': 'ISO 3166-2:BA', 'Independent': 'Yes'},
"Botswana" : {'Alpha-2': 'BW', 'Alpha-3': 'BWA', 'Numeric code': '072', 'Link to ISO 3166-2': 'ISO 3166-2:BW', 'Independent': 'Yes'},
"Bouvet Island" : {'Alpha-2': 'BV', 'Alpha-3': 'BVT', 'Numeric code': '074', 'Link to ISO 3166-2': 'ISO 3166-2:BV', 'Independent': 'No'},
"Brazil" : {'Alpha-2': 'BR', 'Alpha-3': 'BRA', 'Numeric code': '076', 'Link to ISO 3166-2': 'ISO 3166-2:BR', 'Independent': 'Yes'},
"British Indian Ocean Territory" : {'Alpha-2': 'IO', 'Alpha-3': 'IOT', 'Numeric code': '086', 'Link to ISO 3166-2': 'ISO 3166-2:IO', 'Independent': 'No'},
"Brunei Darussalam" : {'Alpha-2': 'BN', 'Alpha-3': 'BRN', 'Numeric code': '096', 'Link to ISO 3166-2': 'ISO 3166-2:BN', 'Independent': 'Yes'},
"Bulgaria" : {'Alpha-2': 'BG', 'Alpha-3': 'BGR', 'Numeric code': '100', 'Link to ISO 3166-2': 'ISO 3166-2:BG', 'Independent': 'Yes'},
"Burkina Faso" : {'Alpha-2': 'BF', 'Alpha-3': 'BFA', 'Numeric code': '854', 'Link to ISO 3166-2': 'ISO 3166-2:BF', 'Independent': 'Yes'},
"Burundi" : {'Alpha-2': 'BI', 'Alpha-3': 'BDI', 'Numeric code': '108', 'Link to ISO 3166-2': 'ISO 3166-2:BI', 'Independent': 'Yes'},
"Cabo Verde" : {'Alpha-2': 'CV', 'Alpha-3': 'CPV', 'Numeric code': '132', 'Link to ISO 3166-2': 'ISO 3166-2:CV', 'Independent': 'Yes'},
"Cambodia" : {'Alpha-2': 'KH', 'Alpha-3': 'KHM', 'Numeric code': '116', 'Link to ISO 3166-2': 'ISO 3166-2:KH', 'Independent': 'Yes'},
"Cameroon" : {'Alpha-2': 'CM', 'Alpha-3': 'CMR', 'Numeric code': '120', 'Link to ISO 3166-2': 'ISO 3166-2:CM', 'Independent': 'Yes'},
"Canada" : {'Alpha-2': 'CA', 'Alpha-3': 'CAN', 'Numeric code': '124', 'Link to ISO 3166-2': 'ISO 3166-2:CA', 'Independent': 'Yes'},
"Cayman Islands" : {'Alpha-2': 'KY', 'Alpha-3': 'CYM', 'Numeric code': '136', 'Link to ISO 3166-2': 'ISO 3166-2:KY', 'Independent': 'No'},
"Central African Republic" : {'Alpha-2': 'CF', 'Alpha-3': 'CAF', 'Numeric code': '140', 'Link to ISO 3166-2': 'ISO 3166-2:CF', 'Independent': 'Yes'},
"Chad" : {'Alpha-2': 'TD', 'Alpha-3': 'TCD', 'Numeric code': '148', 'Link to ISO 3166-2': 'ISO 3166-2:TD', 'Independent': 'Yes'},
"Chile" : {'Alpha-2': 'CL', 'Alpha-3': 'CHL', 'Numeric code': '152', 'Link to ISO 3166-2': 'ISO 3166-2:CL', 'Independent': 'Yes'},
"China" : {'Alpha-2': 'CN', 'Alpha-3': 'CHN', 'Numeric code': '156', 'Link to ISO 3166-2': 'ISO 3166-2:CN', 'Independent': 'Yes'},
"Christmas Island" : {'Alpha-2': 'CX', 'Alpha-3': 'CXR', 'Numeric code': '162', 'Link to ISO 3166-2': 'ISO 3166-2:CX', 'Independent': 'No'},
"Cocos (Keeling) Islands" : {'Alpha-2': 'CC', 'Alpha-3': 'CCK', 'Numeric code': '166', 'Link to ISO 3166-2': 'ISO 3166-2:CC', 'Independent': 'No'},
"Colombia" : {'Alpha-2': 'CO', 'Alpha-3': 'COL', 'Numeric code': '170', 'Link to ISO 3166-2': 'ISO 3166-2:CO', 'Independent': 'Yes'},
"Comoros" : {'Alpha-2': 'KM', 'Alpha-3': 'COM', 'Numeric code': '174', 'Link to ISO 3166-2': 'ISO 3166-2:KM', 'Independent': 'Yes'},
"Congo" : {'Alpha-2': 'CG', 'Alpha-3': 'COG', 'Numeric code': '178', 'Link to ISO 3166-2': 'ISO 3166-2:CG', 'Independent': 'Yes'},
"Congo, Democratic Republic of the" : {'Alpha-2': 'CD', 'Alpha-3': 'COD', 'Numeric code': '180', 'Link to ISO 3166-2': 'ISO 3166-2:CD', 'Independent': 'Yes'},
"Cook Islands" : {'Alpha-2': 'CK', 'Alpha-3': 'COK', 'Numeric code': '184', 'Link to ISO 3166-2': 'ISO 3166-2:CK', 'Independent': 'No'},
"Costa Rica" : {'Alpha-2': 'CR', 'Alpha-3': 'CRI', 'Numeric code': '188', 'Link to ISO 3166-2': 'ISO 3166-2:CR', 'Independent': 'Yes'},
"Côte d'Ivoire" : {'Alpha-2': 'CI', 'Alpha-3': 'CIV', 'Numeric code': '384', 'Link to ISO 3166-2': 'ISO 3166-2:CI', 'Independent': 'Yes'},
"Croatia" : {'Alpha-2': 'HR', 'Alpha-3': 'HRV', 'Numeric code': '191', 'Link to ISO 3166-2': 'ISO 3166-2:HR', 'Independent': 'Yes'},
"Cuba" : {'Alpha-2': 'CU', 'Alpha-3': 'CUB', 'Numeric code': '192', 'Link to ISO 3166-2': 'ISO 3166-2:CU', 'Independent': 'Yes'},
"Curaçao" : {'Alpha-2': 'CW', 'Alpha-3': 'CUW', 'Numeric code': '531', 'Link to ISO 3166-2': 'ISO 3166-2:CW', 'Independent': 'No'},
"Cyprus" : {'Alpha-2': 'CY', 'Alpha-3': 'CYP', 'Numeric code': '196', 'Link to ISO 3166-2': 'ISO 3166-2:CY', 'Independent': 'Yes'},
"Czechia" : {'Alpha-2': 'CZ', 'Alpha-3': 'CZE', 'Numeric code': '203', 'Link to ISO 3166-2': 'ISO 3166-2:CZ', 'Independent': 'Yes'},
"Denmark" : {'Alpha-2': 'DK', 'Alpha-3': 'DNK', 'Numeric code': '208', 'Link to ISO 3166-2': 'ISO 3166-2:DK', 'Independent': 'Yes'},
"Djibouti" : {'Alpha-2': 'DJ', 'Alpha-3': 'DJI', 'Numeric code': '262', 'Link to ISO 3166-2': 'ISO 3166-2:DJ', 'Independent': 'Yes'},
"Dominica" : {'Alpha-2': 'DM', 'Alpha-3': 'DMA', 'Numeric code': '212', 'Link to ISO 3166-2': 'ISO 3166-2:DM', 'Independent': 'Yes'},
"Dominican Republic" : {'Alpha-2': 'DO', 'Alpha-3': 'DOM', 'Numeric code': '214', 'Link to ISO 3166-2': 'ISO 3166-2:DO', 'Independent': 'Yes'},
"Ecuador" : {'Alpha-2': 'EC', 'Alpha-3': 'ECU', 'Numeric code': '218', 'Link to ISO 3166-2': 'ISO 3166-2:EC', 'Independent': 'Yes'},
"Egypt" : {'Alpha-2': 'EG', 'Alpha-3': 'EGY', 'Numeric code': '818', 'Link to ISO 3166-2': 'ISO 3166-2:EG', 'Independent': 'Yes'},
"El Salvador" : {'Alpha-2': 'SV', 'Alpha-3': 'SLV', 'Numeric code': '222', 'Link to ISO 3166-2': 'ISO 3166-2:SV', 'Independent': 'Yes'},
"Equatorial Guinea" : {'Alpha-2': 'GQ', 'Alpha-3': 'GNQ', 'Numeric code': '226', 'Link to ISO 3166-2': 'ISO 3166-2:GQ', 'Independent': 'Yes'},
"Eritrea" : {'Alpha-2': 'ER', 'Alpha-3': 'ERI', 'Numeric code': '232', 'Link to ISO 3166-2': 'ISO 3166-2:ER', 'Independent': 'Yes'},
"Estonia" : {'Alpha-2': 'EE', 'Alpha-3': 'EST', 'Numeric code': '233', 'Link to ISO 3166-2': 'ISO 3166-2:EE', 'Independent': 'Yes'},
"Eswatini" : {'Alpha-2': 'SZ', 'Alpha-3': 'SWZ', 'Numeric code': '748', 'Link to ISO 3166-2': 'ISO 3166-2:SZ', 'Independent': 'Yes'},
"Ethiopia" : {'Alpha-2': 'ET', 'Alpha-3': 'ETH', 'Numeric code': '231', 'Link to ISO 3166-2': 'ISO 3166-2:ET', 'Independent': 'Yes'},
"Falkland Islands (Malvinas)" : {'Alpha-2': 'FK', 'Alpha-3': 'FLK', 'Numeric code': '238', 'Link to ISO 3166-2': 'ISO 3166-2:FK', 'Independent': 'No'},
"Faroe Islands" : {'Alpha-2': 'FO', 'Alpha-3': 'FRO', 'Numeric code': '234', 'Link to ISO 3166-2': 'ISO 3166-2:FO', 'Independent': 'No'},
"Fiji" : {'Alpha-2': 'FJ', 'Alpha-3': 'FJI', 'Numeric code': '242', 'Link to ISO 3166-2': 'ISO 3166-2:FJ', 'Independent': 'Yes'},
"Finland" : {'Alpha-2': 'FI', 'Alpha-3': 'FIN', 'Numeric code': '246', 'Link to ISO 3166-2': 'ISO 3166-2:FI', 'Independent': 'Yes'},
"France" : {'Alpha-2': 'FR', 'Alpha-3': 'FRA', 'Numeric code': '250', 'Link to ISO 3166-2': 'ISO 3166-2:FR', 'Independent': 'Yes'},
"French Guiana" : {'Alpha-2': 'GF', 'Alpha-3': 'GUF', 'Numeric code': '254', 'Link to ISO 3166-2': 'ISO 3166-2:GF', 'Independent': 'No'},
"French Polynesia" : {'Alpha-2': 'PF', 'Alpha-3': 'PYF', 'Numeric code': '258', 'Link to ISO 3166-2': 'ISO 3166-2:PF', 'Independent': 'No'},
"French Southern Territories" : {'Alpha-2': 'TF', 'Alpha-3': 'ATF', 'Numeric code': '260', 'Link to ISO 3166-2': 'ISO 3166-2:TF', 'Independent': 'No'},
"Gabon" : {'Alpha-2': 'GA', 'Alpha-3': 'GAB', 'Numeric code': '266', 'Link to ISO 3166-2': 'ISO 3166-2:GA', 'Independent': 'Yes'},
"Gambia" : {'Alpha-2': 'GM', 'Alpha-3': 'GMB', 'Numeric code': '270', 'Link to ISO 3166-2': 'ISO 3166-2:GM', 'Independent': 'Yes'},
"Georgia" : {'Alpha-2': 'GE', 'Alpha-3': 'GEO', 'Numeric code': '268', 'Link to ISO 3166-2': 'ISO 3166-2:GE', 'Independent': 'Yes'},
"Germany" : {'Alpha-2': 'DE', 'Alpha-3': 'DEU', 'Numeric code': '276', 'Link to ISO 3166-2': 'ISO 3166-2:DE', 'Independent': 'Yes'},
"Ghana" : {'Alpha-2': 'GH', 'Alpha-3': 'GHA', 'Numeric code': '288', 'Link to ISO 3166-2': 'ISO 3166-2:GH', 'Independent': 'Yes'},
"Gibraltar" : {'Alpha-2': 'GI', 'Alpha-3': 'GIB', 'Numeric code': '292', 'Link to ISO 3166-2': 'ISO 3166-2:GI', 'Independent': 'No'},
"Greece" : {'Alpha-2': 'GR', 'Alpha-3': 'GRC', 'Numeric code': '300', 'Link to ISO 3166-2': 'ISO 3166-2:GR', 'Independent': 'Yes'},
"Greenland" : {'Alpha-2': 'GL', 'Alpha-3': 'GRL', 'Numeric code': '304', 'Link to ISO 3166-2': 'ISO 3166-2:GL', 'Independent': 'No'},
"Grenada" : {'Alpha-2': 'GD', 'Alpha-3': 'GRD', 'Numeric code': '308', 'Link to ISO 3166-2': 'ISO 3166-2:GD', 'Independent': 'Yes'},
"Guadeloupe" : {'Alpha-2': 'GP', 'Alpha-3': 'GLP', 'Numeric code': '312', 'Link to ISO 3166-2': 'ISO 3166-2:GP', 'Independent': 'No'},
"Guam" : {'Alpha-2': 'GU', 'Alpha-3': 'GUM', 'Numeric code': '316', 'Link to ISO 3166-2': 'ISO 3166-2:GU', 'Independent': 'No'},
"Guatemala" : {'Alpha-2': 'GT', 'Alpha-3': 'GTM', 'Numeric code': '320', 'Link to ISO 3166-2': 'ISO 3166-2:GT', 'Independent': 'Yes'},
"Guernsey" : {'Alpha-2': 'GG', 'Alpha-3': 'GGY', 'Numeric code': '831', 'Link to ISO 3166-2': 'ISO 3166-2:GG', 'Independent': 'No'},
"Guinea" : {'Alpha-2': 'GN', 'Alpha-3': 'GIN', 'Numeric code': '324', 'Link to ISO 3166-2': 'ISO 3166-2:GN', 'Independent': 'Yes'},
"Guinea-Bissau" : {'Alpha-2': 'GW', 'Alpha-3': 'GNB', 'Numeric code': '624', 'Link to ISO 3166-2': 'ISO 3166-2:GW', 'Independent': 'Yes'},
"Guyana" : {'Alpha-2': 'GY', 'Alpha-3': 'GUY', 'Numeric code': '328', 'Link to ISO 3166-2': 'ISO 3166-2:GY', 'Independent': 'Yes'},
"Haiti" : {'Alpha-2': 'HT', 'Alpha-3': 'HTI', 'Numeric code': '332', 'Link to ISO 3166-2': 'ISO 3166-2:HT', 'Independent': 'Yes'},
"Heard Island and McDonald Islands" : {'Alpha-2': 'HM', 'Alpha-3': 'HMD', 'Numeric code': '334', 'Link to ISO 3166-2': 'ISO 3166-2:HM', 'Independent': 'No'},
"Holy See" : {'Alpha-2': 'VA', 'Alpha-3': 'VAT', 'Numeric code': '336', 'Link to ISO 3166-2': 'ISO 3166-2:VA', 'Independent': 'Yes'},
"Honduras" : {'Alpha-2': 'HN', 'Alpha-3': 'HND', 'Numeric code': '340', 'Link to ISO 3166-2': 'ISO 3166-2:HN', 'Independent': 'Yes'},
"Hong Kong" : {'Alpha-2': 'HK', 'Alpha-3': 'HKG', 'Numeric code': '344', 'Link to ISO 3166-2': 'ISO 3166-2:HK', 'Independent': 'No'},
"Hungary" : {'Alpha-2': 'HU', 'Alpha-3': 'HUN', 'Numeric code': '348', 'Link to ISO 3166-2': 'ISO 3166-2:HU', 'Independent': 'Yes'},
"Iceland" : {'Alpha-2': 'IS', 'Alpha-3': 'ISL', 'Numeric code': '352', 'Link to ISO 3166-2': 'ISO 3166-2:IS', 'Independent': 'Yes'},
"India" : {'Alpha-2': 'IN', 'Alpha-3': 'IND', 'Numeric code': '356', 'Link to ISO 3166-2': 'ISO 3166-2:IN', 'Independent': 'Yes'},
"Indonesia" : {'Alpha-2': 'ID', 'Alpha-3': 'IDN', 'Numeric code': '360', 'Link to ISO 3166-2': 'ISO 3166-2:ID', 'Independent': 'Yes'},
"Iran (Islamic Republic of)" : {'Alpha-2': 'IR', 'Alpha-3': 'IRN', 'Numeric code': '364', 'Link to ISO 3166-2': 'ISO 3166-2:IR', 'Independent': 'Yes'},
"Iraq" : {'Alpha-2': 'IQ', 'Alpha-3': 'IRQ', 'Numeric code': '368', 'Link to ISO 3166-2': 'ISO 3166-2:IQ', 'Independent': 'Yes'},
"Ireland" : {'Alpha-2': 'IE', 'Alpha-3': 'IRL', 'Numeric code': '372', 'Link to ISO 3166-2': 'ISO 3166-2:IE', 'Independent': 'Yes'},
"Isle of Man" : {'Alpha-2': 'IM', 'Alpha-3': 'IMN', 'Numeric code': '833', 'Link to ISO 3166-2': 'ISO 3166-2:IM', 'Independent': 'No'},
"Israel" : {'Alpha-2': 'IL', 'Alpha-3': 'ISR', 'Numeric code': '376', 'Link to ISO 3166-2': 'ISO 3166-2:IL', 'Independent': 'Yes'},
"Italy" : {'Alpha-2': 'IT', 'Alpha-3': 'ITA', 'Numeric code': '380', 'Link to ISO 3166-2': 'ISO 3166-2:IT', 'Independent': 'Yes'},
"Jamaica" : {'Alpha-2': 'JM', 'Alpha-3': 'JAM', 'Numeric code': '388', 'Link to ISO 3166-2': 'ISO 3166-2:JM', 'Independent': 'Yes'},
"Japan" : {'Alpha-2': 'JP', 'Alpha-3': 'JPN', 'Numeric code': '392', 'Link to ISO 3166-2': 'ISO 3166-2:JP', 'Independent': 'Yes'},
"Jersey" : {'Alpha-2': 'JE', 'Alpha-3': 'JEY', 'Numeric code': '832', 'Link to ISO 3166-2': 'ISO 3166-2:JE', 'Independent': 'No'},
"Jordan" : {'Alpha-2': 'JO', 'Alpha-3': 'JOR', 'Numeric code': '400', 'Link to ISO 3166-2': 'ISO 3166-2:JO', 'Independent': 'Yes'},
"Kazakhstan" : {'Alpha-2': 'KZ', 'Alpha-3': 'KAZ', 'Numeric code': '398', 'Link to ISO 3166-2': 'ISO 3166-2:KZ', 'Independent': 'Yes'},
"Kenya" : {'Alpha-2': 'KE', 'Alpha-3': 'KEN', 'Numeric code': '404', 'Link to ISO 3166-2': 'ISO 3166-2:KE', 'Independent': 'Yes'},
"Kiribati" : {'Alpha-2': 'KI', 'Alpha-3': 'KIR', 'Numeric code': '296', 'Link to ISO 3166-2': 'ISO 3166-2:KI', 'Independent': 'Yes'},
"Korea (Democratic People's Republic of)" : {'Alpha-2': 'KP', 'Alpha-3': 'PRK', 'Numeric code': '408', 'Link to ISO 3166-2': 'ISO 3166-2:KP', 'Independent': 'Yes'},
"Korea, Republic of" : {'Alpha-2': 'KR', 'Alpha-3': 'KOR', 'Numeric code': '410', 'Link to ISO 3166-2': 'ISO 3166-2:KR', 'Independent': 'Yes'},
"Kuwait" : {'Alpha-2': 'KW', 'Alpha-3': 'KWT', 'Numeric code': '414', 'Link to ISO 3166-2': 'ISO 3166-2:KW', 'Independent': 'Yes'},
"Kyrgyzstan" : {'Alpha-2': 'KG', 'Alpha-3': 'KGZ', 'Numeric code': '417', 'Link to ISO 3166-2': 'ISO 3166-2:KG', 'Independent': 'Yes'},
"Lao People's Democratic Republic" : {'Alpha-2': 'LA', 'Alpha-3': 'LAO', 'Numeric code': '418', 'Link to ISO 3166-2': 'ISO 3166-2:LA', 'Independent': 'Yes'},
"Latvia" : {'Alpha-2': 'LV', 'Alpha-3': 'LVA', 'Numeric code': '428', 'Link to ISO 3166-2': 'ISO 3166-2:LV', 'Independent': 'Yes'},
"Lebanon" : {'Alpha-2': 'LB', 'Alpha-3': 'LBN', 'Numeric code': '422', 'Link to ISO 3166-2': 'ISO 3166-2:LB', 'Independent': 'Yes'},
"Lesotho" : {'Alpha-2': 'LS', 'Alpha-3': 'LSO', 'Numeric code': '426', 'Link to ISO 3166-2': 'ISO 3166-2:LS', 'Independent': 'Yes'},
"Liberia" : {'Alpha-2': 'LR', 'Alpha-3': 'LBR', 'Numeric code': '430', 'Link to ISO 3166-2': 'ISO 3166-2:LR', 'Independent': 'Yes'},
"Libya" : {'Alpha-2': 'LY', 'Alpha-3': 'LBY', 'Numeric code': '434', 'Link to ISO 3166-2': 'ISO 3166-2:LY', 'Independent': 'Yes'},
"Liechtenstein" : {'Alpha-2': 'LI', 'Alpha-3': 'LIE', 'Numeric code': '438', 'Link to ISO 3166-2': 'ISO 3166-2:LI', 'Independent': 'Yes'},
"Lithuania" : {'Alpha-2': 'LT', 'Alpha-3': 'LTU', 'Numeric code': '440', 'Link to ISO 3166-2': 'ISO 3166-2:LT', 'Independent': 'Yes'},
"Luxembourg" : {'Alpha-2': 'LU', 'Alpha-3': 'LUX', 'Numeric code': '442', 'Link to ISO 3166-2': 'ISO 3166-2:LU', 'Independent': 'Yes'},
"Macao" : {'Alpha-2': 'MO', 'Alpha-3': 'MAC', 'Numeric code': '446', 'Link to ISO 3166-2': 'ISO 3166-2:MO', 'Independent': 'No'},
"Madagascar" : {'Alpha-2': 'MG', 'Alpha-3': 'MDG', 'Numeric code': '450', 'Link to ISO 3166-2': 'ISO 3166-2:MG', 'Independent': 'Yes'},
"Malawi" : {'Alpha-2': 'MW', 'Alpha-3': 'MWI', 'Numeric code': '454', 'Link to ISO 3166-2': 'ISO 3166-2:MW', 'Independent': 'Yes'},
"Malaysia" : {'Alpha-2': 'MY', 'Alpha-3': 'MYS', 'Numeric code': '458', 'Link to ISO 3166-2': 'ISO 3166-2:MY', 'Independent': 'Yes'},
"Maldives" : {'Alpha-2': 'MV', 'Alpha-3': 'MDV', 'Numeric code': '462', 'Link to ISO 3166-2': 'ISO 3166-2:MV', 'Independent': 'Yes'},
"Mali" : {'Alpha-2': 'ML', 'Alpha-3': 'MLI', 'Numeric code': '466', 'Link to ISO 3166-2': 'ISO 3166-2:ML', 'Independent': 'Yes'},
"Malta" : {'Alpha-2': 'MT', 'Alpha-3': 'MLT', 'Numeric code': '470', 'Link to ISO 3166-2': 'ISO 3166-2:MT', 'Independent': 'Yes'},
"Marshall Islands" : {'Alpha-2': 'MH', 'Alpha-3': 'MHL', 'Numeric code': '584', 'Link to ISO 3166-2': 'ISO 3166-2:MH', 'Independent': 'Yes'},
"Martinique" : {'Alpha-2': 'MQ', 'Alpha-3': 'MTQ', 'Numeric code': '474', 'Link to ISO 3166-2': 'ISO 3166-2:MQ', 'Independent': 'No'},
"Mauritania" : {'Alpha-2': 'MR', 'Alpha-3': 'MRT', 'Numeric code': '478', 'Link to ISO 3166-2': 'ISO 3166-2:MR', 'Independent': 'Yes'},
"Mauritius" : {'Alpha-2': 'MU', 'Alpha-3': 'MUS', 'Numeric code': '480', 'Link to ISO 3166-2': 'ISO 3166-2:MU', 'Independent': 'Yes'},
"Mayotte" : {'Alpha-2': 'YT', 'Alpha-3': 'MYT', 'Numeric code': '175', 'Link to ISO 3166-2': 'ISO 3166-2:YT', 'Independent': 'No'},
"Mexico" : {'Alpha-2': 'MX', 'Alpha-3': 'MEX', 'Numeric code': '484', 'Link to ISO 3166-2': 'ISO 3166-2:MX', 'Independent': 'Yes'},
"Micronesia (Federated States of)" : {'Alpha-2': 'FM', 'Alpha-3': 'FSM', 'Numeric code': '583', 'Link to ISO 3166-2': 'ISO 3166-2:FM', 'Independent': 'Yes'},
"Moldova, Republic of" : {'Alpha-2': 'MD', 'Alpha-3': 'MDA', 'Numeric code': '498', 'Link to ISO 3166-2': 'ISO 3166-2:MD', 'Independent': 'Yes'},
"Monaco" : {'Alpha-2': 'MC', 'Alpha-3': 'MCO', 'Numeric code': '492', 'Link to ISO 3166-2': 'ISO 3166-2:MC', 'Independent': 'Yes'},
"Mongolia" : {'Alpha-2': 'MN', 'Alpha-3': 'MNG', 'Numeric code': '496', 'Link to ISO 3166-2': 'ISO 3166-2:MN', 'Independent': 'Yes'},
"Montenegro" : {'Alpha-2': 'ME', 'Alpha-3': 'MNE', 'Numeric code': '499', 'Link to ISO 3166-2': 'ISO 3166-2:ME', 'Independent': 'Yes'},
"Montserrat" : {'Alpha-2': 'MS', 'Alpha-3': 'MSR', 'Numeric code': '500', 'Link to ISO 3166-2': 'ISO 3166-2:MS', 'Independent': 'No'},
"Morocco" : {'Alpha-2': 'MA', 'Alpha-3': 'MAR', 'Numeric code': '504', 'Link to ISO 3166-2': 'ISO 3166-2:MA', 'Independent': 'Yes'},
"Mozambique" : {'Alpha-2': 'MZ', 'Alpha-3': 'MOZ', 'Numeric code': '508', 'Link to ISO 3166-2': 'ISO 3166-2:MZ', 'Independent': 'Yes'},
"Myanmar" : {'Alpha-2': 'MM', 'Alpha-3': 'MMR', 'Numeric code': '104', 'Link to ISO 3166-2': 'ISO 3166-2:MM', 'Independent': 'Yes'},
"Namibia" : {'Alpha-2': 'NA', 'Alpha-3': 'NAM', 'Numeric code': '516', 'Link to ISO 3166-2': 'ISO 3166-2:NA', 'Independent': 'Yes'},
"Nauru" : {'Alpha-2': 'NR', 'Alpha-3': 'NRU', 'Numeric code': '520', 'Link to ISO 3166-2': 'ISO 3166-2:NR', 'Independent': 'Yes'},
"Nepal" : {'Alpha-2': 'NP', 'Alpha-3': 'NPL', 'Numeric code': '524', 'Link to ISO 3166-2': 'ISO 3166-2:NP', 'Independent': 'Yes'},
"Netherlands" : {'Alpha-2': 'NL', 'Alpha-3': 'NLD', 'Numeric code': '528', 'Link to ISO 3166-2': 'ISO 3166-2:NL', 'Independent': 'Yes'},
"New Caledonia" : {'Alpha-2': 'NC', 'Alpha-3': 'NCL', 'Numeric code': '540', 'Link to ISO 3166-2': 'ISO 3166-2:NC', 'Independent': 'No'},
"New Zealand" : {'Alpha-2': 'NZ', 'Alpha-3': 'NZL', 'Numeric code': '554', 'Link to ISO 3166-2': 'ISO 3166-2:NZ', 'Independent': 'Yes'},
"Nicaragua" : {'Alpha-2': 'NI', 'Alpha-3': 'NIC', 'Numeric code': '558', 'Link to ISO 3166-2': 'ISO 3166-2:NI', 'Independent': 'Yes'},
"Niger" : {'Alpha-2': 'NE', 'Alpha-3': 'NER', 'Numeric code': '562', 'Link to ISO 3166-2': 'ISO 3166-2:NE', 'Independent': 'Yes'},
"Nigeria" : {'Alpha-2': 'NG', 'Alpha-3': 'NGA', 'Numeric code': '566', 'Link to ISO 3166-2': 'ISO 3166-2:NG', 'Independent': 'Yes'},
"Niue" : {'Alpha-2': 'NU', 'Alpha-3': 'NIU', 'Numeric code': '570', 'Link to ISO 3166-2': 'ISO 3166-2:NU', 'Independent': 'No'},
"Norfolk Island" : {'Alpha-2': 'NF', 'Alpha-3': 'NFK', 'Numeric code': '574', 'Link to ISO 3166-2': 'ISO 3166-2:NF', 'Independent': 'No'},
"North Macedonia" : {'Alpha-2': 'MK', 'Alpha-3': 'MKD', 'Numeric code': '807', 'Link to ISO 3166-2': 'ISO 3166-2:MK', 'Independent': 'Yes'},
"Northern Mariana Islands" : {'Alpha-2': 'MP', 'Alpha-3': 'MNP', 'Numeric code': '580', 'Link to ISO 3166-2': 'ISO 3166-2:MP', 'Independent': 'No'},
"Norway" : {'Alpha-2': 'NO', 'Alpha-3': 'NOR', 'Numeric code': '578', 'Link to ISO 3166-2': 'ISO 3166-2:NO', 'Independent': 'Yes'},
"Oman" : {'Alpha-2': 'OM', 'Alpha-3': 'OMN', 'Numeric code': '512', 'Link to ISO 3166-2': 'ISO 3166-2:OM', 'Independent': 'Yes'},
"Pakistan" : {'Alpha-2': 'PK', 'Alpha-3': 'PAK', 'Numeric code': '586', 'Link to ISO 3166-2': 'ISO 3166-2:PK', 'Independent': 'Yes'},
"Palau" : {'Alpha-2': 'PW', 'Alpha-3': 'PLW', 'Numeric code': '585', 'Link to ISO 3166-2': 'ISO 3166-2:PW', 'Independent': 'Yes'},
"Palestine, State of" : {'Alpha-2': 'PS', 'Alpha-3': 'PSE', 'Numeric code': '275', 'Link to ISO 3166-2': 'ISO 3166-2:PS', 'Independent': 'No'},
"Panama" : {'Alpha-2': 'PA', 'Alpha-3': 'PAN', 'Numeric code': '591', 'Link to ISO 3166-2': 'ISO 3166-2:PA', 'Independent': 'Yes'},
"Papua New Guinea" : {'Alpha-2': 'PG', 'Alpha-3': 'PNG', 'Numeric code': '598', 'Link to ISO 3166-2': 'ISO 3166-2:PG', 'Independent': 'Yes'},
"Paraguay" : {'Alpha-2': 'PY', 'Alpha-3': 'PRY', 'Numeric code': '600', 'Link to ISO 3166-2': 'ISO 3166-2:PY', 'Independent': 'Yes'},
"Peru" : {'Alpha-2': 'PE', 'Alpha-3': 'PER', 'Numeric code': '604', 'Link to ISO 3166-2': 'ISO 3166-2:PE', 'Independent': 'Yes'},
"Philippines" : {'Alpha-2': 'PH', 'Alpha-3': 'PHL', 'Numeric code': '608', 'Link to ISO 3166-2': 'ISO 3166-2:PH', 'Independent': 'Yes'},
"Pitcairn" : {'Alpha-2': 'PN', 'Alpha-3': 'PCN', 'Numeric code': '612', 'Link to ISO 3166-2': 'ISO 3166-2:PN', 'Independent': 'No'},
"Poland" : {'Alpha-2': 'PL', 'Alpha-3': 'POL', 'Numeric code': '616', 'Link to ISO 3166-2': 'ISO 3166-2:PL', 'Independent': 'Yes'},
"Portugal" : {'Alpha-2': 'PT', 'Alpha-3': 'PRT', 'Numeric code': '620', 'Link to ISO 3166-2': 'ISO 3166-2:PT', 'Independent': 'Yes'},
"Puerto Rico" : {'Alpha-2': 'PR', 'Alpha-3': 'PRI', 'Numeric code': '630', 'Link to ISO 3166-2': 'ISO 3166-2:PR', 'Independent': 'No'},
"Qatar" : {'Alpha-2': 'QA', 'Alpha-3': 'QAT', 'Numeric code': '634', 'Link to ISO 3166-2': 'ISO 3166-2:QA', 'Independent': 'Yes'},
"Réunion" : {'Alpha-2': 'RE', 'Alpha-3': 'REU', 'Numeric code': '638', 'Link to ISO 3166-2': 'ISO 3166-2:RE', 'Independent': 'No'},
"Romania" : {'Alpha-2': 'RO', 'Alpha-3': 'ROU', 'Numeric code': '642', 'Link to ISO 3166-2': 'ISO 3166-2:RO', 'Independent': 'Yes'},
"Russian Federation" : {'Alpha-2': 'RU', 'Alpha-3': 'RUS', 'Numeric code': '643', 'Link to ISO 3166-2': 'ISO 3166-2:RU', 'Independent': 'Yes'},
"Rwanda" : {'Alpha-2': 'RW', 'Alpha-3': 'RWA', 'Numeric code': '646', 'Link to ISO 3166-2': 'ISO 3166-2:RW', 'Independent': 'Yes'},
"Saint Barthélemy" : {'Alpha-2': 'BL', 'Alpha-3': 'BLM', 'Numeric code': '652', 'Link to ISO 3166-2': 'ISO 3166-2:BL', 'Independent': 'No'},
"Saint Helena, Ascension and Tristan da Cunha" : {'Alpha-2': 'SH', 'Alpha-3': 'SHN', 'Numeric code': '654', 'Link to ISO 3166-2': 'ISO 3166-2:SH', 'Independent': 'No'},
"Saint Kitts and Nevis" : {'Alpha-2': 'KN', 'Alpha-3': 'KNA', 'Numeric code': '659', 'Link to ISO 3166-2': 'ISO 3166-2:KN', 'Independent': 'Yes'},
"Saint Lucia" : {'Alpha-2': 'LC', 'Alpha-3': 'LCA', 'Numeric code': '662', 'Link to ISO 3166-2': 'ISO 3166-2:LC', 'Independent': 'Yes'},
"Saint Martin (French part)" : {'Alpha-2': 'MF', 'Alpha-3': 'MAF', 'Numeric code': '663', 'Link to ISO 3166-2': 'ISO 3166-2:MF', 'Independent': 'No'},
"Saint Pierre and Miquelon" : {'Alpha-2': 'PM', 'Alpha-3': 'SPM', 'Numeric code': '666', 'Link to ISO 3166-2': 'ISO 3166-2:PM', 'Independent': 'No'},
"Saint Vincent and the Grenadines" : {'Alpha-2': 'VC', 'Alpha-3': 'VCT', 'Numeric code': '670', 'Link to ISO 3166-2': 'ISO 3166-2:VC', 'Independent': 'Yes'},
"Samoa" : {'Alpha-2': 'WS', 'Alpha-3': 'WSM', 'Numeric code': '882', 'Link to ISO 3166-2': 'ISO 3166-2:WS', 'Independent': 'Yes'},
"San Marino" : {'Alpha-2': 'SM', 'Alpha-3': 'SMR', 'Numeric code': '674', 'Link to ISO 3166-2': 'ISO 3166-2:SM', 'Independent': 'Yes'},
"Sao Tome and Principe" : {'Alpha-2': 'ST', 'Alpha-3': 'STP', 'Numeric code': '678', 'Link to ISO 3166-2': 'ISO 3166-2:ST', 'Independent': 'Yes'},
"Saudi Arabia" : {'Alpha-2': 'SA', 'Alpha-3': 'SAU', 'Numeric code': '682', 'Link to ISO 3166-2': 'ISO 3166-2:SA', 'Independent': 'Yes'},
"Senegal" : {'Alpha-2': 'SN', 'Alpha-3': 'SEN', 'Numeric code': '686', 'Link to ISO 3166-2': 'ISO 3166-2:SN', 'Independent': 'Yes'},
"Serbia" : {'Alpha-2': 'RS', 'Alpha-3': 'SRB', 'Numeric code': '688', 'Link to ISO 3166-2': 'ISO 3166-2:RS', 'Independent': 'Yes'},
"Seychelles" : {'Alpha-2': 'SC', 'Alpha-3': 'SYC', 'Numeric code': '690', 'Link to ISO 3166-2': 'ISO 3166-2:SC', 'Independent': 'Yes'},
"Sierra Leone" : {'Alpha-2': 'SL', 'Alpha-3': 'SLE', 'Numeric code': '694', 'Link to ISO 3166-2': 'ISO 3166-2:SL', 'Independent': 'Yes'},
"Singapore" : {'Alpha-2': 'SG', 'Alpha-3': 'SGP', 'Numeric code': '702', 'Link to ISO 3166-2': 'ISO 3166-2:SG', 'Independent': 'Yes'},
"Sint Maarten (Dutch part)" : {'Alpha-2': 'SX', 'Alpha-3': 'SXM', 'Numeric code': '534', 'Link to ISO 3166-2': 'ISO 3166-2:SX', 'Independent': 'No'},
"Slovakia" : {'Alpha-2': 'SK', 'Alpha-3': 'SVK', 'Numeric code': '703', 'Link to ISO 3166-2': 'ISO 3166-2:SK', 'Independent': 'Yes'},
"Slovenia" : {'Alpha-2': 'SI', 'Alpha-3': 'SVN', 'Numeric code': '705', 'Link to ISO 3166-2': 'ISO 3166-2:SI', 'Independent': 'Yes'},
"Solomon Islands" : {'Alpha-2': 'SB', 'Alpha-3': 'SLB', 'Numeric code': '090', 'Link to ISO 3166-2': 'ISO 3166-2:SB', 'Independent': 'Yes'},
"Somalia" : {'Alpha-2': 'SO', 'Alpha-3': 'SOM', 'Numeric code': '706', 'Link to ISO 3166-2': 'ISO 3166-2:SO', 'Independent': 'Yes'},
"South Africa" : {'Alpha-2': 'ZA', 'Alpha-3': 'ZAF', 'Numeric code': '710', 'Link to ISO 3166-2': 'ISO 3166-2:ZA', 'Independent': 'Yes'},
"South Georgia and the South Sandwich Islands" : {'Alpha-2': 'GS', 'Alpha-3': 'SGS', 'Numeric code': '239', 'Link to ISO 3166-2': 'ISO 3166-2:GS', 'Independent': 'No'},
"South Sudan" : {'Alpha-2': 'SS', 'Alpha-3': 'SSD', 'Numeric code': '728', 'Link to ISO 3166-2': 'ISO 3166-2:SS', 'Independent': 'Yes'},
"Spain" : {'Alpha-2': 'ES', 'Alpha-3': 'ESP', 'Numeric code': '724', 'Link to ISO 3166-2': 'ISO 3166-2:ES', 'Independent': 'Yes'},
"Sri Lanka" : {'Alpha-2': 'LK', 'Alpha-3': 'LKA', 'Numeric code': '144', 'Link to ISO 3166-2': 'ISO 3166-2:LK', 'Independent': 'Yes'},
"Sudan" : {'Alpha-2': 'SD', 'Alpha-3': 'SDN', 'Numeric code': '729', 'Link to ISO 3166-2': 'ISO 3166-2:SD', 'Independent': 'Yes'},
"Suriname" : {'Alpha-2': 'SR', 'Alpha-3': 'SUR', 'Numeric code': '740', 'Link to ISO 3166-2': 'ISO 3166-2:SR', 'Independent': 'Yes'},
"Svalbard and Jan Mayen" : {'Alpha-2': 'SJ', 'Alpha-3': 'SJM', 'Numeric code': '744', 'Link to ISO 3166-2': 'ISO 3166-2:SJ', 'Independent': 'No'},
"Sweden" : {'Alpha-2': 'SE', 'Alpha-3': 'SWE', 'Numeric code': '752', 'Link to ISO 3166-2': 'ISO 3166-2:SE', 'Independent': 'Yes'},
"Switzerland" : {'Alpha-2': 'CH', 'Alpha-3': 'CHE', 'Numeric code': '756', 'Link to ISO 3166-2': 'ISO 3166-2:CH', 'Independent': 'Yes'},
"Syrian Arab Republic" : {'Alpha-2': 'SY', 'Alpha-3': 'SYR', 'Numeric code': '760', 'Link to ISO 3166-2': 'ISO 3166-2:SY', 'Independent': 'Yes'},
"Taiwan, Province of China[a]" : {'Alpha-2': 'TW', 'Alpha-3': 'TWN', 'Numeric code': '158', 'Link to ISO 3166-2': 'ISO 3166-2:TW', 'Independent': 'No'},
"Tajikistan" : {'Alpha-2': 'TJ', 'Alpha-3': 'TJK', 'Numeric code': '762', 'Link to ISO 3166-2': 'ISO 3166-2:TJ', 'Independent': 'Yes'},
"Tanzania, United Republic of" : {'Alpha-2': 'TZ', 'Alpha-3': 'TZA', 'Numeric code': '834', 'Link to ISO 3166-2': 'ISO 3166-2:TZ', 'Independent': 'Yes'},
"Thailand" : {'Alpha-2': 'TH', 'Alpha-3': 'THA', 'Numeric code': '764', 'Link to ISO 3166-2': 'ISO 3166-2:TH', 'Independent': 'Yes'},
"Timor-Leste" : {'Alpha-2': 'TL', 'Alpha-3': 'TLS', 'Numeric code': '626', 'Link to ISO 3166-2': 'ISO 3166-2:TL', 'Independent': 'Yes'},
"Togo" : {'Alpha-2': 'TG', 'Alpha-3': 'TGO', 'Numeric code': '768', 'Link to ISO 3166-2': 'ISO 3166-2:TG', 'Independent': 'Yes'},
"Tokelau" : {'Alpha-2': 'TK', 'Alpha-3': 'TKL', 'Numeric code': '772', 'Link to ISO 3166-2': 'ISO 3166-2:TK', 'Independent': 'No'},
"Tonga" : {'Alpha-2': 'TO', 'Alpha-3': 'TON', 'Numeric code': '776', 'Link to ISO 3166-2': 'ISO 3166-2:TO', 'Independent': 'Yes'},
"Trinidad and Tobago" : {'Alpha-2': 'TT', 'Alpha-3': 'TTO', 'Numeric code': '780', 'Link to ISO 3166-2': 'ISO 3166-2:TT', 'Independent': 'Yes'},
"Tunisia" : {'Alpha-2': 'TN', 'Alpha-3': 'TUN', 'Numeric code': '788', 'Link to ISO 3166-2': 'ISO 3166-2:TN', 'Independent': 'Yes'},
"Turkey" : {'Alpha-2': 'TR', 'Alpha-3': 'TUR', 'Numeric code': '792', 'Link to ISO 3166-2': 'ISO 3166-2:TR', 'Independent': 'Yes'},
"Turkmenistan" : {'Alpha-2': 'TM', 'Alpha-3': 'TKM', 'Numeric code': '795', 'Link to ISO 3166-2': 'ISO 3166-2:TM', 'Independent': 'Yes'},
"Turks and Caicos Islands" : {'Alpha-2': 'TC', 'Alpha-3': 'TCA', 'Numeric code': '796', 'Link to ISO 3166-2': 'ISO 3166-2:TC', 'Independent': 'No'},
"Tuvalu" : {'Alpha-2': 'TV', 'Alpha-3': 'TUV', 'Numeric code': '798', 'Link to ISO 3166-2': 'ISO 3166-2:TV', 'Independent': 'Yes'},
"Uganda" : {'Alpha-2': 'UG', 'Alpha-3': 'UGA', 'Numeric code': '800', 'Link to ISO 3166-2': 'ISO 3166-2:UG', 'Independent': 'Yes'},
"Ukraine" : {'Alpha-2': 'UA', 'Alpha-3': 'UKR', 'Numeric code': '804', 'Link to ISO 3166-2': 'ISO 3166-2:UA', 'Independent': 'Yes'},
"United Arab Emirates" : {'Alpha-2': 'AE', 'Alpha-3': 'ARE', 'Numeric code': '784', 'Link to ISO 3166-2': 'ISO 3166-2:AE', 'Independent': 'Yes'},
"United Kingdom of Great Britain and Northern Ireland" : {'Alpha-2': 'GB', 'Alpha-3': 'GBR', 'Numeric code': '826', 'Link to ISO 3166-2': 'ISO 3166-2:GB', 'Independent': 'Yes'},
"United States of America" : {'Alpha-2': 'US', 'Alpha-3': 'USA', 'Numeric code': '840', 'Link to ISO 3166-2': 'ISO 3166-2:US', 'Independent': 'Yes'},
"United States Minor Outlying Islands" : {'Alpha-2': 'UM', 'Alpha-3': 'UMI', 'Numeric code': '581', 'Link to ISO 3166-2': 'ISO 3166-2:UM', 'Independent': 'No'},
"Uruguay" : {'Alpha-2': 'UY', 'Alpha-3': 'URY', 'Numeric code': '858', 'Link to ISO 3166-2': 'ISO 3166-2:UY', 'Independent': 'Yes'},
"Uzbekistan" : {'Alpha-2': 'UZ', 'Alpha-3': 'UZB', 'Numeric code': '860', 'Link to ISO 3166-2': 'ISO 3166-2:UZ', 'Independent': 'Yes'},
"Vanuatu" : {'Alpha-2': 'VU', 'Alpha-3': 'VUT', 'Numeric code': '548', 'Link to ISO 3166-2': 'ISO 3166-2:VU', 'Independent': 'Yes'},
"Venezuela (Bolivarian Republic of)" : {'Alpha-2': 'VE', 'Alpha-3': 'VEN', 'Numeric code': '862', 'Link to ISO 3166-2': 'ISO 3166-2:VE', 'Independent': 'Yes'},
"Viet Nam" : {'Alpha-2': 'VN', 'Alpha-3': 'VNM', 'Numeric code': '704', 'Link to ISO 3166-2': 'ISO 3166-2:VN', 'Independent': 'Yes'},
"Virgin Islands (British)" : {'Alpha-2': 'VG', 'Alpha-3': 'VGB', 'Numeric code': '092', 'Link to ISO 3166-2': 'ISO 3166-2:VG', 'Independent': 'No'},
"Virgin Islands (U.S.)" : {'Alpha-2': 'VI', 'Alpha-3': 'VIR', 'Numeric code': '850', 'Link to ISO 3166-2': 'ISO 3166-2:VI', 'Independent': 'No'},
"Wallis and Futuna" : {'Alpha-2': 'WF', 'Alpha-3': 'WLF', 'Numeric code': '876', 'Link to ISO 3166-2': 'ISO 3166-2:WF', 'Independent': 'No'},
"Western Sahara" : {'Alpha-2': 'EH', 'Alpha-3': 'ESH', 'Numeric code': '732', 'Link to ISO 3166-2': 'ISO 3166-2:EH', 'Independent': 'No'},
"Yemen" : {'Alpha-2': 'YE', 'Alpha-3': 'YEM', 'Numeric code': '887', 'Link to ISO 3166-2': 'ISO 3166-2:YE', 'Independent': 'Yes'},
"Zambia" : {'Alpha-2': 'ZM', 'Alpha-3': 'ZMB', 'Numeric code': '894', 'Link to ISO 3166-2': 'ISO 3166-2:ZM', 'Independent': 'Yes'},
"Zimbabwe" : {'Alpha-2': 'ZW', 'Alpha-3': 'ZWE', 'Numeric code': '716', 'Link to ISO 3166-2': 'ISO 3166-2:ZW', 'Independent': 'Yes'} }


# Examples:
# print('Montenegro,', 'Numeric code:', dict['Montenegro']['Numeric code'])
# print('Timor-Leste,', 'Link to ISO 3166-2:', dict['Montenegro']['Link to ISO 3166-2'])
