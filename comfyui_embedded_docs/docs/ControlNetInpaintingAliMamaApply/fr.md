> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ControlNetInpaintingAliMamaApply/fr.md)

Le nœud ControlNetInpaintingAliMamaApply applique un conditionnement ControlNet pour les tâches d'inpainting en combinant les conditionnements positif et négatif avec une image de contrôle et un masque. Il traite l'image d'entrée et le masque pour créer un conditionnement modifié qui guide le processus de génération, permettant un contrôle précis des zones de l'image à restaurer. Le nœud prend en charge l'ajustement de la force et des contrôles temporels pour affiner l'influence du ControlNet pendant les différentes étapes du processus de génération.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | Oui | - | Le conditionnement positif qui guide la génération vers le contenu souhaité |
| `negative` | CONDITIONING | Oui | - | Le conditionnement négatif qui éloigne la génération du contenu indésirable |
| `control_net` | CONTROL_NET | Oui | - | Le modèle ControlNet qui fournit un contrôle supplémentaire sur la génération |
| `vae` | VAE | Oui | - | Le VAE (Autoencodeur variationnel) utilisé pour l'encodage et le décodage des images |
| `image` | IMAGE | Oui | - | L'image d'entrée qui sert de guide de contrôle pour le ControlNet |
| `mask` | MASK | Oui | - | Le masque qui définit les zones de l'image à restaurer |
| `strength` | FLOAT | Oui | 0.0 à 10.0 | La force de l'effet ControlNet (par défaut : 1.0) |
| `start_percent` | FLOAT | Oui | 0.0 à 1.0 | Le point de départ (en pourcentage) du début de l'influence du ControlNet pendant la génération (par défaut : 0.0) |
| `end_percent` | FLOAT | Oui | 0.0 à 1.0 | Le point d'arrêt (en pourcentage) de la fin de l'influence du ControlNet pendant la génération (par défaut : 1.0) |

**Note :** Lorsque le ControlNet a l'option `concat_mask` activée, le masque est inversé et appliqué à l'image avant le traitement, et le masque est inclus dans les données de concaténation supplémentaires envoyées au ControlNet.

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `negative` | CONDITIONING | Le conditionnement positif modifié avec ControlNet appliqué pour l'inpainting |
| `negative` | CONDITIONING | Le conditionnement négatif modifié avec ControlNet appliqué pour l'inpainting |