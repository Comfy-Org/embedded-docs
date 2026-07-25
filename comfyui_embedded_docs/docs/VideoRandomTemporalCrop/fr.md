# Rogner la vidéo (aléatoire temporel)

Effectuer un recadrage aléatoire d'une plage continue d'images à partir d'une vidéo d'entrée. La longueur du recadrage est contrôlée par le paramètre `length`, et la position de départ est choisie à l'aide d'une graine aléatoire. Le nœud fonctionne de manière paresseuse, ce qui signifie qu'il ne traite pas la vidéo entière tant que la sortie n'est pas utilisée en aval.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `vidéo` | Vidéo d'entrée. | VIDEO | Oui | – |
| `longueur` | Nombre d'images à conserver. (par défaut : 16) | INT | Oui | min : 1, max : 99999 |
| `graine` | Graine aléatoire. (par défaut : 0) | INT | Oui | min : 0, max : 0xFFFFFFFFFFFFFFFF |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `vidéo` | Vidéo recadrée (paresseuse). | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VideoRandomTemporalCrop/fr.md)

---
**Source fingerprint (SHA-256):** `8249feb5ac3607fcabf3de0ec4d2eb90ab4aa46c18613040c341b825c9db1b1e`
