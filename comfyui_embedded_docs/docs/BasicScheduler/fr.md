> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BasicScheduler/fr.md)

Le nœud `BasicScheduler` est conçu pour calculer une séquence de valeurs sigma pour les modèles de diffusion en fonction du planificateur, du modèle et des paramètres de débruitage fournis. Il ajuste dynamiquement le nombre total d'étapes en fonction du facteur de débruitage pour affiner le processus de diffusion, fournissant des « recettes » précises pour différentes étapes dans les processus d'échantillonnage avancés nécessitant un contrôle fin (comme l'échantillonnage multi-étapes).

## Entrées

| Paramètre   | Type de données | Type d'entrée | Valeur par défaut | Plage     | Description Métaphorique           | Objectif Technique            |
| ----------- | --------------- | ------------- | ----------------- | --------- | ---------------------------------- | ----------------------------- |
| `modèle`     | MODEL           | Entrée        | -                 | -         | **Type de toile** : Différents matériaux de toile nécessitent différentes formules de peinture | Objet modèle de diffusion, détermine la base de calcul des sigma |
| `planificateur` | COMBO[STRING]   | Widget        | -                 | 9 options | **Technique de mélange** : Choisir comment la concentration de peinture change | Algorithme de planification, contrôle le mode de décroissance du bruit |
| `étapes`     | INT             | Widget        | 20                | 1-10000   | **Nombre de mélanges** : Précision entre 20 mélanges et 50 mélanges | Étapes d'échantillonnage, affecte la qualité et la vitesse de génération |
| `débruitage`   | FLOAT           | Widget        | 1.0               | 0.0-1.0   | **Intensité de création** : Contrôle le niveau, du réglage fin à la repeinture | Force de débruitage, prend en charge les scénarios de repeinture partielle |

### Types de planificateurs

Basé sur le code source `comfy.samplers.SCHEDULER_NAMES`, prend en charge les 9 planificateurs suivants :

| Nom du planificateur | Caractéristiques      | Cas d'utilisation                    | Motif de décroissance du bruit          |
| -------------------- | --------------------- | ------------------------------------ | --------------------------------------- |
| **normal**           | Linéaire standard     | Scénarios généraux, équilibré        | Décroissance uniforme                   |
| **karras**           | Transition douce      | Haute qualité, riche en détails      | Décroissance non linéaire douce         |
| **exponential**      | Décroissance exponentielle | Génération rapide, efficacité    | Décroissance exponentielle rapide       |
| **sgm_uniform**      | Uniforme SGM          | Optimisation de modèle spécifique    | Décroissance optimisée SGM              |
| **simple**           | Planification simple  | Tests rapides, utilisation de base   | Décroissance simplifiée                 |
| **ddim_uniform**     | Uniforme DDIM         | Optimisation d'échantillonnage DDIM  | Décroissance spécifique DDIM            |
| **beta**             | Distribution bêta     | Besoins de distribution spéciaux     | Décroissance par fonction bêta          |
| **linear_quadratic** | Linéaire quadratique  | Optimisation de scénarios complexes  | Décroissance par fonction quadratique   |
| **kl_optimal**       | Optimal KL            | Optimisation théorique               | Décroissance optimisée par divergence KL|

## Sorties

| Paramètre | Type de données | Type de sortie | Description Métaphorique   | Signification Technique                |
| --------- | --------------- | -------------- | -------------------------- | --------------------------------------- |
| `sigmas`  | SIGMAS          | Sortie         | **Tableau de recettes de peinture** : Liste détaillée des concentrations de peinture pour une utilisation étape par étape | Séquence de niveaux de bruit, guide le processus de débruitage du modèle de diffusion |

## Rôle du nœud : Assistant de mélange de couleurs de l'artiste

Imaginez que vous êtes un artiste créant une image claire à partir d'un mélange chaotique de peinture (bruit). `BasicScheduler` agit comme votre **assistant professionnel de mélange de couleurs**, dont le travail consiste à préparer une série de recettes précises de concentration de peinture :

### Flux de travail

- **Étape 1** : Utiliser une peinture à 90 % de concentration (niveau de bruit élevé)
- **Étape 2** : Utiliser une peinture à 80 % de concentration
- **Étape 3** : Utiliser une peinture à 70 % de concentration
- **...**
- **Étape finale** : Utiliser une peinture à 0 % de concentration (toile propre, sans bruit)

### Compétences spéciales de l'assistant couleur

**Différentes méthodes de mélange (planificateur)** :

- **Méthode de mélange "karras"** : La concentration de peinture change très doucement, comme la technique de dégradé d'un artiste professionnel
- **Méthode de mélange "exponential"** : La concentration de peinture diminue rapidement, adaptée à la création rapide
- **Méthode de mélange "linear"** : La concentration de peinture diminue uniformément, stable et contrôlable

**Contrôle fin (étapes)** :

- **20 mélanges** : Peinture rapide, priorité à l'efficacité
- **50 mélanges** : Peinture fine, priorité à la qualité

**Intensité de création (débruitage)** :

- **1.0 = Nouvelle création complète** : Commencer entièrement à partir d'une toile vierge
- **0.5 = Demi-transformation** : Garder la moitié de la peinture originale, transformer l'autre moitié
- **0.2 = Ajustement fin** : Effectuer uniquement des ajustements subtils sur la peinture originale

### Collaboration avec d'autres nœuds

`BasicScheduler` (Assistant couleur) → Préparer la recette → `SamplerCustom` (Artiste) → Peinture réelle → Œuvre terminée