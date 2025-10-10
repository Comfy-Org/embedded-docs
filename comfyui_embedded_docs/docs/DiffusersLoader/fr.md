> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DiffusersLoader/fr.md)

Le nœud DiffusersLoader charge des modèles pré-entraînés au format diffusers. Il recherche les répertoires de modèles diffusers valides contenant un fichier model_index.json et les charge en tant que composants MODEL, CLIP et VAE pour une utilisation dans le pipeline. Ce nœud fait partie de la catégorie des chargeurs dépréciés et assure la compatibilité avec les modèles Hugging Face diffusers.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `model_path` | STRING | Oui | Plusieurs options disponibles<br>(remplissage automatique à partir des dossiers diffusers) | Le chemin vers le répertoire du modèle diffusers à charger. Le nœud scanne automatiquement les modèles diffusers valides dans les dossiers diffusers configurés et liste les options disponibles. |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `MODEL` | MODEL | Le composant de modèle chargé à partir du format diffusers |
| `CLIP` | CLIP | Le composant de modèle CLIP chargé à partir du format diffusers |
| `VAE` | VAE | Le composant VAE (Autoencodeur Variationnel) chargé à partir du format diffusers |