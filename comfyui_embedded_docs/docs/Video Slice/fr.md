# Découpage Vidéo

Voici la traduction en français de la documentation du nœud Video Slice :

Le nœud Video Slice vous permet d'extraire un segment spécifique d'une vidéo. Vous pouvez définir un temps de début et une durée pour rogner la vidéo, ou simplement ignorer les premières images. Si la durée demandée est plus longue que la vidéo restante, le nœud peut soit retourner ce qui est disponible, soit générer une erreur.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `vidéo` | La vidéo d'entrée à découper. | VIDEO | Oui | - |
| `heure_de_début` | Temps de début en secondes (par défaut : 0.0). | FLOAT | Non | -1e5 à 1e5 |
| `durée` | Durée en secondes, ou 0 pour une durée illimitée (par défaut : 0.0). | FLOAT | Non | 0.0 et plus |
| `durée_stricte` | Si Vrai, lorsque la durée spécifiée n'est pas possible, une erreur sera générée (par défaut : Faux). | BOOLEAN | Non | - |

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `vidéo` | Le segment vidéo rogné. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Video Slice/fr.md)

---
**Source fingerprint (SHA-256):** `5e3e3e69931a25183eb01b7b87ec12cbf9f5a748781993dcbeec7a6d5f7260c1`
