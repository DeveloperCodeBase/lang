import json

en = json.load(open('locales/en/features.json'))
fa = json.load(open('locales/fa/features.json'))

# We will build the French tree based on en and fa
fr = {}

# index
fr['index'] = {
    "eyebrow": "Fonctionnalités universitaires",
    "title": "Tout ce dont une université a besoin, sur une plateforme unique",
    "lead": "{brand} est constitué de {count, number} fonctionnalités interconnectées — de l'évaluation des compétences et des cours en direct aux finances, au support et à l'infrastructure. Cliquez sur une carte pour voir sa composition détaillée."
}

# detail
fr['detail'] = {
    "notFound": {
        "title": "Fonctionnalité introuvable",
        "body": "L'URL fournie ne correspond à aucune des fonctionnalités de l'université.",
        "cta": "Voir toutes les fonctionnalités"
    },
    "backToIndex": "Toutes les fonctionnalités",
    "routeNotBuiltNote": "Cette fonctionnalité n'a pas encore été développée sous forme de page sur la plateforme — contactez-nous pour des commandes sur mesure ou plus d'informations.",
    "blocks": {
        "what": "Ce que fait cette fonctionnalité",
        "who": "À qui elle s'adresse",
        "problem": "Quel problème elle résout",
        "parts": "De quels composants elle est constituée"
    },
    "partsHint": "Ordre des étapes de travail de droite à gauche.",
    "nav": {
        "prev": "Fonctionnalité précédente",
        "next": "Fonctionnalité suivante"
    },
    "listSeparator": " · ",
    "schematicAria": "Schéma des étapes de travail pour la fonctionnalité {title}"
}

# Now for each feature in en['detail'], if it's a dict with what/who/problem/parts, translate it
# Let's map key terms and build high quality French descriptions
