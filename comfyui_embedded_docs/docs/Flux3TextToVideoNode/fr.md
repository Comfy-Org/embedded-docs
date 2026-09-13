# Flux 3 Texte vers Vidéo

Génère une vidéo avec un audio synchronisé à partir d’un prompt textuel à l’aide de FLUX 3. Le nœud envoie votre prompt au service FLUX 3, attend la fin de la génération et renvoie le clip vidéo terminé.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt` | Ce que vous voulez, en langage naturel ; le prompt est interprété et développé avant la génération. Décrivez séparément les sons d’ambiance, la musique et la parole pour un audio en couches. (par défaut : "") | STRING | Oui | Texte multiligne |
| `aspect_ratio` | Ratio d’aspect de sortie. 'auto' en choisit un à partir du prompt et des entrées. (par défaut : "auto") | COMBO | Oui | Plusieurs options disponibles, dont `"auto"` |
| `duration` | Durée du clip en secondes. 'auto' adapte la durée au contenu. (par défaut : "auto") | COMBO | Oui | Plusieurs options disponibles, dont `"auto"` |
| `resolution` | Résolution de sortie. (par défaut : "720p") | COMBO | Oui | `"720p"`<br>`"1080p"` |
| `generate_audio` | Générer un audio synchronisé (ambiance, parole, effets). Désactivé produit une vidéo sans piste audio. (par défaut : True) | BOOLEAN | Oui | True<br>False |
| `safety_tolerance` | Tolérance de modération, 0 étant la plus stricte. Les requêtes qui envoient des images ou des vidéos sont plafonnées à 2, quelle que soit la valeur définie ici. (par défaut : 2) | INT | Oui | 0 à 4 |
| `seed` | Graine pour déterminer si le nœud doit être réexécuté ; FLUX 3 choisit sa propre graine, donc les résultats réels sont non déterministes quelle que soit cette valeur. (par défaut : 42) | INT | Oui | 0 à 4294967295 |

Remarque : `safety_tolerance` est une entrée avancée. L’entrée `seed` inclut les contrôles Control After Generate dans l’interface. Le prix affiché est basé sur `resolution` et `duration` : la HD (720p) est facturée à 0,2431 $ par seconde et la FHD (1080p) à 0,4147 $ par seconde. Lorsqu’une durée fixe est choisie, le coût total estimé du clip est affiché ; lorsque `duration` vaut "auto", le tarif par seconde est affiché.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `video` | Le clip vidéo généré, avec un audio synchronisé lorsque `generate_audio` est activé. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Flux3TextToVideoNode/fr.md)

---
**Source fingerprint (SHA-256):** `9957c78291c320b1a8a6a9c0edeefae5f1ccc21a6b58f0b39069c2df8decd100`
