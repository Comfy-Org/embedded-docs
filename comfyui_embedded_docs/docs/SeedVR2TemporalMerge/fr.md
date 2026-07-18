# SeedVR2TemporalMerge

Ce nœud recompose les segments temporels de données vidéo latentes qui ont été précédemment divisés par le nœud Split SeedVR2 Latent. Il utilise un fondu enchaîné par fenêtre de Hann sur les zones de chevauchement pour créer une transition fluide entre les segments, ou effectue une simple concaténation lorsqu'aucun chevauchement n'est spécifié.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `latents` | Les segments temporels échantillonnés dans l'ordre séquentiel. | LATENT | Oui | Liste de latents |
| `temporal_overlap` | La sortie `temporal_overlap` de Split SeedVR2 Latent. 0 = concaténation simple. | INT | Oui | 0 à 16384 (par défaut : 0) |

**Remarque :** Le paramètre `temporal_overlap` doit être connecté à la sortie `temporal_overlap` du nœud Split SeedVR2 Latent. Tous les latents d'entrée doivent avoir la même taille de lot, le même nombre de canaux, la même hauteur et la même largeur. Seul le dernier segment peut avoir une dimension temporelle plus courte que les autres.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `latent` | Le latent recomposé de pleine longueur. | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SeedVR2TemporalMerge/fr.md)

---
**Source fingerprint (SHA-256):** `647653fc651462f62bcc9dca2919cfcaa4b476b4c679b0a1111698facab83f28`
