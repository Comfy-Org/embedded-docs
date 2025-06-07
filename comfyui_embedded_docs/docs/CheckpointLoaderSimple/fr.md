Ceci est un nœud chargeur de modèles qui charge des fichiers de modèles à partir d'emplacements spécifiés et les décompose en trois composants principaux : le modèle principal, l'encodeur de texte et l'encodeur/décodeur d'images.

Ce nœud détecte automatiquement tous les fichiers de modèles dans le dossier `ComfyUI/models/checkpoints`, ainsi que les chemins supplémentaires configurés dans votre fichier `extra_model_paths.yaml`.

1. **Compatibilité du modèle** : Assurez-vous que le modèle sélectionné est compatible avec votre flux de travail. Différents types de modèles (comme SD1.5, SDXL, Flux, etc.) doivent être associés aux échantillonneurs correspondants et autres nœuds
2. **Gestion des fichiers** : Placez les fichiers de modèles dans le dossier `ComfyUI/models/checkpoints`, ou configurez d'autres chemins via extra_model_paths.yaml
3. **Actualisation de l'interface** : Si de nouveaux fichiers de modèles sont ajoutés pendant que ComfyUI fonctionne, vous devez actualiser le navigateur (Ctrl+R) pour voir les nouveaux fichiers dans la liste déroulante

## Entrées

| Nom du Paramètre | Type de Données | Méthode d'Entrée | Valeur Par Défaut | Plage de Valeurs | Description |
|-------------------|-----------------|------------------|-------------------|------------------|-------------|
| nom_ckpt | STRING | Sélection Déroulante | null | Tous les fichiers de modèles dans le dossier checkpoints | Sélectionne le nom du fichier de checkpoint du modèle à charger, qui détermine le modèle IA utilisé pour la génération d'images ultérieure |

## Paramètres de Sortie

| Nom de Sortie | Type de Données | Description |
|---------------|-----------------|-------------|
| MODÈLE | MODEL | Le modèle de diffusion principal utilisé pour la génération d'images par débruitage, le composant central de la création d'images IA |
| CLIP | CLIP | Le modèle utilisé pour encoder les prompts textuels, convertissant les descriptions textuelles en informations que l'IA peut comprendre |
| VAE | VAE | Le modèle utilisé pour l'encodage et le décodage d'images, responsable de la conversion entre l'espace pixel et l'espace latent |
