# Fusionner les latents SeedVR2

Ce nœud recompose les morceaux temporels latents échantillonnés de SeedVR2 en un latent complet de pleine longueur. Lorsqu'un chevauchement temporel est spécifié, il applique un fondu enchaîné à fenêtre de Hann à chaque région de chevauchement pour créer des transitions fluides entre les morceaux ; lorsque le chevauchement est 0, il effectue une concaténation simple.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `latents` | Les morceaux temporels échantillonnés dans l'ordre séquentiel. | LATENT | Oui | Liste de latents |
| `temporal_overlap` | La sortie `temporal_overlap` de Split SeedVR2 Latent. 0 = concaténation simple. (par défaut : 0) | INT | Oui | 0 à 16384 |

**Remarque :** La valeur de `temporal_overlap` doit être supérieure ou égale à 0. Tous les morceaux doivent être des latents vidéo 5-dimensionnels (B, C, T, H, W) et doivent correspondre dans chaque dimension sauf l'axe temporel (T) ; seul le dernier morceau peut être plus court que les autres. Si un seul morceau est fourni, il est renvoyé inchangé.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `latent` | Le latent recomposé de pleine longueur. | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SeedVR2TemporalMerge/fr.md)

---
**Source fingerprint (SHA-256):** `647653fc651462f62bcc9dca2919cfcaa4b476b4c679b0a1111698facab83f28`
