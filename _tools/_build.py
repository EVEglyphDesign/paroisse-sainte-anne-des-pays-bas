"""Build all pages from verbatim source content."""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).parent))
from _partials import head, foot

OUT = Path(__file__).parent

# --- INDEX ---
(OUT / "index.html").write_text(head("Accueil", "index.html") + """
<h1>Bienvenue</h1>
<p class="lead">Bonjour et bienvenue au site de la Paroisse Sainte-Anne-des-Pays-Bas.</p>

<p>La Paroisse Sainte-Anne-des-Pays-Bas, fondée en 1981, est située à Fredericton au Nouveau-Brunswick (Canada) et dessert les francophones et les francophiles de la région du Grand Fredericton. En créant ce site, le Comité paroissial de pastorale a voulu se doter d'un outil de communication avec les paroissiennes et les paroissiens et présenter au grand public la vie paroissiale entourant cette paroisse dynamique. Bonne visite&nbsp;!</p>

<div class="card">
  <h3>Bâtir pour l'avenir… on continue</h3>
  <p>Plan stratégique de la paroisse. Voir la description du projet et le mot sur le lancement de cette campagne.</p>
</div>

<h2>Petites annonces</h2>

<div class="announce">
  <h4>Bureau</h4>
  <p>Le secrétariat de la paroisse Sainte-Anne-des-Pays-Bas est ouvert du mardi au vendredi, entre 14&nbsp;h&nbsp;30 et 17&nbsp;h&nbsp;30.</p>
</div>

<div class="announce">
  <h4>Groupe de prières</h4>
  <p>Vous êtes invités à vous rassembler pour prier ensemble aux intentions de la communauté, les samedis à 16&nbsp;h&nbsp;30 et les dimanches à 10&nbsp;h&nbsp;15.</p>
</div>

<div class="announce">
  <h4>Café après la messe de 11&nbsp;h</h4>
  <p>Le café fait relâche pour l'été et recommence le 10 septembre. Merci aux personnes qui, par leurs efforts, ont soutenu le café durant les derniers mois, ainsi qu'aux personnes qui ont profité de l'occasion pour se rassembler après la messe. Passez un bel été et au plaisir de vous revoir en septembre&nbsp;!</p>
</div>

<div class="announce">
  <h4>Fête de Sainte-Anne</h4>
  <p>Nous planifions une activité spéciale pour souligner la fête de Sainte-Anne. Le tout se déroulera le dimanche 23 juillet, à l'église. Nous aurons un BBQ et des activités plaisantes. Nous avons besoin de bénévoles pour nous aider. Si vous êtes disponible, prière d'envoyer un courriel à Lynn Chenard à <a href="mailto:lynnchenard@gmail.com">lynnchenard@gmail.com</a>.</p>
</div>

<div class="announce">
  <h4>Campagne de financement — Briques</h4>
  <p>La vente de briques se continue au coût de 10&nbsp;$ par brique. Pour participer, vous pouvez remettre une enveloppe sur laquelle vous indiquez votre nom, votre adresse et le nombre de briques que vous désirez acheter. Vous pouvez aussi utiliser les enveloppes identifiées «&nbsp;Briques&nbsp;» que vous retrouverez dans les bancs et au secrétariat de l'église. Vous pouvez remettre votre enveloppe au bureau de la paroisse les mardis, mercredis, jeudis et vendredis, entre 12&nbsp;h et 15&nbsp;h, ou la déposer dans la quête. Une brique, deux briques… Tentez votre chance&nbsp;!</p>
</div>

<div class="announce">
  <h4>Cuisine communautaire</h4>
  <p>La Cuisine communautaire est à la recherche de bénévoles pour aider dans la préparation et servir les repas du midi et du souper, sept jours par semaine. Les heures sont comme suit&nbsp;: pour le dîner, de 9&nbsp;h à 13&nbsp;h ou de 11&nbsp;h à 13&nbsp;h, et pour le souper, de 16&nbsp;h à 18&nbsp;h. Les besoins les plus pressants sont les lundis midi et les vendredis soirs, mais tous les jours ont des ouvertures pour des bénévoles. Prière de prendre contact avec Jothi au (506)&nbsp;457-1788. Merci de considérer vous impliquer pour venir en aide aux gens les plus démunis, une cause d'une importance vitale.</p>
</div>

<div class="announce">
  <h4>Adoration eucharistique</h4>
  <p>L'adoration eucharistique les dimanches à 14&nbsp;h&nbsp;30 est annulée et retournera en septembre. Les mardis et vendredis, l'adoration est entre 8&nbsp;h&nbsp;30 et 9&nbsp;h&nbsp;30, sans la bénédiction.</p>
</div>

<div class="announce">
  <h4>Sacrement de réconciliation</h4>
  <p>Tous les samedis, entre 15&nbsp;h et 16&nbsp;h, il y a le sacrement de réconciliation. Il est aussi possible de recevoir ce sacrement pendant l'adoration eucharistique.</p>
</div>

<div class="announce">
  <h4>Débit préautorisé</h4>
  <p>Il est encore temps de s'inscrire au débit préautorisé afin de faciliter la quête. Vous trouverez à l'entrée de l'église des formulaires pour les comptes de construction ou régulier. Une fois remplie avec les informations requises, vous pouvez apporter votre formulaire au secrétariat de la paroisse sur les heures de bureau. Merci&nbsp;!</p>
</div>

<div class="announce">
  <h4>Bienvenue aux nouveaux arrivants</h4>
  <p>Pour en savoir plus sur les différents groupes œuvrant dans la paroisse, visitez la section <a href="vie.html">Vie paroissiale</a>.</p>
</div>
""" + foot("2 juillet 2023"), encoding="utf-8")

