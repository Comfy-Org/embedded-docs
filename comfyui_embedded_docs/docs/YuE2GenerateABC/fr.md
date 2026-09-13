# YuE2 Generate ABC

Ce nœud génère une notation ABC pour une chanson à partir d'une description de style et de paroles, en utilisant un modèle YuE2 texte et paroles. La sortie `abc` résultante peut être connectée au nœud YuE2 Generate Music pour produire de l'audio.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `clip` | Le modèle YuE2 utilisé pour tokeniser le style et les paroles et générer la notation ABC. | CLIP | Oui | - |
| `style` | Texte décrivant le style musical de la chanson. | STRING | Oui | - |
| `lyrics` | Texte contenant les paroles de la chanson. | STRING | Oui | - |
| `seed` | Graine aléatoire utilisée pour la génération. La modifier produit des résultats différents. Par défaut : 0. | INT | Oui | 0 à 18446744073709551615 |
| `mode` | full : génère la mélodie et les accords ; melody : génère uniquement la mélodie, recommandé pour les reprises. | COMBO | Oui | "full"<br>"melody" |
| `max_abc_tokens` | Nombre maximum de tokens générés pour la notation ABC. Par défaut : 8192. | INT | Oui | 1 à 20000 |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `abc` | La notation ABC générée pour la chanson, qui peut être connectée au nœud YuE2 Generate Music. | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/YuE2GenerateABC/fr.md)

---
**Source fingerprint (SHA-256):** `3e06f980a53e90b750f4190a95199e0e5ed1bd8c54d4dbf8485602ff1af00102`
