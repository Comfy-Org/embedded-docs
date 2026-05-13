> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TomePatchModel/fr.md)

Le nœud TomePatchModel applique la technique de fusion de tokens (ToMe) à un modèle de diffusion afin de réduire les besoins en calcul lors de l'inférence. Il fonctionne en fusionnant sélectivement des tokens similaires dans le mécanisme d'attention, ce qui permet au modèle de traiter moins de tokens tout en préservant la qualité de l'image. Cette technique permet d'accélérer la génération sans perte significative de qualité.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `model` | MODEL | Oui | - | Le modèle de diffusion auquel appliquer la fusion de tokens |
| `ratio` | FLOAT | Non | 0.0 - 1.0 | Le ratio de tokens à fusionner (par défaut : 0.3) |

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `model` | MODEL | Le modèle modifié avec la fusion de tokens appliquée |

---
**Source fingerprint (SHA-256):** `23d63ffa1b468a8a41533cc926125f4ef566b13edd1d95a6ef1ae63096a9d878`
