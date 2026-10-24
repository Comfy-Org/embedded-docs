# Comfy Cloud MiniMax H3 Texte vers vidéo [BÊTA]

Exécute le flux de travail texte-vers-vidéo MiniMax H3 sur un GPU Comfy Cloud et renvoie une vidéo accompagnée d'une bande-son correspondante. L'image et l'audio sont produits en une seule passe, au lieu d'être doublés par la suite. Ce nœud est en version bêta et est facturé à la seconde de GPU.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt` | Description textuelle de la vidéo, y compris les sons que le plan doit véhiculer. Les espaces en début et en fin de chaîne sont supprimés avant l'envoi. | STRING | Oui | 1 à 4096 caractères |
| `seed` | Graine aléatoire qui contrôle le résultat généré (par défaut : 42). | INT | Oui | 0 à 18446744073709551615 |
| `aspect_ratio` | Rapport d'aspect de la vidéo générée (par défaut : `"16:9"`). | COMBO | Oui | `"1:1"`<br>`"3:4"`<br>`"2:3"`<br>`"3:2"`<br>`"4:3"`<br>`"16:9"`<br>`"9:16"`<br>`"21:9"` |
| `resolution` | Budget de taille d'image (par défaut : `"480p"`). La 720p coûte environ deux fois plus de secondes de GPU que la 480p. | COMBO | Oui | `"480p"`<br>`"720p"` |
| `duration_seconds` | Durée en secondes (par défaut : 5). Le pipeline quantifie par pas de 17 images à 24 i/s, de sorte que le clip se situe à environ deux tiers de seconde près de cette valeur. | INT | Oui | 5 à 15 |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `VIDEO` | La vidéo générée avec sa bande-son. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyCloudMiniMaxH3TextToVideoNode/fr.md)

---
**Source fingerprint (SHA-256):** `bd1cbc80baa3b77ba48b529119495052252570b949676742b4c77cfe86b70ee2`
