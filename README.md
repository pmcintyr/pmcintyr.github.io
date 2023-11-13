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
Map rows between each yearly file and illustrate qualitative descriptions of the lives of the best mapped homeowners.

### Recits Lausannois
![AI-generated Photo of Jean Mandrot's Family](/docs/assets/jean_mandrot.jpg)

Je m'appelle Jean Mandrot, et je suis né en 1785 à Morges, au bord du lac Léman en Suisse. 
Dès mon plus jeune âge, j'ai développé un vif intérêt pour la loi et la justice, ce qui m'a finalement conduit à devenir avocat.
Durant mes études juridiques, j'ai rencontré l'amour de ma vie, Hendens, une femme extraordinaire avec qui j'ai pu fonder une famille à Lausanne à la Place de la Riponne 23. Nous nous sommes mariés et nous avons eu cinq enfants merveilleux, Lina, Jules, Dorille, Marie, et Elisa. Au fil des ans, notre maison est devenue un lieu accueillant pour plusieurs pensionnaires qui ont trouvé refuge sous notre toit. Parmi ces pensionnaires, Anne Roth était une cuisinière distinguée. Ses plats délicieux ont uni notre famille autour de la nourriture, même si je dois vous avouer que notre petite Elisa préférait jouer avec sa nourriture que de la manger. Nos enfants ont grandi et se sont épanouis, suivant leurs propres chemins dans la vie avec les valeurs que nous leur avons transmises. Je suis reconnaissant pour la vie que j'ai eue, pour ma famille aimante et pour la chance d'avoir pu servir ma communauté en tant qu'avocat. J'espère que vous trouverez autant de bonheur dans votre vie que moi et ma famille et je dois vous dire adieu, je suis en retard pour le procès de mon client!

![AI-generated Photo of Charles Perrin and brothers](/docs/assets/charles_perrin.jpg)
Je m'appelle Charles Perrin, je viens de Lausanne et j'habite à l'Avenue d'Ouchy 8 depuis que je suis né, c'est-à-dire en 1801.
J'ai grandi dans une famille de pêcheurs avec mes frères Jean-Gaspard et Samuel-André.
J'ai épousé Julie Blanc, née en 1807, avec qui j'ai eu 2 enfants: Louis et Henri, nés en 1835 et 1842.
Mes frères et moi sommes tous pêcheurs et nous pêchons ensemble tous les jours pour nourrir notre famille.
Nous vivons sans pensionnaires, mais avec mes frères on se sent jamais seul!

![AI-generated Photo of Maurice Epach and appentice](/docs/assets/maurice_epach.jpg)
Je m'appelle Maurice Epach, je suis né en 1805 à Lausanne et j'habite à la Rue Centrale 1 qui s'appelait à mon époque la Rue du Pré.
Je suis un marchand célibataire et sans enfants.
Pour me porter compagnie, j'ai décidé d'héberger des pensionnaires pour m'assister dans mes tâches quotidiennes.
D'abord j'avais une domestique qui s'appelait Marie Sorent, mais maintenant j'ai une autre domestique au nom de Marguerite Desfayes qui vient de Grandvaux.
J'héberge également mon apprentie bernoise qui s'appelle Léonor ainsi que Francois qui m'aide en tant que commis de cuisine et qui vient d'Orzens. Je suis heureux de savoir que Léonor va pouvoir reprendre mon commerce lorsque je serai trop agé pour m'en occuper.

![AI-generated Photo of Auguste Piot and wife](/docs/assets/auguste_piot.jpg)
Je m'appelle Auguste Piot, je suis né en 1784 à Pailly et j'habite à la Rue Caroline 60.
Ma femme Ansermier est née en 1783 et est décédée en 1852.
En 1845, nous avions hébergé une pensionnaire bernoise: Marie Pinchotte.
À partir de 1848, on hébergeait 2 domestiques: Susette et Mermoud de Poliez-le-Grand.

![AI-generated Photo of César Dufournet and family](/docs/assets/cesar_dufournet.jpg)
Je m'appelle César Dufournet. Je suis né en 1790, je viens de Lausanne et j'habite à la Rue Cité-Devant 1.
Je suis un professeur dans une école vaudoise. Je suis marié à Madame Chavannes, née en 1793.
Nous avons 6 filles, Pauline, Charlotte, Elise, Emma, Helene et Sophie nées en 1827, 1828, 1830, 1831, 1835 et 1835.
Charlotte est décédée en 1843 à 15 ans. Emma s'est mariée et est partie de la maison en 1850 à 19 ans.
On héberge 3 domestiques: Marianne Gonnet de Vuarrens, Lise Bosset de Bex et Henriette Pillet de Pampigny.