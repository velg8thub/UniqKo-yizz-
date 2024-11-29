import mysql.connector
get_valid_answer = {
    "MusicalInstruments" : ["Piano", "Guitar", "Violin", "Drums", "Saxophone", "Flute", "Trumpet", "Clarinet", "Trombone", "Harp", "Cello", "Tuba", "Accordion", "Banjo", "Oboe", "Mandolin", "Bassoon", "Marimba", "Xylophone", "Ukulele", "Harmonica", "Viola", "Bagpipes", "Synthesizer", "Piccolo", "Lute", "Bongo", "Conga", "Sitar", "Tabla", "Didgeridoo", "Djembe", "Kalimba", "Dulcimer", "Castanets", "Glockenspiel", "Zither", "Lyre", "Sousaphone", "Euphonium", "Kazoo", "Steelpan", "Shamisen", "Erhu", "Theremin", "Vuvuzela", "Mouth Harp", "Recorder", "Jew's Harp", "Triangle", "Bodhrán", "Cajón", "Clavichord", "Organ", "Bugle", "Crumhorn", "Spoons", "Cimbalom", "Fiddle", "Pennywhistle", "Melodica", "Taiko Drums", "Shakuhachi", "Balalaika", "Chimes", "Dombra", "Bandoneon", "Tambourine", "Bass Guitar", "Electronic Drum Pad", "Agogo", "Kalimba", "Guitalele", "Whistle", "Octobass", "Hang Drum", "French Horn", "Ghatam", "Maracas", "Spinet"],
    "Sports": ["Soccer", "Basketball", "Baseball", "Tennis", "Volleyball", "Golf", "Rugby", "Cricket", "Hockey", "Boxing", "Swimming", "Archery", "Wrestling", "Table Tennis", "Badminton", "Skiing", "Snowboarding", "Figure Skating", "Rowing", "Canoeing", "Kayaking", "Sailing", "Surfing", "Skateboarding", "Cycling", "Fencing", "Weightlifting", "Gymnastics", "Handball", "Lacrosse", "Softball", "Polo", "Judo", "Karate", "Taekwondo", "Triathlon", "Marathon Running", "Sumo Wrestling", "Equestrian", "Snooker", "Billiards", "Darts", "Auto Racing", "Rally Racing", "Drag Racing", "Motocross", "Ice Hockey", "Horse Racing", "Mixed Martial Arts", "Kickboxing", "Scuba Diving", "Bobsledding", "Skeleton Racing", "Curling", "Biathlon", "Disc Golf", "Ultimate Frisbee", "Netball", "Orienteering", "Kendo", "Shooting", "Climbing", "Parkour", "Bowling", "Cheerleading", "Bocce", "Petanque", "Tug of War", "Paintball", "Dodgeball", "Roller Derby", "Speed Skating", "Bungee Jumping", "Wind Surfing", "Spearfishing", "Gymkhana", "Field Hockey", "American Football", "CrossFit", "Aqua Aerobics"],
    "Famous Fashion Designers":["Coco Chanel", "Giorgio Armani", "Karl Lagerfeld", "Ralph Lauren", "Christian Dior", "Versace", "Yves Saint Laurent", "Alexander McQueen", "Valentino Garavani", "Donna Karan", "Oscar de la Renta", "Jean-Paul Gaultier", "Stella McCartney", "Givenchy", "Balenciaga", "Marc Jacobs", "Tom Ford", "Diane von Furstenberg", "Balmain", "Fendi", "Miuccia Prada", "Issey Miyake", "Kenzo Takada", "Vivienne Westwood", "Emilio Pucci", "Ralph & Russo", "Ann Demeulemeester", "Dries Van Noten", "Comme des Garçons (Rei Kawakubo)", "Maison Margiela", "Lanvin", "Salvatore Ferragamo", "Bottega Veneta", "Azzedine Alaïa", "Christian Lacroix", "Roberto Cavalli", "Jil Sander", "Thom Browne", "Etro", "Tory Burch", "Carolina Herrera", "Zac Posen", "Mary Katrantzou", "Peter Pilotto", "Giles Deacon", "Haider Ackermann", "Sacai (Chitose Abe)", "Nanushka", "Toga (Yasuko Furuta)", "Off-White (Virgil Abloh)", "Sacai", "Alexander Wang", "Reem Acra", "Jason Wu", "Christian Siriano", "Prabal Gurung", "Lela Rose", "Alice + Olivia (Stacey Bendet)", "Monique Lhuillier", "Naeem Khan", "Cushnie et Ochs", "Khaite (Catherine Holstein)", "Brock Collection", "A.P.C. (Jean Touitou)", "Ganni", "Roksanda Ilincic", "Peter Som", "Jonathan Simkhai", "3.1 Phillip Lim", "Tibi", "Simon Miller", "Ulla Johnson", "Loro Piana", "Fenty (Rihanna)", "The Row (Mary-Kate and Ashley Olsen)", "Eres (Marie-Pierre Mancin)", "Kenzo", "Diesel (Renzo Rosso)", "AllSaints", "H&M (Collaboration designers)"],
    "Female Singers":["Whitney Houston", "Beyoncé", "Rihanna", "Mariah Carey", "Adele", "Celine Dion", "Aretha Franklin", "Madonna", "Taylor Swift", "Alicia Keys", "Lady Gaga", "Sia", "Ella Fitzgerald", "Billie Eilish", "Shakira", "Dolly Parton", "Norah Jones", "Amy Winehouse", "Katy Perry", "Miley Cyrus", "Demi Lovato", "Nicki Minaj", "Lana Del Rey", "Camila Cabello", "Halsey", "Bebe Rexha", "Lizzo", "Cher", "Nina Simone", "Patti Smith", "Grace Slick", "Sarah Vaughan", "Diana Ross", "Erykah Badu", "Roberta Flack", "Joan Baez", "Bjork", "Janis Joplin", "Donna Summer", "Tori Amos", "Ciara", "Ashanti", "Kelly Clarkson", "Brandy", "Monica", "Bonnie Tyler", "Gloria Estefan", "Carly Rae Jepsen", "Alanis Morissette", "Pink", "Meghan Trainor", "Florence Welch", "Aaliyah", "Jewel", "M.I.A.", "Fergie", "Debbie Harry", "Gwen Stefani", "Janelle Monáe", "Cheryl Cole", "Lea Salonga", "Regine Velasquez", "Sarah Geronimo", "Sharon Cuneta", "Jaya", "Jolina Magdangal", "Lani Misalucha", "Aicelle Santos", "KZ Tandingan", "Yeng Constantino", "Kyla", "Zsa Zsa Padilla", "Rachelle Ann Go", "Angeline Quinto", "Morissette Amon", "Janella Salvador", "Nina", "Toni Gonzaga", "Donna Cruz", "Moira Dela Torre"],
    "Body Parts":["Head", "Neck", "Shoulder", "Arm", "Elbow", "Wrist", "Hand", "Finger", "Thumb", "Chest", "Back", "Spine", "Rib", "Hip", "Leg", "Thigh", "Knee", "Ankle", "Foot", "Toe", "Heel", "Pelvis", "Abdomen", "Stomach", "Heart", "Lung", "Liver", "Kidney", "Pancreas", "Spleen", "Brain", "Eye", "Nose", "Mouth", "Ear", "Jaw", "Tooth", "Tongue", "Lip", "Cheek", "Chin", "Skull", "Collarbone", "Scapula", "Tricep", "Bicep", "Forearm", "Palm", "Fist", "Fingernail", "Groin", "Muscle", "Nerve", "Vein", "Artery", "Skin", "Hair", "Scalp", "Eye Socket", "Eyebrow", "Eyelash", "Pupil", "Cornea", "Retina", "Bone", "Cartilage", "Joint", "Tendon", "Ligament", "Intestine", "Gallbladder", "Bladder", "Esophagus", "Diaphragm", "Aorta", "Appendix", "Large Intestine", "Small Intestine", "Urethra", "Blood Vessel"],
    "Disney Movies":["Snow White and the Seven Dwarfs", "Cinderella", "Sleeping Beauty", "Peter Pan", "Dumbo", "Bambi", "Alice in Wonderland", "The Little Mermaid", "Beauty and the Beast", "Aladdin", "The Lion King", "Pocahontas", "Mulan", "Tarzan", "The Hunchback of Notre Dame", "Hercules", "The Jungle Book", "Lady and the Tramp", "101 Dalmatians", "The Aristocats", "Robin Hood", "The Fox and the Hound", "The Rescuers", "Oliver & Company", "The Great Mouse Detective", "The Sword in the Stone", "Pinocchio", "Fantasia", "Tangled", "Frozen", "Big Hero 6", "Zootopia", "Moana", "Frozen II", "Raya and the Last Dragon", "Encanto", "Strange World", "Bolt", "Meet the Robinsons", "Lilo & Stitch", "The Princess and the Frog", "Atlantis: The Lost Empire", "Treasure Planet", "The Black Cauldron", "Brother Bear", "Home on the Range", "Chicken Little", "Dinosaur", "Winnie the Pooh", "Ralph Breaks the Internet", "Wreck-It Ralph", "The Emperor’s New Groove", "Brave", "Cars", "A Bug’s Life", "Toy Story", "Toy Story 2", "Toy Story 3", "Toy Story 4", "Finding Nemo", "Finding Dory", "Inside Out", "Monsters, Inc.", "Monsters University", "Onward", "Soul", "Luca", "Lightyear", "Elemental", "Coco", "Turning Red", "Planes", "Planes: Fire & Rescue", "Cars 2", "Cars 3", "Ratatouille", "The Incredibles", "The Incredibles 2", "WALL-E", "Up"],
    "Philippine Cities":["Manila", "Quezon City", "Cebu City", "Davao City", "Zamboanga City", "Taguig", "Pasig", "Cagayan de Oro", "Makati", "Mandaluyong", "Caloocan", "Malabon", "Las Piñas", "Marikina", "Muntinlupa", "Parañaque", "Pasay", "San Juan", "Valenzuela", "Navotas", "Antipolo", "Angeles City", "Bacolod", "Baguio", "Batangas City", "Biñan", "Butuan", "Cabanatuan", "Calamba", "Dagupan", "General Santos", "Gingoog", "Iligan", "Iloilo City", "Kabankalan", "Laoag", "Lapu-Lapu City", "Ligao", "Lucena", "Malaybalay", "Mandaue", "Masbate City", "Naga City (Camarines Sur)", "Olongapo", "Ormoc", "Ozamiz", "Pagadian", "Palayan", "Passi", "Roxas City", "Sagay", "Samal", "San Carlos", "San Jose del Monte", "San Pablo", "Santa Rosa", "Santiago City", "Silay", "Sorsogon City", "Surigao City", "Tacloban", "Tagaytay", "Tagbilaran", "Talisay (Cebu)", "Tandag", "Tarlac City", "Toledo", "Trece Martires", "Tuguegarao", "Urdaneta", "Vigan", "Victorias", "Zamboanga Sibugay", "Cotabato City", "Dipolog", "Digos", "Dumaguete", "Kidapawan", "Koronadal", "Bais City"],
    "Colors":["Red", "Blue", "Green", "Yellow", "Orange", "Purple", "Pink", "Brown", "Black", "White", "Gray", "Navy", "Aqua", "Teal", "Olive", "Maroon", "Lavender", "Beige", "Peach", "Salmon", "Magenta", "Turquoise", "Mint", "Coral", "Cyan", "Indigo", "Violet", "Crimson", "Ruby", "Amber", "Jade", "Sapphire", "Gold", "Silver", "Bronze", "Lilac", "Fuchsia", "Slate", "Charcoal", "Mint Green", "Sky Blue", "Seafoam", "Lime", "Ivory", "Pearl", "Champagne", "Cream", "Cherry", "Lemon", "Rust", "Khaki", "Blush", "Mustard", "Denim", "Sangria", "Copper", "Sand", "Hazelnut", "Mahogany", "Mulberry", "Azure", "Mint Blue", "Lavender Blue", "Electric Blue", "Bubblegum", "Canary", "Brick", "Sunflower", "Burnt Orange", "Pistachio", "Rose", "Berry", "Moss Green", "Espresso", "Taupe", "Honey", "Teak", "Orchid", "Moss", "Pumpkin"],
    "Presidents":["Emilio Aguinaldo", "Manuel L. Quezon", "Jose P. Laurel", "Sergio Osmeña", "Manuel Roxas", "Elpidio Quirino", "Ramon Magsaysay", "Carlos P. Garcia", "Diosdado Macapagal", "Ferdinand Marcos", "Corazon Aquino", "Fidel V. Ramos", "Joseph Estrada", "Gloria Macapagal-Arroyo", "Benigno Aquino III", "Rodrigo Duterte", "Ferdinand Marcos Jr.", "George Washington", "John Adams", "Thomas Jefferson", "James Madison", "James Monroe", "John Quincy Adams", "Andrew Jackson", "Martin Van Buren", "William Henry Harrison", "John Tyler", "James K. Polk", "Zachary Taylor", "Millard Fillmore", "Franklin Pierce", "James Buchanan", "Abraham Lincoln", "Andrew Johnson", "Ulysses S. Grant", "Rutherford B. Hayes", "James A. Garfield", "Chester A. Arthur", "Grover Cleveland", "Benjamin Harrison", "William McKinley", "Theodore Roosevelt", "William Howard Taft", "Woodrow Wilson", "Warren G. Harding", "Calvin Coolidge", "Herbert Hoover", "Franklin D. Roosevelt", "Harry S. Truman", "Dwight D. Eisenhower", "John F. Kennedy", "Lyndon B. Johnson", "Richard Nixon", "Gerald Ford", "Jimmy Carter", "Ronald Reagan", "George H.W. Bush", "Bill Clinton", "George W. Bush", "Barack Obama", "Donald Trump", "Joe Biden", "Emmanuel Macron", "Vladimir Putin", "Xi Jinping", "Angela Merkel", "Shinzo Abe", "Moon Jae-in", "Andrés Manuel López Obrador", "Jair Bolsonaro", "Narendra Modi", "Justin Trudeau", "Boris Johnson", "Abdel Fattah el-Sisi", "Hassan Rouhani", "Recep Tayyip Erdoğan", "Pedro Sánchez", "Sebastian Kurz", "Tsai Ing-wen", "Alberto Fernández"],
    "Pets":["Dog", "Cat", "Hamster", "Guinea Pig", "Rabbit", "Fish", "Parrot", "Turtle", "Lizard", "Snake", "Frog", "Ferret", "Hedgehog", "Chinchilla", "Rat", "Mouse", "Hermit Crab", "Tarantula", "Iguana", "Bearded Dragon", "Canary", "Budgerigar", "Cockatiel", "Lovebird", "Pigeon", "Gerbil", "Goat", "Miniature Pig", "Chickens", "Duck", "Miniature Horse", "Sugar Glider", "Scorpion", "Gecko", "Koi Fish", "Tortoise", "Axolotl", "Finches", "Salamander", "Budgie", "Alpaca", "Degu", "Zebra Finch", "Cockatoo", "Ball Python", "Tree Frog", "Millipede", "Stick Insect", "Starfish", "Seahorse", "Rat Snake", "Corn Snake", "Sphynx Cat", "Maine Coon", "Siamese Cat", "Persian Cat", "German Shepherd", "Golden Retriever", "Beagle", "Pomeranian", "Pug", "Shih Tzu", "Boxer", "Dachshund", "Cocker Spaniel", "Border Collie", "Ragdoll Cat", "Bengal Cat", "Scottish Fold", "Pekingese", "Chihuahua", "Parakeet", "Lovebird", "Amazon Parrot", "African Grey Parrot", "Macaw", "Miniature Schnauzer", "Maltese", "Japanese Spitz", "Cavalier King Charles Spaniel"],
    "Philippines Top Universities":["University of the Philippines Diliman", "Ateneo de Manila University", "De La Salle University", "University of Santo Tomas", "University of the East", "Mindanao State University", "San Beda University", "Far Eastern University", "Adamson University", "University of San Carlos", "University of the Cordilleras", "Central Luzon State University", "University of the Philippines Los Baños", "University of the Philippines Manila", "National University", "Lyceum of the Philippines University", "Mapúa University", "University of Negros Occidental-Recoletos", "University of the Visayas", "Xavier University - Ateneo de Cagayan", "Jose Rizal University", "Philippine Normal University", "Arellano University", "San Sebastian College - Recoletos", "University of Santo Tomas - Legazpi", "University of the Cordilleras", "Bataan Peninsula State University", "Cavite State University", "Bulacan State University", "Mindanao State University - Iligan Institute of Technology", "University of the East Ramon Magsaysay Memorial Medical Center", "Far Eastern University - Institute of Technology", "University of San Agustin", "Silliman University", "University of the East - Caloocan", "Central Mindanao University", "University of Northern Philippines", "University of Batangas", "Philippine State College of Aeronautics", "National College of Business and Arts", "Ateneo de Davao University", "University of the Cordilleras", "University of the Philippines Mindanao", "Central Mindanao University", "University of the East - Manila", "University of San Jose - Recoletos", "St. Paul University Manila", "University of the East Caloocan", "Lyceum of the Philippines University - Batangas", "Adamson University", "University of the Philippines Cebu", "University of the Philippines Baguio", "San Sebastian College - Recoletos", "University of the East Ramon Magsaysay Memorial Medical Center", "Philippine Military Academy", "Philippine College of Criminology", "San Beda University - Alabang", "La Consolacion College Manila", "University of Perpetual Help System", "Mindanao University of Science and Technology", "University of Nueva Caceres", "University of St. La Salle", "Central Luzon State University", "University of the Cordilleras", "San Beda University - Manila", "Holy Angel University", "Bulacan State University", "Cagayan State University", "University of Northern Philippines", "University of San Carlos - Cebu", "National College of Science and Technology", "University of San Agustin - Iloilo", "University of the Immaculate Conception", "Notre Dame University", "University of the Philippines Los Baños", "Mindanao State University - Main Campus", "University of the Philippines Manila", "University of the East - Caloocan", "University of the East - Manila", "Far Eastern University - Makati"],
    "Shapes":["Circle", "Square", "Triangle", "Rectangle", "Pentagon", "Hexagon", "Octagon", "Ellipse", "Rhombus", "Trapezoid", "Parallelogram", "Kite", "Cube", "Sphere", "Cylinder", "Cone", "Pyramid", "Tetrahedron", "Dodecagon", "Octahedron", "Scalene Triangle", "Isosceles Triangle", "Equilateral Triangle", "Right Triangle", "Sector", "Annulus", "Frustum", "Torus", "Star Shape", "Heart Shape", "Crescent", "Cross", "Diamond", "Lattice", "Arrow", "Wave", "Spiral", "Rectangle with Rounded Corners", "Trapezium", "Spherical Triangle", "Trapezium", "Heptagon", "Nonagon", "Decagon", "Dodecagon", "Icosahedron", "Tesseract", "Rhomboid", "Oval", "Crescent", "Star Polygon", "Spiral", "Mobius Strip", "Spherical Cap", "Polyhedron", "Fractal", "Quadrilateral", "Scalene Triangle", "Isosceles Triangle", "Equilateral Triangle", "Regular Polygon", "Irregular Polygon", "Kite", "Right Angled Triangle", "Acute Triangle", "Obtuse Triangle", "Sector", "Annular Sector", "Arch", "Chord", "Segment", "Lune", "Lens", "Conic Section", "Parabola", "Hyperbola", "Ellipsoid", "Paraboloid", "Cone", "Sphere"],
    "OPM Artists":["Gary Valenciano", "Regine Velasquez", "Sarah Geronimo", "Bamboo", "Lea Salonga", "Eraserheads", "Sponge Cola", "Parokya Ni Edgar", "Rivermaya", "Moira Dela Torre", "Apo Hiking Society", "Francis M.", "Yeng Constantino", "Gloc-9", "KZ Tandingan", "Ben&Ben", "The Juans", "Sponge Cola", "Hale", "Itchyworms", "Callalily", "Aiza Seguerra", "Christian Bautista", "Kyla", "Nina", "Ogie Alcasid", "Jaya", "Bamboo", "Pupil", "Parokya Ni Edgar", "Rivermaya", "The Dawn", "Asin", "Freestyle", "6cyclemind", "Sponge Cola", "Silent Sanctuary", "Kamikazee", "Zsazsa Padilla", "Regine Velasquez-Alcasid", "Rivermaya", "The Dawn", "Sponge Cola", "Kamikazee", "Hale", "Callalily", "6cyclemind", "Silent Sanctuary", "Chicosci", "Mayonnaise", "Aegis", "True Faith", "The Itchyworms", "KZ Tandingan", "Moira Dela Torre", "Ben&Ben", "The Juans", "Gracenote", "Ebe Dancel", "Gloc-9", "Yeng Constantino", "Christian Bautista", "Ogie Alcasid", "Jaya", "Zsazsa Padilla", "Regine Velasquez-Alcasid", "Martin Nievera", "Gary V.", "Sarah Geronimo", "Bamboo", "Lea Salonga", "Francis M.", "Apo Hiking Society", "Parokya Ni Edgar", "Rivermaya", "Sponge Cola", "Hale", "Itchyworms", "Callalily", "Aiza Seguerra"],
    "Public Holidays(Philippines)":["New Year's Day", "Maundy Thursday", "Good Friday", "Araw ng Kagitingan", "Labor Day", "Independence Day", "National Heroes Day", "Bonifacio Day", "Christmas Day", "Rizal Day", "Chinese New Year", "Eid al-Fitr", "Eid al-Adha", "Ninoy Aquino Day", "All Saints' Day", "All Souls' Day", "National Women's Day", "National Children's Day", "National Teachers' Day", "National Youth Day", "National Flag Day", "National Arts Month", "National Book Week", "National Science and Technology Week", "National Rice Awareness Month", "National Nutrition Month", "National Heritage Month", "National Indigenous Peoples Month", "National Mental Health Month", "National Environmental Awareness Month", "National Reading Month", "National Peace Consciousness Month", "National Clean-Up Month", "National Maritime Week", "National Tourism Week", "National ICT Month", "National Language Month", "National Flag Day", "National Police Month", "National Fire Prevention Month", "New Year’s Eve", "Chinese New Year", "Black Saturday", "Feast of the Immaculate Conception", "National Day of Mourning", "National Flag Day", "National Arts Month", "National Science Month", "National Environment Month", "National Nutrition Month", "National Teachers' Month", "National Indigenous Peoples Month", "National Women’s Month", "National Youth Month", "National Reading Month", "National Mental Health Month", "National Clean-Up Month", "National Maritime Week", "National Tourism Week", "National ICT Month", "National Language Month", "National Police Month", "National Fire Prevention Month", "National Rice Awareness Month", "National Book Week", "National Heritage Month", "National Peace Consciousness Month", "National Clean Air Month", "National Tree Planting Month", "National HIV Awareness Month", "National Handwashing Month", "National Disaster Resilience Month", "National Food Security Month", "National Child Month", "National Family Week", "National Volunteer Month", "National Homeownership Month", "National Blood Donor Month", "National Coconut Week", "National Rice Month"],
    "Philippine National Heroes":["José Rizal", "Andres Bonifacio", "Emilio Aguinaldo", "Apolinario Mabini", "Gabriela Silang", "Juan Luna", "Antonio Luna", "Ninoy Aquino", "Corazon Aquino", "Sultan Kudarat", "Lapu-Lapu", "Josefa Llanes Escoda", "Andres Bonifacio", "Emilio Jacinto", "Apolinario Mabini", "Rizal's Sisters", "Francisco Balagtas", "Marcela Agoncillo", "Jose Rizal's Parents", "Jose Palma", "Hilarion Del Castillo", "Vicente Lim", "Artemio Ricarte", "Pedro Paterno", "Andres Bonifacio", "Teodoro Agoncillo", "Diego Silang", "Jose Rizal", "Emilio Aguinaldo", "Antonio Luna", "Rizal's Friends", "Manuel L. Quezon", "Claro M. Recto", "Benigno Aquino Jr.", "Josefa Llanes Escoda", "Apolinario Mabini", "Jose Rizal", "Andres Bonifacio", "Francisco Balagtas", "Lapu-Lapu", "Josefa Llanes Escoda", "Apolinario Mabini", "Emilio Jacinto", "Andres Bonifacio", "Francisco Balagtas", "Lapu-Lapu", "Gabriela Silang", "Antonio Luna", "Juan Luna", "Rizal's Sisters", "Hilarion Del Castillo", "Vicente Lim", "Artemio Ricarte", "Pedro Paterno", "Teodoro Agoncillo", "Diego Silang", "Jose Rizal", "Manuel L. Quezon", "Claro M. Recto", "Benigno Aquino Jr.", "Corazon Aquino", "Josefa Llanes Escoda", "Ninoy Aquino", "Sultan Kudarat", "Jose Rizal", "Andres Bonifacio", "Emilio Aguinaldo", "Apolinario Mabini", "Rizal's Friends", "Jose Palma", "Francisco Balagtas", "Lapu-Lapu", "Hilarion Del Castillo", "Vicente Lim", "Artemio Ricarte", "Jose Rizal's Parents", "Josefa Llanes Escoda", "Andres Bonifacio", "Emilio Aguinaldo", "Antonio Luna"],
    "College Majors":["Business Administration", "Computer Science", "Engineering", "Psychology", "Nursing", "Education", "Communication", "Biology", "Environmental Science", "Fine Arts", "Accounting", "Marketing", "Information Technology", "Political Science", "Sociology", "History", "Mathematics", "Chemistry", "Physics", "Hospitality Management", "Criminal Justice", "Graphic Design", "Animation", "Music", "Theater Arts", "Agriculture", "Pharmacy", "Dentistry", "Architecture", "Marine Biology", "Data Science", "Public Administration", "International Relations", "Linguistics", "Social Work", "Sports Management", "Veterinary Medicine", "Film Studies", "Fashion Design", "Event Management", "Environmental Studies", "Biochemistry", "Graphic Design", "Animation", "Sports Science", "Public Health", "International Business", "Hospitality Management", "Cybersecurity", "Information Systems", "Fashion Merchandising", "Film Production", "Event Planning", "Forensic Science", "Marine Biology", "Agricultural Science", "Real Estate", "Human Resource Management", "Supply Chain Management", "Web Development", "Artificial Intelligence", "Robotics", "Digital Marketing", "Game Design", "Music Production", "Interior Design", "Social Work", "Theology", "Philosophy", "Journalism", "Fine Arts", "Photography", "Culinary Arts", "Veterinary Technology", "Landscape Architecture", "Aerospace Engineering", "Nuclear Engineering", "Biomedical Engineering", "Chemical Engineering", "Civil Engineering"],
    "Asian Countries":["China", "India", "Japan", "South Korea", "Indonesia", "Philippines", "Vietnam", "Thailand", "Malaysia", "Bangladesh", "Pakistan", "Nepal", "Sri Lanka", "Myanmar", "Cambodia", "Singapore", "Mongolia", "Laos", "Brunei", "Bhutan", "Maldives", "Timor-Leste", "Kazakhstan", "Uzbekistan", "Kyrgyzstan", "Tajikistan", "Turkmenistan", "Georgia", "Armenia", "Azerbaijan", "Iraq", "Iran", "Afghanistan", "Syria", "Jordan", "Lebanon", "Israel", "Palestine", "Saudi Arabia", "United Arab Emirates", "Mongolia", "Afghanistan", "Sri Lanka", "Maldives", "Bhutan", "Nepal", "Kazakhstan", "Uzbekistan", "Kyrgyzstan", "Tajikistan", "Turkmenistan", "Georgia", "Armenia", "Azerbaijan", "Iraq", "Iran", "Syria", "Lebanon", "Jordan", "Palestine", "Saudi Arabia", "United Arab Emirates", "Oman", "Qatar", "Kuwait", "Bahrain", "Yemen", "Cyprus", "Singapore", "Brunei", "Timor-Leste", "Laos", "Cambodia", "Vietnam", "Thailand", "Malaysia", "Indonesia", "Philippines", "South Korea", "Japan"],
    "Hollywood Artists": ["Leonardo DiCaprio", "Meryl Streep", "Denzel Washington", "Jennifer Lawrence", "Tom Hanks", "Scarlett Johansson", "Brad Pitt", "Cate Blanchett", "Johnny Depp", "Will Smith", "Natalie Portman", "Robert Downey Jr.", "Emma Stone", "Chris Hemsworth", "Viola Davis", "Morgan Freeman", "Anne Hathaway", "Al Pacino", "Julia Roberts", "Dwayne Johnson", "Matt Damon", "Nicole Kidman", "Ben Affleck", "Ryan Reynolds", "Michelle Williams", "Hugh Jackman", "Kristen Stewart", "Idris Elba", "Jamie Foxx", "Reese Witherspoon", "Sandra Bullock", "Mark Ruffalo", "Amy Adams", "Tom Cruise", "Zendaya", "Jared Leto", "Joaquin Phoenix", "Gal Gadot", "Chris Pratt", "Anne Hathaway", "Natalie Portman", "Robert Downey Jr.", "Emma Stone", "Chris Hemsworth", "Viola Davis", "Morgan Freeman", "Anne Hathaway", "Al Pacino", "Julia Roberts", "Dwayne Johnson", "Matt Damon", "Nicole Kidman", "Ben Affleck", "Ryan Reynolds", "Michelle Williams", "Hugh Jackman", "Kristen Stewart", "Idris Elba", "Jamie Foxx", "Reese Witherspoon", "Sandra Bullock", "Mark Ruffalo", "Amy Adams", "Tom Cruise", "Zendaya", "Jared Leto", "Joaquin Phoenix", "Gal Gadot", "Chris Pratt", "Anne Hathaway", "Timothée Chalamet", "Florence Pugh", "Lupita Nyong'o", "John Boyega", "Margot Robbie", "Oscar Isaac", "Tessa Thompson", "Rami Malek", "Dakota Johnson", "John David Washington"],
    "Anime Characters":["Naruto Uzumaki", "Goku", "Luffy (One Piece)", "Sailor Moon", "Edward Elric", "Light Yagami", "Mikasa Ackerman", "Deku (My Hero Academia)", "Spike Spiegel", "Ash Ketchum", "Kakashi Hatake", "Hinata Hyuga", "Erza Scarlet", "Natsu Dragneel", "Kirito (Sword Art Online)", "Rem (Re:Zero)", "Bulma", "Shoto Todoroki", "Inuyasha", "Usagi Tsukino", "Levi Ackerman", "Gon Freecss", "Sailor Mars", "Yuki Sohma", "Shinsou Hitoshi", "Tanjiro Kamado", "Nezuko Kamado", "Kageyama Tobio", "Yato (Noragami)", "Mob (Mob Psycho 100)", "Kyouya Sata", "L (Death Note)", "Vash the Stampede", "Gintoki Sakata", "Chihiro (Spirited Away)", "Alphonse Elric", "San (Princess Mononoke)", "Kiki (Kiki's Delivery Service)", "Shinji Ikari", "Hachiman Hikigaya", "Sakura Haruno", "Hinata Shoyo", "Kageyama Tobio", "Roronoa Zoro", "Gintoki Sakata", "Natsu Dragneel", "Erza Scarlet", "Reigen Arataka", "Mob Kageyama", "Yato", "Tanjiro Kamado", "Nezuko Kamado", "Ash Ketchum", "Chihiro Ogino", "Hachiman Hikigaya", "Shouyou Hinata", "Shinsou Hitoshi", "Kirito", "Asuka Langley Soryu", "Shinji Ikari", "Mikasa Ackerman", "Levi Ackerman", "Light Yagami", "Ryuk", "Luffy", "Goku", "Inuyasha", "Edward Elric", "Roy Mustang", "Bulma", "Sailor Venus", "Sailor Mercury", "Sailor Jupiter", "Sailor Saturn", "Sailor Neptune", "Sailor Uranus", "Sailor Pluto", "Sailor Chibi Moon", "Yuki Sohma", "Kaneki Ken"],
    "Traditional Pinoy Games":["Tumbang Preso", "Sipa", "Patintero", "Luksong Baka", "Luksong Tinik", "Chinese Garter", "Piko", "Agawang Buko", "Bato-Bato Pik", "Taya-taya", "Habulan", "Sungka", "Pagsasaka", "Buhay na Sanggol", "Pabuno", "Pagtawid", "Kagandahan", "Pato-Pato", "Bingo", "Taga", "Kite Flying", "Sipa sa Pader", "Gulong ng Palad", "Siyato", "Langit-Lupa", "Bola-Bola", "Hawak-Buhay", "Siyang", "Buhay na Kahon", "Puno ng Kahoy", "Paghahanap ng Buwan", "Karamihan", "Pagtawid ng Ilog", "Bato-Bato sa Langit", "Pagsasama", "Tawag ng Tanghalan", "Pagtakbo", "Paligsahan ng Taga", "Pagsusulit", "Kaharian ng Alon", "Labanan ng Puno", "Kaharian ng Buwan", "Sipa ng Buwan", "Kaharian ng Araw", "Sipa ng Araw", "Pagbaba ng Bundok", "Pag-akyat ng Bundok", "Pagsasaka", "Pagsasaya", "Paghahanap ng Kayamanan", "Taga ng Buwan", "Pagtawid ng Daan", "Pagsasama-sama", "Pagbaba ng Ilog", "Pag-akyat ng Ilog", "Pagbaba ng Bundok", "Pag-akyat ng Bundok", "Pag-akyat ng Dahon", "Pagbaba ng Dahon", "Pagbaba ng Buwan", "Pag-akyat ng Buwan", "Pagbaba ng Araw", "Pag-akyat ng Araw", "Pagbaba ng Ulan", "Pag-akyat ng Ulan", "Pagbaba ng Hangin", "Pag-akyat ng Hangin", "Pagbaba ng Lupa", "Pag-akyat ng Lupa", "Pagbaba ng Ulan", "Pag-akyat ng Ulan", "Pagbaba ng Hangin", "Pag-akyat ng Hangin", "Pagbaba ng Lupa", "Pag-akyat ng Lupa", "Pagbaba ng Buwan", "Pag-akyat ng Buwan", "Pagbaba ng Araw", "Pag-akyat ng Araw", "Pagbaba ng Dahon"],
    "Cartoon Characters":["Mickey Mouse", "Bugs Bunny", "SpongeBob SquarePants", "Homer Simpson", "Scooby-Doo", "Tom and Jerry", "Daffy Duck", "Bart Simpson", "Fred Flintstone", "Popeye", "Donald Duck", "Garfield", "Tweety Bird", "Pink Panther", "Charlie Brown", "Johnny Bravo", "Dexter (Dexter's Laboratory)", "Kim Possible", "Courage the Cowardly Dog", "The Powerpuff Girls", "Finn the Human", "Jake the Dog", "Phineas Flynn", "Ferb Fletcher", "Timmy Turner", "Jimmy Neutron", "Stewie Griffin", "Peter Griffin", "Daria Morgendorffer", "Arnold (Hey Arnold!)", "Tigger", "Winnie the Pooh", "Elmo", "Big Bird", "Bert and Ernie", "The Joker (Batman)", "Harley Quinn", "Rick Sanchez", "Morty Smith", "Yoda (Star Wars: The Clone Wars)", "Snoopy", "Charlie Brown", "The Joker", "Harley Quinn", "Rick Sanchez", "Morty Smith", "Daria Morgendorffer", "Arnold (Hey Arnold!)", "Tigger", "Winnie the Pooh", "Elmo", "Big Bird", "Bert and Ernie", "Stewie Griffin", "Peter Griffin", "Finn the Human", "Jake the Dog", "Phineas Flynn", "Ferb Fletcher", "Timmy Turner", "Jimmy Neutron", "Courage the Cowardly Dog", "Kim Possible", "The Powerpuff Girls", "Johnny Bravo", "Dexter (Dexter's Laboratory)", "Garfield", "Tweety Bird", "Pink Panther", "Tom and Jerry", "Bugs Bunny", "Daffy Duck", "Porky Pig", "Foghorn Leghorn", "Wile E. Coyote", "Road Runner", "Yogi Bear", "Boo Boo", "Captain Planet", "The Animaniacs"]
}

