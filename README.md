# PerSpellData

A comprehensive parallel dataset designed for the task of spell checking in Persian. Misspelled sentences together with the correct form are produced using a massive confusion matrix, which is gathered from many sources. This dataset contains informal sentences in addition to the formal sentences, and contains texts from diverse topics. Both non-word and real-word errors are collected in the dataset


## Description

Our approach is based on a large corpus of Persian texts in addition to the confusion matrix. Confusion matrix is a set of words that may mistakenly be replaced with each other, like ‘there’ and ‘their’ in English. We gathered a confusion matrix containing 2,072,396 pairs of words from various sources, which are explained below. Given the confusion matrix, we make our parallel dataset by replacing correct words of corpus sentences with words which are confusing with them.

Following shows some statistics of PerSpellData:

Errors   | Confusion Matrix | PerSpellData|
---------|------------------|-------------|
non-word errors | 643,849     |2,500,000|
real-word errors| 1,428,547   |5,000,000|
Total           | 2,072,396   |7,500,000|


## Examples

Example of real-word and non-word errors in Persian and English:


<table>
    <thead>
        <tr>
	    <th rowspan=2></th>
	    <th></th>
            <th colspan=2>English Errors</th>
            <th colspan=2 >Persian Errors</th>
        </tr>
	     <th>Error type</th>
	     <th>Correct Form</th>
	     <th>Wrong Form</th>
	     <th>Correct Form</th>
	     <th>Wrong Form</th>
	<tr>
	</tr>
    </thead>
    <tbody>
        <tr>
            <td rowspan=4>non-word</td>
            <td>insertion</td>
	    <td>This story is embracing</td>
	    <td>This storey is embracing </td>
	    <td>خوشبختانه همه هنوز دچار نشده اند </td>
	    <td>خوشبخنانه همه هنوز دچار نشده اند</td>
        </tr>
        <tr>
            <td>deletion</td>
            <td>She is an actress </td>
	    <td>She is an acress</td>
	    <td>مردم آن شهر خیلی خسته بودند</td>
	    <td>مردم آن شهر خیی خسته بودند</td>
        </tr>
     <tr>
            <td>substitution</td>
            <td>Tehran is the capital of Iran </td>
	    <td>Tehran is the capitol of Iran</td>
	    <td>ساعت هفت بیدار میشوم </td>
	    <td>صاعت هفت بیدار میشوم</td>
        </tr>
     <tr>
            <td>transposition</td>
            <td>He is afraid of bears </td>
	    <td>He is afraid of bares</td>
	    <td>از آنجا تاکسی گرفتیم</td>
	    <td>از آنجا تاکسی گرتفیم</td>
        </tr>
        <tr>
            <td rowspan=6>real-word</td>
	    <td>insertion</td>
	    <td>Good jobs are found in big cities</td>
            <td>Good jobs are found ink big cities</td>
	    <td>در این مکان اسکان کنید</td>
	    <td>در این مکان استکان کنید</td>
	    <td></td>
        </tr>
	<tr>
	    <td>deletion</td>
	    <td>They live on their own</td>
            <td>They live on their on</td>
	    <td>گرادیان این زاویه چند است؟</td>
	    <td>گدایان این زاویه چند است؟</td>
        </tr>
	<tr>
	    <td>substitution</td>
            <td>I cannot see you</td>
	    <td>I cannot sea you</td>
	    <td>این مبل گران است</td>
	    <td>این مبل میان است</td>
        </tr>
	<tr>
	    <td>transposition</td>
            <td>I live here</td>
	    <td>I live heer</td>
	    <td>این عدد بر مبنای دو است</td>
	    <td>ین عدد بر مبانی دو است</td>
        </tr>
	<tr>
	    <td>same pronunciation</td>
            <td>This is too much money</td>
	    <td>This is two much money</td>
	    <td>این میوه پرتقال است</td>
	    <td>این میوه پرتغال است</td>
        </tr>
	<tr>
	    <td>word boundary </td>
            <td>You can do it </td>
	    <td>Youcan do it</td>
	    <td>به خانه می روم</td>
	    <td>به خانه میروم</td>
        </tr>
    </tbody>
</table>


For some error type we provide two files, one of them is confusion matrix and the other is perSpellData parallel corpus.
all of PerSpellData is upladed and can be downloaded.
Here are statistics and links of different type of errors:

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


## Reference 

If you use or discuss this dataset in your work, please cite our paper:

```
@InProceedings{}
```

## Contact

If you have any technical question regarding the dataset or publication, please
create an issue in this repository.
