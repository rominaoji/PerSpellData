# PerSpellData

A comprehensive parallel dataset designed for the task of spell checking in Persian. Misspelled sentences together with the correct form are produced using a massive confusion matrix, which is gathered from many sources. This dataset contains informal sentences in addition to the formal sentences, and contains texts from diverse topics. Both non-word and real-word errors are collected in the dataset


## Description

An atomic edit is defined as an edit *e* applied to a natural language expression *S* as the insertion, deletion, or substitution of a sub-expression *P* such that both the original expression S and the resulting expression *e(S)* are well-formed semantic constituents (MacCartney, 2009). In this corpus, we release such atomic insertions and deletions made to sentences in wikipedia. __**Please click on the numbers below to download the data**__.

Following are the number of examples by language:

Errors   | Confusion Matrix | PerSpellData|
---------|------------------|-------------|
non-word errors | 500,000     |2,500,000|
real-word errors| 1,800,000   |5,000,000|
Total           | 2,300,000   |7,500,000|


## Examples

Example of an insertion:

"*She died there after a long illness.*" + "*in 1949*" = "*She died there in 1949 after a long illness.*"

Example of a deletion:

"*She dreams about entering the Black Lodge and about a ring.*" - "*and about a ring.*" = "*She dreams about entering the Black Lodge.*"

For each language we provide two files, one each for insertions and deletions. The files contains the following tab-separated columns:

Type |Error_type | Confusion Matrix | PerSpellData |
---------|---------|------------|-----------|
Real-word |Virastar's logs  			| [1034] 	| [18,690]	|
Real-word |Synthetic  				| [1425693] 	| [?]		|
Real-word |Make informal plural again plural 	| [165]		| [?] 		|
Real-word |Common mistakes 			| [87]		| [2,018] 	|
Real-word |Same sound 				| [?] 		| [?]		|
Real-word |Gozar words 				| [296] 	| [4,920] 	|
Real-word |CPG 					| [?] 		| [?]		|
Real-word |Tanvin 				| [79]  	| [1,072] 	|
Real-word |Hamza 				| [1,193]  	| [?] 		|
Non-word  |Virastar's logs  			| [136,164] 	| [1,185,512]	|
Non-word  |CPG  				| [?] 		| [1,185,512]	|
Non-word  |FAspell  				| [5063] 	| [?]		|
Non-word  |Virastar logs 			| [?] 		| [1,185,512]	|
Non-word  |Be 					| [515]		| [4,374] 	|
Non-word  |Close words  			| [502,107] 	| [?] 		|
Real-word |Total  				| [?] 		| [?]		|
Non-word  |Total  				| [?]		| [?] 		|


## Reference 

If you use or discuss this dataset in your work, please cite our paper:

```
@InProceedings{}
```

## Contact

If you have a technical question regarding the dataset or publication, please
create an issue in this repository.
