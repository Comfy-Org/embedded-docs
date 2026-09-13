# SplitSigmasDenoise

Le nœud SplitSigmasDenoise divise une séquence de valeurs sigma en deux parties selon un paramètre de force de débruitage. Il sépare les sigmas d'entrée en séquences de sigmas élevés et faibles, où le point de séparation est déterminé en multipliant le nombre total d'étapes (un de moins que le nombre de valeurs sigma) par le facteur de débruitage. Cela permet de séparer le programme de bruit en différentes plages d'intensité pour un traitement spécialisé.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `sigmas` | La séquence d'entrée de valeurs sigma représentant le programme de bruit | SIGMAS | Oui | - |
| `réduction_du_bruit` | Le facteur de force de débruitage qui détermine où diviser la séquence sigma (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 (pas : 0.01) |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `high_sigmas` | La première partie de la séquence sigma, contenant les valeurs sigma les plus élevées jusqu'au point de séparation | SIGMAS |
| `low_sigmas` | La seconde partie de la séquence sigma, contenant les valeurs sigma les plus faibles à partir du point de séparation | SIGMAS |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SplitSigmasDenoise/fr.md)

---
**Source fingerprint (SHA-256):** `6198cdbc07b5c9aacf1137a5d6350e090ffd14050abbcc37ff79ff5e975a8c20`
