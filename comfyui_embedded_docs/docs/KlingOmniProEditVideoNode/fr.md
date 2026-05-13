> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingOmniProEditVideoNode/fr.md)

Le nœud Kling Omni Edit Video (Pro) utilise un modèle d'IA pour éditer une vidéo existante en fonction d'une description textuelle. Vous fournissez une vidéo source et un prompt, et le nœud génère une nouvelle vidéo de même durée avec les modifications demandées. Il peut éventuellement utiliser des images de référence pour guider le style et conserver l'audio original de la vidéo source.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `model_name` | COMBO | Oui | `"kling-v3-omni"`<br>`"kling-video-o1"` | Le modèle d'IA à utiliser pour l'édition vidéo (par défaut : `"kling-v3-omni"`). |
| `prompt` | STRING | Oui | | Un prompt textuel décrivant le contenu vidéo. Cela peut inclure des descriptions à la fois positives et négatives. |
| `video` | VIDEO | Oui | | Vidéo à éditer. La durée de la vidéo de sortie sera identique. |
| `keep_original_sound` | BOOLEAN | Oui | | Détermine si l'audio original de la vidéo d'entrée est conservé dans la sortie (par défaut : True). |
| `reference_images` | IMAGE | Non | | Jusqu'à 4 images de référence supplémentaires. |
| `resolution` | COMBO | Non | `"1080p"`<br>`"720p"` | La résolution de la vidéo de sortie (par défaut : `"1080p"`). |
| `seed` | INT | Non | 0 à 2147483647 | La graine contrôle si le nœud doit être réexécuté ; les résultats sont non déterministes quelle que soit la graine (par défaut : 0). |

**Contraintes et limitations :**

* Le `prompt` doit contenir entre 1 et 2500 caractères.
* La `video` d'entrée doit avoir une durée comprise entre 3,0 et 10,05 secondes.
* Les dimensions de la `video` d'entrée doivent être comprises entre 720x720 et 2160x2160 pixels.
* Un maximum de 4 `reference_images` peut être fourni lorsqu'une vidéo est utilisée.
* Chaque `reference_image` doit faire au moins 300x300 pixels.
* Chaque `reference_image` doit avoir un rapport hauteur/largeur compris entre 1:2,5 et 2,5:1.

## Sorties

| Nom de la sortie | Type de données | Description |
|------------------|-----------------|-------------|
| `video` | VIDEO | La vidéo éditée générée par le modèle d'IA. |

---
**Source fingerprint (SHA-256):** `ddc3fdc8c97cdcdd34f16a0916b13ffe6adeb46e58e2933516c9a6aef7c36730`
