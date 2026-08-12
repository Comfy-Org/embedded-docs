# Flux3TextToVideoNode

Génère une vidéo avec audio synchronisé à partir d’un prompt texte en utilisant FLUX 3. Le nœud envoie votre prompt au service FLUX 3, attend la fin de la génération et renvoie le clip vidéo terminé.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt` | Ce que vous voulez, en langage naturel ; le prompt est interprété et enrichi avant la génération. Décrivez séparément l’ambiance sonore, la musique et la parole pour un audio en couches. (défaut : "") | STRING | Oui | Texte multiligne |
| `aspect_ratio` | Format de sortie. 'auto' choisit un format en fonction du prompt et des entrées. (défaut : "auto") | STRING | Oui | Plusieurs options disponibles, y compris `"auto"` |
| `duration` | Durée du clip en secondes. 'auto' adapte la durée au contenu. (défaut : "auto") | STRING | Oui | Plusieurs options disponibles, y compris `"auto"` |
| `resolution` | Résolution de sortie. (défaut : "720p") | STRING | Oui | `"720p"`<br>`"1080p"` |
| `generate_audio` | Génère un audio synchronisé (ambiance, parole, effets). Désactivé produit une vidéo sans piste audio. (défaut : True) | BOOLEAN | Oui | True<br>False |
| `safety_tolerance` | Tolérance de modération, 0 étant la plus stricte. Les requêtes qui envoient des images ou des vidéos sont plafonnées à 2 quel que soit le réglage. (défaut : 2) | INT | Oui | 0 à 4 |
| `seed` | Graine (seed) pour déterminer si le nœud doit s’exécuter à nouveau ; FLUX 3 choisit sa propre graine, donc les résultats réels sont non déterministes quelle que soit cette valeur. (défaut : 42) | INT | Oui | 0 à 4294967295 |

Remarque : L’entrée `seed` inclut les contrôles Control After Generate dans l’interface. Le prix affiché est basé sur `resolution` et `duration` : HD (720p) est facturé à 0,2431 $ par seconde et FHD (1080p) à 0,4147 $ par seconde. Lorsqu’une durée fixe est choisie, le coût total estimé du clip est affiché ; lorsque `duration` est "auto", le tarif par seconde est affiché.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `video` | Le clip vidéo généré, avec audio synchronisé lorsque `generate_audio` est activé. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Flux3TextToVideoNode/fr.md)

---
**Source fingerprint (SHA-256):** `35f5e5b1c6dd737afab78f53700997a458781d38149cb64fc60d86a86858b2e6`
