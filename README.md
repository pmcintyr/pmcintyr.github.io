![Photo of Lausanne](/docs/assets/lausanne.jpg)

### Task 1
Identify streets with unique or multiple spellings by comparing yearly files and building a [dictionary](https://github.com/pmcintyr/pmcintyr.github.io/blob/main/dictionary.csv) of the top 100 most popular street names.✔️

### Task 2
Find mistakes in street names (spaces, numbers, different spellings, missing characters, overflows in next column/row).
Correct mistakes and log changes.✔️ (This was achieved by manual dictionary and suggestion modifications in the notebook).

### Task 3
Provide [mappings](https://github.com/pmcintyr/pmcintyr.github.io/blob/main/mappings.csv) between uniquely named and non-uniquely named streets with their corresponding modern street names. ✔️ (This was be done by cross-examining street names with Lausanne [toponyms](https://github.com/RPetitpierre/merian/blob/main/assets/data/toponyms.geojson)).

### Task 4
Verify the house numbers are in strictly increasing order for a same street, by adding an error detection column with encoded values based on error type. ✔️ (This is done in the notebook in the house_number_clean function that we can call on each function).

### Task 5
Track the homeowner name continuity by comparing yearly files for a same address.

### Task 6
Map rows between each yearly file and make a streetmap with yearly evolution of the best homeowner mappings.

### Recits Lausannois
![AI-generated Photo of Jean Mandrot's Family](/docs/assets/jean_mandrot.jpg)

Je m'appelle Jean Mandrot, et je suis né en 1785 à Morges, au bord du lac Léman en Suisse. 
Dès mon plus jeune âge, j'ai développé un vif intérêt pour la loi et la justice, ce qui m'a finalement conduit à devenir avocat.
Durant mes études juridiques, j'ai rencontré l'amour de ma vie, Hendens, une femme extraordinaire avec qui j'ai pu fonder une famille à Lausanne à la place de la Riponne 23. Nous nous sommes mariés et nous avons eu cinq enfants merveilleux, Lina, Jules, Dorille, Marie, et Elisa. Au fil des ans, notre maison est devenue un lieu accueillant pour plusieurs pensionnaires qui ont trouvé refuge sous notre toit. Parmi ces pensionnaires, Anne Roth était une cuisinière distinguée. Ses plats délicieux ont uni notre famille autour de la nourriture, même si je dois vous avouer que notre petite Elisa préférait jouer avec sa nourriture que de la manger. Nos enfants ont grandi et se sont épanouis, suivant leurs propres chemins dans la vie avec les valeurs que nous leur avons transmises. Je suis reconnaissant pour la vie que j'ai eue, pour ma famille aimante et pour la chance d'avoir pu servir ma communauté en tant qu'avocat. J'espère que vous trouverez autant de bonheur dans votre vie que moi et ma famille et je dois vous dire adieu, je suis en retard pour le procès de mon client!

![AI-generated Photo of Charles Perrin and brothers](/docs/assets/charles_perrin.jpg)
Je m'appelle Charles Perrin, je viens de Lausanne et j'habite à la rue d'Ouchy 8 avec ma famille et mes frères depuis 1801.
Je suis né en 1801 et j'ai grandi avec mes frères Jean-Gaspard et Samuel-André.
J'ai épousé Julie Blanc, née en 1807, avec qui j'ai eu 2 enfants: Louis et Henri, nés en 1835 et 1842.
Mes frères et moi sommes tous pêcheurs et nous pêchons ensemble tous les jours pour nourrir notre famille.
Nous vivons sans pensionnaires, mais avec mes frères on se sent jamais seul!