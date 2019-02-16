edges = (('Atlanta', 'Chicago'),
         ('Atlanta', 'Washington'),
         ('Atlanta', 'Miami'),
         ('Chicago', 'San Francisco'),
         ('Chicago', 'Los Angeles'),
         ('Chicago', 'Montreal'),
         ('Chicago', 'Atlanta'),
         ('Chicago', 'Mexico City'),
         ('Montreal', 'Chicago'),
         ('Montreal', 'New York'),
         ('Montreal', 'Washington'),
         ('Washington', 'Miami'),
         ('Washington', 'Atlanta'),
         ('Washington', 'Montreal'),
         ('Washington', 'New York'),
         ('Los Angeles', 'Mexico City'),
         ('Los Angeles', 'Chicago'),
         ('Los Angeles', 'San Francisco'),
         ('Los Angeles', 'Sydney'),
         ('Los Angeles', 'Lima'),
         ('San Francisco', 'Los Angeles'),
         ('San Francisco', 'Chicago'),
         ('San Francisco', 'Manila'),
         ('San Francisco', 'Tokyo'),
         ('Miami', 'Atlanta'),
         ('Miami', 'Washington'),
         ('Miami', 'Bogota'),
         ('Miami', 'Mexico City'),
         ('Bogota', 'Miami'),
         ('Bogota', 'Mexico City'),
         ('Bogota', 'Lima'),
         ('Bogota', 'Sao Paulo'),
         ('Bogota', 'Buenos Aires'),
         ('Lima', 'Santiago'),
         ('Lima', 'Bogota'),
         ('Lima', 'Mexico City'),
         ('Lima', 'Los Angeles'),
         ('Santiago', 'Lima'),
         ('Santiago', 'Buenos Aires'),
         ('Sao Paulo', 'Bogota'),
         ('Sao Paulo', 'Buenos Aires'),
         ('Sao Paulo', 'Lagos'),
         ('Sao Paulo', 'Madrid'),
         ('Buenos Aires', 'Santiago'),
         ('Buenos Aires', 'Sao Paulo'),
         ('Buenos Aires', 'Bogota'),
         ('Buenos Aires', 'Johannesburg'),
         ('New York', 'Montreal'),
         ('New York', 'Washington'),
         ('New York', 'London'),
         ('New York', 'Madrid'),
         ('London', 'New York'),
         ('London', 'Madrid'),
         ('London', 'Paris'),
         ('London', 'Essen'),
         ('Madrid', 'New York'),
         ('Madrid', 'London'),
         ('Madrid', 'Paris'),
         ('Madrid', 'Sao Paulo'),
         ('Madrid', 'Algiers'),
         ('Paris', 'Madrid'),
         ('Paris', 'London'),
         ('Paris', 'Essen'),
         ('Paris', 'Algiers'),
         ('Paris', 'Milan'),
         ('Essen', 'London'),
         ('Essen', 'Paris'),
         ('Essen', 'Milan'),
         ('Essen', 'St Petersburg'),
         ('Milan', 'Paris'),
         ('Milan', 'Essen'),
         ('Milan', 'Istanbul'),
         ('St Petersburg', 'Essen'),
         ('St Petersburg', 'Istanbul'),
         ('St Petersburg', 'Moscow'),
         ('Algiers', 'Madrid'),
         ('Algiers', 'Paris'),
         ('Algiers', 'Istanbul'),
         ('Algiers', 'Cairo'),
         ('Istanbul', 'Algiers'),
         ('Istanbul', 'Milan'),
         ('Istanbul', 'St Petersburg'),
         ('Istanbul', 'Moscow'),
         ('Istanbul', 'Baghdad'),
         ('Istanbul', 'Cairo'),
         ('Cairo', 'Algiers'),
         ('Cairo', 'Istanbul'),
         ('Cairo', 'Baghdad'),
         ('Cairo', 'Riyadh'),
         ('Cairo', 'Khartoum'),
         ('Khartoum', 'Cairo'),
         ('Khartoum', 'Johannesburg'),
         ('Khartoum', 'Kinshasa'),
         ('Khartoum', 'Lagos'),
         ('Johannesburg', 'Khartoum'),
         ('Johannesburg', 'Kinshasa'),
         ('Johannesburg', 'Buenos Aires'),
         ('Kinshasa', 'Johannesburg'),
         ('Kinshasa', 'Khartoum'),
         ('Kinshasa', 'Lagos'),
         ('Lagos', 'Khartoum'),
         ('Lagos', 'Kinshasa'),
         ('Lagos', 'Sao Paulo'),
         ('Moscow', 'St Petersburg'),
         ('Moscow', 'Istanbul'),
         ('Moscow', 'Tehran'),
         ('Baghdad', 'Istanbul'),
         ('Baghdad', 'Cairo'),
         ('Baghdad', 'Riyadh'),
         ('Baghdad', 'Tehran'),
         ('Riyadh', 'Cairo'),
         ('Riyadh', 'Baghdad'),
         ('Riyadh', 'Karachi'),
         ('Tehran', 'Moscow'),
         ('Tehran', 'Baghdad'),
         ('Tehran', 'Karachi'),
         ('Tehran', 'Delhi'),
         ('Karachi', 'Tehran'),
         ('Karachi', 'Riyadh'),
         ('Karachi', 'Mumbai'),
         ('Karachi', 'Delhi'),
         ('Delhi', 'Tehran'),
         ('Delhi', 'Karachi'),
         ('Delhi', 'Mumbai'),
         ('Delhi', 'Kolkata'),
         ('Delhi', 'Chennai'),
         ('Kolkata', 'Delhi'),
         ('Kolkata', 'Chennai'),
         ('Kolkata', 'Bangkok'),
         ('Kolkata', 'Hong Kong'),
         ('Chennai', 'Mumbai'),
         ('Chennai', 'Delhi'),
         ('Chennai', 'Kolkata'),
         ('Chennai', 'Jakarta'),
         ('Mumbai', 'Karachi'),
         ('Mumbai', 'Delhi'),
         ('Mumbai', 'Chennai'),
         ('Bangkok', 'Kolkata'),
         ('Bangkok', 'Jakarta'),
         ('Bangkok', 'Hong Kong'),
         ('Bangkok', 'Ho Chi Minh City'),
         ('Jakarta', 'Chennai'),
         ('Jakarta', 'Bangkok'),
         ('Jakarta', 'Ho Chi Minh City'),
         ('Jakarta', 'Sydney'),
         ('Sydney', 'Jakarta'),
         ('Sydney', 'Manila'),
         ('Sydney', 'Los Angeles'),
         ('Beijing', 'Seoul'),
         ('Beijing', 'Shanghai'),
         ('Shanghai', 'Beijing'),
         ('Shanghai', 'Seoul'),
         ('Shanghai', 'Tokyo'),
         ('Shanghai', 'Taipei'),
         ('Shanghai', 'Hong Kong'),
         ('Hong Kong', 'Kolkata'),
         ('Hong Kong', 'Bangkok'),
         ('Hong Kong', 'Ho Chi Minh City'),
         ('Hong Kong', 'Manila'),
         ('Hong Kong', 'Taipei'),
         ('Hong Kong', 'Shanghai'),
         ('Ho Chi Minh City', 'Hong Kong'),
         ('Ho Chi Minh City', 'Bangkok'),
         ('Ho Chi Minh City', 'Jakarta'),
         ('Ho Chi Minh City', 'Manila'),
         ('Seoul', 'Beijing'),
         ('Seoul', 'Shanghai'),
         ('Seoul', 'Tokyo'),
         ('Tokyo', 'Seoul'),
         ('Tokyo', 'Shanghai'),
         ('Tokyo', 'San Francisco'),
         ('Tokyo', 'Osaka'),
         ('Osaka', 'Tokyo'),
         ('Osaka', 'Taipei'),
         ('Taipei', 'Osaka'),
         ('Taipei', 'Shanghai'),
         ('Taipei', 'Hong Kong'),
         ('Taipei', 'Manila'),
         ('Manila', 'Taipei'),
         ('Manila', 'Hong Kong'),
         ('Manila', 'Ho Chi Minh City'),
         ('Manila', 'Sydney'),
         ('Manila', 'San Francisco'))


