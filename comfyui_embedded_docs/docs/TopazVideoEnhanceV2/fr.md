# Topaz Video Enhance

Le nœud **Topaz Video Enhance V2** donne une nouvelle vie aux vidéos grâce à une puissante technologie d’upscaling et de récupération. Il peut augmenter la résolution d’une vidéo à l’aide de différents modèles d’upscaler Topaz, ajuster la fréquence d’images par interpolation d’images et appliquer des paramètres d’amélioration créatifs ou réalistes.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `vidéo` | Vidéo d’entrée à traiter. Doit être au format conteneur MP4. | VIDEO | Oui | - |
| `modèle d’agrandissement` | Le modèle d’IA utilisé pour upscaler la vidéo. Les sous-paramètres disponibles dépendent du modèle sélectionné. La sélection de `"Disabled"` désactive l’upscaling. | DYNAMIC_COMBO | Oui | `"Astra 2"`<br>`"Starlight (Astra) Fast"`<br>`"Starlight (Astra) Creative"`<br>`"Starlight Precise 2.5"`<br>`"Disabled"` |
| `modèle d’interpolation` | Le modèle d’IA utilisé pour l’interpolation d’images. Les sous-paramètres disponibles dépendent du modèle sélectionné. La sélection de `"Disabled"` désactive l’interpolation. | DYNAMIC_COMBO | Oui | `"Disabled"`<br>`"apo-8"` |
| `niveau de compression dynamique` | Niveau CQP utilisé pour la compression vidéo (par défaut : `"Low"`). | COMBO | Non | `"Low"`<br>`"Mid"`<br>`"High"` |

Les sections suivantes décrivent les sous-paramètres qui apparaissent pour chaque option des sélecteurs `upscaler_model` et `interpolation_model`. Les options `"Disabled"` n’affichent aucun paramètre supplémentaire.

### Entrées Astra 2

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `upscaler_model.upscaler_resolution` | Résolution de sortie cible pour l’upscale. | COMBO | Oui (lorsque « Astra 2 » est sélectionné) | `"FullHD (1080p)"`<br>`"4K (2160p)"` |
| `upscaler_model.creativity` | Intensité créative de l’upscale (par défaut : 0.5). | FLOAT | Non | 0.0 à 1.0 (step 0.1) |
| `upscaler_model.prompt` | Invite de scène descriptive facultative (non instructive). Limite l’entrée à 450 images (~15 s à 30 images/s) lorsqu’elle est définie (par défaut : vide). | STRING | Non | - |
| `upscaler_model.sharp` | Netteté de pré-amélioration : 0.0 = flou gaussien, 0.5 = passthrough (par défaut), 1.0 = accentuation USM. | FLOAT | Non | 0.0 à 1.0 (step 0.01) |
| `upscaler_model.realism` | Tire la sortie vers un réalisme photographique. Laissez à 0 pour le réglage par défaut du modèle (par défaut : 0.0). | FLOAT | Non | 0.0 à 1.0 (step 0.01) |

### Entrées Starlight (Astra) Fast

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `upscaler_model.upscaler_resolution` | Résolution de sortie cible pour l’upscale. | COMBO | Oui (lorsque ce modèle est sélectionné) | `"FullHD (1080p)"`<br>`"4K (2160p)"` |

### Entrées Starlight (Astra) Creative

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `upscaler_model.upscaler_resolution` | Résolution de sortie cible pour l’upscale. | COMBO | Oui (lorsque ce modèle est sélectionné) | `"FullHD (1080p)"`<br>`"4K (2160p)"` |
| `upscaler_model.creativity` | Intensité créative de l’upscale (par défaut : `"low"`). | COMBO | Non | `"low"`<br>`"middle"`<br>`"high"` |

### Entrées Starlight Precise 2.5

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `upscaler_model.upscaler_resolution` | Résolution de sortie cible pour l’upscale. | COMBO | Oui (lorsque ce modèle est sélectionné) | `"FullHD (1080p)"`<br>`"4K (2160p)"` |

### Entrées apo-8

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `interpolation_model.interpolation_frame_rate` | Fréquence d’images de sortie (par défaut : 60). | INT | Oui (lorsque « apo-8 » est sélectionné) | 15 à 240 |
| `interpolation_model.interpolation_slowmo` | Facteur de ralenti appliqué à la vidéo d’entrée. Par exemple, 2 rend la sortie deux fois plus lente et double la durée (par défaut : 1). | INT | Non | 1 à 16 |
| `interpolation_model.interpolation_duplicate` | Analyse l’entrée à la recherche de trames en double et les supprime (par défaut : False). | BOOLEAN | Non | True<br>False |
| `interpolation_model.interpolation_duplicate_threshold` | Sensibilité de détection des trames en double (par défaut : 0.01). | FLOAT | Non | 0.001 à 0.1 (step 0.001) |

**Contraintes importantes :**

- Au moins l’un des paramètres `upscaler_model` ou `interpolation_model` doit être activé. Si les deux sont définis sur `"Disabled"`, le nœud génère une erreur car il n’y a rien à traiter.
- La vidéo d’entrée `video` doit être au format conteneur MP4.
- Le modèle `"Astra 2"` est limité à 9000 images d’entrée. Lorsqu’un `prompt` est défini, la limite est de 450 images d’entrée (~15 secondes à 30 images/s). Le nœud génère une erreur si la vidéo dépasse la limite applicable.
- `upscaler_model.upscaler_resolution` est requis dès qu’un modèle d’upscaler autre que `"Disabled"` est sélectionné. `"FullHD (1080p)"` vise un résultat 1080p et `"4K (2160p)"` vise un résultat 2160p ; la largeur et la hauteur exactes de sortie sont calculées à partir du ratio d’aspect de l’entrée, plafonnées à un côté long maximal de 1920 ou 3840 pixels respectivement, et arrondies à un nombre pair.
- `interpolation_model.interpolation_frame_rate` est requis dès que `interpolation_model` est défini sur `"apo-8"`.
- Les fichiers très volumineux ne sont actuellement pas pris en charge ; les téléversements sont limités à une seule partie, sinon le nœud génère une erreur.
- Plusieurs paramètres (`sharp`, `realism`, `interpolation_slowmo`, `interpolation_duplicate`, `interpolation_duplicate_threshold`) sont marqués comme avancés dans l’interface et peuvent être masqués par défaut.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `video` | La vidéo améliorée après application des filtres d’upscaling et/ou d’interpolation sélectionnés. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TopazVideoEnhanceV2/fr.md)

---
**Source fingerprint (SHA-256):** `14627dc772a6a46a645517bd34b545e0986a84561e24bdfe810b67f791ee47e3`