# --- HISTORIQUE ---
(OUT / "historique.html").write_text(head("Historique", "historique.html") + """
<h1>Historique</h1>

<p>Les années 1960 sont témoins d'un accroissement de la population francophone dans la région de Fredericton et des environs. Devant la nécessité d'offrir à ces fidèles des services religieux en français, la paroisse St.&nbsp;Dunstan est la première, en 1965, à avoir une messe en français deux fois par mois&nbsp;; puis, au début des années 1970, des messes en français sont célébrées au Rosary Hall, couvent des religieuses. Ensuite, en 1976, une messe dominicale bimensuelle est également offerte à la paroisse St.&nbsp;Theresa de Nashwaaksis. À Noël de 1967, pour la première fois en deux siècles, les francophones de Fredericton peuvent assister à une messe de minuit en français dans la chapelle de l'université Saint&nbsp;Thomas. De 1978 à 1986, le père Samuel&nbsp;E. Diotte, vicaire à la paroisse St.&nbsp;Dunstan, est chargé de desservir la communauté francophone et, à partir du 15 octobre 1978, il célèbre deux messes tous les dimanches au théâtre du Centre communautaire Sainte-Anne. Ces célébrations occasionnent aussi la formation d'équipes d'animation liturgique et musicale. Viendront s'ajouter d'autres services&nbsp;: cours de catéchèse, de préparation au mariage, etc.</p>

<p>Privée d'une église depuis 221 ans, suite à la destruction de l'église du village de la pointe Sainte-Anne, la population francophone se fait lentement à l'idée d'avoir sa propre église. Au début des années 1980, un projet finira par se dessiner et aboutira, en l'an 2000, à la construction de l'église actuelle.</p>

<h2>Fondation de la paroisse Sainte-Anne-des-Pays-Bas</h2>

<p>Le comité paroissial de pionniers francophones de la région rencontre, au printemps de 1981, l'évêque de Saint-Jean, Mgr&nbsp;Arthur Gilbert, et lui propose la fondation d'une «&nbsp;paroisse française nationale&nbsp;» qui engloberait tous les catholiques romains de langue française de Fredericton et des environs. Ainsi, le 2 septembre de la même année, Mgr&nbsp;Gilbert annonce la naissance de la paroisse Sainte-Anne-des-Pays-Bas. Le premier curé sera le père Samuel&nbsp;E. Diotte.</p>

<p>En 1986, le père J.&nbsp;Stanislas Paulin est nommé 2<sup>e</sup> curé de la paroisse. Il y demeurera 15 ans, soit de 1986 à 2001. En 1987, l'évêque J.&nbsp;Edward Troy encourage la population à construire une église. Aidé de nombreux bénévoles, le père J.&nbsp;Stanislas Paulin deviendra le bâtisseur de l'église Sainte-Anne-des-Pays-Bas. Ce projet aura nécessité deux campagnes financières, la deuxième ayant le thème «&nbsp;Bâtir pour l'avenir&nbsp;». Au moment de l'octroi du contrat de construction, le coût prévu de l'église était de 1&nbsp;500&nbsp;000&nbsp;$, mais en réalité, il a été de plus de 2&nbsp;000&nbsp;000&nbsp;$. Au 31 août 2006, la dette se chiffrait à 449&nbsp;500&nbsp;$.</p>

<h2>Construction de l'église actuelle</h2>

<p>Le 18 octobre 1998, Mgr&nbsp;George Martin bénit le site à l'occasion de la cérémonie de la première pelletée de terre. En janvier 1999, le nouvel évêque de Saint-Jean est nommé&nbsp;: Mgr&nbsp;Joseph Faber MacDonald. Ce dernier appuie le projet église dès le début et c'est ainsi que la construction de l'église, dont l'architecte est Carl Smyth, est confiée à l'entrepreneur général B.&nbsp;&amp;&nbsp;S.&nbsp;Construction ltée. Le comité de construction achète les bancs d'une église de Québec, reçoit en don un chemin de la croix du diocèse de Valleyfield et le marbre de l'autel du diocèse de Québec. Un paroissien coordonne l'aménagement paysager du terrain.</p>

<p>La première messe célébrée dans la nouvelle église sera la messe de minuit de l'an 2000. L'entrée officielle se fera la fin de semaine du 18 février 2001.</p>

<h2>Dédicace</h2>

<p>La cérémonie de dédicace a lieu le 13 mai 2001 et est présidée par notre évêque, Mgr&nbsp;Joseph Faber MacDonald, le curé d'alors, le père J.&nbsp;Stanislas Paulin, le curé fondateur, le père Samuel&nbsp;E. Diotte, ainsi que par l'évêque émérite de Saint-Jean, Mgr&nbsp;J.&nbsp;Edward Troy. Il convient de signaler aussi la présence de nombreux autres prêtres. Notre curé actuel, le père Emery Brien, csc, remplace le père Paulin et entre en fonction le 31 juillet 2001. Le père Brien continue lui aussi à travailler avec les paroissiens et paroissiennes pour effacer la dette de construction de l'église.</p>

<h2>Vie paroissiale</h2>

<p>Un Conseil paroissial de pastorale et un Conseil paroissial des finances voient au bon fonctionnement des affaires de la paroisse. Divers groupes participent à toutes les tâches inhérentes à la vie paroissiale de Sainte-Anne-des-Pays-Bas, dont&nbsp;:</p>

<ul class="groups">
  <li>Comité de liturgie</li>
  <li>Chevaliers de Colomb</li>
  <li>Équipe de catéchètes</li>
  <li>Musiciens</li>
  <li>Autres groupes (visite des malades, cours de préparation au mariage, etc.)</li>
</ul>

<p>Deux congrégations religieuses ont participé pendant un certain temps à la vie paroissiale. Sœur Dora Bourgeois, de la congrégation des Filles de Jésus, a commencé à faire de l'animation liturgique aux messes célébrées au Centre communautaire Sainte-Anne dès 1978. Les Filles de Jésus ont été remplacées en 1983 par les Religieuses Notre-Dame-du-Sacré-Cœur. Ces dernières y sont restées jusqu'en 2001.</p>

<h2>Salle J.-Stanislas-Paulin</h2>

<p>Le 29 juillet 2001, la grande salle du sous-sol de l'église est dédiée en l'honneur du père J.&nbsp;Stanislas Paulin pour ses nombreuses années de service à la paroisse comme curé. Ce local peut accueillir au-delà de 150 personnes et est utilisé pour les besoins du groupe scout, pour les séances de catéchèse, ainsi que pour de nombreuses célébrations, dont les réceptions après les funérailles.</p>
""" + foot("28 mars 2011"), encoding="utf-8")

