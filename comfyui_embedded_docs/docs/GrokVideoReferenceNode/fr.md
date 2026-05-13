> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokVideoReferenceNode/fr.md)

Voici la traduction en français de la documentation technique du nœud ComfyUI **Grok Reference-to-Video Node**, en respectant vos consignes.

---

Le nœud Grok Reference-to-Video génère une vidéo à partir d’une invite textuelle, en utilisant jusqu’à sept images de référence pour guider le style et le contenu de la sortie. Il se connecte à une API externe pour créer la vidéo, qui est ensuite téléchargée et renvoyée.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `prompt` | STRING | Oui | N/A | Description textuelle de la vidéo souhaitée. |
| `model` | COMBO | Oui | `"grok-imagine-video"` | Le modèle à utiliser pour la génération vidéo. |
| `model.reference_images` | IMAGE | Oui | 1 à 7 images | Jusqu’à 7 images de référence pour guider la génération vidéo. |
| `model.resolution` | COMBO | Oui | `"480p"`<br>`"720p"` | La résolution de la vidéo de sortie. |
| `model.aspect_ratio` | COMBO | Oui | `"16:9"`<br>`"4:3"`<br>`"3:2"`<br>`"1:1"`<br>`"2:3"`<br>`"3:4"`<br>`"9:16"` | Le rapport hauteur/largeur de la vidéo de sortie. |
| `model.duration` | INT | Oui | 2 à 10 | La durée de la vidéo de sortie en secondes (par défaut : 6). |
| `seed` | INT | Non | 0 à 2147483647 | Graine pour déterminer si le nœud doit être réexécuté ; les résultats réels sont non déterministes quelle que soit la graine (par défaut : 0). |

**Remarque :** Le paramètre `model` est un groupe contenant `reference_images`, `resolution`, `aspect_ratio` et `duration`. Vous devez fournir au moins une image de référence, et vous pouvez en fournir jusqu’à sept.

## Sorties

| Nom de la sortie | Type de données | Description |
|------------------|-----------------|-------------|
| `video` | VIDEO | Le fichier vidéo généré. |

---
**Source fingerprint (SHA-256):** `e368769b869b7a0d0be8e6fdcc2b82774c11805483b2e83a448b6985a6dd9f96`
