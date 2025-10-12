> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PikaScenesV2_2/fr.md)

Le nœud PikaScenes v2.2 combine plusieurs images pour créer une vidéo qui intègre des objets provenant de toutes les images d'entrée. Vous pouvez télécharger jusqu'à cinq images différentes en tant qu'ingrédients et générer une vidéo de haute qualité qui les fusionne de manière homogène.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `prompt_text` | STRING | Oui | - | Description textuelle de ce qu'il faut générer |
| `negative_prompt` | STRING | Oui | - | Description textuelle de ce qu'il faut éviter dans la génération |
| `seed` | INT | Oui | - | Valeur de graine aléatoire pour la génération |
| `resolution` | STRING | Oui | - | Résolution de sortie pour la vidéo |
| `duration` | INT | Oui | - | Durée de la vidéo générée |
| `ingredients_mode` | COMBO | Non | "creative"<br>"precise" | Mode de combinaison des ingrédients (par défaut : "creative") |
| `aspect_ratio` | FLOAT | Non | 0.4 - 2.5 | Ratio d'aspect (largeur / hauteur) (par défaut : 1.778) |
| `image_ingredient_1` | IMAGE | Non | - | Image qui sera utilisée comme ingrédient pour créer une vidéo |
| `image_ingredient_2` | IMAGE | Non | - | Image qui sera utilisée comme ingrédient pour créer une vidéo |
| `image_ingredient_3` | IMAGE | Non | - | Image qui sera utilisée comme ingrédient pour créer une vidéo |
| `image_ingredient_4` | IMAGE | Non | - | Image qui sera utilisée comme ingrédient pour créer une vidéo |
| `image_ingredient_5` | IMAGE | Non | - | Image qui sera utilisée comme ingrédient pour créer une vidéo |

**Note :** Vous pouvez fournir jusqu'à 5 images en tant qu'ingrédients, mais au moins une image est requise pour générer une vidéo. Le nœud utilisera toutes les images fournies pour créer la composition vidéo finale.

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `output` | VIDEO | La vidéo générée combinant toutes les images d'entrée |