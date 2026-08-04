# Rogner la vidéo (temporel)

Ce nœud découpe une plage continue d'images d'une vidéo. Il fonctionne de manière entièrement paresseuse (lazy), ce qui signifie qu'il ne traite que la portion sélectionnée de la vidéo lorsque cela est nécessaire ultérieurement dans le workflow.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|------------------|--------|-------|
| `vidéo` | Vidéo d'entrée. | VIDEO | Oui | – |
| `image de départ` | Index de l'image de début (par défaut : 0). | INT | Oui | 0 à 99999 |
| `longueur` | Nombre d'images à conserver (par défaut : 16). | INT | Oui | 1 à 99999 |
Remarque : `start_frame` est limité à la dernière image de la vidéo, et `length` est réduit s'il dépasserait les images disponibles.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|------------------|
| `vidéo` | Vidéo découpée (lazy). | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VideoTemporalCrop/fr.md)

---
**Source fingerprint (SHA-256):** `1d28a55399c9fe7ca47f0aaa872751ac89c5419a6f6be6636fbf7f020a02749d`
