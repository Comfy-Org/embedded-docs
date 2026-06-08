Le nœud EmptyAudio génère un clip audio silencieux avec une durée, un taux d'échantillonnage et une configuration de canaux spécifiés. Il crée une forme d'onde contenant uniquement des zéros, produisant un silence complet pour la durée donnée. Ce nœud est utile pour créer des espaces réservés audio ou générer des segments silencieux dans des workflows audio.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `durée` | Durée du clip audio vide en secondes (par défaut : 60,0) | FLOAT | Oui | 0,0 à 1,8446744073709552e+19 |
| `fréquence_d'échantillonnage` | Taux d'échantillonnage du clip audio vide (par défaut : 44100) | INT | Oui | 1 à 192000 |
| `canaux` | Nombre de canaux audio (1 pour mono, 2 pour stéréo) (par défaut : 2) | INT | Oui | 1 à 2 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `AUDIO` | Le clip audio silencieux généré contenant les données de forme d'onde et les informations de taux d'échantillonnage | AUDIO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyAudio/fr.md)

---
**Source fingerprint (SHA-256):** `61b9cd6c8e518f28533b7586fdd1f909e5c356c7f2f7690da4e1ec7965d53c5d`
