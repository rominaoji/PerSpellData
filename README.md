# PerSpellData

A comprehensive parallel dataset designed for the task of spell checking in Persian. Misspelled sentences together with the correct form are produced using a massive confusion matrix, which is gathered from many sources. This dataset contains informal sentences in addition to the formal sentences, and contains texts from diverse topics. Both non-word and real-word errors are collected in the dataset


## Description

Our approach is based on a large corpus of Persian texts in addition to the confusion matrix. Confusion matrix is a set of words that may mistakenly be replaced with each other, like ‘there’ and ‘their’ in English. We gathered a confusion matrix containing X pairs of words from various sources, which are explained below. Given the confusion matrix, we make our parallel dataset by replacing correct words of corpus sentences with words which are confusing with them.

Following shows some statistics of PerSpellData:

Errors   | Confusion Matrix | PerSpellData|
---------|------------------|-------------|
non-word errors | 500,000     |2,500,000|
real-word errors| 1,800,000   |5,000,000|
Total           | 2,300,000   |7,500,000|


## Examples

Example of real-word and non-word errors in Persian and English:


<table>
    <thead>
        <tr>
	    <th colspan="2"></th>
	    <th></th>
            <th>English Errors</th>
            <th ></th>
            <th>Persian Errors</th>
	    <th>Layer 3</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td rowspan=4>L1 Name</td>
            <td rowspan=2>L2 Name A</td>
            <td>L3 Name A</td>
        </tr>
        <tr>
            <td>L3 Name B</td>
        </tr>
        <tr>
            <td rowspan=2>L2 Name B</td>
            <td>L3 Name C</td>
        </tr>
        <tr>
            <td>L3 Name D</td>
        </tr>
    </tbody>
</table>


For soem error type we provide two files, one of them is confusion matrix and the other is perSpellData parallel corpus:

Type |Error_type | Confusion Matrix | PerSpellData |
---------|---------|------------|-----------|
Real-word |Virastar's logs  			| 1034	 	| [18,690]	|
Real-word |Synthetic  				| [1,425,693](https://github.com/rominaoji/PerSpellData/blob/main/confusion_matrix/real-word/final_confusion_real.csv) 	| [?]		|
Real-word |Make informal plural again plural 	| 165		| [?] 		|
Real-word |Common mistakes 			| 87		| [2,018] 	|
Real-word |Same sound 				| ? 		| ?		|
Real-word |Gozar words 				| 296	 	| [4,920] 	|
Real-word |Tanvin 				| 79	  	| [1,072] 	|
Real-word |Hamza 				| 1,193		| [?] 		|
Non-word  |Virastar's logs  			| 136,164 	| [1,185,512]	|
Non-word  |FAspell  				| [5063](https://www.kaggle.com/rtatman/faspell) 	| [?]		|
Non-word  |Be 					| 515		| [4,374] 	|
Non-word  |Close words  			| 502,107 	| [?] 		|
Both-form |CPG  				| - 		| [707](https://github.com/rominaoji/PerSpellData/tree/main/dehkhoda)	|
Real-word |Total  				| 1,428,547	| ?		|
Non-word  |Total  				| 643,849	| ? 		|


## Reference 

If you use or discuss this dataset in your work, please cite our paper:

```
@InProceedings{}
```

## Contact

If you have a technical question regarding the dataset or publication, please
create an issue in this repository.
