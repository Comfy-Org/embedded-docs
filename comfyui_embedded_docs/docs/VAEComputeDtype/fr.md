# VAE Compute Dtype

Ce nœud définit le dtype de calcul utilisé lorsqu'un VAE encode ou décode, sans modifier le reste du graphe du modèle. Il renvoie une copie du VAE d'entrée avec la précision demandée, afin qu'un workflow puisse exécuter une branche à une précision supérieure tandis que les autres restent inchangées. « default » conserve le dtype de calcul déjà utilisé par le VAE d'entrée.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `vae` | VAE à ajuster. Le nœud travaille sur une copie, donc le VAE connecté n'est pas modifié. | VAE | Oui | - |
| `dtype` | Dtype de calcul pour l'encodage et le décodage VAE. « default » conserve le dtype de calcul du VAE d'entrée (par défaut : « default »). | COMBO | Oui | "default"<br>"fp32"<br>"fp16"<br>"bf16" |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `vae` | La copie du VAE à laquelle le dtype de calcul sélectionné est appliqué. | VAE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEComputeDtype/fr.md)

---
**Source fingerprint (SHA-256):** `239e5829d76b4bd43ec300fc2b7c8c408b5bd4a93918da417ecf43817aee3e12`
