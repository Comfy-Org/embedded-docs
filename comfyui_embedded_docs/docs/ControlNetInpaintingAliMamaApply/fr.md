# ControlNetInpaintingAliMamaApply

---

Ce nœud applique le conditionnement ControlNet pour des tâches d'inpainting en combinant le conditionnement positif et négatif avec une image de contrôle et un masque. Il traite l'image et le masque pour créer un conditionnement modifié qui guide le processus de génération, permettant un contrôle précis sur les zones à repeindre. Le nœud prend également en charge des contrôles de force et de calendrier pour ajuster l'influence du ControlNet pendant la génération.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `positive` | Le conditionnement positif qui guide la génération vers le contenu souhaité. | CONDITIONING | Oui | - |
| `negative` | Le conditionnement négatif qui écarte la génération du contenu indésirable. | CONDITIONING | Oui | - |
| `control_net` | Le modèle ControlNet qui fournit un contrôle supplémentaire sur la génération. | CONTROL_NET | Oui | - |
| `vae` | Le VAE utilisé pour encoder et décoder les images. | VAE | Oui | - |
| `image` | L'image d'entrée utilisée comme guide de contrôle pour le ControlNet. | IMAGE | Oui | - |
| `mask` | Le masque qui définit les zones de l'image à repeindre (inpainting). | MASK | Oui | - |
| `strength` | La force de l'effet ControlNet (par défaut : 1.0). | FLOAT | Oui | 0.0 à 10.0 |
| `start_percent` | Option avancée. La fraction du processus de génération à laquelle l'influence du ControlNet commence (par défaut : 0.0). | FLOAT | Oui | 0.0 à 1.0 |
| `end_percent` | Option avancée. La fraction du processus de génération à laquelle l'influence du ControlNet s'arrête (par défaut : 1.0). | FLOAT | Oui | 0.0 à 1.0 |

**Remarque :** Lorsque le ControlNet sélectionné a `concat_mask` activé, les valeurs du masque sont inversées (1 - masque), une version redimensionnée du masque inversé est appliquée à l'image, et le masque inversé est inclus dans les données de concaténation supplémentaires transmises au ControlNet. Si `concat_mask` est désactivé, l'entrée `mask` n'est pas utilisée.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `positive` | Le conditionnement positif modifié avec le ControlNet appliqué pour l'inpainting. | CONDITIONING |
| `negative` | Le conditionnement négatif modifié avec le ControlNet appliqué pour l'inpainting. | CONDITIONING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ControlNetInpaintingAliMamaApply/fr.md)

---
**Source fingerprint (SHA-256):** `307b55c7b4936826b9e4424c172248fa4b41921c2362de724e5cfa2f1c25de68`
