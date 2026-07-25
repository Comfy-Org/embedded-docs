# Échantillonner une image vidéo

Le nœud `VideoFrameSample` extrait un nombre fixe d'images d'une vidéo en utilisant l'une des quatre stratégies. Pour les stratégies contiguës « head » et « tail », la sortie est une référence vidéo paresseuse (les images ne sont pas décodées) ; pour les stratégies non contiguës « uniform » et « random », seules les images sélectionnées sont décodées.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `vidéo` | Vidéo d'entrée. | VIDEO | Oui | – |
| `nombre d’images` | Nombre d'images à échantillonner (par défaut : 16). | INT | Oui | 1 – 9999 |
| `stratégie` | Stratégie d'échantillonnage (par défaut : "uniform"). | COMBO | Oui | `"uniform"`<br>`"head"`<br>`"tail"`<br>`"random"` |
| `graine` | Graine aléatoire, utilisée uniquement avec la stratégie "random" (par défaut : 0). | INT | Oui | 0 – 18446744073709551615 |

- `num_frames` est automatiquement limité au nombre total d'images de la vidéo d'entrée.
- Le paramètre `seed` n'a aucun effet sauf si `strategy` est définie sur `"random"`.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `vidéo` | Vidéo échantillonnée. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VideoFrameSample/fr.md)

---
**Source fingerprint (SHA-256):** `727504a9cf7fe5505c33da071cb8f21a38e1b7c0f964c5da172d9cedfc2f2300`
