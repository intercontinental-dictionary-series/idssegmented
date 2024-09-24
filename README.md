# CLDF dataset accompanying List's "Inference of Partial Colexifications" from 2023 building on Key and Comrie's "Intercontinental Dictionary Series" from 2021

[![CLDF validation](https://github.com/intercontinental-dictionary-series/idssegmented/workflows/CLDF-validation/badge.svg)](https://github.com/intercontinental-dictionary-series/idssegmented/actions?query=workflow%3ACLDF-validation)

## How to cite

If you use these data please cite
- the original source
  > List, J.-M. (2023): Inference of partial colexifications from multilingual wordlists. Frontiers in Psychology 14.1156540. 1-10.
- the derived dataset using the DOI of the [particular released version](../../releases/) you were using

## Description


This dataset is licensed under a CC-BY-4.0 license

Available online at https://github.com/intercontinental-dictionary-series/idssegmented


Conceptlists in Concepticon:
- [Key-2016-1310](https://concepticon.clld.org/contributions/Key-2016-1310)
## Notes

In this derived version of the original Intercontinental Dictionary Series, all entries have been roughly mapped to the International Phonetic Alphabet in the version provided by the Cross-Linguistic Transcriptin Systems initiative (https://clts.clld.org). The conversions should be largely consistent, but it is quite possible that there remain many erroneous conversions, where experts of the respective language varieties would select different transcription values. We emphasize that this is but a first step towards a standardizatio of the IDS data, and that additional work can and should be carried out by experts in the future.

In a first version, we later found several errors for languages for which orthographies were confused with phonetic or phonemic transcriptions in the original. The updated version now tries to take this into account by removing the respective languages with problems and also by slowly planning to make targeted segmentations for particular languages in the dataset. As a recent example for such a targeted segmentation, consider the segmented version of Panoan languages in the dataset [keypano](https://github.com/intercontinental-dictionary-series/keypano), which contains targeted transcriptions for two dozen languages. These languages have also been ignored in this version, since we consider that a better solution for transcriptions in segmented form has been provided. This means also, that the current dataset will hopefully shrink in the future whenever we manage to provide targeted segmentations for more languages in the sample.




## Statistics


[![CLDF validation](https://github.com/intercontinental-dictionary-series/idssegmented/workflows/CLDF-validation/badge.svg)](https://github.com/intercontinental-dictionary-series/idssegmented/actions?query=workflow%3ACLDF-validation)
![Glottolog: 98%](https://img.shields.io/badge/Glottolog-98%25-green.svg "Glottolog: 98%")
![Concepticon: 100%](https://img.shields.io/badge/Concepticon-100%25-brightgreen.svg "Concepticon: 100%")
![Source: 100%](https://img.shields.io/badge/Source-100%25-brightgreen.svg "Source: 100%")
![BIPA: 100%](https://img.shields.io/badge/BIPA-100%25-brightgreen.svg "BIPA: 100%")
![CLTS SoundClass: 100%](https://img.shields.io/badge/CLTS%20SoundClass-100%25-brightgreen.svg "CLTS SoundClass: 100%")

- **Varieties:** 268 (linked to 219 different Glottocodes)
- **Concepts:** 1,310 (linked to 1,308 different Concepticon concept sets)
- **Lexemes:** 360,553
- **Sources:** 268
- **Synonymy:** 1.24
- **Invalid lexemes:** 0
- **Tokens:** 2,335,052
- **Segments:** 515 (0 BIPA errors, 0 CLTS sound class errors, 515 CLTS modified)
- **Inventory size (avg):** 52.02

# Contributors

Name | GitHub user | Description | Role
--- | --- | --- | ---
Johann-Mattis List | @Lingulist | maintainer | Editor
Key, M. R | | | Author, DataCollector
Comrie, B. | | | Author, DataCollector




## CLDF Datasets

The following CLDF datasets are available in [cldf](cldf):

- CLDF [Wordlist](https://github.com/cldf/cldf/tree/master/modules/Wordlist) at [cldf/cldf-metadata.json](cldf/cldf-metadata.json)