# Découper le latent SeedVR2

Ce nœud divise un latent vidéo SeedVR2 en segments temporels plus petits pouvant être traités un par un dans la mémoire VRAM disponible. Il calcule automatiquement la taille optimale des segments en fonction de votre mémoire GPU ou vous permet de spécifier manuellement la taille des segments, et produit les segments dans l'ordre séquentiel pour le traitement.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `latent` | Le latent SeedVR2 encodé par VAE à diviser. Doit être un tenseur 5-D (B, C, T, H, W) avec le nombre de canaux latents attendu pour SeedVR2. | LATENT | Oui | - |
| `temporal_overlap` | Images latentes partagées entre segments adjacents et fondues enchaînées lors de la fusion ; 0 signifie aucun chevauchement (par défaut : 0). Le chevauchement effectif est plafonné à un de moins que le nombre d'images latentes du segment. | INT | Non | 0 à 16384 |
| `chunking_mode` | Manuel utilise exactement `frames_per_chunk` ; automatique prédit le plus grand segment pouvant tenir dans la VRAM libre. | COMBO | Oui | "auto"<br>"manual" |

Lorsque `chunking_mode` est défini sur "manuel", un paramètre supplémentaire devient disponible :

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `frames_per_chunk` | Images pixels par segment temporel (4n+1 : 1, 5, 9, 13, 17, 21, ...) ; l'interface avance par pas de 4 (par défaut : 21). | INT | Oui | 1 à 16384 |

Remarque : Le paramètre `frames_per_chunk` n'apparaît que lorsque `chunking_mode` est défini sur "manual". La valeur doit satisfaire la formule `(frames_per_chunk - 1) % 4 == 0`, c'est-à-dire être l'une des valeurs : 1, 5, 9, 13, 17, 21, etc. Le latent d'entrée doit être 5-dimensionnel et contenir le nombre de canaux latents attendu pour SeedVR2 ; sinon, le nœud génère une erreur. Si le nombre total d'images pixels dans le latent est égal ou inférieur à la taille de segment choisie (ou à la taille calculée automatiquement), le nœud renvoie le latent d'origine comme un seul segment sans chevauchement.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `latents` | Les segments temporels dans l'ordre séquentiel. | LATENT |
| `temporal_overlap` | Le chevauchement effectif d'images latentes entre segments adjacents, pour le nœud Fusionner SeedVR2 Latents. | INT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SeedVR2TemporalChunk/fr.md)

---
**Source fingerprint (SHA-256):** `40af2b690f74555efbe38f4cf76825417f52735ce90296a9ad662f78cfe4c6bf`
