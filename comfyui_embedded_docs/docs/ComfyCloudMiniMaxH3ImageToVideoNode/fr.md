# Comfy Cloud MiniMax H3 Image vers vidéo [BÊTA]

Exécute le workflow image-vers-vidéo MiniMax H3 sur un GPU Comfy Cloud et renvoie une vidéo avec une bande-son associée. L’image fixe devient la première image. Réinjecter l’image de fin d’un clip poursuit la séquence ; ainsi, en enchaînant plusieurs exécutions, on construit un plan plus long. Ce nœud est en version bêta et est facturé à la seconde GPU.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `first_frame` | L’image à partir de laquelle la vidéo démarre. Elle est téléversée en 2048x2048 pixels maximum avant l’exécution du workflow. | IMAGE | Oui | - |
| `prompt` | Description textuelle du mouvement et des sons que le plan doit comporter. Les espaces blancs en début et en fin sont supprimés avant la soumission. | STRING | Oui | 1 à 4096 caractères |
| `seed` | Graine aléatoire qui contrôle le résultat généré (par défaut : 42). | INT | Oui | 0 à 18446744073709551615 |
| `aspect_ratio` | Rapport d’aspect de la vidéo générée (par défaut : `"1:1"`). | COMBO | Oui | `"1:1"`<br>`"3:4"`<br>`"2:3"`<br>`"3:2"`<br>`"4:3"`<br>`"16:9"`<br>`"9:16"`<br>`"21:9"` |
| `resolution` | Budget de taille de trame (par défaut : `"480p"`). La 720p coûte environ deux fois plus de secondes GPU que la 480p. | COMBO | Oui | `"480p"`<br>`"720p"` |
| `duration_seconds` | Durée en secondes (par défaut : 5). Le pipeline quantifie par pas de 17 images à 24 i/s, de sorte que le clip s’écarte d’environ deux tiers de seconde au maximum de cette valeur. | INT | Oui | 5 à 15 |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `VIDEO` | La vidéo générée avec sa bande-son. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyCloudMiniMaxH3ImageToVideoNode/fr.md)

---
**Source fingerprint (SHA-256):** `d3657e266f2b9f789414a106ef66b6c64ec314d27c3b6a99c3a6a9b8584abf61`
