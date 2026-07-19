# Sonilo Vidéo en Musique

Générer de la musique à partir d'une vidéo en utilisant le modèle IA de Sonilo. Ce nœud analyse le contenu d'une vidéo d'entrée et crée un morceau de musique correspondant. Il utilise un service IA externe pour traiter la vidéo et générer l'audio.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `video` | Vidéo d'entrée à partir de laquelle générer la musique. Durée maximale : 6 minutes. | VIDEO | Oui | - |
| `prompt` | Texte d'invite optionnel pour guider la génération musicale. Laissez vide pour une qualité optimale - le modèle analysera entièrement le contenu de la vidéo. (par défaut : chaîne vide) | STRING | Non | - |
| `seed` | Graine pour la reproductibilité. Actuellement ignorée par le service Sonilo mais conservée pour la cohérence du graphe. (par défaut : 0) | INT | Non | 0 à 18446744073709551615 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `audio` | La musique générée sous forme de fichier audio. | AUDIO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SoniloVideoToMusic/fr.md)

---
**Source fingerprint (SHA-256):** `542fff1d8db8e48156bf9d1ff4690c91a7d71676332eef4708a6d36686abb31e`
