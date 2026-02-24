> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TopazVideoEnhance/fr.md)

Le nœud Topaz Video Enhance utilise une API externe pour améliorer la qualité vidéo. Il peut augmenter la résolution vidéo, augmenter la fréquence d'images par interpolation et appliquer une compression. Le nœud traite une vidéo MP4 d'entrée et renvoie une version améliorée basée sur les paramètres sélectionnés.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `video` | VIDEO | Oui | - | Le fichier vidéo d'entrée à améliorer. |
| `upscaler_enabled` | BOOLEAN | Oui | - | Active ou désactive la fonction de suréchantillonnage vidéo (par défaut : True). |
| `upscaler_model` | COMBO | Oui | `"Proteus v3"`<br>`"Artemis v13"`<br>`"Artemis v14"`<br>`"Artemis v15"`<br>`"Gaia v6"`<br>`"Theia v3"`<br>`"Starlight (Astra) Creative"`<br>`"Starlight (Astra) Optimized"`<br>`"Starlight (Astra) Balanced"`<br>`"Starlight (Astra) Quality"`<br>`"Starlight (Astra) Speed"` | Le modèle d'IA utilisé pour le suréchantillonnage de la vidéo. |
| `upscaler_resolution` | COMBO | Oui | `"FullHD (1080p)"`<br>`"4K (2160p)"` | La résolution cible pour la vidéo suréchantillonnée. |
| `upscaler_creativity` | COMBO | Non | `"low"`<br>`"middle"`<br>`"high"` | Niveau de créativité (s'applique uniquement à Starlight (Astra) Creative). (par défaut : "low") |
| `interpolation_enabled` | BOOLEAN | Non | - | Active ou désactive la fonction d'interpolation d'images (par défaut : False). |
| `interpolation_model` | COMBO | Non | `"apo-8"` | Le modèle utilisé pour l'interpolation d'images (par défaut : "apo-8"). |
| `interpolation_slowmo` | INT | Non | 1 à 16 | Facteur de ralenti appliqué à la vidéo d'entrée. Par exemple, 2 rend la sortie deux fois plus lente et double la durée. (par défaut : 1) |
| `interpolation_frame_rate` | INT | Non | 15 à 240 | Fréquence d'images de sortie. (par défaut : 60) |
| `interpolation_duplicate` | BOOLEAN | Non | - | Analyse l'entrée pour détecter les images en double et les supprime. (par défaut : False) |
| `interpolation_duplicate_threshold` | FLOAT | Non | 0.001 à 0.1 | Sensibilité de détection pour les images en double. (par défaut : 0.01) |
| `dynamic_compression_level` | COMBO | Non | `"Low"`<br>`"Mid"`<br>`"High"` | Niveau CQP. (par défaut : "Low") |

**Note :** Au moins une fonction d'amélioration doit être activée. Le nœud générera une erreur si `upscaler_enabled` et `interpolation_enabled` sont tous deux définis sur `False`. La vidéo d'entrée doit être au format MP4.

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `video` | VIDEO | Le fichier vidéo de sortie amélioré. |
