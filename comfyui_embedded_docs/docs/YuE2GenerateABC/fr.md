# YuE2 Generate ABC

Ce nœud génère une notation ABC pour une chanson à partir d'une description de style et de paroles, en utilisant un modèle YuE2 texte et paroles. La sortie `abc` résultante peut être connectée au nœud YuE2 Generate Music pour produire de l'audio.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `clip` | Le modèle YuE2 utilisé pour tokeniser le style et les paroles et générer la notation ABC. | CLIP | Oui | - |
| `style` | Texte décrivant le style musical de la chanson. Prend en charge la saisie multiligne et les prompts dynamiques. | STRING | Oui | - |
| `lyrics` | Texte contenant les paroles de la chanson. Prend en charge la saisie multiligne et les prompts dynamiques. | STRING | Oui | - |
| `graine` | Graine aléatoire utilisée pour la génération. La modifier produit des résultats différents. Par défaut : 0. | INT | Oui | 0 à 18446744073709551615 |
| `mode` | full : génère la mélodie et les accords ; melody : génère uniquement la mélodie, recommandé pour les reprises. | COMBO | Oui | "full"<br>"melody" |
| `max_abc_tokens` | Nombre maximum de tokens générés pour la notation ABC. Par défaut : 8192. Réglage avancé. | INT | Oui | 1 à 20000 |
| `temperature` | Contrôle le caractère aléatoire des tokens générés. Des valeurs plus élevées produisent des sorties plus variées. Par défaut : 0.7. Réglage avancé. | FLOAT | Oui | 0.0 à 5.0 |
| `top_p` | Seuil d'échantillonnage nucleus ; seuls les tokens dont la probabilité cumulée est inférieure à ce seuil sont pris en compte. Par défaut : 0.9. Réglage avancé. | FLOAT | Oui | 0.01 à 1.0 |
| `top_k` | Limite la sélection des tokens aux K plus probables. Par défaut : 30. Réglage avancé. | INT | Oui | 1 à 32768 |
| `repetition_penalty` | Pénalité appliquée aux tokens répétés pendant la génération. Par défaut : 1.005. Réglage avancé. | FLOAT | Oui | 0.01 à 10.0 |
| `penalty_window` | Nombre de tokens ABC récents utilisés pour pénaliser les répétitions. Par défaut : 100. Réglage avancé. | INT | Oui | 1 à 20000 |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `abc` | La notation ABC générée pour la chanson, qui peut être connectée au nœud YuE2 Generate Music. | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/YuE2GenerateABC/fr.md)

---
**Source fingerprint (SHA-256):** `2c1bf0841a044724ff0477f920972d70bbd97de49b56fbe6213a9ac134797130`
