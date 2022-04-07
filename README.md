# PerSpellData

A comprehensive parallel dataset designed for the task of spell checking in Persian. Misspelled sentences together with the correct form are produced using a massive confusion matrix, which is gathered from many sources. This dataset contains informal sentences in addition to the formal sentences, and contains texts from diverse topics. Both non-word and real-word errors are collected in the dataset


## Description

Our approach is based on a large corpus of Persian texts in addition to the confusion matrix. Confusion matrix is a set of words that may mistakenly be replaced with each other, like ‘there’ and ‘their’ in English. We gathered a confusion matrix containing 2,072,396 pairs of words from various sources, which are explained below. Given the confusion matrix, we make our parallel dataset by replacing correct words of corpus sentences with words which are confusing with them.

Following shows some statistics of PerSpellData:

Errors   | Confusion Matrix | PerSpellData|
---------|------------------|-------------|
non-word errors | 643,849     |3.8M|
real-word errors| 1,428,547   |2.5M|
Total           | 2,072,396   |6.4M|


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


<table>
	<thead>
		<th>Type</th>
		<th>Error-Type</th>
		<th>Confused-words</th>
		<th>PerSpellData</th>
	</thead>
	 <tbody>
        <tr>
	    	<td>Real-word</td>
	    	<td>Virastman's logs</td>
	    	<td>1034</td>
	    	<td><a href="https://github.com/rominaoji/PerSpellData/tree/main/DataSet/real-word/virastman">7,753</a></td>
		</tr>
        <tr>
	    	<td>Real-word</td>
	    	<td>Synthetic</td>
	    	<td><a href="https://github.com/rominaoji/PerSpellData/blob/main/confusion_matrix/real-word/final_confusion_real.csv">1,425,693</a></td>
	    	<td><a href="https://drive.google.com/drive/u/6/folders/1VK6tUEJoqPTE7SCs6FJt4p0P6BosDj2x">2,959,054</a></td>
		</tr>
        <tr>
	   		<td>Real-word</td>
	    	<td>Make informal plural again plural</td>
	    	<td>165</td>
	    	<td><a href="https://github.com/rominaoji/PerSpellData/tree/main/DataSet/real-word/plural">2,968</a></td>
		</tr>
        <tr>
	    	<td>Real-word</td>
	    	<td>Common mistakes</td>
	    	<td>87</td>
	    	<td><a href="https://github.com/rominaoji/PerSpellData/tree/main/DataSet/real-word/common">847</a></td>
		</tr>
        <tr>
	    	<td>Real-word</td>
	    	<td>Gozar</td>
	    	<td>296</td>
	    	<td><a href="https://github.com/rominaoji/PerSpellData/tree/main/DataSet/real-word/gozar">2,088</a></td>
		</tr>
        <tr>
	    	<td>Real-word</td>
	    	<td>Tanvin</td>
	    	<td>79</td>
	    	<td><a href="https://github.com/rominaoji/PerSpellData/tree/main/DataSet/real-word/tanvin">448</a></td>
		</tr>
		<tr>
	    	<td>Non-word</td>
	    	<td>Be</td>
	    	<td>515</td>
	    	<td><a href="https://github.com/rominaoji/PerSpellData/tree/main/DataSet/real-word/be">1520</a></td>
		</tr>
	    <td>Non-word</td>
	    	<td>FaSepell</td>
	    	<td>5,063</td>
	    	<td><a href="https://drive.google.com/drive/u/6/folders/1k9U4N9W-StBaKWFetckwj3fROAyzRNg9">8,953</a></td>
		</tr>
        <tr>
	    	<td>Non-word</td>
	    	<td>Virastman's logs</td>
	    	<td>136,164</td>
	    	<td><a href="https://drive.google.com/drive/u/6/folders/1CP6DyLwIBHer7TsVE9ca0rjHjWc0QSFF">467,946</a></td>
		</tr>
		<tr>
	    	<td>Non-word</td>
	    	<td>Close words</td>
	    	<td>502,107</td>
	    	<td><a href="https://drive.google.com/drive/u/6/folders/1vchA4BOlyBz0-POZqvgSRs1dxPb-bMNx">1,440,854</a></td>
		</tr>
		<tr>
	    	<td>Non-word</td>
	    	<td>CPG</td>
	    	<td>-</td>
	    	<td><a href="https://github.com/rominaoji/PerSpellData/tree/main/dehkhoda">707</a></td>
		</tr>

</table>

## Reference 

If you use or discuss this dataset in your work, please cite our paper:

```
@inproceedings{persian-2021-romina-oji,
    title = "Romina Oji, Nasrin Taghizadeh and Heshaam Faili",
    author = "Persian, PerSpellData: An Exhaustive Parallel Spell Dataset For",
    booktitle = "Proceedings of The Second International Workshop on NLP Solutions for Under Resourced Languages (NSURL 2021) co-located with ICNLSP 2021",
    month = "12--13 " # nov,
    year = "2021",
    address = "Trento, Italy",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2021.nsurl-1.2",
    pages = "8--14",
}
```

## Contact

If you have any technical question regarding the dataset or publication, please
create an issue in this repository.