# --- NOS CURÉS (remplace la page Message du Curé) ---
(OUT / "cures.html").write_text(head("Nos curés", "cures.html") + """
<h1>Nos curés</h1>

<p class="lead">La paroisse Sainte-Anne-des-Pays-Bas a été servie par plusieurs curés depuis sa fondation en 1981. Cette page les nomme dans l'ordre, sans hiérarchie ni préférence.</p>

<h2>Père Samuel E. Diotte</h2>
<p><em>Curé fondateur (1981&ndash;1986).</em> Vicaire à la paroisse St.&nbsp;Dunstan de 1978 à 1986, chargé de desservir la communauté francophone. À partir du 15 octobre 1978, il célèbre deux messes tous les dimanches au théâtre du Centre communautaire Sainte-Anne. Lorsque Mgr Arthur Gilbert annonce la naissance de la paroisse le 2 septembre 1981, le père Diotte en devient le premier curé.</p>

<h2>Père J. Stanislas Paulin</h2>
<p><em>2<sup>e</sup> curé (1986&ndash;2001) &mdash; bâtisseur de l'église.</em> Nommé en 1986, il demeure curé pendant quinze ans. Aidé de nombreux bénévoles, il devient le bâtisseur de l'église Sainte-Anne-des-Pays-Bas &mdash; deux campagnes financières, dont la seconde portée par le thème «&nbsp;Bâtir pour l'avenir&nbsp;». Le 29 juillet 2001, la grande salle du sous-sol de l'église est dédiée en son honneur : la <strong>Salle J.-Stanislas-Paulin</strong>, qui peut accueillir plus de 150 personnes et sert au groupe scout, aux séances de catéchèse, et à de nombreuses célébrations dont les réceptions après les funérailles.</p>

<h2>Père Emery Brien, c.s.c.</h2>
<p><em>Curé à partir du 31 juillet 2001.</em> Entre en fonction après le père Paulin, et continue à travailler avec les paroissiens et paroissiennes pour effacer la dette de construction de l'église.</p>

<h2>Curés subséquents</h2>
<p>La paroisse a été servie par plusieurs autres prêtres au fil des années, dont le Père Léon Robichaud et le Père Savoie. Le curé en fonction est indiqué sur le <a href="feuillet.html">feuillet paroissial</a> courant et joignable au secrétariat, (506)&nbsp;444-6015.</p>

<div class="card">
  <h3>Plan stratégique de la paroisse</h3>
  <p>Vous pouvez consulter le plan stratégique «&nbsp;Bâtir pour l'avenir&hellip; on continue&nbsp;» au secrétariat de la paroisse.</p>
</div>
""" + foot(""), encoding="utf-8")

