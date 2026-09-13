# ModèlePatchTome

TomePatchModel applique la fusion de tokens (ToMe) à un modèle de diffusion afin de réduire le coût de calcul lors de l'inférence. Il fonctionne en fusionnant des tokens similaires dans le mécanisme d'attention du modèle, de sorte que le modèle traite moins de tokens tout en conservant en grande partie la qualité de sortie.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Le modèle de diffusion auquel appliquer la fusion de tokens | MODEL | Oui | - |
| `ratio` | La proportion de tokens à fusionner (par défaut : 0,3). Des valeurs plus élevées fusionnent davantage de tokens, ce qui peut accélérer davantage mais potentiellement réduire la qualité. | FLOAT | Oui | 0.0 - 1.0 |

Remarque : Si le nombre de tokens dans un bloc d'attention est suffisamment faible pour qu'aucun sous-échantillonnage ne soit nécessaire, les fonctions de fusion sont remplacées par des opérations sans effet, et le modèle s'exécute sans modification pour ce bloc.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `model` | Le modèle modifié avec la fusion de tokens appliquée | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TomePatchModel/fr.md)

---
**Source fingerprint (SHA-256):** `1202c0df17f357440cd156fa0920f70c18a318e32c41dc04cecff11613f0072f`
