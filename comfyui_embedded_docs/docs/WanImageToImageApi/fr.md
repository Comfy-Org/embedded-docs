> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanImageToImageApi/fr.md)

Voici la traduction en français de la documentation du nœud WanImageToImageApi :

Le nœud Wan Image to Image génère une image à partir d'une ou deux images d'entrée et d'une invite textuelle. Il transforme vos images d'entrée en fonction de la description fournie, créant une nouvelle image qui conserve le rapport hauteur/largeur de votre image d'origine. L'image de sortie est fixée à 1,6 mégapixels, quelle que soit la taille d'entrée.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `modèle` | COMBO | Oui | "wan2.5-i2i-preview" | Modèle à utiliser (par défaut : "wan2.5-i2i-preview"). |
| `image` | IMAGE | Oui | - | Édition d'une seule image ou fusion de plusieurs images, maximum 2 images. |
| `invite` | STRING | Oui | - | Invite décrivant les éléments et les caractéristiques visuelles. Prend en charge l'anglais et le chinois (par défaut : vide). |
| `invite_négative` | STRING | Non | - | Invite négative décrivant ce qu'il faut éviter (par défaut : vide). |
| `graine` | INT | Non | 0 à 2147483647 | Graine à utiliser pour la génération (par défaut : 0). |
| `filigrane` | BOOLEAN | Non | - | Indique s'il faut ajouter un filigrane généré par IA au résultat (par défaut : false). |

**Remarque :** Ce nœud accepte exactement 1 ou 2 images d'entrée. Si vous fournissez plus de 2 images ou aucune image, le nœud renverra une erreur.

## Sorties

| Nom de la sortie | Type de données | Description |
|------------------|-----------------|-------------|
| `image` | IMAGE | L'image générée à partir des images d'entrée et des invites textuelles. |

---
**Source fingerprint (SHA-256):** `d69811ddaba718e5468f539fb9b25827efdf79f3ee9cbf31ad8f9387cea9b9be`
