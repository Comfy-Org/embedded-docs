# Appliquer Wan Uni3C ControlNet

---

## Aperçu

Ce nœud applique un ControlNet Uni3C à un modèle de diffusion vidéo Wan, en utilisant une vidéo de guidage rendue (par exemple, des rendus de nuages de points déformés) pour influencer la sortie du modèle. Il injecte des signaux de contrôle à des couches de blocs spécifiques, permettant un guidage basé sur la trajectoire de la caméra pendant la génération vidéo.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `modèle` | Le modèle de diffusion Wan à patcher. | MODEL | Oui | – |
| `correctif du modèle` | Un patch ControlNet Uni3C (doit être une instance de `comfy.ldm.wan.uni3c.WanUni3CControlnet`). | MODEL_PATCH | Oui | – |
| `vae` | Le VAE utilisé pour encoder la vidéo de guidage en latents. | VAE | Oui | – |
| `vidéo de rendu` | La vidéo de guidage rendue à partir de la trajectoire de la caméra, le plus souvent des rendus de nuages de points déformés de l'image d'entrée. | IMAGE | Oui | – |
| `force` | La force du signal de contrôle appliqué. | FLOAT | Oui | -10.0 à 10.0 (défaut : 1.0) |
| `pourcentage de début` | Le pourcentage du processus de débruitage auquel le contrôle commence. | FLOAT | Oui | 0.0 à 1.0 (défaut : 0.0) |
| `pourcentage de fin` | Le pourcentage du processus de débruitage auquel le contrôle se termine. | FLOAT | Oui | 0.0 à 1.0 (défaut : 1.0) |

**Notes :**
- Le `model_patch` doit être un ControlNet Uni3C ; sinon le nœud génère une erreur.
- Le ControlNet Uni3C ne fonctionne qu'avec les modèles Wan ; une erreur est levée si le modèle n'est pas basé sur Wan.
- La dimension interne du ControlNet doit correspondre à celle du modèle Wan ; une erreur est levée si elles diffèrent.
- L'image d'entrée `render_video` doit être au format RVB (seuls les 3 premiers canaux sont utilisés).
- Ce nœud est expérimental.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `MODEL` | Le modèle Wan patché avec le ControlNet Uni3C appliqué. | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanUni3CControlnetApply/fr.md)

---
**Source fingerprint (SHA-256):** `f69253f06aba9208778f713ad36e9995f53a15d2e61243b853b9ac9131637371`
