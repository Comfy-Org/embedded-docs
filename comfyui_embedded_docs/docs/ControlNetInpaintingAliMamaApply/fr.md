# ControlNetInpaintingAliMamaApply

Voici la traduction de la documentation du nœud ControlNetInpaintingAliMamaApply :

Le nœud ControlNetInpaintingAliMamaApply applique un conditionnement ControlNet pour les tâches d'incrustation (inpainting) en combinant le conditionnement positif et négatif avec une image de contrôle et un masque. Il traite l'image d'entrée et le masque pour créer un conditionnement modifié qui guide le processus de génération, permettant un contrôle précis des zones de l'image à incruster. Le nœud prend en charge le réglage de la force et des contrôles temporels pour affiner l'influence du ControlNet à différentes étapes du processus de génération.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `positive` | Le conditionnement positif qui guide la génération vers le contenu souhaité | CONDITIONING | Oui | - |
| `negative` | Le conditionnement négatif qui éloigne la génération du contenu indésirable | CONDITIONING | Oui | - |
| `control_net` | Le modèle ControlNet qui fournit un contrôle supplémentaire sur la génération | CONTROL_NET | Oui | - |
| `vae` | Le VAE (Autoencodeur Variationnel) utilisé pour encoder et décoder les images | VAE | Oui | - |
| `image` | L'image d'entrée qui sert de guide de contrôle pour le ControlNet | IMAGE | Oui | - |
| `mask` | Le masque qui définit les zones de l'image à incruster | MASK | Oui | - |
| `strength` | La force de l'effet ControlNet (par défaut : 1.0) | FLOAT | Oui | 0.0 à 10.0 |
| `start_percent` | Le point de départ (en pourcentage) du début de l'influence du ControlNet pendant la génération (par défaut : 0.0) | FLOAT | Oui | 0.0 à 1.0 |
| `end_percent` | Le point d'arrêt (en pourcentage) de la fin de l'influence du ControlNet pendant la génération (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |

**Remarque :** Lorsque le ControlNet a `concat_mask` activé, le masque est inversé et appliqué à l'image avant le traitement, et le masque est inclus dans les données de concaténation supplémentaires envoyées au ControlNet.


| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `positive` | Le conditionnement positif modifié avec le ControlNet appliqué pour l'incrustation | CONDITIONING |
| `negative` | Le conditionnement négatif modifié avec le ControlNet appliqué pour l'incrustation | CONDITIONING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ControlNetInpaintingAliMamaApply/fr.md)

---
**Source fingerprint (SHA-256):** `30b49991b5ead039122a282fb48e3ed30477f89ce1430c371529bc42f921020d`
