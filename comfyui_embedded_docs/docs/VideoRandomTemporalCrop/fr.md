# Rogner la vidéo (aléatoire temporel)

Recadre aléatoirement une plage continue d'images d'une vidéo d'entrée. Le nombre d'images à conserver est défini par le paramètre `length`, et la position de départ est choisie aléatoirement à l'aide du paramètre `seed`. Le nœud fonctionne de manière paresseuse, ce qui signifie qu'il ne traite pas toute la vidéo tant que la sortie n'est pas utilisée en aval.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `vidéo` | Vidéo d'entrée. | VIDEO | Oui | – |
| `longueur` | Nombre d'images à conserver. Si `longueur` est supérieur au nombre total d'images de la vidéo, toute la vidéo est conservée. (par défaut : 16) | INT | Oui | min : 1, max : 99999 |
| `graine` | Graine aléatoire. (par défaut : 0) | INT | Oui | min : 0, max : 0xFFFFFFFFFFFFFFFF |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `vidéo` | Vidéo recadrée (paresseuse). | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VideoRandomTemporalCrop/fr.md)

---
**Source fingerprint (SHA-256):** `8249feb5ac3607fcabf3de0ec4d2eb90ab4aa46c18613040c341b825c9db1b1e`
