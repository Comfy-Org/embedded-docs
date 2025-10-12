> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyAudio/fr.md)

Le nœud EmptyAudio génère un clip audio silencieux avec une durée, une fréquence d'échantillonnage et une configuration de canaux spécifiées. Il crée une forme d'onde contenant uniquement des zéros, produisant un silence complet pour la durée donnée. Ce nœud est utile pour créer des audio de substitution ou générer des segments silencieux dans les flux de travail audio.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `duration` | FLOAT | Oui | 0.0 à 1.8446744073709552e+19 | Durée du clip audio silencieux en secondes (par défaut : 60.0) |
| `sample_rate` | INT | Oui | - | Fréquence d'échantillonnage du clip audio silencieux (par défaut : 44100) |
| `channels` | INT | Oui | 1 à 2 | Nombre de canaux audio (1 pour mono, 2 pour stéréo) (par défaut : 2) |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `AUDIO` | AUDIO | Le clip audio silencieux généré contenant les données de forme d'onde et les informations de fréquence d'échantillonnage |
