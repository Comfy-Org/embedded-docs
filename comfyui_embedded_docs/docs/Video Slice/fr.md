> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Video Slice/fr.md)

Voici la traduction en français de la documentation du nœud Video Slice :

Le nœud Video Slice vous permet d'extraire un segment spécifique d'une vidéo. Vous pouvez définir un temps de début et une durée pour rogner la vidéo, ou simplement ignorer les premières images. Si la durée demandée est plus longue que la vidéo restante, le nœud peut soit retourner ce qui est disponible, soit générer une erreur.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `vidéo` | VIDEO | Oui | - | La vidéo d'entrée à découper. |
| `heure_de_début` | FLOAT | Non | -1e5 à 1e5 | Temps de début en secondes (par défaut : 0.0). |
| `durée` | FLOAT | Non | 0.0 et plus | Durée en secondes, ou 0 pour une durée illimitée (par défaut : 0.0). |
| `durée_stricte` | BOOLEAN | Non | - | Si Vrai, lorsque la durée spécifiée n'est pas possible, une erreur sera générée (par défaut : Faux). |

## Sorties

| Nom de la sortie | Type de données | Description |
|------------------|-----------------|-------------|
| `vidéo` | VIDEO | Le segment vidéo rogné. |

---
**Source fingerprint (SHA-256):** `5e3e3e69931a25183eb01b7b87ec12cbf9f5a748781993dcbeec7a6d5f7260c1`
