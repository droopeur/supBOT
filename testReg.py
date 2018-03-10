# -*-coding:utf-8 -*

import re
phrase_test ='Supr﻿eme®﻿/S﻿IGG﻿™ Tr﻿aveller 0.6L Wat﻿er B﻿o﻿ttle
Re﻿d'
regex='B\ufeff?o\ufeff?t\ufeff?t\ufeff?l\ufeff?e\ufeff?'
print(re.match(regex,phrase_test))