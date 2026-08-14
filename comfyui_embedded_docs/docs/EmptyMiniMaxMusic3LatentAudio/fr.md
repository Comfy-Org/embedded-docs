# EmptyMiniMaxMusic3LatentAudio

Ce nœud crée un tenseur audio latent vide (rempli de zéros) pour le modèle MiniMax Music3. Il convertit la durée demandée en secondes en trames audio correspondantes et produit un latent vide de la taille correcte, prêt à être utilisé comme point de départ pour la génération musicale.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `seconds` | La durée du latent audio en secondes (par défaut : 120.0). La valeur est convertie en trames audio puis limitée aux durées maximales prises en charge par le modèle. | FLOAT | Oui | 0.04 au maximum du modèle (MAX_AUDIO_FRAMES / AUDIO_FRAMES_PER_SECOND), pas de 0.04 |
| `batch_size` | Le nombre de latents audio à générer en un seul lot (par défaut : 1). | INT | Oui | 1 à 4096 |

Note : La valeur `seconds` est arrondie à la trame audio la plus proche puis limitée à un minimum de 1 trame et à un maximum de `MAX_AUDIO_FRAMES` trames. La longueur réelle du latent peut donc différer légèrement de la valeur exacte saisie.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `LATENT` | Un tenseur audio latent rempli de zéros de forme (batch_size, 128, latent_length). Inclut des métadonnées qui marquent l'échantillon comme données audio avec un ratio de sous-échantillonnage temporel de 512. | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyMiniMaxMusic3LatentAudio/fr.md)

---
**Source fingerprint (SHA-256):** `77e6a69702a837c958c2954bba061c979152f034bc7774a5b6c97ea8d57bda4b`
