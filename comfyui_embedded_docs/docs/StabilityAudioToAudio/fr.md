Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StabilityAudioToAudio/fr.md)

Transforme des échantillons audio existants en nouvelles compositions de haute qualité à l'aide d'instructions textuelles. Ce nœud prend un fichier audio en entrée et le modifie en fonction de votre invite textuelle pour créer un nouveau contenu audio.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Le modèle d'IA à utiliser pour la transformation audio | COMBO | Oui | "stable-audio-2.5" |
| `consigne` | Instructions textuelles décrivant comment transformer l'audio (par défaut : vide) | STRING | Oui |  |
| `audio` | L'audio doit durer entre 6 et 190 secondes | AUDIO | Oui |  |
| `durée` | Contrôle la durée en secondes de l'audio généré (par défaut : 190) | INT | Non | 1-190 |
| `graine` | La graine aléatoire utilisée pour la génération (par défaut : 0) | INT | Non | 0-4294967294 |
| `étapes` | Contrôle le nombre d'étapes d'échantillonnage (par défaut : 8) | INT | Non | 4-8 |
| `intensité` | Ce paramètre contrôle l'influence du paramètre audio sur l'audio généré (par défaut : 1.0) | FLOAT | Non | 0.01-1.0 |

**Remarque :** L'audio d'entrée doit durer entre 6 et 190 secondes.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `audio` | L'audio transformé généré à partir de l'audio d'entrée et de l'invite textuelle | AUDIO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StabilityAudioToAudio/fr.md)

---
**Source fingerprint (SHA-256):** `d63ee2585be1ec1a21da72656ecea37f051a56595b15637013e515eb298fc4dc`
