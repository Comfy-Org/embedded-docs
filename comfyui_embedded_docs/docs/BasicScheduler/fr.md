# PlanificateurBasique

Le nœud `BasicScheduler` est conçu pour calculer une séquence de valeurs sigma pour les modèles de diffusion en fonction du planificateur, du modèle et des paramètres de débruitage fournis. Il ajuste dynamiquement le nombre total d’étapes en fonction du facteur denoise afin d’affiner le processus de diffusion, fournissant des « recettes » précises pour différentes étapes des processus d’échantillonnage avancés nécessitant un contrôle fin (comme l’échantillonnage multi-étapes).

## Entrées

| Paramètre | Description métaphorique | Type de données | Type d’entrée | Défaut | Plage | Objectif technique |
| --- | --- | --- | --- | --- | --- | --- |
| `model` | **Type de toile** : Différents matériaux de toile nécessitent différentes formules de peinture | MODEL | Entrée | - | - | Objet de modèle de diffusion, détermine la base de calcul des sigmas |
| `scheduler` | **Technique de mélange** : Choisissez la manière dont la concentration de peinture évolue | COMBO[STRING] | Widget | - | 9 options | Algorithme de planification, contrôle le mode de décroissance du bruit |
| `steps` | **Nombre de mélanges** : 20 mélanges vs 50 mélanges, différence de précision | INT | Widget | 20 | 1-10000 | Étapes d’échantillonnage, affecte la qualité et la vitesse de génération |
| `denoise` | **Intensité de création** : Niveau de contrôle, du réglage fin à la repeinture complète | FLOAT | Widget | 1.0 | 0.0-1.0 | Force de débruitage, prend en charge les scénarios de repeinture partielle |

### Types de planificateurs

D’après le code source `comfy.samplers.SCHEDULER_NAMES`, prend en charge les 9 planificateurs suivants :

| Nom du planificateur | Caractéristiques | Cas d’utilisation | Schéma de décroissance du bruit |
| -------------------- | -------------------- | ---------------------------- | ---------------------------- |
| **normal**           | Linéaire standard    | Scénarios généraux, équilibrés | Décroissance uniforme         |
| **karras**           | Transition fluide    | Haute qualité, riche en détails | Décroissance non linéaire douce |
| **exponential**      | Décroissance exponentielle | Génération rapide, efficacité | Décroissance exponentielle rapide |
| **sgm_uniform**      | Uniforme SGM         | Optimisation pour modèle spécifique | Décroissance optimisée SGM    |
| **simple**           | Planification simple | Test rapide, utilisation de base | Décroissance simplifiée       |
| **ddim_uniform**     | Uniforme DDIM        | Optimisation de l’échantillonnage DDIM | Décroissance spécifique DDIM  |
| **beta**             | Distribution bêta    | Besoins de distribution particuliers | Décroissance par fonction bêta |
| **linear_quadratic** | Linéaire quadratique | Optimisation de scénarios complexes | Décroissance par fonction quadratique |
| **kl_optimal**       | KL optimal           | Optimisation théorique       | Décroissance optimisée par divergence KL |

## Sorties

| Paramètre | Description métaphorique | Type de données | Type de sortie | Signification technique |
| --- | --- | --- | --- | --- |
| `sigmas` | **Graphique de recette de peinture** : Liste détaillée des concentrations de peinture à utiliser étape par étape | SIGMAS | Sortie | Séquence de niveaux de bruit, guide le processus de débruitage du modèle de diffusion |

## Rôle du nœud : Assistant de mélange des couleurs de l’artiste

Imaginez que vous êtes un artiste créant une image claire à partir d’un mélange chaotique de peinture (bruit). `BasicScheduler` agit comme votre **assistant professionnel de mélange des couleurs**, dont le rôle est de préparer une série de recettes précises de concentration de peinture :

### Flux de travail

- **Étape 1** : Utiliser une peinture à 90 % de concentration (niveau de bruit élevé)
- **Étape 2** : Utiliser une peinture à 80 % de concentration  
- **Étape 3** : Utiliser une peinture à 70 % de concentration
- **...**
- **Étape finale** : Utiliser une concentration de 0 % (toile propre, sans bruit)

### Compétences particulières de l’assistant de mélange des couleurs

**Différentes méthodes de mélange (planificateur)** :

- **Méthode de mélange « karras »** : La concentration de peinture évolue très doucement, comme la technique de dégradé d’un artiste professionnel
- **Méthode de mélange « exponential »** : La concentration de peinture diminue rapidement, adaptée à la création rapide
- **Méthode de mélange « linear »** : La concentration de peinture diminue uniformément, stable et contrôlable

**Contrôle fin (steps)** :

- **20 mélanges** : Peinture rapide, priorité à l’efficacité
- **50 mélanges** : Peinture fine, priorité à la qualité

**Intensité de création (denoise)** :

- **1.0 = Création entièrement nouvelle** : Partir complètement d’une toile blanche
- **0.5 = Transformation à moitié** : Conserver la moitié de la peinture originale, transformer l’autre moitié
- **0.2 = Réglage fin** : Effectuer uniquement de légers ajustements sur la peinture originale

### Collaboration avec d’autres nœuds

`BasicScheduler` (assistant de mélange des couleurs) → Préparer la recette → `SamplerCustom` (artiste) → Peinture réelle → Œuvre terminée

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BasicScheduler/fr.md)
