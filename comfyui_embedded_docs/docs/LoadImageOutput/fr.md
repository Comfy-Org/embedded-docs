> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImageOutput/fr.md)

Le nœud LoadImageOutput charge les images depuis le dossier de sortie. Lorsque vous cliquez sur le bouton d'actualisation, il met à jour la liste des images disponibles et sélectionne automatiquement la première, facilitant ainsi l'itération à travers vos images générées.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `image` | COMBO | Oui | Plusieurs options disponibles | Charge une image depuis le dossier de sortie. Inclut une option de téléchargement et un bouton d'actualisation pour mettre à jour la liste des images. |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `image` | IMAGE | L'image chargée depuis le dossier de sortie |
| `mask` | MASK | Le masque associé à l'image chargée |
