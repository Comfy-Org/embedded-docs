# SplitSigmasDenoise

Le nœud SplitSigmasDenoise divise une séquence de valeurs sigma en deux parties en fonction d’un paramètre d’intensité de débruitage. Il sépare les sigmas d’entrée en séquences de sigmas élevés et faibles, le point de division étant déterminé en multipliant le nombre total d’étapes par le facteur de débruitage. Cela permet de séparer le calendrier de bruit en différentes plages d’intensité pour un traitement spécialisé.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `sigmas` | La séquence de valeurs sigma d’entrée représentant le calendrier de bruit | SIGMAS | Oui | - |
| `denoise` | Le facteur d’intensité de débruitage qui détermine où diviser la séquence de sigmas (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |

Remarque : Le nombre total d’étapes est égal au nombre de valeurs sigma moins 1. Les deux séquences de sortie partagent une valeur sigma au point de division. À `denoise` = 0.0, `high_sigmas` est vide ; à `denoise` = 1.0, `high_sigmas` ne contient que la première valeur sigma et `low_sigmas` contient la séquence complète.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `high_sigmas` | La première partie de la séquence de sigmas contenant les valeurs sigma les plus élevées | SIGMAS |
| `low_sigmas` | La deuxième partie de la séquence de sigmas contenant les valeurs sigma les plus faibles | SIGMAS |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SplitSigmasDenoise/fr.md)

---
**Source fingerprint (SHA-256):** `6198cdbc07b5c9aacf1137a5d6350e090ffd14050abbcc37ff79ff5e975a8c20`
