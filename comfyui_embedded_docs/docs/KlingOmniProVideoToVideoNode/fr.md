# Kling Omni Vidéo à Vidéo (Pro)

Ce nœud utilise le modèle Kling AI pour générer une nouvelle vidéo à partir d'une vidéo d'entrée et d'images de référence facultatives. Vous fournissez un prompt textuel décrivant le contenu souhaité, et le nœud transforme la vidéo de référence en conséquence. Il peut également intégrer jusqu'à quatre images de référence supplémentaires pour guider le style et le contenu de la sortie.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model_name` | Le modèle Kling spécifique à utiliser pour la génération vidéo (par défaut : "kling-v3-omni"). | COMBO | Oui | `"kling-v3-omni"`<br>`"kling-video-o1"` |
| `prompt` | Un prompt textuel décrivant le contenu de la vidéo. Il peut inclure des descriptions positives et négatives. | STRING | Oui | N/A |
| `aspect_ratio` | Le rapport d'aspect souhaité pour la vidéo générée. | COMBO | Oui | `"16:9"`<br>`"9:16"`<br>`"1:1"` |
| `duration` | La durée de la vidéo générée en secondes (par défaut : 3). | INT | Oui | 3 à 10 |
| `reference_video` | Vidéo à utiliser comme référence. | VIDEO | Oui | N/A |
| `keep_original_sound` | Détermine si l'audio de la vidéo de référence est conservé dans la sortie (par défaut : True). | BOOLEAN | Oui | N/A |
| `reference_images` | Jusqu'à 4 images de référence supplémentaires. | IMAGE | Non | N/A |
| `resolution` | La résolution de la vidéo générée (par défaut : "1080p"). | COMBO | Non | `"1080p"`<br>`"720p"` |
| `seed` | La graine contrôle si le nœud doit être réexécuté ; les résultats sont non déterministes quelle que soit la graine (par défaut : 0). | INT | Non | 0 à 2147483647 |

**Contraintes des paramètres :**

* Le `prompt` doit contenir entre 1 et 2500 caractères.
* La `reference_video` doit avoir une durée comprise entre 3.0 et 10.05 secondes.
* La `reference_video` doit avoir des dimensions comprises entre 720x720 et 2160x2160 pixels.
* Vous pouvez fournir au maximum 4 `reference_images`. Chaque image doit mesurer au moins 300x300 pixels et avoir un rapport d'aspect compris entre 1:2.5 et 2.5:1.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `output` | La vidéo nouvellement générée. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingOmniProVideoToVideoNode/fr.md)

---
**Source fingerprint (SHA-256):** `3dc2e3d153ddd9e6da705b764c51b4a859d66464b893fdebb0689d2ad5e870c7`