def pandemicGraphTests(g):
    assert g.degree('Lima') == 4
    assert g.degree('Mexico City') == 5
    assert g.degree('Manila') == 5
    assert g.degree('Taipei') == 4
    assert g.degree('Osaka') == 2
    assert g.degree('Tokyo') == 4
    assert g.degree('Seoul') == 3
    assert g.degree('Ho Chi Minh City') == 4
    assert g.degree('Hong Kong') == 6
    assert g.degree('Shanghai') == 5
    assert g.degree('Beijing') == 2
    assert g.degree('Sydney') == 3
    assert g.degree('Jakarta') == 4
    assert g.degree('Bangkok') == 4
    assert g.degree('Mumbai') == 3
    assert g.degree('Chennai') == 4
    assert g.degree('Kolkata') == 4
    assert g.degree('Delhi') == 5
    assert g.degree('Karachi') == 4
    assert g.degree('Tehran') == 4
    assert g.degree('Riyadh') == 3
    assert g.degree('Baghdad') == 4
    assert g.degree('Moscow') == 3
    assert g.degree('Lagos') == 3
    assert g.degree('Kinshasa') == 3
    assert g.degree('Khartoum') == 4
    assert g.degree('Johannesburg') == 3
    assert g.degree('Cairo') == 5
    assert g.degree('Istanbul') == 6
    assert g.degree('Algiers') == 4
    assert g.degree('St Petersburg') == 3
    assert g.degree('Milan') == 3
    assert g.degree('Essen') == 4
    assert g.degree('Atlanta') == 3
    assert g.degree('Chicago') == 5
    assert g.degree('Montreal') == 3
    assert g.degree('Washington') == 4
    assert g.degree('Los Angeles') == 5
    assert g.degree('San Francisco') == 4
    assert g.degree('Miami') == 4
    assert g.degree('Bogota') == 5
    assert g.degree('Santiago') == 2
    assert g.degree('Sao Paulo') == 4
    assert g.degree('Buenos Aires') == 4
    assert g.degree('New York') == 4
    assert g.degree('London') == 4
    assert g.degree('Madrid') == 5
    assert g.degree('Paris') == 5
