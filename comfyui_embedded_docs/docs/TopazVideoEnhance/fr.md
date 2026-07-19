# Topaz Video Enhance

Voici la traduction en français de la documentation du nœud Topaz Video Enhance, conforme à vos règles de spécialisation technique :

---

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TopazVideoEnhance/en.md)

Le nœud Topaz Video Enhance utilise une API externe pour améliorer la qualité vidéo. Il peut augmenter la résolution de la vidéo, augmenter la fréquence d'images par interpolation et appliquer une compression. Le nœud traite une vidéo MP4 en entrée et renvoie une version améliorée selon les paramètres sélectionnés.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `vidéo` | Le fichier vidéo d'entrée à améliorer. | VIDEO | Oui | - |
| `upscaler_enabled` | Active ou désactive la fonction de suréchantillonnage vidéo (par défaut : True). | BOOLEAN | Oui | - |
| `upscaler_model` | Le modèle d'IA utilisé pour le suréchantillonnage de la vidéo. | COMBO | Oui | `"Starlight (Astra) Fast"`<br>`"Starlight (Astra) Creative"`<br>`"Starlight Precise 2.5"` |
| `upscaler_resolution` | La résolution cible pour la vidéo suréchantillonnée. | COMBO | Oui | `"FullHD (1080p)"`<br>`"4K (2160p)"` |
| `upscaler_creativity` | Niveau de créativité (s'applique uniquement à Starlight (Astra) Creative). (par défaut : "low") | COMBO | Non | `"low"`<br>`"middle"`<br>`"high"` |
| `interpolation_enabled` | Active ou désactive la fonction d'interpolation d'images (par défaut : False). | BOOLEAN | Non | - |
| `interpolation_model` | Le modèle utilisé pour l'interpolation d'images (par défaut : "apo-8"). | COMBO | Non | `"apo-8"` |
| `interpolation_slowmo` | Facteur de ralenti appliqué à la vidéo d'entrée. Par exemple, 2 rend la sortie deux fois plus lente et double la durée. (par défaut : 1) | INT | Non | 1 à 16 |
| `interpolation_frame_rate` | Fréquence d'images de sortie. (par défaut : 60) | INT | Non | 15 à 240 |
| `interpolation_duplicate` | Analyser l'entrée pour détecter les images en double et les supprimer. (par défaut : False) | BOOLEAN | Non | - |
| `interpolation_duplicate_threshold` | Sensibilité de détection des images en double. (par défaut : 0,01) | FLOAT | Non | 0,001 à 0,1 |
| `dynamic_compression_level` | Niveau CQP. (par défaut : "Low") | COMBO | Non | `"Low"`<br>`"Mid"`<br>`"High"` |

**Remarque :** Au moins une fonction d'amélioration doit être activée. Le nœud générera une erreur si `upscaler_enabled` et `interpolation_enabled` sont tous deux définis sur `False`. La vidéo d'entrée doit être au format MP4.

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `vidéo` | Le fichier vidéo de sortie amélioré. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TopazVideoEnhance/fr.md)

---
**Source fingerprint (SHA-256):** `70e1a6e0d7bd250f58c43beefe070fd83af19d11ac08cb9a6ac9655a9bfa839f`
