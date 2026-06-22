# Grok Référence-vers-Vidéo

Voici la traduction en français de la documentation technique du nœud ComfyUI **Grok Reference-to-Video Node**, en respectant vos consignes.

---

Le nœud Grok Reference-to-Video génère une vidéo à partir d’une invite textuelle, en utilisant jusqu’à sept images de référence pour guider le style et le contenu de la sortie. Il se connecte à une API externe pour créer la vidéo, qui est ensuite téléchargée et renvoyée.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `invite` | Description textuelle de la vidéo souhaitée. | STRING | Oui | N/A |
| `modèle` | Le modèle à utiliser pour la génération vidéo. | COMBO | Oui | `"grok-imagine-video"` |
| `model.reference_images` | Jusqu’à 7 images de référence pour guider la génération vidéo. | IMAGE | Oui | 1 à 7 images |
| `model.resolution` | La résolution de la vidéo de sortie. | COMBO | Oui | `"480p"`<br>`"720p"` |
| `model.aspect_ratio` | Le rapport hauteur/largeur de la vidéo de sortie. | COMBO | Oui | `"16:9"`<br>`"4:3"`<br>`"3:2"`<br>`"1:1"`<br>`"2:3"`<br>`"3:4"`<br>`"9:16"` |
| `model.duration` | La durée de la vidéo de sortie en secondes (par défaut : 6). | INT | Oui | 2 à 10 |
| `graine` | Graine pour déterminer si le nœud doit être réexécuté ; les résultats réels sont non déterministes quelle que soit la graine (par défaut : 0). | INT | Non | 0 à 2147483647 |

**Remarque :** Le paramètre `model` est un groupe contenant `reference_images`, `resolution`, `aspect_ratio` et `duration`. Vous devez fournir au moins une image de référence, et vous pouvez en fournir jusqu’à sept.

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `video` | Le fichier vidéo généré. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokVideoReferenceNode/fr.md)

---
**Source fingerprint (SHA-256):** `e368769b869b7a0d0be8e6fdcc2b82774c11805483b2e83a448b6985a6dd9f96`
