> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxProExpandNode/fr.md)

Agrandit l'image en fonction de l'invite. Ce nœud étend une image en ajoutant des pixels sur les côtés supérieur, inférieur, gauche et droit tout en générant un nouveau contenu qui correspond à la description textuelle fournie.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Oui | - | L'image d'entrée à agrandir |
| `prompt` | STRING | Non | - | Invite pour la génération d'image (par défaut : "") |
| `prompt_upsampling` | BOOLEAN | Non | - | Indique s'il faut effectuer un suréchantillonnage sur l'invite. Si actif, modifie automatiquement l'invite pour une génération plus créative, mais les résultats sont non déterministes (la même graine ne produira pas exactement le même résultat). (par défaut : False) |
| `top` | INT | Non | 0-2048 | Nombre de pixels à ajouter en haut de l'image (par défaut : 0) |
| `bottom` | INT | Non | 0-2048 | Nombre de pixels à ajouter en bas de l'image (par défaut : 0) |
| `left` | INT | Non | 0-2048 | Nombre de pixels à ajouter à gauche de l'image (par défaut : 0) |
| `right` | INT | Non | 0-2048 | Nombre de pixels à ajouter à droite de l'image (par défaut : 0) |
| `guidance` | FLOAT | Non | 1.5-100 | Intensité de guidage pour le processus de génération d'image (par défaut : 60) |
| `steps` | INT | Non | 15-50 | Nombre d'étapes pour le processus de génération d'image (par défaut : 50) |
| `seed` | INT | Non | 0-18446744073709551615 | La graine aléatoire utilisée pour créer le bruit. (par défaut : 0) |

## Sorties

| Sortie | Type de données | Description |
|-------------|-----------|-------------|
| `image` | IMAGE | L'image de sortie agrandie |