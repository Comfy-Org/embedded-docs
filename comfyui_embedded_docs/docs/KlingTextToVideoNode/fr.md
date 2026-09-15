# Kling Texte en Vidéo

Le nœud Kling Text to Video génère des vidéos à partir de descriptions textuelles en utilisant l'API de génération vidéo Kling. Il envoie le prompt et les paramètres (rapport d'aspect, mode de génération et échelle de configuration) à l'API, attend que la tâche de génération soit terminée, puis renvoie la vidéo résultante ainsi que son ID et sa durée.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt` | Prompt texte positif | STRING | Oui | Maximum 2500 caractères |
| `negative_prompt` | Prompt texte négatif | STRING | Non | Maximum 2500 caractères |
| `cfg_scale` | Valeur d'échelle de configuration qui contrôle à quel point la vidéo suit le prompt (par défaut : 1.0) | FLOAT | Non | 0.0 à 1.0 |
| `aspect_ratio` | Réglage du rapport d'aspect de la vidéo (par défaut : "16:9") | COMBO | Non | "16:9"<br>"9:16"<br>"1:1" |
| `mode` | Configuration à utiliser pour la génération de la vidéo selon le format : mode / duration / model_name (par défaut : "pro mode / 5s duration / kling-v2-5-turbo") | COMBO | Non | "pro mode / 5s duration / kling-v2-5-turbo"<br>"pro mode / 10s duration / kling-v2-5-turbo" |

Remarque : le paramètre `prompt` est requis et ne doit pas être vide. Les paramètres `prompt` et `negative_prompt` sont limités à un maximum de 2500 caractères. L'option `mode` de 10 secondes coûte plus cher que l'option de 5 secondes.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `output` | La sortie vidéo générée | VIDEO |
| `video_id` | Identifiant unique de la vidéo générée | STRING |
| `duration` | Informations sur la durée de la vidéo générée | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingTextToVideoNode/fr.md)

---
**Source fingerprint (SHA-256):** `6a63b0b8bc45dc5a6300cdfe7a373399eeead36de6727f7aae2c026ba0deaea8`