def play_round(category, num_players, eliminated_players):
    print(f"\nPlaying round in category: {category}")

    # Only players who are not eliminated should be involved in this round
    players_in_round = [i for i in range(num_players) if i + 1 not in eliminated_players]

    scores = [10 if i + 1 not in eliminated_players else 0 for i in range(num_players)]
    answers = [None] * num_players  # Store answers for all players
    eliminated_in_round = set()  # Set to track players eliminated in this round
    answer_map = {}  # Track answers to detect duplicates

    # Collect answers alternately for all players who are not eliminated
    while len(eliminated_in_round) < len(players_in_round):  # Continue until all players are eliminated
        # Only allow active players to submit answers
        for i in range(num_players):
            if i + 1 not in eliminated_players and i not in eliminated_in_round:  # Only ask players who are not eliminated
                # Ask the player for their answer
                answer = input(f"Player {i + 1}, enter your answer for {category} (or press Enter to stop): ").strip()

                # If player presses Enter without entering an answer, stop collecting answers for this player
                if not answer:
                    print(f"Player {i + 1} gave no answer! They are eliminated from this round.")
                    eliminated_in_round.add(i)
                    answers[i] = None
                    continue

                # Handle invalid answer case (eliminate player)
                if answer not in get_valid_answer[category]:
                    print(
                        f"Player {i + 1} entered an invalid answer for {category}! They are eliminated from this round.")
                    eliminated_in_round.add(i)
                    answers[i] = None
                    continue

                # Handle duplicate answer (eliminate player)
                if answer in answer_map:
                    print(
                        f"Player {i + 1} copied Player {answer_map[answer][0] + 1}'s answer: {answer}! Oh, no. It's taken, my dear.")
                    eliminated_in_round.add(i)
                    answers[i] = None
                    continue

                 # If the answer is valid and correct, add score and store the answer
                if answer in get_valid_answer[category]:  # Check if answer is valid and correct
                    #print(f"Player {i + 1} gave a correct answer!")
                    scores[i] += 10  # Increase score for correct answer

                # If the answer is valid, store it and move to the next player
                answer_map[answer] = [i]
                answers[i] = answer

        # Update the list of remaining players after elimination
        remaining_players = [i + 1 for i in range(num_players) if i not in eliminated_in_round]

        # Check if only one player remains after elimination
        if len(remaining_players) == 1:
            print(f"\n Player {remaining_players[0]}! They are the winner!")
            # Display the scores
            for i in range(num_players):
                print(f"Player {i + 1} Score: {scores[i]}")
            return [remaining_players[0]], scores  # Return the winner

    # If no player is eliminated and both finish their answers, end the round
    print("\n--- Round Results ---")
    for i in range(num_players):
        if i in eliminated_in_round:
            continue  # Don't show eliminated players
        print(f"Player {i + 1} Answer: {answers[i]} Score: {scores[i]}")

    # Find the winners of the round (those who gave valid answers and are not eliminated)
    valid_players = [i + 1 for i in range(num_players) if i not in eliminated_in_round and answers[i] is not None]

    return valid_players, scores