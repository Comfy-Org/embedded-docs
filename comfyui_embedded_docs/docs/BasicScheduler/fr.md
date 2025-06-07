Le nœud `BasicScheduler` est conçu pour calculer une séquence de valeurs sigma pour les modèles de diffusion en fonction du planificateur, du modèle et des paramètres de débruitage fournis. Il ajuste dynamiquement le nombre total d'étapes en fonction du facteur de débruitage pour affiner le processus de diffusion, fournissant des "recettes" précises pour différentes étapes dans les processus d'échantillonnage avancés qui nécessitent un contrôle fin (comme l'échantillonnage par étapes).

## Entrées

| Paramètre      | Type de Données | Type d'Entrée | Par Défaut | Plage     | Description Métaphorique | Objectif Technique |
| -------------- | --------------- | ------------- | ---------- | --------- | ------------------------ | ------------------ |
| `modèle`       | MODEL           | Input         | -          | -         | **Type de Toile**: Différents matériaux de toile nécessitent différentes formules de peinture | Objet de modèle de diffusion, détermine la base du calcul sigma |
| `planificateur`| COMBO[STRING]   | Widget        | -          | 9 options | **Technique de Mélange**: Choisir comment la concentration de peinture change | Algorithme de planification, contrôle le mode de décroissance du bruit |
| `étapes`       | INT             | Widget        | 20         | 1-10000   | **Comptage de Mélanges**: Différence de précision entre 20 vs 50 mélanges | Étapes d'échantillonnage, affecte la qualité et la vitesse de génération |
| `débruitage`   | FLOAT           | Widget        | 1.0        | 0.0-1.0   | **Intensité de Création**: Niveau de contrôle du réglage fin à la repeinture | Force de débruitage, supporte les scénarios de repeinture partielle |

### Types de Planificateurs

Basé sur le code source `comfy.samplers.SCHEDULER_NAMES`, supporte les 9 planificateurs suivants:

| Nom du Planificateur | Caractéristiques           | Cas d'Usage                         | Modèle de Décroissance du Bruit         |
| -------------------- | -------------------------- | ----------------------------------- | --------------------------------------- |
| **normal**           | Linéaire standard          | Scénarios généraux, équilibré       | Décroissance uniforme                   |
| **karras**           | Transition douce           | Haute qualité, riche en détails     | Décroissance non-linéaire douce         |
| **exponential**      | Décroissance exponentielle | Génération rapide, efficacité       | Décroissance rapide exponentielle       |
| **sgm_uniform**      | SGM uniforme               | Optimisation de modèle spécifique   | Décroissance optimisée SGM              |
| **simple**           | Planification simple       | Tests rapides, usage de base        | Décroissance simplifiée                 |
| **ddim_uniform**     | DDIM uniforme              | Optimisation d'échantillonnage DDIM | Décroissance spécifique DDIM            |
| **beta**             | Distribution Beta          | Besoins de distribution spéciale    | Décroissance de fonction Beta           |
| **linear_quadratic** | Quadratique linéaire       | Optimisation de scénarios complexes | Décroissance de fonction quadratique    |
| **kl_optimal**       | KL optimal                 | Optimisation théorique              | Décroissance optimisée de divergence KL |

## Sorties

| Paramètre | Type de Données | Type de Sortie | Description Métaphorique | Signification Technique |
| --------- | --------------- | -------------- | ------------------------ | ----------------------- |
| `sigmas`  | SIGMAS          | Output         | **Tableau de Recettes de Peinture**: Liste détaillée de concentration de peinture pour usage étape par étape | Séquence de niveaux de bruit, guide le processus de débruitage du modèle de diffusion |

## Rôle du Nœud: Assistant de Mélange de Couleurs de l'Artiste

Imaginez que vous êtes un artiste créant une image claire à partir d'un mélange chaotique de peinture (bruit). `BasicScheduler` agit comme votre **assistant professionnel de mélange de couleurs**, dont le travail est de préparer une série de recettes précises de concentration de peinture:

### Flux de Travail

- **Étape 1**: Utiliser de la peinture à 90% de concentration (niveau de bruit élevé)
- **Étape 2**: Utiliser de la peinture à 80% de concentration  
- **Étape 3**: Utiliser de la peinture à 70% de concentration
- **...**
- **Étape Finale**: Utiliser 0% de concentration (toile propre, sans bruit)

### Compétences Spéciales de l'Assistant Couleurs

**Différentes méthodes de mélange (scheduler)**:

- **Méthode de mélange "karras"**: La concentration de peinture change très doucement, comme la technique de dégradé d'un artiste professionnel
- **Méthode de mélange "exponential"**: La concentration de peinture diminue rapidement, adaptée pour une création rapide
- **Méthode de mélange "linear"**: La concentration de peinture diminue uniformément, stable et contrôlable

**Contrôle fin (steps)**:

- **20 mélanges**: Peinture rapide, priorité à l'efficacité
- **50 mélanges**: Peinture fine, priorité à la qualité

**Intensité de création (denoise)**:

- **1.0 = Création complètement nouvelle**: Commencer complètement à partir d'une toile vierge
- **0.5 = Demi-transformation**: Garder la moitié de la peinture originale, transformer la moitié
- **0.2 = Ajustement fin**: Faire seulement des ajustements subtils à la peinture originale

### Collaboration avec d'Autres Nœuds

`BasicScheduler` (Assistant Couleurs) → Préparer Recette → `SamplerCustom` (Artiste) → Peinture Réelle → Travail Terminé
