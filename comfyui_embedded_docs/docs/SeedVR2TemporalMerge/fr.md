# SeedVR2TemporalMerge

Ce nœud recompose les morceaux temporels latents échantillonnés de SeedVR2 en un latent complet de pleine longueur. Il utilise un fondu enchaîné par fenêtre de Hann sur la zone de chevauchement entre les morceaux pour créer des transitions fluides, ou effectue une concaténation simple lorsqu'aucun chevauchement n'est spécifié.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `latents` | Les morceaux temporels échantillonnés dans l'ordre séquentiel. | LATENT | Oui | Liste de latents |
| `temporal_overlap` | La sortie `temporal_overlap` de Split SeedVR2 Latent. 0 = concaténation simple. (par défaut : 0) | INT | Oui | 0 à 16384 |

**Remarque :** La valeur de `temporal_overlap` doit être supérieure ou égale à 0. Le dernier morceau de la séquence peut contenir moins d'images temporelles que les autres morceaux. Tous les morceaux doivent avoir des dimensions correspondantes, à l'exception de l'axe temporel (T), et le premier morceau doit être en 5 dimensions (B, C, T, H, W).

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `latent` | Le latent recomposé de pleine longueur. | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SeedVR2TemporalMerge/fr.md)

---
**Source fingerprint (SHA-256):** `647653fc651462f62bcc9dca2919cfcaa4b476b4c679b0a1111698facab83f28`
