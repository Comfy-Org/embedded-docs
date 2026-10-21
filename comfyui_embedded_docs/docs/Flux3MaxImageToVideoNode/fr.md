# FLUX 3 Max Image to Video

FLUX 3 Max Image to Video anime de 1 à 10 images avec FLUX 3 Max. Chaque image fournie devient une image du clip : une seule image l’ouvre, deux en deviennent la première et la dernière image, et au-delà, elles sont réparties sur le clip ou fixées aux instants que vous choisissez.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt` | Comment la scène doit se déplacer et produire du son (par défaut : vide). | STRING | Oui | Texte multiligne |
| `keyframes` | Emplacement extensible : connectez de 1 à 10 images clés dans l’ordre de lecture, par ex. `image_1`, `image_2`, etc. Chaque image devient une image du clip. | IMAGE | Oui | 1 à 10 images |
| `placement` | `"spread across the clip"` place la première image au début, la dernière à la fin et les autres uniformément entre les deux ; `"at times"` fixe chaque image à une seconde que vous choisissez (par défaut : `"spread across the clip"`). | DYNAMIC_COMBO | Oui | `"spread across the clip"`<br>`"at times"` |
| `aspect_ratio` | Ratio d’aspect de sortie. `"auto"` suit la première image clé (par défaut : `"auto"`). | COMBO | Oui | `"auto"`<br>`"21:9"`<br>`"2:1"`<br>`"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"` |
| `duration` | Durée du clip en secondes (par défaut : `"5"`). | COMBO | Oui | `"5"`<br>`"6"`<br>`"7"`<br>`"8"`<br>`"9"`<br>`"10"`<br>`"11"`<br>`"12"`<br>`"13"`<br>`"14"`<br>`"15"`<br>`"16"`<br>`"17"`<br>`"18"`<br>`"19"`<br>`"20"` |
| `resolution` | Résolution de sortie (par défaut : `"720p"`). | COMBO | Oui | `"720p"`<br>`"1080p"` |
| `reasoning_level` | Dans quelle mesure le modèle raisonne sur le prompt et l’étend avant de générer. `"high"` prend plus de temps ; le prix reste identique (par défaut : `"high"`). | COMBO | Oui | `"low"`<br>`"high"` |
| `generate_audio` | Générer un audio synchronisé. Désactivé produit une vidéo sans piste audio (par défaut : true). | BOOLEAN | Oui | `true`<br>`false` |
| `seed` | Graine contrôlant si le nœud se relance. Les résultats sont non déterministes quelle que soit cette valeur (par défaut : 42). | INT | Oui | 0 à 2147483646 |

### Entrées « at times »

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `times` | Un temps en secondes par image, séparés par des virgules et croissants, par ex. « 0, 2.5, 5 ». N’apparaît que lorsque `placement` vaut `"at times"`. | STRING | Non | Secondes séparées par des virgules |

Remarque : `prompt` doit contenir au moins un caractère. `keyframes` doit contenir au moins une image et ne peut pas en contenir plus de 10 ; une entrée par lot compte une fois par image.

Lorsque `placement` est défini sur `"spread across the clip"`, une ou deux images sont envoyées comme image de début et, éventuellement, image de fin, tandis que trois images ou plus sont placées sur des images clés réparties uniformément sur le clip à 24 i/s.

Lorsque `placement` est défini sur `"at times"`, `times` doit fournir une valeur par image ; ces valeurs doivent être croissantes, ne peuvent pas être négatives et la dernière ne peut pas dépasser la fin du clip.

Le prix affiché est basé sur `resolution` et `duration` : la 720p est facturée à $0.060775 par seconde et la 1080p à $0.103675 par seconde jusqu’au 7 novembre 2026, puis à $0.2431 et $0.4147 par seconde après cette date. Le coût total estimé du clip est affiché dans l’interface.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `video` | Le clip vidéo généré construit à partir des images clés avec le ratio d’aspect, la durée, la résolution et le paramètre audio choisis. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Flux3MaxImageToVideoNode/fr.md)

---
**Source fingerprint (SHA-256):** `fd8bbd627022f86d3ecb3482530a6c8c37d4225e32db36c35185eac318ed4c75`
