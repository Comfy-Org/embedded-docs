# PikaScenesV2_2

Le nœud PikaScenes v2.2 combine plusieurs images pour créer une vidéo intégrant les objets de toutes les images d'entrée. Vous pouvez télécharger jusqu'à cinq images différentes comme ingrédients et générer une vidéo de haute qualité qui les fusionne de manière transparente.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `prompt_text` | Description textuelle de ce qu'il faut générer | STRING | Oui | - |
| `negative_prompt` | Description textuelle de ce qu'il faut éviter dans la génération | STRING | Oui | - |
| `seed` | Valeur de graine aléatoire pour la génération | INT | Oui | - |
| `resolution` | Résolution de sortie pour la vidéo | STRING | Oui | - |
| `duration` | Durée de la vidéo générée | INT | Oui | - |
| `ingredients_mode` | Mode de combinaison des ingrédients (par défaut : "creative") | STRING | Non | "creative"<br>"precise" |
| `aspect_ratio` | Rapport hauteur/largeur (largeur / hauteur) (par défaut : 1,778) | FLOAT | Non | 0,4 - 2,5 |
| `image_ingredient_1` | Image qui sera utilisée comme ingrédient pour créer une vidéo | IMAGE | Non | - |
| `image_ingredient_2` | Image qui sera utilisée comme ingrédient pour créer une vidéo | IMAGE | Non | - |
| `image_ingredient_3` | Image qui sera utilisée comme ingrédient pour créer une vidéo | IMAGE | Non | - |
| `image_ingredient_4` | Image qui sera utilisée comme ingrédient pour créer une vidéo | IMAGE | Non | - |
| `image_ingredient_5` | Image qui sera utilisée comme ingrédient pour créer une vidéo | IMAGE | Non | - |

**Remarque :** Vous pouvez fournir jusqu'à 5 ingrédients d'image, mais au moins une image est requise pour générer une vidéo. Le nœud utilisera toutes les images fournies pour créer la composition vidéo finale.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `output` | La vidéo générée combinant toutes les images d'entrée | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PikaScenesV2_2/fr.md)

---
**Source fingerprint (SHA-256):** `dda8f10a58527c2b9037744f59f30821cdde37ad23427b856ba5e699a05acafd`
