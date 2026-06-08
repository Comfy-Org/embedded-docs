Voici la traduction en français de la documentation du nœud ComfyUI, en respectant vos règles :

Étend une image en fonction d'une description textuelle. Ce nœud agrandit une image en ajoutant des pixels sur les côtés supérieur, inférieur, gauche et droit, tout en générant un nouveau contenu correspondant à la description textuelle fournie.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `image` | L'image d'entrée à étendre | IMAGE | Oui | - |
| `prompt` | Description textuelle pour la génération d'image (par défaut : "") | STRING | Non | - |
| `suréchantillonnage du prompt` | Indique s'il faut effectuer un sur-échantillonnage de la description textuelle. Si activé, modifie automatiquement la description pour une génération plus créative, mais les résultats sont non déterministes (une même graine ne produira pas exactement le même résultat). (par défaut : False) | BOOLEAN | Non | - |
| `haut` | Nombre de pixels à ajouter en haut de l'image (par défaut : 0) | INT | Non | 0-2048 |
| `bas` | Nombre de pixels à ajouter en bas de l'image (par défaut : 0) | INT | Non | 0-2048 |
| `gauche` | Nombre de pixels à ajouter à gauche de l'image (par défaut : 0) | INT | Non | 0-2048 |
| `droite` | Nombre de pixels à ajouter à droite de l'image (par défaut : 0) | INT | Non | 0-2048 |
| `guidage` | Force d'orientation pour le processus de génération d'image (par défaut : 60) | FLOAT | Non | 1.5-100 |
| `étapes` | Nombre d'étapes pour le processus de génération d'image (par défaut : 50) | INT | Non | 15-50 |
| `graine` | La graine aléatoire utilisée pour créer le bruit. (par défaut : 0) | INT | Non | 0-18446744073709551615 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `image` | L'image étendue en sortie | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxProExpandNode/fr.md)

---
**Source fingerprint (SHA-256):** `15b21f1de8a98a6bcde131a61c01b062434c6a959bc563550d613972412973fe`
