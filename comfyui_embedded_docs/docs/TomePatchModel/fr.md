# ModèlePatchTome

Le nœud TomePatchModel applique la technique de fusion de tokens (ToMe) à un modèle de diffusion afin de réduire les besoins en calcul lors de l'inférence. Il fonctionne en fusionnant sélectivement des tokens similaires dans le mécanisme d'attention, ce qui permet au modèle de traiter moins de tokens tout en préservant la qualité de l'image. Cette technique permet d'accélérer la génération sans perte significative de qualité.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Le modèle de diffusion auquel appliquer la fusion de tokens | MODEL | Oui | - |
| `ratio` | Le ratio de tokens à fusionner (par défaut : 0.3) | FLOAT | Non | 0.0 - 1.0 |


| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `model` | Le modèle modifié avec la fusion de tokens appliquée | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TomePatchModel/fr.md)

---
**Source fingerprint (SHA-256):** `23d63ffa1b468a8a41533cc926125f4ef566b13edd1d95a6ef1ae63096a9d878`
