# MiniMaxH3FunControlNetApply

Ce nœud applique un MiniMax H3 Fun ControlNet à un modèle texte-vers-vidéo sous forme de patch de modèle. Il peut utiliser une vidéo de contrôle facultative et un masque facultatif pour orienter la génération, et renvoie une copie patchée du modèle pour un échantillonnage ultérieur. Lorsque `strength` est réglée sur 0, ou si aucune vidéo de contrôle ni aucun masque n’est fourni, le modèle d’entrée est renvoyé inchangé.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model` | Le modèle de diffusion auquel le patch MiniMax H3 Fun ControlNet est appliqué. | MODEL | Oui | N/A |
| `model_patch` | Le patch MiniMax H3 Fun ControlNet dont les signaux de contrôle sont injectés dans le modèle ; il doit être compatible avec le `model` fourni. | MODEL_PATCH | Oui | N/A |
| `vae` | VAE utilisé pour encoder les images des vidéos de contrôle et source dans l’espace latent attendu par le modèle. | VAE | Oui | N/A |
| `strength` | Force globale de l’effet ControlNet. Lorsqu’elle est définie sur 0, le nœud ne fait rien et renvoie le modèle d’entrée inchangé. (par défaut : 1.0) | FLOAT | Oui | min 0.0, max 10.0, step 0.01 |
| `start_percent` | Début de la plage d’échantillonnage, exprimé en pourcentage du calendrier d’échantillonnage, pendant laquelle le ControlNet est actif. Il est converti en interne en valeur sigma équivalente. (par défaut : 0.0) | FLOAT | Oui | min 0.0, max 1.0, step 0.001 |
| `end_percent` | Fin de la plage d’échantillonnage, exprimé en pourcentage du calendrier d’échantillonnage, pendant laquelle le ControlNet est actif. Elle est convertie en interne en valeur sigma équivalente. (par défaut : 1.0) | FLOAT | Oui | min 0.0, max 1.0, step 0.001 |
| `control_video` | Images vidéo facultatives utilisées comme indication visuelle pour le ControlNet. Les images sont redimensionnées pour correspondre à la vidéo générée, puis encodées avec le `vae`. | IMAGE | Non | N/A |
| `mask` | 1 marque les régions à régénérer. Les valeurs du masque supérieures à 0.5 sont considérées comme des régions marquées. | MASK | Non | N/A |
| `source_video` | Vidéo située derrière le masque ; elle n’est lue que si un masque est fourni. | IMAGE | Non | N/A |

Remarque : Pour que le patch ait un effet, `strength` doit être supérieure à 0 et au moins l’un des paramètres `control_video` ou `mask` doit être fourni. `source_video` est ignoré sauf si `mask` est fourni ; si `mask` est fourni sans `source_video`, le contenu derrière les régions masquées est considéré comme noir.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `model` | Un clone patché du modèle d’entrée avec le MiniMax H3 Fun ControlNet appliqué. Si `strength` vaut 0, ou si aucune vidéo de contrôle ni aucun masque n’est fourni, le modèle d’origine est renvoyé inchangé. | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MiniMaxH3FunControlNetApply/fr.md)

---
**Source fingerprint (SHA-256):** `e907fb8e5ae60663d1d10b315985695ee5d49397fef6bd76b0e723637457a74a`
