# HeyGenVideoTranslateNode

### Traduction

Traduisez une vidéo parlée dans une autre langue avec clonage vocal et synchronisation labiale. Ce nœud clone la voix du locuteur original et réanime la bouche pour correspondre à la parole traduite, produisant un résultat d'apparence naturelle.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `video` | Vidéo avec parole à traduire. | VIDEO | Oui | - |
| `output_language` | Langue cible pour la vidéo traduite. | STRING | Oui | "Arabic"<br>"Bengali"<br>"Chinese"<br>"Danish"<br>"Dutch"<br>"English"<br>"French"<br>"German"<br>"Greek"<br>"Hindi"<br>"Indonesian"<br>"Italian"<br>"Japanese"<br>"Korean"<br>"Malay"<br>"Polish"<br>"Portuguese"<br>"Russian"<br>"Spanish"<br>"Swedish"<br>"Tamil"<br>"Telugu"<br>"Thai"<br>"Turkish"<br>"Ukrainian"<br>"Vietnamese" |
| `mode` | 'speed' est plus rapide ; 'precision' produit une synchronisation labiale de meilleure qualité au double du coût. | STRING | Oui | "speed"<br>"precision" |
| `translate_audio_only` | Remplace uniquement la piste audio, en conservant les mouvements de bouche d'origine (pas de synchronisation labiale). (par défaut : False) | BOOLEAN | Non | True<br>False |
| `speaker_count` | Nombre de locuteurs dans la vidéo. 0 = détection automatique. (par défaut : 0) | INT | Non | 0 à 10 |
| `seed` | N'est pas envoyé à HeyGen ; modifiez-le pour forcer une nouvelle exécution. (par défaut : 42) | INT | Non | 0 à 2147483647 |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `video` | La vidéo traduite avec clonage vocal et synchronisation labiale appliqués. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenVideoTranslateNode/fr.md)

---
**Source fingerprint (SHA-256):** `31056060b6309b8ec28b37b353322403e173fd2862b56021392dba24e7a15f69`
