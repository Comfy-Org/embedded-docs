# ModèlePatchTome

Le nœud TomePatchModel applique le Token Merging (ToMe) à un modèle de diffusion afin de réduire les exigences de calcul lors de l'inférence. Il fonctionne en fusionnant sélectivement les jetons similaires dans le mécanisme d'attention, ce qui permet au modèle de traiter moins de jetons tout en conservant la qualité de l'image. Cette technique accélère la génération sans perte de qualité significative.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model` | Le modèle de diffusion auquel appliquer le Token Merging | MODEL | Oui | - |
| `ratio` | Le ratio de jetons à fusionner (défaut : 0.3, pas : 0.01). Des valeurs plus élevées fusionnent plus de jetons, ce qui entraîne une accélération plus importante mais potentiellement une qualité inférieure. | FLOAT | Oui | 0.0 - 1.0 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `model` | Le modèle modifié avec le Token Merging appliqué | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TomePatchModel/fr.md)

---
**Source fingerprint (SHA-256):** `1202c0df17f357440cd156fa0920f70c18a318e32c41dc04cecff11613f0072f`
