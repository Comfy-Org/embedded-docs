# MOSS-Image Layout Prompt

Construit le prompt de mise en page que lit MOSS-Image. Il prend les éléments dessinés dans le nœud Create Bounding Boxes et émet une mise en page JSON avec une entrée par boîte : son libellé, sa légende et son rectangle dans l'espace pixel du canevas cible. Définissez `width` et `height` sur la taille de l'image que vous prévoyez de générer, puis connectez la sortie à l'entrée prompt de l'encodeur de texte. Lorsqu'aucun élément n'est connecté, le texte du prompt est renvoyé inchangé.

## Entrées

| Paramètre | Description | Type de données | Obligatoire | Plage |
| --- | --- | --- | --- | --- |
| `prompt` | Description de l'image entière. Elle devient la légende de la mise en page. | STRING | Oui | - |
| `element` | Les éléments à placer, provenant du nœud Create Bounding Boxes. Chaque boîte fournit sa légende ; les boîtes de texte fournissent également leur texte, et les boîtes qui portent une palette de couleurs la conservent. | ARRAY | Oui | - |
| `width` | Largeur de l'image générée en pixels. Les boîtes sont converties dans cette grille de pixels, utilisez donc la taille de l'image que vous prévoyez de générer (par défaut : 1024). | INT | Oui | 16 à 16384 (pas 16) |
| `height` | Hauteur de l'image générée en pixels. Les boîtes sont converties dans cette grille de pixels, utilisez donc la taille de l'image que vous prévoyez de générer (par défaut : 1024). | INT | Oui | 16 à 16384 (pas 16) |
| `character_boxes` | Numéros des boîtes à étiqueter comme personnages plutôt que comme objets, tels qu'indiqués dans l'aperçu de Create Bounding Boxes, par exemple « 1, 3 ». Chaque nombre de la chaîne est lu, donc n'importe quel séparateur fonctionne (par défaut : vide). | STRING | Oui | - |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `prompt` | Le prompt de mise en page : un objet JSON contenant la légende, une entrée par boîte et le format des coordonnées des boîtes. Le texte d'entrée est transmis tel quel lorsqu'aucun élément n'est connecté. | STRING |

## Remarques

Les rectangles des boîtes proviennent de Create Bounding Boxes sous forme de coordonnées normalisées entre 0 et 1000 et sont écrits dans la mise en page en pixels par rapport au centre du canevas, dans l'ordre `yxyx`. Les valeurs `width` et `height` doivent donc correspondre à l'image que vous générez, sinon les boîtes se placent au mauvais endroit.

Une boîte qui contient du texte est toujours étiquetée comme texte, une boîte dont le numéro est listé dans `character_boxes` est étiquetée comme personnage, et toute autre boîte est étiquetée comme objet.

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MOSSImageLayoutPrompt/fr.md)

---
**Source fingerprint (SHA-256):** `da012a8d0dceaf6391110c90bd677d7929920d60fe961c00e5011b037206aa9a`