# --- NOTRE ÉGLISE ---
(OUT / "eglise.html").write_text(head("Notre église", "eglise.html") + """
<h1>Notre église</h1>

<p>L'église est construite sur l'emplacement original du local scout-guide, au coin des rues Regent et Priestman. Les paroissiens et paroissiennes ont fêté Noël 2000 dans leur nouvelle église. L'entrée officielle a eu lieu la fin de semaine du 18 février 2001, 242 ans après la destruction de la première église francophone de Fredericton lors de la déportation.</p>

<h2>Sections photographiques</h2>

<ul class="groups">
  <li>Extérieur de l'église</li>
  <li>Intérieur de l'église</li>
  <li>Chemin de croix</li>
  <li>Fonts baptismaux</li>
  <li>Bannières</li>
  <li>Vitraux</li>
</ul>
""" + foot("28 mars 2011"), encoding="utf-8")

# --- MESSES ---
(OUT / "messes.html").write_text(head("Horaire des messes", "messes.html") + """
<h1>Horaire des messes</h1>

<table class="schedule">
  <thead>
    <tr><th>Jour</th><th>Heure</th></tr>
  </thead>
  <tbody>
    <tr><td>Samedi soir</td><td>17&nbsp;h&nbsp;00</td></tr>
    <tr><td>Dimanche</td><td>11&nbsp;h&nbsp;00</td></tr>
    <tr><td>Lundi, mardi et vendredi</td><td>12&nbsp;h&nbsp;05</td></tr>
  </tbody>
</table>

<p>Voir le <a href="feuillet.html">Feuillet paroissial de la semaine</a> pour les exceptions.</p>
""" + foot("20 novembre 2020"), encoding="utf-8")

# --- FEUILLET ---
(OUT / "feuillet.html").write_text(head("Feuillet paroissial", "feuillet.html") + """
<h1>Feuillet paroissial</h1>

<p class="lead">Bulletins hebdomadaires de la Paroisse Sainte-Anne-des-Pays-Bas.</p>

<ul>
  <li>2 juillet 2023</li>
  <li>25 juin 2023</li>
  <li>18 juin 2023</li>
  <li>11 juin 2023</li>
</ul>

<p><em>Les archives complètes des feuillets sont maintenues par le secrétariat de la paroisse. Prière de consulter le <a href="https://www.sainte-anne-des-pays-bas.ca">site officiel</a> pour la publication la plus récente.</em></p>
""" + foot("2 juillet 2023"), encoding="utf-8")

