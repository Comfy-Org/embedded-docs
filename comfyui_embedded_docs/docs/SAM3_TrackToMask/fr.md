# SAM3 Suivi vers Masque

Voici la traduction en français de la documentation du nœud ComfyUI `SAM3_TrackToMask` :

## Aperçu

Sélectionne des objets suivis spécifiques à partir d'une session de suivi SAM3 en fonction de leurs numéros d'index et les combine en un seul masque de sortie. Cela vous permet de choisir les objets à conserver et ceux à ignorer parmi les résultats du suivi.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `données_suivi` | Les données de suivi provenant d'un nœud de suivi SAM3, contenant les masques compressés et la taille d'image d'origine. | SAM3TRACKDATA | Oui | N/D |
| `indices_objets` | Index des objets à inclure dans le masque de sortie, séparés par des virgules (par exemple, '0,2,3'). Si laissé vide, tous les objets suivis sont inclus. | STRING | Non | Toute liste d'entiers séparés par des virgules |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `masks` | Un masque binaire unique pour chaque image, où les objets sélectionnés sont combinés en un seul masque. Si aucun objet n'est sélectionné ou si aucune donnée de suivi n'existe, renvoie un masque nul. | MASK |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SAM3_TrackToMask/fr.md)

---
**Source fingerprint (SHA-256):** `2da82effc4cdc6655d0d37e281858bf33f7b62d9056629ec810e3ff9b2e7b5a6`
