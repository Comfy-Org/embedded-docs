# FLUX 3 Max Text to Video

FLUX 3 Max Text to Video génère une vidéo avec un audio synchronisé à partir d’un prompt textuel. Le prompt est interprété et développé par FLUX 3 Max avant le rendu ; le nœud attend la fin du rendu, puis renvoie le clip terminé.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt` | Ce que le clip doit montrer, en langage naturel. Décrivez séparément les sons d’ambiance, la musique et la parole pour un audio multicouche (par défaut : vide). | STRING | Oui | Texte multiligne |
| `aspect_ratio` | Format d’image de sortie. `"auto"` correspond à 16:9 pour les prompts textuels (par défaut : `"auto"`). | COMBO | Oui | `"auto"`<br>`"21:9"`<br>`"2:1"`<br>`"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"` |
| `duration` | Durée du clip en secondes (par défaut : `"5"`). | COMBO | Oui | `"5"`<br>`"6"`<br>`"7"`<br>`"8"`<br>`"9"`<br>`"10"`<br>`"11"`<br>`"12"`<br>`"13"`<br>`"14"`<br>`"15"`<br>`"16"`<br>`"17"`<br>`"18"`<br>`"19"`<br>`"20"` |
| `resolution` | Résolution de sortie (par défaut : `"720p"`). | COMBO | Oui | `"720p"`<br>`"1080p"` |
| `reasoning_level` | Niveau de raisonnement et de développement du prompt par le modèle avant la génération. `"high"` prend plus de temps ; le prix reste le même (par défaut : `"high"`). | COMBO | Oui | `"low"`<br>`"high"` |
| `generate_audio` | Générer un audio synchronisé. Désactivé, le résultat est une vidéo sans piste audio (par défaut : true). | BOOLEAN | Oui | `true`<br>`false` |
| `seed` | Graine contrôlant si le nœud est réexécuté. Les résultats ne sont pas déterministes, quelle que soit cette valeur (par défaut : 42). | INT | Oui | 0 à 2147483646 |

Remarque : `prompt` doit contenir au moins un caractère. Le prix affiché dépend de `resolution` et de `duration` : la 720p est facturée 0,060775 $ par seconde et la 1080p 0,103675 $ par seconde jusqu’au 7 novembre 2026, puis 0,2431 $ et 0,4147 $ par seconde après cette date. Le coût total estimé du clip est affiché dans l’interface utilisateur.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `video` | Le clip vidéo généré, avec un audio synchronisé lorsque `generate_audio` est activé. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Flux3MaxTextToVideoNode/fr.md)

---
**Source fingerprint (SHA-256):** `6dcb11e7aa7f1592169ede449c4092740db43e635501205eba02a066f03a967f`