# --- VIE PAROISSIALE ---
(OUT / "vie.html").write_text(head("Vie paroissiale", "vie.html") + """
<h1>Vie paroissiale</h1>

<p>Le Conseil paroissial de pastorale et le Conseil paroissial des finances voient au bon fonctionnement des affaires de la paroisse. Divers groupes participent à toutes les tâches inhérentes à la vie paroissiale de Sainte-Anne-des-Pays-Bas, dont&nbsp;:</p>

<ul class="groups">
  <li>Conseil paroissial de pastorale</li>
  <li>Conseil paroissial des finances</li>
  <li>Comité de liturgie</li>
  <li>Conseil de catéchèse</li>
  <li>Comité d'action sociale</li>
  <li>Chorale paroissiale</li>
  <li>Musiciens</li>
  <li>Club Richelieu</li>
  <li>Chevaliers de Colomb</li>
  <li>Autres groupes (visite des malades, cours de préparation au mariage, etc.)</li>
</ul>

<h2>Statistiques</h2>

<p>Vous pouvez accéder aux statistiques de la paroisse (baptêmes, confirmations, premières communions, mariages et sépultures/funérailles) au secrétariat.</p>
""" + foot("20 avril 2013"), encoding="utf-8")

# --- CATÉCHÈSE ---
(OUT / "catechese.html").write_text(head("Catéchèse", "catechese.html") + """
<h1>Catéchèse</h1>

<div class="card">
  <h3>Responsables de la catéchèse</h3>
  <p>Dans notre paroisse, la catéchèse est gérée par des bénévoles. Vous pouvez nous contacter en téléphonant à la secrétaire de la paroisse, Elisabeth, au (506)&nbsp;444-6015, ou en envoyant un courriel à <a href="mailto:catechese.paroisse@gmail.com">catechese.paroisse@gmail.com</a>.</p>
</div>

<h2>Petites annonces</h2>

<div class="announce">
  <h4>Février 2018 — Préparation à la 1<sup>re</sup> communion</h4>
  <p>Début de la préparation le dimanche 8 avril. Quatre rendez-vous&nbsp;: 8 avril, 22 avril, 6 mai et 26 mai. Date de la première communion&nbsp;: le dimanche 27 mai à 11&nbsp;h.</p>
</div>

<div class="announce">
  <h4>Février 2018 — Préparation à la confirmation</h4>
  <p>Démarrage le mardi 13 février, deuxième rendez-vous le 13 mars. Date de la confirmation&nbsp;: le mercredi 18 avril à 18&nbsp;h&nbsp;30.</p>
</div>

<div class="announce">
  <h4>Catéchistes</h4>
  <p>Tous les bénévoles sont les bienvenus. N'hésitez pas à nous appeler pour participer un dimanche selon vos disponibilités.</p>
</div>

<div class="announce">
  <h4>Novembre 2017 — Grade 7/8</h4>
  <p>Première réunion le vendredi 1<sup>er</sup> décembre&nbsp;: première soirée et nuit du groupe.</p>
</div>

<div class="announce">
  <h4>Concours de dessin — date limite le 10 décembre</h4>
  <p>Concours de dessin sur le thème «&nbsp;Garder le Christ dans la fête de Noël&nbsp;». Participez au concours d'une carte de Noël organisé par le Conseil 8409 et courez la chance de gagner des prix et de voir votre dessin imprimé. Le concours s'adresse aux enfants dès la maternelle.</p>
</div>

<div class="announce">
  <h4>Septembre 2017 — Catéchèse 2017-2018</h4>
  <p>Inscription le dimanche 17 octobre, à l'église, après la messe. 30&nbsp;$ par enfant. Nouveau format cette année vers une catéchèse intergénérationnelle. La catéchèse se déroule durant la messe du dimanche (11&nbsp;h&nbsp;00). Pour information&nbsp;: <a href="mailto:catechese.paroisse@gmail.com">catechese.paroisse@gmail.com</a>.</p>
</div>

<div class="card">
  <h4>Témoignage d'une mère</h4>
  <p>«&nbsp;J'ai accompagné ma fille à un de ses cours de catéchèse de 5<sup>e</sup> année aujourd'hui et ma foi, j'ai été très impressionnée. Je ne sais pas si c'est dû au nouveau programme, mais je n'avais encore jamais vu les enfants aussi heureux et à l'aise dans un cours de catéchèse. Le groupe a été divisé en 5 ou 6 petits groupes et chacun a dû faire une histoire basée sur l'histoire de David et Goliath. On transpose vers la réalité des enfants en leur disant que c'est comme lancer des mots poches. On fait un lien avec l'intimidation (le bullying). Et chaque groupe a fait une histoire et ils ont joué leurs histoires devant les parents.&nbsp;» — Marie-Claire</p>
</div>
""" + foot("24 mars 2018"), encoding="utf-8")

