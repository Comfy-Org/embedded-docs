# HeyGen Traduction Vidéo

Traduire une vidéo parlée dans une autre langue avec clonage vocal et synchronisation labiale. Ce nœud clone la voix du locuteur d'origine et ré-anime la bouche pour correspondre à la parole traduite, produisant un résultat d'apparence naturelle.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `vidéo` | Vidéo avec de la parole à traduire. | VIDEO | Oui | - |
| `langue de sortie` | Langue cible pour la vidéo traduite. | COMBO | Oui | "Arabic"<br>"Bengali"<br>"Chinese"<br>"Danish"<br>"Dutch"<br>"English"<br>"French"<br>"German"<br>"Greek"<br>"Hindi"<br>"Indonesian"<br>"Italian"<br>"Japanese"<br>"Korean"<br>"Malay"<br>"Polish"<br>"Portuguese"<br>"Russian"<br>"Spanish"<br>"Swedish"<br>"Tamil"<br>"Telugu"<br>"Thai"<br>"Turkish"<br>"Ukrainian"<br>"Vietnamese" |
| `mode` | « speed » est plus rapide ; « precision » produit une synchronisation labiale de meilleure qualité à un prix plus élevé. (par défaut : « speed ») | COMBO | Oui | "speed"<br>"precision" |
| `traduire uniquement l'audio` | Remplacez uniquement la piste audio en conservant les mouvements de bouche d'origine (sans synchronisation labiale). (par défaut : False) | BOOLEAN | Non | True<br>False |
| `nombre de locuteurs` | Nombre de locuteurs dans la vidéo. 0 = détection automatique. Les valeurs supérieures à 0 sont envoyées à l'API comme nombre de locuteurs. (par défaut : 0) | INT | Non | 0 à 10 |
| `graine` | Non envoyé à HeyGen ; modifiez-le pour forcer une nouvelle exécution. (par défaut : 42) | INT | Non | 0 à 2147483647 |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `video` | La vidéo traduite avec clonage vocal et synchronisation labiale appliqués. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenVideoTranslateNode/fr.md)

---
**Source fingerprint (SHA-256):** `709438c0c713d6db750643cc48f75352c6f293ae1ff2fd82c1bacb03b2581923`
