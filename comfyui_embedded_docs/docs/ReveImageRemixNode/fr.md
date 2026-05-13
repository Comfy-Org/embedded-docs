> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReveImageRemixNode/fr.md)

Le nœud Reve Image Remix utilise l'API Reve pour générer une nouvelle image. Il combine une ou plusieurs images de référence avec un prompt textuel afin de créer une nouvelle image remixée basée sur la description fournie.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `reference_images` | IMAGE | Oui | 1 à 6 images | Une ou plusieurs images de référence à utiliser comme base pour le remix. Vous pouvez ajouter entre 1 et 6 images. |
| `prompt` | STRING | Oui | 1 à 2560 caractères | Une description textuelle de l'image souhaitée. Vous pouvez inclure des balises XML `<img>` pour référencer des images spécifiques par leur index (par exemple, `<img>0</img>`, `<img>1</img>`). (par défaut : vide) |
| `model` | COMBO | Oui | `reve-remix@20250915`<br>`reve-remix-fast@20251030` | La version du modèle à utiliser pour le remix. Chaque option de modèle inclut des ratios d'aspect configurables et une mise à l'échelle au moment du test. |
| `upscale` | COMBO | Non | `"disabled"`<br>`"enabled"` | Contrôle si l'image générée doit être agrandie. Lorsque cette option est activée, vous pouvez sélectionner un facteur d'agrandissement. |
| `remove_background` | BOOLEAN | Non | `true`<br>`false` | Lorsque cette option est activée, tente de supprimer l'arrière-plan de l'image générée. |
| `seed` | INT | Non | 0 à 2147483647 | Une valeur de graine. Modifier cette valeur entraînera la réexécution du nœud, mais les résultats restent non déterministes quelle que soit la graine. (par défaut : 0) |

**Remarque :** Le paramètre `model` est une liste déroulante dynamique qui inclut des paramètres imbriqués pour `aspect_ratio` (options : "auto", "16:9", "9:16", "3:2", "2:3", "4:3", "3:4", "1:1") et `test_time_scaling`. Le paramètre `upscale`, lorsqu'il est défini sur "enabled", révèle un paramètre imbriqué `upscale_factor`.

## Sorties

| Nom de la sortie | Type de données | Description |
|------------------|-----------------|-------------|
| `image` | IMAGE | La nouvelle image générée par le processus de remix Reve. |

---
**Source fingerprint (SHA-256):** `e64dccddfd55ebaa7e28bf17c2a5ff1a0c130db1475e307940b75106c788f687`