# --- ÉVÉNEMENTS ---
(OUT / "evenements.html").write_text(head("Événements", "evenements.html") + """
<h1>Événements</h1>

<ul>
  <li>30<sup>e</sup> anniversaire de prêtrise du Père Savoie — le 20 octobre 2012.</li>
  <li>Les décorations de Noël 2011 — décembre 2011.</li>
  <li>Messe du 30<sup>e</sup> anniversaire de la paroisse et du 10<sup>e</sup> anniversaire de l'église — le 16 octobre 2011.</li>
  <li>Rencontre des paroisses francophones du diocèse — le 20 mars 2011.</li>
  <li>Remerciements au Père Léon Robichaud — le 26 février 2011.</li>
  <li>Enregistrement de l'émission «&nbsp;Le Jour du Seigneur&nbsp;» — le 13 avril 2008.</li>
  <li>Visite de Mgr Robert Harris — les 29 et 30 septembre 2007.</li>
  <li>Au revoir au Père Brien — le 15 juillet 2007.</li>
  <li>Événements 2001.</li>
</ul>
""" + foot("16 novembre 2012"), encoding="utf-8")

# --- LIENS ---
(OUT / "liens.html").write_text(head("Liens", "liens.html") + """
<h1>Liens d'intérêt</h1>

<h2>Diocèse et Église</h2>
<ul>
  <li><a href="https://www.diocesesj.org">Diocèse de Saint-Jean</a></li>
  <li><a href="https://www.cccb.ca/fr/">Conférence des évêques catholiques du Canada</a></li>
  <li><a href="https://www.vatican.va">Saint-Siège (Vatican)</a></li>
</ul>

<h2>Ressources liturgiques</h2>
<ul>
  <li><a href="http://www.prionseneglise.ca/">Prions en Église (édition canadienne française)</a></li>
  <li><a href="https://www.aelf.org/">AELF — textes liturgiques pour les pays francophones</a></li>
</ul>

<h2>Communauté francophone</h2>
<ul>
  <li><a href="https://centre-sainte-anne.nb.ca/">Centre communautaire Sainte-Anne</a></li>
  <li><a href="http://www.franco-fredericton.com/">Franco-Fredericton</a></li>
</ul>
""" + foot("2 juillet 2023"), encoding="utf-8")

# --- CONTACT ---
(OUT / "contact.html").write_text(head("Contact", "contact.html") + """
<h1>Contact</h1>

<p class="lead">N'hésitez pas à communiquer avec nous pour tout renseignement.</p>

<div class="contact-block">
  <dl>
    <dt>Secrétariat de la paroisse</dt>
    <dd>Téléphone&nbsp;: (506)&nbsp;444-6015</dd>
    <dd>Télécopieur&nbsp;: (506)&nbsp;450-8699</dd>
    <dd>Courriel&nbsp;: <a href="mailto:sainteannedespaysbas@gmail.com">sainteannedespaysbas@gmail.com</a></dd>

    <dt>Heures de bureau</dt>
    <dd>Ouvert du mardi au vendredi, entre 14&nbsp;h&nbsp;30 et 17&nbsp;h&nbsp;30.</dd>

    <dt>En cas d'urgence</dt>
    <dd>Presbytère&nbsp;: (506)&nbsp;455-0815</dd>

    <dt>Adresse</dt>
    <dd>715, rue Priestman<br>Fredericton (N.-B.) &nbsp;E3B 5W7</dd>

    <dt>Charité enregistrée</dt>
    <dd>N<sup>o</sup> 107020331 RR0043</dd>
  </dl>
</div>

<p><em>Pour joindre le curé en fonction, prière de passer par le secrétariat de la paroisse au (506)&nbsp;444-6015.</em></p>
""" + foot("9 septembre 2022"), encoding="utf-8")

print("Built", len(list(OUT.glob("*.html"))), "HTML pages")
