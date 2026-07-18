# SeedVR2TemporalChunk

Ce nœud divise un latent vidéo SeedVR2 en segments temporels plus petits et chevauchants, pouvant être traités un par un dans la mémoire VRAM disponible. Les segments sont conçus pour être transmis à la fois au nœud Apply SeedVR2 Conditioning et à l'entrée latente de l'échantillonneur, puis recombinés ultérieurement à l'aide du nœud Merge SeedVR2 Latents.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `latent` | Le latent SeedVR2 encodé par VAE à diviser | LATENT | Oui | - |
| `temporal_overlap` | Images latentes partagées entre segments adjacents et fondues lors de la fusion ; 0 signifie aucun chevauchement (par défaut : 0) | INT | Non | 0 à 16384 |
| `chunking_mode` | manuel = utilise exactement frames_per_chunk ; auto = prédit la plus grande taille de segment pouvant tenir dans la VRAM libre | COMBO | Oui | "auto"<br>"manual" |

Lorsque `chunking_mode` est défini sur "manuel", le paramètre suivant devient disponible :

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `frames_per_chunk` | Images pixel par segment temporel (doit être 4n+1 : 1, 5, 9, 13, ...) (par défaut : 21) | INT | Oui | 1 à 16384, pas 4 |

**Remarques sur les contraintes des paramètres :**
- Le `latent` d'entrée doit être un latent vidéo à 5 dimensions de forme (B, C, T, H, W) avec exactement 4 canaux latents
- En mode "manuel", `frames_per_chunk` doit être une valeur 4n+1 (1, 5, 9, 13, 17, 21, ...)
- `temporal_overlap` est automatiquement limité pour être inférieur à la taille du segment
- En mode "auto", le nœud calcule la taille optimale du segment en fonction de la VRAM libre disponible

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `latents` | Les segments temporels dans l'ordre séquentiel | LATENT |
| `temporal_overlap` | Le chevauchement effectif d'images latentes entre segments adjacents, pour Merge SeedVR2 Latents | INT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SeedVR2TemporalChunk/fr.md)

---
**Source fingerprint (SHA-256):** `40af2b690f74555efbe38f4cf76825417f52735ce90296a9ad662f78cfe4c6bf`
