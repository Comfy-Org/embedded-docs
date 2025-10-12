> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SD_4XUpscale_Conditioning/fr.md)

Le nœud SD_4XUpscale_Conditioning prépare les données de conditionnement pour le suréchantillonnage d'images à l'aide de modèles de diffusion. Il prend en entrée des images et des données de conditionnement, puis applique une mise à l'échelle et une augmentation de bruit pour créer un conditionnement modifié qui guide le processus de suréchantillonnage. Le nœud produit à la fois un conditionnement positif et négatif ainsi que des représentations latentes pour les dimensions suréchantillonnées.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `images` | IMAGE | Oui | - | Images d'entrée à suréchantillonner |
| `positive` | CONDITIONING | Oui | - | Données de conditionnement positif qui guident la génération vers le contenu souhaité |
| `negative` | CONDITIONING | Oui | - | Données de conditionnement négatif qui éloignent la génération du contenu indésirable |
| `scale_ratio` | FLOAT | Non | 0.0 - 10.0 | Facteur d'échelle appliqué aux images d'entrée (par défaut : 4.0) |
| `noise_augmentation` | FLOAT | Non | 0.0 - 1.0 | Quantité de bruit à ajouter pendant le processus de suréchantillonnage (par défaut : 0.0) |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | Conditionnement positif modifié avec les informations de suréchantillonnage appliquées |
| `negative` | CONDITIONING | Conditionnement négatif modifié avec les informations de suréchantillonnage appliquées |
| `latent` | LATENT | Représentation latente vide correspondant aux dimensions suréchantillonnées |