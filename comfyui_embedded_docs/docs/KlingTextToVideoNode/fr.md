# Kling Texte en Vidéo

Le nœud Kling Text to Video convertit des invites textuelles en courts clips vidéo à l'aide du service de génération vidéo Kling. Vous fournissez des invites positives et négatives ainsi que des paramètres tels que le rapport hauteur/largeur, l'échelle de configuration et le mode de génération, et le nœud renvoie la vidéo générée avec son identifiant et sa durée.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Invite de texte positive décrivant le contenu vidéo souhaité. Saisie multiligne. Ne peut pas être vide. | STRING | Oui | Maximum 2500 caractères |
| `negative_prompt` | Invite de texte négative décrivant ce qu'il faut éviter dans la vidéo. Saisie multiligne. Peut être laissée vide. | STRING | Oui | Maximum 2500 caractères |
| `cfg_scale` | Valeur d'échelle de configuration qui contrôle la fidélité de la vidéo à l'invite (par défaut : 1.0). | FLOAT | Non | 0.0 à 1.0 |
| `aspect_ratio` | Paramètre de rapport hauteur/largeur de la vidéo (par défaut : « 16:9 »). | COMBO | Non | `"16:9"`<br>`"9:16"`<br>`"1:1"` |
| `mode` | La configuration à utiliser pour la génération vidéo selon le format : mode / durée / nom du modèle (par défaut : « pro mode / 5s duration / kling-v2-5-turbo »). Le mode 5 s coûte 0,35 USD, le mode 10 s coûte 0,70 USD. | COMBO | Non | `"pro mode / 5s duration / kling-v2-5-turbo"`<br>`"pro mode / 10s duration / kling-v2-5-turbo"` |

## Sorties

| Nom de sortie | Description | Type de données |
|-------------|-------------|-----------|
| `output` | La sortie vidéo générée. | VIDEO |
| `video_id` | Identifiant unique de la vidéo générée. | STRING |
| `duration` | Informations de durée pour la vidéo générée. | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingTextToVideoNode/fr.md)

---
**Source fingerprint (SHA-256):** `6a63b0b8bc45dc5a6300cdfe7a373399eeead36de6727f7aae2c026ba0deaea8`
