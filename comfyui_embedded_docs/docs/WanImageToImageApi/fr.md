> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanImageToImageApi/fr.md)

Le nœud Wan Image to Image génère une image à partir d'une ou deux images d'entrée et d'une invite textuelle. Il transforme vos images d'entrée en fonction de la description que vous fournissez, créant une nouvelle image qui conserve le rapport d'aspect de votre entrée originale. L'image de sortie est fixée à 1,6 mégapixels, quelle que soit la taille d'entrée.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | Oui | "wan2.5-i2i-preview" | Modèle à utiliser (par défaut : "wan2.5-i2i-preview"). |
| `image` | IMAGE | Oui | - | Édition d'image unique ou fusion de plusieurs images, maximum 2 images. |
| `prompt` | STRING | Oui | - | Invite utilisée pour décrire les éléments et les caractéristiques visuelles, prend en charge l'anglais/le chinois (par défaut : vide). |
| `negative_prompt` | STRING | Non | - | Invite textuelle négative pour guider ce qu'il faut éviter (par défaut : vide). |
| `seed` | INT | Non | 0 à 2147483647 | Graine à utiliser pour la génération (par défaut : 0). |
| `watermark` | BOOLEAN | Non | - | Indique s'il faut ajouter un filigrane "Généré par IA" au résultat (par défaut : true). |

**Remarque :** Ce nœud accepte exactement 1 ou 2 images d'entrée. Si vous fournissez plus de 2 images ou aucune image, le nœud renverra une erreur.

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `image` | IMAGE | L'image générée basée sur les images d'entrée et les invites textuelles. |