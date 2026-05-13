> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SoniloVideoToMusic/fr.md)

Générer de la musique à partir d'une vidéo en utilisant le modèle IA de Sonilo. Ce nœud analyse le contenu d'une vidéo d'entrée et crée un morceau de musique correspondant. Il utilise un service IA externe pour traiter la vidéo et générer l'audio.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `video` | VIDEO | Oui | - | Vidéo d'entrée à partir de laquelle générer la musique. Durée maximale : 6 minutes. |
| `prompt` | STRING | Non | - | Texte d'invite optionnel pour guider la génération musicale. Laissez vide pour une qualité optimale - le modèle analysera entièrement le contenu de la vidéo. (par défaut : chaîne vide) |
| `seed` | INT | Non | 0 à 18446744073709551615 | Graine pour la reproductibilité. Actuellement ignorée par le service Sonilo mais conservée pour la cohérence du graphe. (par défaut : 0) |

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `audio` | AUDIO | La musique générée sous forme de fichier audio. |

---
**Source fingerprint (SHA-256):** `542fff1d8db8e48156bf9d1ff4690c91a7d71676332eef4708a6d36686abb31e`
