> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingOmniProVideoToVideoNode/fr.md)

Ce nœud utilise le modèle Kling AI pour générer une nouvelle vidéo à partir d'une vidéo d'entrée et d'images de référence optionnelles. Vous fournissez un prompt textuel décrivant le contenu souhaité, et le nœud transforme la vidéo de référence en conséquence. Il peut également intégrer jusqu'à quatre images de référence supplémentaires pour guider le style et le contenu de la sortie.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `model_name` | COMBO | Oui | `"kling-v3-omni"`<br>`"kling-video-o1"` | Le modèle Kling spécifique à utiliser pour la génération vidéo (par défaut : "kling-v3-omni"). |
| `prompt` | STRING | Oui | N/A | Un prompt textuel décrivant le contenu vidéo. Peut inclure des descriptions à la fois positives et négatives. |
| `aspect_ratio` | COMBO | Oui | `"16:9"`<br>`"9:16"`<br>`"1:1"` | Le format d'image souhaité pour la vidéo générée. |
| `duration` | INT | Oui | 3 à 10 | La durée de la vidéo générée en secondes (par défaut : 3). |
| `reference_video` | VIDEO | Oui | N/A | Vidéo à utiliser comme référence. |
| `keep_original_sound` | BOOLEAN | Oui | N/A | Détermine si l'audio de la vidéo de référence est conservé dans la sortie (par défaut : True). |
| `reference_images` | IMAGE | Non | N/A | Jusqu'à 4 images de référence supplémentaires. |
| `resolution` | COMBO | Non | `"1080p"`<br>`"720p"` | La résolution de la vidéo générée (par défaut : "1080p"). |
| `seed` | INT | Non | 0 à 2147483647 | La graine contrôle si le nœud doit être réexécuté ; les résultats sont non déterministes quelle que soit la graine (par défaut : 0). |

**Contraintes des paramètres :**

* Le `prompt` doit contenir entre 1 et 2500 caractères.
* La `reference_video` doit avoir une durée comprise entre 3,0 et 10,05 secondes.
* La `reference_video` doit avoir des dimensions comprises entre 720x720 et 2160x2160 pixels.
* Un maximum de 4 `reference_images` peut être fourni. Chaque image doit faire au moins 300x300 pixels et avoir un format d'image compris entre 1:2,5 et 2,5:1.

## Sorties

| Nom de la sortie | Type de données | Description |
|------------------|-----------------|-------------|
| `output` | VIDEO | La nouvelle vidéo générée. |

---
**Source fingerprint (SHA-256):** `1bed976530603bcf7db67048e89ad6adac218fba8597744f8ece3e16a2ee4993`
