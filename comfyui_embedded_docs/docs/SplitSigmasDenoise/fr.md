# SplitSigmasDenoise

Le nœud SplitSigmasDenoise divise une séquence de valeurs sigma en deux parties en fonction d'un paramètre de force de débruitage. Il sépare les sigmas d'entrée en séquences haute et basse, où le point de division est déterminé en multipliant le nombre total d'étapes par le facteur de débruitage. Cela permet de séparer le calendrier de bruit en différentes plages d'intensité pour un traitement spécialisé.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `sigmas` | La séquence de valeurs sigma d'entrée représentant le calendrier de bruit | SIGMAS | Oui | - |
| `réduction_du_bruit` | Le facteur de force de débruitage qui détermine où diviser la séquence sigma (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 (pas : 0.01) |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `sigmas_hauts` | La première partie de la séquence sigma contenant les valeurs sigma les plus élevées | SIGMAS |
| `sigmas_bas` | La seconde partie de la séquence sigma contenant les valeurs sigma les plus basses | SIGMAS |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SplitSigmasDenoise/fr.md)

---
**Source fingerprint (SHA-256):** `6198cdbc07b5c9aacf1137a5d6350e090ffd14050abbcc37ff79ff5e975a8c20`
