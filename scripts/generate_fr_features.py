import json

en = json.load(open('locales/en/features.json'))
fa = json.load(open('locales/fa/features.json'))

fr = {
    "index": {
        "eyebrow": "Fonctionnalités universitaires",
        "title": "Tout ce dont une université a besoin, sur une plateforme unique",
        "lead": "{brand} est constitué de {count, number} fonctionnalités interconnectées — de l'évaluation des compétences et des cours en direct aux finances, au support et à l'infrastructure. Cliquez sur une carte pour voir sa composition détaillée."
    },
    "detail": {
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
}

trans = {
  "competency-assessment-center": {
    "what": "Le centre d'évaluation gère le cycle complet d'évaluation d'un candidat, de la définition du projet à la publication du rapport : les exercices sont planifiés, les évaluateurs notent de manière indépendante et les résultats ne sont finalisés qu'après une séance de consensus humain.",
    "who": ["Responsable du centre d'évaluation", "Évaluateurs", "Organisations mesurant le recrutement ou la promotion sur la base des compétences"],
    "problem": "L'évaluation des compétences est généralement réduite à des entretiens subjectifs sans documentation défendable. Ici, chaque score est lié à un exercice précis, un évaluateur identifié et un indicateur spécifique.",
    "parts": ["Définition du modèle de compétences", "Planification des exercices", "Notation indépendante", "Séance de consensus (Wash-up)", "Rapport final"]
  },
  "candidate-assessment-journey": {
    "what": "Le parcours du candidat guide chaque participant à travers les étapes d'évaluation, les tests psychométriques, les études de cas et les entretiens avec un calendrier clair et des consignes adaptées.",
    "who": ["Candidats à l'évaluation", "Candidats au recrutement", "Employés en parcours de promotion"],
    "problem": "Le manque de clarté dans le processus d'évaluation crée du stress et fausse les résultats. Ce parcours offre transparence et sérénité aux candidats.",
    "parts": ["Tableau de bord candidat", "Consignes d'exercices", "Passation des tests", "Accès aux retours"]
  },
  "assessor-console": {
    "what": "La console de l'évaluateur permet de saisir les observations en temps réel pendant les simulations, de noter selon des grilles comportementales normées et de soumettre des évaluations argumentées.",
    "who": ["Évaluateurs certifiés", "Psychologues du travail", "Jurys d'évaluation"],
    "problem": "La prise de notes sur papier entraîne des pertes d'informations et des retards dans l'agrégation des scores.",
    "parts": ["Grille d'observation", "Échelles de comportement", "Saisie des preuves", "Calcul d'alignement"]
  },
  "washup-consensus-session": {
    "what": "La séance de consensus (Wash-up) réunit les évaluateurs pour confronter leurs notations indépendantes, débattre des écarts et s'accorder sur le profil final de compétences du candidat.",
    "who": ["Président du jury", "Évaluateurs ayant observé le candidat", "Responsable qualité"],
    "problem": "Les biais individuels faussent l'évaluation sans une étape formelle de calibration et d'arbitrage collégial.",
    "parts": ["Matrice des écarts", "Débat collégial", "Arbitrage des notes", "Validation du consensus"]
  },
  "assessment-report-publish": {
    "what": "Le module de publication génère des rapports d'évaluation détaillés avec cartographie radar, points forts, axes de développement et recommandations opérationnelles.",
    "who": ["Commanditaires RH", "Responsables d'évaluation", "Candidats évalués"],
    "problem": "La rédaction manuelle de rapports prend des jours et manque d'homogénéité graphique et méthodologique.",
    "parts": ["Moteur de rendu graphique", "Radar de compétences", "Synthèse qualitative", "Export PDF sécurisé"]
  },
  "shared-competency-core": {
    "what": "Le référentiel central de compétences définit les familles de compétences, les niveaux de maîtrise et les indicateurs observables réutilisables dans toute l'institution.",
    "who": ["Directeurs des programmes", "Responsables RH", "Concepteurs pédagogiques"],
    "problem": "La dispersion des définitions de compétences crée des incohérences entre formation, certification et évaluation professionnelle.",
    "parts": ["Taxonomie des compétences", "Indicateurs comportementaux", "Niveaux de maîtrise", "Dictionnaire partagé"]
  },
  "assessment-tool-registry": {
    "what": "Le registre des outils d'évaluation répertorie les simulations, jeux de rôle, bacs à sable et exercices validés avec leurs critères psychométriques.",
    "who": ["Responsables méthodologiques", "Concepteurs d'épreuves", "Évaluateurs"],
    "problem": "L'utilisation d'exercices non calibrés ou obsolètes dégrade la validité prédictive des évaluations.",
    "parts": ["Catalogue d'épreuves", "Fiches techniques", "Versionnage des scénarios", "Normes d'étalonnage"]
  },
  "psychometric-test-bank": {
    "what": "La banque de tests psychométriques héberge des questionnaires de personnalité, de raisonnement et d'aptitudes cognitives conformes aux standards scientifiques.",
    "who": ["Psychologues", "Candidats", "Responsables d'évaluation"],
    "problem": "Le recours à des plateformes tierces non intégrées disperse les données candidats et complique la conformité RGPD.",
    "parts": ["Passation chronométrée", "Calcul automatique des percentiles", "Détection d'anomalies", "Banque d'items"]
  },
  "individual-development-plan": {
    "what": "Le plan individuel de développement (PID) traduit les résultats de l'évaluation en actions concrètes : formations recommandées, mentorat et jalons d'apprentissage.",
    "who": ["Apprenants", "Managers", "Tuteurs et mentors"],
    "problem": "Les évaluations restent souvent lettre morte sans suivi opérationnel post-évaluation.",
    "parts": ["Objectifs SMART", "Recommandations de cours", "Suivi des jalons", "Entretiens de progrès"]
  },
  "employer-portal": {
    "what": "Le portail employeur permet aux entreprises partenaires de commander des évaluations, de suivre les cohortes de candidats et de consulter les profils certifiés.",
    "who": ["Recruteurs d'entreprises", "Responsables formation partenaires", "Administrateurs des partenariats"],
    "problem": "Les échanges par e-mail et tableurs dispersés ralentissent le recrutement et augmentent le risque d'erreurs.",
    "parts": ["Gestion des commandes", "Suivi des cohortes", "Consultation des profils", "Facturation entreprise"]
  },
  "membership-registry": {
    "what": "Le registre des membres gère les adhésions institutionnelles, les cotisations, les statuts d'affiliation et les droits d'accès aux services réservés.",
    "who": ["Secrétariat général", "Membres individuels et collectifs", "Responsables des adhésions"],
    "problem": "Le suivi manuel des adhésions entraîne des impayés et une gestion fastidieuse des droits d'accès.",
    "parts": ["Fiches d'adhésion", "Renouvellement automatique", "Attestations de membre", "Contrôle des droits"]
  },
  "member-directory": {
    "what": "L'annuaire des membres offre une recherche multicritères par spécialité, localisation et affiliation pour favoriser le réseautage académique et professionnel.",
    "who": ["Communauté universitaire", "Alumni", "Partenaires industriels"],
    "problem": "L'isolement des diplômés et des membres freine les opportunités de collaboration et de mentorat.",
    "parts": ["Recherche à facettes", "Filtres par discipline", "Messagerie directe", "Protection des données"]
  },
  "expertise-card": {
    "what": "La carte d'expertise résume les compétences certifiées, les publications, les projets menés et les validations de pairs d'un membre.",
    "who": ["Enseignants-chercheurs", "Experts métier", "Consultants académiques"],
    "problem": "Les CV statiques ne reflètent pas les compétences vérifiées en temps réel par l'institution.",
    "parts": ["Badges de compétence", "Preuves associées", "Vérification par les pairs", "Lien partageable"]
  },
  "credential-registry-verify": {
    "what": "Le registre des titres et certifications permet la vérification instantanée et infalsifiable des diplômes via QR code et signature cryptographique.",
    "who": ["Employeurs", "Diplômés", "Services académiques de vérification"],
    "problem": "La fraude aux diplômes et la lourdeur des vérifications téléphoniques nuisent à la réputation de l'université.",
    "parts": ["Identifiant unique", "Signature numérique", "Page de vérification publique", "Registre inviolable"]
  },
  "live-class": {
    "what": "La classe en direct offre un environnement de visioconférence pédagogique complet avec tableau blanc, levée de main, sous-titres, sondages et répartition en salles.",
    "who": ["Enseignants", "Étudiants", "Assistants pédagogiques"],
    "problem": "Les outils de visioconférence génériques ne sont pas conçus pour la pédagogie universitaire et ne tracent pas la participation.",
    "parts": ["Audio/Vidéo WebRTC", "Tableau blanc collaboratif", "Salles de sous-groupes", "Sondages en direct"]
  },
  "session-report-attendance": {
    "what": "Le rapport de séance consolide automatiquement les présences réelles, la durée de connexion, les interactions et les transcriptions dès la fin du cours.",
    "who": ["Enseignants", "Scolarité", "Responsables pédagogiques"],
    "problem": "Le pointage manuel en début de cours fait perdre un temps précieux et ne mesure pas la présence effective.",
    "parts": ["Feuille de présence horodatée", "Statistiques d'engagement", "Journal du chat", "Enregistrement vidéo"]
  },
  "exam-assessment-engine": {
    "what": "Le moteur d'évaluation des examens gère la passation sécurisée des épreuves écrites et QCM avec tirage aléatoire, chronomètre strict et sauvegarde continue.",
    "who": ["Étudiants", "Enseignants concepteurs", "Surveillants d'examen"],
    "problem": "Les pertes de connexion pendant les examens en ligne provoquent la panique et des pertes de données.",
    "parts": ["Passation hors-ligne résiliente", "Tirage d'items", "Chronomètre verrouillé", "Sauvegarde continue"]
  },
  "question-bank": {
    "what": "La banque de questions centralise les items d'évaluation classés par compétence, niveau de difficulté taxonomique et historique de performance psychométrique.",
    "who": ["Équipes pédagogiques", "Commissions d'examen", "Auteurs de contenus"],
    "problem": "La création répétitive de sujets d'examen de zéro engendre des disparités de niveau entre sessions.",
    "parts": ["Indexation par compétence", "Analyse de discrimination", "Versionnage des items", "Générateur d'épreuves"]
  },
  "proctoring-review": {
    "what": "Le module de revue de surveillance analyse les alertes comportementales détectées pendant les épreuves pour permettre une décision humaine équitable.",
    "who": ["Commission de discipline", "Surveillants assermentés", "Responsables d'examen"],
    "problem": "La surveillance automatisée génère de faux positifs qui exigent un examen humain contradictoire.",
    "parts": ["Journal des alertes", "Revue vidéo horodatée", "Rapport de conformité", "Décision collégiale"]
  },
  "academic-sis": {
    "what": "Le système d'information académique (SIS) structure l'arborescence des facultés, départements, maquettes de cours, inscriptions et parcours des étudiants.",
    "who": ["Directeurs de scolarité", "Secrétaires pédagogiques", "Doyens"],
    "problem": "Les logiciels de scolarité historiques sont rigides, lents et déconnectés des outils d'enseignement numérique.",
    "parts": ["Maquettes pédagogiques", "Inscriptions administratives", "Gestion des cohortes", "Dossier étudiant"]
  },
  "regulation-policy-engine": {
    "what": "Le moteur de règlements applique automatiquement les règles de compensation, de crédits ECTS, de prérequis et de conditions de diplomation.",
    "who": ["Responsables de la scolarité", "Commissions des examens", "Conseillers d'orientation"],
    "problem": "Le calcul manuel des conditions de validation de semestre est source d'erreurs contentieuses.",
    "parts": ["Règles de compensation", "Contrôle des prérequis", "Gestion des dispenses", "Validation des ECTS"]
  },
  "gradebook-grade-flow": {
    "what": "Le carnet de notes numérique orchestre la saisie des notes continues et d'examen, les coefficients, les recours et la délibération finale du jury.",
    "who": ["Enseignants", "Membres du jury de délibération", "Étudiants"],
    "problem": "La circulation de fichiers tableurs par e-mail compromet la confidentialité et la cohérence des notes.",
    "parts": ["Saisie sécurisée des notes", "Pondération et barèmes", "Procédure d'appel", "Procès-verbal de délibération"]
  },
  "admissions-apply": {
    "what": "Le portail des admissions gère la candidature en ligne, le dépôt des pièces justificatives, l'évaluation des dossiers et le paiement des frais de dossier.",
    "who": ["Candidats externes", "Commission d'admission", "Service financier"],
    "problem": "Le traitement des dossiers papier sature les services et allonge les délais de réponse aux candidats.",
    "parts": ["Formulaire de candidature", "Dépôt des pièces", "Grille d'évaluation du dossier", "Décision d'admission"]
  },
  "wallet-payments": {
    "what": "Le portefeuille étudiant permet la gestion du solde, le paiement des frais annexes, les recharges en ligne et la consultation des reçus fiscaux.",
    "who": ["Étudiants", "Comptabilité", "Parents d'élèves"],
    "problem": "La multiplicité des canaux de paiement engendre des retards de conciliation comptable.",
    "parts": ["Solde du compte", "Passerelle de paiement sécurisée", "Historique des transactions", "Reçus officiels"]
  },
  "tuition-finance": {
    "what": "Le module de frais de scolarité gère les échéanciers de paiement, les bourses, les remises institutionnelles et les relances automatiques.",
    "who": ["Direction administrative et financière", "Étudiants boursiers", "Comptables"],
    "problem": "Les impayés non anticipés fragilisent la trésorerie de l'établissement.",
    "parts": ["Plan d'échéances", "Attribution des bourses", "Suivi des encaissements", "Relances graduées"]
  },
  "subscription-plans": {
    "what": "Le catalogue des forfaits gère les abonnements d'accès aux cours, aux bibliothèques numériques et aux services d'assistance IA selon le profil.",
    "who": ["Responsables marketing", "Abonnés", "Équipes financières"],
    "problem": "La gestion rigide des accès empêche la diversification des modèles de revenus de l'université.",
    "parts": ["Grille tarifaire", "Gestion des quotas", "Renouvellement récurrent", "Plafonds d'utilisation"]
  },
  "knowledge-marketplace": {
    "what": "La place de marché du savoir permet la publication, l'achat et la distribution de cours en ligne, modules de perfectionnement et ressources académiques.",
    "who": ["Auteurs de cours", "Apprenants tout au long de la vie", "Gestionnaires du catalogue"],
    "problem": "Les créateurs de contenus universitaires manquent d'un canal direct et valorisant pour diffuser leur savoir.",
    "parts": ["Boutique de cours", "Aperçus et avis", "Paiement en un clic", "Accès immédiat"]
  },
  "course-studio": {
    "what": "Le studio de conception de cours offre un éditeur modulaire pour structurer chapitres, leçons, vidéos, quiz intégrés et devoirs interactifs.",
    "who": ["Ingénieurs pédagogiques", "Enseignants auteurs", "Coordonnateurs de modules"],
    "problem": "Les interfaces de création de cours classiques sont austères et découragent les enseignants innovants.",
    "parts": ["Éditeur de plan de cours", "Glisser-déposer de blocs", "Intégration multimédia", "Prévisualisation apprenant"]
  },
  "media-pipeline-captions": {
    "what": "Le pipeline multimédia traite les vidéos enregistrées, génère les sous-titres automatiques, transcrit les cours et indexe le contenu pour la recherche.",
    "who": ["Étudiants malentendants", "Enseignants", "Apprenants en révision"],
    "problem": "L'inaccessibilité des enregistrements vidéo prive les étudiants en situation de handicap et nuit à l'indexation.",
    "parts": ["Transcodage adaptatif", "Génération de sous-titres VTT", "Indexation textuelle", "Lecteur accessible"]
  },
  "author-payouts": {
    "what": "Le module de rémunération des auteurs calcule les redevances issues des ventes de cours et d'abonnements, génère les états fiscaux et pilote les virements.",
    "who": ["Enseignants auteurs", "Service paie et comptabilité", "Direction des partenariats"],
    "problem": "Le calcul manuel du partage de revenus sur les ventes de cours est complexe et source de litiges.",
    "parts": ["Calcul des commissions", "Tableau de bord auteur", "Bordereaux de reversement", "Historique fiscal"]
  },
  "wellness-counseling": {
    "what": "Le pôle bien-être et conseil assure la prise de rendez-vous confidentielle avec les psychologues et conseillers universitaires et oriente vers les aides.",
    "who": ["Étudiants en difficulté", "Psychologues universitaires", "Assistantes sociales"],
    "problem": "La stigmatisation et la difficulté d'accès aux services de santé mentale aggravent le décrochage universitaire.",
    "parts": ["Prise de rendez-vous anonyme", "Lignes d'assistance d'urgence", "Fiches d'auto-évaluation", "Dossier médico-social protégé"]
  },
  "ai-assistant-agents": {
    "what": "Les assistants intelligents spécialisés fournissent du tutorat 24/7 basé sur les documents de cours (RAG) et aident les enseignants à générer des exercices.",
    "who": ["Étudiants en quête d'aide", "Enseignants concepteurs", "Tuteurs d'accompagnement"],
    "problem": "Les enseignants ne peuvent répondre individuellement et en continu aux milliers de questions des étudiants.",
    "parts": ["Tuteur IA augmenté par RAG", "Générateur d'exercices", "Citations des sources de cours", "Garde-fous académiques"]
  },
  "academic-messenger-network": {
    "what": "Le réseau de messagerie académique propose des canaux structurés par cours, groupes de travail et échanges directs avec respect des heures de disponibilité.",
    "who": ["Étudiants", "Enseignants", "Délégués de promotion"],
    "problem": "L'utilisation d'applications de messagerie grand public mélange vie privée et études et disperse les communications officielles.",
    "parts": ["Canaux de cours", "Conversations de groupe", "Partage de documents académiques", "Plages de disponibilité"]
  },
  "service-desk": {
    "what": "Le centre d'assistance universitaire (Service Desk) centralise les demandes techniques, administratives et pédagogiques avec suivi par tickets et SLA.",
    "who": ["Étudiants et personnels", "Équipes support technique", "Gestionnaires de scolarité"],
    "problem": "Les e-mails sans suivi finissent perdus et créent de la frustration chez les usagers.",
    "parts": ["Création de tickets", "Attribution intelligente", "Base de connaissances", "Suivi des délais de réponse"]
  },
  "exec-dashboard": {
    "what": "Le tableau de bord exécutif offre à la gouvernance une vue consolidée des KPI : taux de rétention, assiduité globale, finances et satisfaction étudiante.",
    "who": ["Présidence d'université", "Doyens", "Membres du conseil d'administration"],
    "problem": "Les décideurs manquent d'indicateurs consolidés en temps réel pour piloter la stratégie universitaire.",
    "parts": ["Indicateurs clés de performance", "Graphiques d'évolution", "Alertes stratégiques", "Rapports pour le conseil"]
  },
  "multi-tenancy": {
    "what": "L'architecture multi-établissements permet d'héberger plusieurs facultés ou institutions partenaires avec une isolation stricte des données et personnalisation de marque.",
    "who": ["Administrateurs système", "Réseaux d'universités", "Établissements partenaires"],
    "problem": "Le déploiement d'instances séparées pour chaque école multiplie les coûts de maintenance et d'infrastructure.",
    "parts": ["Cloisonnement des données", "Marque blanche", "Configuration par campus", "Console d'administration globale"]
  },
  "auth-security-hardening": {
    "what": "Le socle de sécurité et d'authentification assure le contrôle d'accès basé sur les rôles (RBAC), la double authentification et la protection contre les intrusions.",
    "who": ["Responsables sécurité (RSSI)", "Administrateurs système", "Utilisateurs finaux"],
    "problem": "Les universités sont des cibles privilégiées de cyberattaques et de vols d'identifiants.",
    "parts": ["Authentification multifacteur (MFA)", "Contrôle d'accès RBAC", "Gestion des sessions", "Protection contre les attaques par force brute"]
  },
  "sms-otp-verification": {
    "what": "La vérification par SMS OTP sécurise la connexion, la réinitialisation de mot de passe et la confirmation d'opérations sensibles par code temporaire.",
    "who": ["Utilisateurs de la plateforme", "Services de scolarité", "Équipe sécurité"],
    "problem": "Les mots de passe simples sont facilement compromis sans second facteur sur téléphone mobile.",
    "parts": ["Envoi de code par SMS", "Validation à usage unique", "Gestion des quotas d'envoi", "Protection anti-abus"]
  },
  "hr-hiring-payroll": {
    "what": "Le module RH gère les recrutements académiques, les contrats d'enseignement, le suivi des heures de cours et la préparation de la paie des vacataires.",
    "who": ["Direction des ressources humaines", "Enseignants vacataires", "Chefs de département"],
    "problem": "Le décompte des heures d'enseignement complémentaires sur tableur génère des retards de paie et des contentieux.",
    "parts": ["Gestion des candidatures académiques", "Contrats de travail", "Décompte des heures d'enseignement", "Exports paie"]
  },
  "course-hub-ia": {
    "what": "Le pôle de cours organise l'architecture de l'information pédagogique : syllabus, bibliographie, ressources téléchargeables et calendrier d'évaluation.",
    "who": ["Étudiants", "Enseignants", "Tuteurs"],
    "problem": "La dispersion des documents de cours désoriente les étudiants et nuit à la régularité du travail.",
    "parts": ["Syllabus interactif", "Arborescence documentaire", "Jalons du semestre", "Ressources recommandées"]
  },
  "panel-analytics": {
    "what": "Le panneau d'analyse fournit des métriques précises sur la consultation des vidéos, l'avancement des devoirs et les risques de décrochage individuel.",
    "who": ["Enseignants", "Tuteurs pédagogiques", "Conseillers d'études"],
    "problem": "Les enseignants ne détectent les étudiants en décrochage qu'au moment des examens finaux, trop tard pour agir.",
    "parts": ["Taux de complétion", "Temps d'apprentissage", "Détection précoce des décrocheurs", "Rapports par cohorte"]
  },
  "parent-portal": {
    "what": "Le portail parental permet aux parents de consulter les présences, le calendrier des examens et le solde financier de leurs enfants en toute transparence.",
    "who": ["Parents d'élèves", "Tuteurs légaux", "Services administratifs"],
    "problem": "L'absence d'information des familles limite l'accompagnement des étudiants plus jeunes ou internationaux.",
    "parts": ["Suivi d'assiduité", "Relevés de notes officiels", "Paiement en ligne des frais", "Messagerie avec l'établissement"]
  },
  "org-portal": {
    "what": "Le portail d'organisation permet aux entreprises et institutions d'inscrire des groupes de collaborateurs et de suivre leur montée en compétences.",
    "who": ["Responsables formation d'entreprises", "Commanditaires institutionnels", "Responsables formation continue"],
    "problem": "Les financeurs d'entreprises exigent des preuves d'assiduité et de réussite difficiles à collecter manuellement.",
    "parts": ["Inscriptions groupées", "Rapports d'assiduité entreprise", "Certificats de réalisation", "Facturation centralisée"]
  },
  "self-hosted-monitoring": {
    "what": "Le module de supervision surveille en continu la santé des serveurs, la latence des flux vidéo, la charge des bases de données et la disponibilité des API.",
    "who": ["Administrateurs système", "Équipes DevOps", "Directeurs techniques"],
    "problem": "Les pannes imprévues pendant les périodes de cours perturbent gravement l'activité universitaire.",
    "parts": ["Sondes de disponibilité", "Alertes en temps réel", "Métriques de performance", "Statut public des services"]
  },
  "audit-log": {
    "what": "Le journal d'audit enregistre de manière immuable chaque action sensible : modification de note, accès aux dossiers, transactions financières et changements de droits.",
    "who": ["Responsables conformité", "Auditeurs internes", "Délégué à la protection des données (DPO)"],
    "problem": "L'absence de traçabilité empêche de résoudre les contestations de notes ou les suspicions de fuite de données.",
    "parts": ["Horodatage certifié", "Identifiant de l'opérateur", "Données avant/après", "Recherche d'audit infalsifiable"]
  },
  "academic-calendar": {
    "what": "Le calendrier universitaire centralise les périodes de cours, les semaines d'examens, les vacances, les dates limites d'inscription et les événements du campus.",
    "who": ["Toute la communauté universitaire", "Étudiants", "Services de planification"],
    "problem": "La coexistence de calendriers contradictoires entre facultés crée des conflits d'emploi du temps insolubles.",
    "parts": ["Semestrialisation", "Sessions d'examens", "Jours fériés et fermetures", "Synchronisation iCal"]
  },
  "brand-trust-seals": {
    "what": "Les sceaux de confiance et accréditations valorisent les labels de qualité, les classements internationaux et les certifications de conformité de l'établissement.",
    "who": ["Direction de la communication", "Candidats internationaux", "Partenaires académiques"],
    "problem": "Le manque de visibilité des accréditations affaiblit l'attractivité internationale de l'université.",
    "parts": ["Badges d'accréditation", "Liens de vérification officielle", "Mentions de conformité", "Affichage institutionnel"]
  },
  "jalali-calendar-ui": {
    "what": "L'interface calendrier Jalali assure la prise en charge native du calendrier solaire hégirien pour la planification des cours, examens et échéances.",
    "who": ["Étudiants et personnels des régions utilisant le calendrier persan", "Scolarité", "Enseignants"],
    "problem": "Les plateformes internationales imposent le calendrier grégorien, créant des confusions sur les jours fériés locaux et semestres.",
    "parts": ["Sélecteur de date Jalali", "Conversion grégorienne bidirectionnelle", "Affichage des jours fériés", "Prise en charge de la numération persane"]
  }
}

for k, v in trans.items():
    fr['detail'][k] = v

with open('locales/fr/features.json', 'w', encoding='utf-8') as f:
    json.dump(fr, f, ensure_ascii=False, indent=2)

print("Generated locales/fr/features.json successfully!")
